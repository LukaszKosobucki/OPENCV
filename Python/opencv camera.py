# https://github.com/DavidWangWood/Camera-Calibration-Python/blob/master/camera_calibration.ipynb
# https://docs.opencv.org/3.3.0/dc/dbb/tutorial_py_calibration.html
# https://docs.opencv.org/master/dc/dbb/tutorial_py_calibration.html


import numpy as np
import cv2
import glob

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((7 * 10, 3), np.float32)
objp[:, :2] = np.mgrid[0:10, 0:7].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane.
# images = glob.glob('*.bmp')
images=glob.glob('*.bmp')
print(images)
k=0
p=0
for fname in images:
    img = cv2.imread(fname)
    img_size = (img.shape[1], img.shape[0])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (10, 7), None)
    if ret==False:
        p+=1
    print("ominięto", p)
    # If found, add object points, image points (after refining them)
    if ret == True:
        k+=1
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners)

        # Draw and display the corners

        kozak=cv2.drawChessboardCorners(gray, (10, 7), corners2, ret)
        cv2.imwrite(f"obrazek{k}.jpg",kozak)
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_size, None, None)
        k+=1
        print(ret)
        print("przyjeto",k)
        dst = cv2.undistort(img, mtx, dist, None, mtx)

        cv2.imwrite(f'obrazek{k}.jpg', dst)
        # dst = cv2.undistort(dist, mtx, dist, None, mtx)
        # cv2.imshow('img',gray)

        cv2.waitKey(0)

# cv2.destroyAllWindows()
img=cv2.imread('img00308_r.bmp')
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_size, None, None)
print(ret)
dst = cv2.undistort(img, mtx, dist, None, mtx)
cv2.imwrite('undistorted.jpg', dst)

import matplotlib.pyplot as plt

# Test undistortion on an image


# Do camera calibration given object points and image points
# ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_size, None, None)
#
# dst = cv2.undistort(img, mtx, dist, None, mtx)
# cv2.imwrite('TEST.jpg', dst)
#
#
# # dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
# # Visualize undistortion
# f, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
# ax1.imshow(img)
# ax1.set_title('Original Image', fontsize=30)
# ax2.imshow(dst)
# ax2.set_title('Undistorted Image', fontsize=30)
# plt.show()