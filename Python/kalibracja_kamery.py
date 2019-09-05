import numpy as np
import cv2
import glob

"""
kalibracja kamery na podstawie zdjęć z nagrań kalibracyjnych
używana jest tablica kalibracyjna z szachownicą gdzie długość
jednej kratki to 251mm
"""
rozm_zdj=(1920,1200)
fname = glob.glob("Z:\BazaNexus\Praktykanci\K3\*.jpg")
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((6 * 9, 3), np.float32)
objp[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)
objp=objp*25.1
objpoints = []
imgpoints = []
k = 0
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
print(f"blad reprojekcji: {ret}")
"""
zapisywanie potrzebnych wartości kalibracji kamery
do plików formatu pickle
potrzebne są potem do kalibracji stereo
"""
with open("k3\mtxvideo.pickle","wb") as file:
    pickle.dump(mtx,file)
with open("k3\distvideo.pickle","wb") as file:
    pickle.dump(dist,file)
with open("k3/rvecs.pickle","wb") as file:
    pickle.dump(rvecs,file)
with open("k3/tvecs.pickle","wb") as file:
    pickle.dump(tvecs,file)




"""
wybieranie wspólnych klatek dla pary kamer na których 
jest wykrywana tablica kalibracyjna i sciąganie z nich punktów
jest to potrzebne aby stereo kalibracja była poprawnie przeprowadzona
"""
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((6 * 9, 3), np.float32)
objp[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)
objp=objp*25.1
objpoints = []
imgpoints = []
imgpoints2 = []
k = 0
for i in range(1729):
    frame = cv2.imread(f"Z:/BazaNexus/Praktykanci/K2/frame{1210+k}.jpg")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)
    if ret == False:
        print('Dzieki,dziala')
    if ret == True:
        frame2 = cv2.imread(f"Z:/BazaNexus/Praktykanci/K3/frame{1210+k}.jpg")
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
"""
zapisywanie image i object pointsów do plików formatu pickle
zeby potem ich uzyc do stereo kalibracji
"""
with open("k2k3/imagepointsk2.pickle","wb") as file:
    pickle.dump(imgpoints,file)
with open("k2k3/imagepointsk3.pickle","wb") as file:
    pickle.dump(imgpoints2,file)
with open("k2k3/objectpointsk2k3.pickle","wb") as file:
    pickle.dump(objpoints,file)