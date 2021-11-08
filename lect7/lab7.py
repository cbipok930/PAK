import os
import numpy as np
import matplotlib.pyplot as plt
import cv2.cv2 as cv2


def find_and_mark(ghost, top, occult):
    ghost = cv2.dilate(cv2.cornerHarris(ghost, 2, 3, 0.00001), None)
    plt.imshow(ghost)
    _, ghost = cv2.threshold(ghost, ghost.max() / 100, 255, cv2.THRESH_BINARY)
    ghost = np.uint8(ghost)
    plt.imshow(ghost)
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
                  (dst_corners[1][0][0], dst_corners[1][0][1]), (255, 0, 0), 4)
    cv2.rectangle(occult, (dst_corners[0][0][0], dst_corners[0][0][1]),
                  (dst_corners[1][0][0], dst_corners[1][0][1]), (0, 0, 0), -1)
    plt.imshow(top)
    plt.imshow(occult)
    plt.show()
    return top, occult


def main():
    candy = cv2.imread('candy_ghost.png')
    pumpkin = cv2.imread('pumpkin_ghost.png')
    scary = cv2.imread('scary_ghost.png')
    picture_main = cv2.imread('lab7.png')
    picture_main_back = np.float32(cv2.cvtColor(picture_main, cv2.COLOR_BGR2GRAY))
    picture_main_back = cv2.dilate(cv2.cornerHarris(picture_main_back, 2, 3, 0.00001), None)
    plt.imshow(picture_main_back)
    _, picture_main_back = cv2.threshold(picture_main_back, picture_main_back.max() / 100, 255, cv2.THRESH_BINARY)
    picture_main_back = np.uint8(picture_main_back)
    plt.imshow(picture_main_back)
    picture_main, picture_main_back = find_and_mark(cv2.cvtColor(candy, cv2.COLOR_BGR2GRAY),
                                                    picture_main, picture_main_back)
    picture_main, picture_main_back = find_and_mark(cv2.cvtColor(candy, cv2.COLOR_BGR2GRAY),
                                                    picture_main, picture_main_back)
    picture_main, picture_main_back = find_and_mark(cv2.cvtColor(scary, cv2.COLOR_BGR2GRAY),
                                                    picture_main, picture_main_back)
    picture_main, picture_main_back = find_and_mark(cv2.cvtColor(pumpkin, cv2.COLOR_BGR2GRAY),
                                                    picture_main, picture_main_back)
    # picture_main, picture_main_back = find_and_mark(cv2.cvtColor(scary, cv2.COLOR_BGR2GRAY),
    #                                                 picture_main, picture_main_back)
    # find Harris corners
    # candy_g = np.float32(cv2.cvtColor(candy, cv2.COLOR_BGR2GRAY))
    # cg_dst = cv2.cornerHarris(candy_g, 2, 3, 0.04)
    # plt.imshow(cg_dst, cmap='gray')
    # cg_dst = cv2.dilate(cg_dst, None)
    # plt.imshow(cg_dst, cmap='gray')
    # _, cg_dst = cv2.threshold(cg_dst, cg_dst.max()/100, 255, cv2.THRESH_BINARY)
    # plt.imshow(cg_dst, cmap='gray')
    # cg_dst = np.uint8(cg_dst)
    # plt.imshow(cg_dst, cmap='gray')

    sift = cv2.SIFT_create()
    # key_points_cg = sift.detect(cv2.cvtColor(candy, cv2.COLOR_BGR2GRAY), None)
    # result = candy.copy()
    # result = cv2.drawKeypoints(cv2.cvtColor(candy, cv2.COLOR_BGR2GRAY), key_points_cg, result)
    # plt.imshow(result, cmap='gray')
    # plt.show()

    keypoints_1, descriptors_1 = sift.detectAndCompute(scary, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(picture_main_back, None)

    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=False)

    matches = bf.match(descriptors_1, descriptors_2)
    matches = sorted(matches, key=lambda x: x.distance)
    pt_src = np.float32([keypoints_1[m.queryIdx].pt for m in matches[:20]]).reshape(-1, 1, 2)
    pt_dst = np.float32([keypoints_2[m.trainIdx].pt for m in matches[:20]]).reshape(-1, 1, 2)
    img3 = cv2.drawMatches(scary, keypoints_1, picture_main_back, keypoints_2, matches[:20], picture_main_back, flags=2)
    plt.imshow(img3)
    h, status = cv2.findHomography(pt_src, pt_dst)
    src_corners = np.array([[1, 1], [214, 220]]).reshape(-1, 1, 2).astype(np.float)
    dst_corners = cv2.perspectiveTransform(src_corners, h).astype(int)
    a = (dst_corners[0][0][0], dst_corners[0][0][1])
    cv2.rectangle(picture_main, (dst_corners[0][0][0], dst_corners[0][0][1]),
                  (dst_corners[1][0][0], dst_corners[1][0][1]), (255, 0, 0), 4)
    # a = np.dot(h, src_corners[0])
    # dst_corners = cv2.warpPerspective(src_corners, h, (src_corners.shape[1], src_corners.shape[0]))
    # plt.imshow(candy_dst)
    # plt.figure(figsize=(10, 6))
    plt.imshow(picture_main)
    # plt.imshow(im_dst)
    plt.show()


main()