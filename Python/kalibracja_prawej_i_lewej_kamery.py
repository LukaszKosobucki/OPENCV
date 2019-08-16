import glob
import cv2
import numpy as np
fname= glob.glob("*.bmp")
print(len(fname))
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0), in this exercise they should be 100,200... etc
objp = np.zeros((7 * 10, 3), np.float32)
objp[:, :2] = np.mgrid[0:10, 0:7].T.reshape(-1, 2)
objp=objp*100
# Arrays to store object points and image points from all the images.
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane of right camera
imgpoints2=[] # 2d points in image plane of left camera
k=110
p=0
corners2OLD=[[[0,0]],[[0,0]],[[0,0]],[[0,0]],[[0,0]],[[0,0]],[[0,0]],[[0,0]],[[0,0]],[[0,0]],[[0,0]],[[0,0]]]
przekatna=0
przekatna2=0
for image in fname:
    k+=1
    print(k)
    img=cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners=cv2.findChessboardCorners(gray, (10, 7), None)
    if ret==True:
        corners2 = cv2.cornerSubPix(gray, corners, (5,5), (-1, -1), criteria)
        xd=np.absolute(przekatna - (np.sqrt((corners2[0][0][0]-corners2[-1][0][0])**2)+np.sqrt((corners2[0][0][1]-corners2[-1][0][1])**2))) #warunek o roznicy dlugosci #1 przekątnej
        xd2=np.absolute(przekatna2 - (np.sqrt((corners2[9][0][0]-corners2[-10][0][0])**2+(corners2[9][0][1]-corners2[-10][0][1])**2))) #warunek o roznicy dlugosci #2 przekątnej
        # wartosc 15 dla warunkow jest wartoscia zeminna wg uznania
        if np.absolute(np.sqrt(corners2[0][0][0]**2+corners2[0][0][1]**2)-np.sqrt(corners2OLD[0][0][0]**2+corners2OLD[0][0][1]**2))>15 or xd>15 or xd2>15: 
            objpoints.append(objp)
            imgpoints.append(corners2)
            corners2OLD=corners2
            img2=cv2.imread(f"left\img{k}_l.bmp")
            gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            ret2, corners3 = cv2.findChessboardCorners(gray2, (10, 7), None)
            corners4 = cv2.cornerSubPix(gray, corners, (5, 5), (-1, -1), criteria)
            imgpoints2.append(corners4)
            przekatna=np.sqrt((corners2OLD[0][0][0]-corners2OLD[-1][0][0])**2)+np.sqrt((corners2OLD[0][0][1]-corners2OLD[-1][0][1])**2)
            przekatna2=np.sqrt((corners2OLD[9][0][0]-corners2OLD[-10][0][0])**2+(corners2OLD[9][0][1]-corners2OLD[-10][0][1])**2)
            print(f"znalazlem{k}")
            p+=1

print(f"wzialem: {p} obrazkow, odrzucilem: {len(fname)-p}")
img=cv2.imread('img00111_r.bmp')
img_size = (img.shape[1], img.shape[0])
asd=np.array([[1200,0,1279/2],[0,1280,1023/2],[0.0,0.0,1.0]])
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, img_size,distCoeffs=None,cameraMatrix=asd)
print("blad:",ret)
dst = cv2.undistort(img, mtx, dist, None, mtx) #obrazek 111 jako przyklad usuniecia dystorsji
cv2.imwrite('undistorted.jpg', dst)
import pickle
with open("ObjPoints.pickle","wb") as file:
    pickle.dump(objpoints,file)
with open("ImagePoints1.pickle","wb") as file: #prawa kamera
    pickle.dump(imgpoints,file)
with open("ImagePoints2.pickle","wb") as file: #lewa kamera
    pickle.dump(imgpoints2,file)

