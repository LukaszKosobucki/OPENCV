from imutils import face_utils, translate, resize
import dlib
import cv2
import numpy as np

p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

camera = cv2.VideoCapture("P3.avi")

while True:

    _, image = camera.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 0)
    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        kozak=[shape[27],shape[30],shape[31],shape[35],shape[36],shape[39],shape[42],shape[45],shape[48],shape[54]]
        shape=kozak
        for point in shape:
            cv2.circle(image, tuple(point), 3, (0, 255, 0), -1)

    cv2.imshow("Output", image)

    k = cv2.waitKey(5) & 0xFF

    if k == 27:
        break

cv2.destroyAllWindows()
camera.release()
