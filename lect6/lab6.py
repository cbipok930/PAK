import cv2.cv2 as cv2
import time
def get_contours_frames_dif(f1, f2):
    """
    :param f1: first frame
    :param f2: second frame
    :return: contours of frames difference
    """
    blur1 = cv2.GaussianBlur(cv2.cvtColor(f1, cv2.COLOR_BGR2GRAY), (3, 3), 3)
    blur2 = cv2.GaussianBlur(cv2.cvtColor(f2, cv2.COLOR_BGR2GRAY), (3, 3), 3)
    diff = cv2.GaussianBlur(cv2.absdiff(blur1, blur2), (3, 3), 3)
    _, thd = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    cnt_rs, _ = cv2.findContours(thd, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return cnt_rs


def look_for_movements(frame, cnt_r, o_lay, alpha):
    """
    :param frame: background frame
    :param cnt_r: movements contours
    :param o_lay: frame with same size as background frame
    :param alpha: alpha
    :return: frame with green/red areas drawn
    """
    flag = False
    overlay = cv2.rectangle(o_lay, (0, 0), (640, 480), (0, 255, 0), -1)
    for ct in contours:
        if cv2.contourArea(ct) > 500:
            flag = True
            cv2.fillPoly(overlay, cnt_r, (0, 0, 255))
    frame_ret = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
    return frame_ret, flag


cap = cv2.VideoCapture(0)
_, frame_f = cap.read()
_, frame_s = cap.read()
start = time.time()
mode = "red"
while True:
    contours = get_contours_frames_dif(frame_f, frame_s)
    if mode == "red":
        _, overlay_mov = cap.read()
        frame_f, mov = look_for_movements(frame_f, contours, overlay_mov, 0.5)
        cv2.putText(frame_f, "RED LIGHT", (40, 40), cv2.FONT_ITALIC, 1, (0, 0, 255), 2)
        if mov:
            cv2.putText(frame_f, "DETECTED", (240, 40), cv2.FONT_ITALIC, 1, (0, 0, 255), 2)
    else:
        cv2.putText(frame_f, "GREEN LIGHT", (40, 40), cv2.FONT_ITALIC, 1, (0, 255, 0), 2)

    cv2.putText(frame_f, "Timer: "+str(10 - int(time.time() - start)), (40, 80), cv2.FONT_ITALIC, 1, (255, 0, 255), 2)
    cv2.imshow('frame', frame_f)
    key = cv2.waitKey(60)
    frame_f = frame_s
    if int(time.time() - start) == 10:
        mode = "red" if mode == "green" else "green"
        start = time.time()
    ref, frame_s = cap.read()
    if key == 27:
        break
cv2.destroyWindow('frame')
cap.release()
