import numpy as np
import matplotlib.pyplot as plt
import cv2.cv2 as cv2


def find_and_mark(ghost, top, occult):
    sift = cv2.SIFT_create()
    keypoints_src, descriptors_src = sift.detectAndCompute(ghost, None)
    keypoints_dst, descriptors_dst = sift.detectAndCompute(occult, None)
    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=False)
    matches = bf.match(descriptors_src, descriptors_dst)
    matches = sorted(matches, key=lambda x: x.distance)
    pt_src = np.float32([keypoints_src[m.queryIdx].pt for m in matches[:20]]).reshape(-1, 1, 2)
    pt_dst = np.float32([keypoints_dst[m.trainIdx].pt for m in matches[:20]]).reshape(-1, 1, 2)
    h, status = cv2.findHomography(pt_src, pt_dst)
    src_corners = np.array([[1, 1], [ghost.shape[1], ghost.shape[0]]]).reshape(-1, 1, 2).astype(np.float32)
    dst_corners = cv2.perspectiveTransform(src_corners, h).astype(int)
    cv2.rectangle(top, (dst_corners[0][0][0], dst_corners[0][0][1]),
                  (dst_corners[1][0][0], dst_corners[1][0][1]), (0, 0, 255), 4)
    cv2.rectangle(occult, (dst_corners[0][0][0], dst_corners[0][0][1]),
                  (dst_corners[1][0][0], dst_corners[1][0][1]), (0, 0, 0), -1)
    return top, occult


def main():
    candy = cv2.imread('candy_ghost.png')
    picture_main = cv2.imread('lab7.png')
    picture_main_back = cv2.cvtColor(picture_main, cv2.COLOR_BGR2GRAY)
    picture_main, picture_main_back = find_and_mark(cv2.cvtColor(candy, cv2.COLOR_BGR2GRAY),
                                                    picture_main, picture_main_back)
    plt.imshow(cv2.cvtColor(picture_main, cv2.COLOR_BGR2RGB))
    plt.show()


main()
