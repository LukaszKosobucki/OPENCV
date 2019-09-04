import numpy as np
import cv2
import glob
rozm_zdj=(1920,1200)
fname = glob.glob("Z:\BazaNexus\Praktykanci\K3\*.jpg")
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((6 * 9, 3), np.float32)
objp[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)
objp=objp*25.1

objpoints = []
imgpoints = []

k = 1
for image in fname:
    frame = cv2.imread(image)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)
    if ret == False:
        print('Dzieki,dziala')
    if ret == True:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)
        print(k)
    k+=1
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, rozm_zdj, None,None)
import pickle
print(ret)
with open("k3\mtxvideo.pickle","wb") as file:
    pickle.dump(mtx,file)
with open("k3\distvideo.pickle","wb") as file:
    pickle.dump(dist,file)
with open("k3/retvideo.pickle","wb") as file:
    pickle.dump(ret,file)
with open("k3/rvecs.pickle","wb") as file:
    pickle.dump(rvecs,file)
with open("k3/tvecs.pickle","wb") as file:
    pickle.dump(tvecs,file)



fname = glob.glob("Z:\BazaNexus\Praktykanci\K2\*.jpg")
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((6 * 9, 3), np.float32)
objp[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)
objp=objp*25.1

objpoints = []
imgpoints = []

k = 1
for image in fname:
    frame = cv2.imread(image)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)
    if ret == False:
        print('Dzieki,dziala')
    if ret == True:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)
        print(k)
    k+=1
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, rozm_zdj, None,None)
import pickle
print(ret)
with open("k2\mtxvideo.pickle","wb") as file:
    pickle.dump(mtx,file)
with open("k2\distvideo.pickle","wb") as file:
    pickle.dump(dist,file)
with open("k2/retvideo.pickle", "wb") as file:
    pickle.dump(ret, file)
with open("k2/rvecs.pickle", "wb") as file:
    pickle.dump(rvecs, file)
with open("k2/tvecs.pickle", "wb") as file:
    pickle.dump(tvecs, file)


fname = glob.glob("Z:\BazaNexus\Praktykanci\K1\*.jpg")
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((6 * 9, 3), np.float32)
objp[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)
objp=objp*25.1

objpoints = []
imgpoints = []

k = 1
for image in fname:
    frame = cv2.imread(image)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)
    if ret == False:
        print('Dzieki,dziala')
    if ret == True:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)
        print(k)
    k+=1
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, rozm_zdj, None,None)
import pickle
print(ret)
with open("k1\mtxvideo.pickle","wb") as file:
    pickle.dump(mtx,file)
with open("k1\distvideo.pickle","wb") as file:
    pickle.dump(dist,file)
with open("k1/retvideo.pickle", "wb") as file:
    pickle.dump(ret, file)
with open("k1/rvecs.pickle", "wb") as file:
    pickle.dump(rvecs, file)
with open("k1/tvecs.pickle", "wb") as file:
    pickle.dump(tvecs, file)





criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((6 * 9, 3), np.float32)
objp[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)
objp=objp*25.1

objpoints = []
imgpoints = []
imgpoints2 = []
k = 0
for i in range(2942):
    frame = cv2.imread(f"Z:/BazaNexus/Praktykanci/K1/frame{k}.jpg")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)
    if ret == False:
        print('Dzieki,dziala')
    if ret == True:
        frame2 = cv2.imread(f"Z:/BazaNexus/Praktykanci/K3/frame{k}.jpg")
        gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret2, corners3 = cv2.findChessboardCorners(gray, (9, 6), None)
        if ret2==True:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            corners4 = cv2.cornerSubPix(gray2, corners3, (11, 11), (-1, -1), criteria)
            imgpoints2.append(corners4)
            imgpoints.append(corners2)
            print(k)
    k+=1

with open("k1k3/imagepointsk1.pickle","wb") as file:
    pickle.dump(imgpoints,file)
with open("k1k3/imagepointsk3.pickle","wb") as file:
    pickle.dump(imgpoints2,file)
with open("k1k3/objectpointsk1k3.pickle","wb") as file:
    pickle.dump(objpoints,file)


criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((6 * 9, 3), np.float32)
objp[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)
objp=objp*25.1

objpoints = []
imgpoints = []
imgpoints2 = []
k = 0
for i in range(2942):
    frame = cv2.imread(f"Z:/BazaNexus/Praktykanci/K2/frame{k}.jpg")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)
    if ret == False:
        print('Dzieki,dziala')
    if ret == True:
        frame2 = cv2.imread(f"Z:/BazaNexus/Praktykanci/K3/frame{k}.jpg")
        gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret2, corners3 = cv2.findChessboardCorners(gray, (9, 6), None)
        if ret2==True:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            corners4 = cv2.cornerSubPix(gray2, corners3, (11, 11), (-1, -1), criteria)
            imgpoints2.append(corners4)
            imgpoints.append(corners2)
            print(k)
    k+=1

with open("k2k3/imagepointsk2.pickle","wb") as file:
    pickle.dump(imgpoints,file)
with open("k2k3/imagepointsk3.pickle","wb") as file:
    pickle.dump(imgpoints2,file)
with open("k2k3/objectpointsk2k3.pickle","wb") as file:
    pickle.dump(objpoints,file)