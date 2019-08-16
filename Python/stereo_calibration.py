import glob
import cv2
import numpy as np
import pickle
with open ("OBJECTPOINTS.pickle","rb") as file:
    objectpoints=pickle.load(file)
with open ("IMAGEPOINTSLEFT.pickle","rb") as file:
    imagepoints1=pickle.load(file)
with open ("IMAGEPOINTSRIGHT.pickle","rb") as file:
    imagepoints2=pickle.load(file)

cameramatrix1=np.array([[1155.10032, 0.0, 599.616631],
 [0.0, 1141.68758, 505.226607],
 [0.0, 0.0,1.0]])
cameramatrix2=np.array([[1167.58511, 0.0, 635.841114],
 [0.0, 1157.18929, 559.695009],
 [0.0, 0.0, 1.0]])
dist1=np.array([[-0.1406258 ,  0.36306865, -0.00418759, -0.00513541, -0.4840844 ]])
dist2=np.array([[-0.09380673, -0.10257934, -0.0018907 , -0.00323752 , 0.40330875]])
img=cv2.imread('img00111_l.bmp')
img_size = (img.shape[1], img.shape[0])
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 70, 0.001)
flags = 0
flags |= cv2.CALIB_FIX_INTRINSIC
flags |= cv2.CALIB_USE_INTRINSIC_GUESS
error,mtxx1,disst1,mtxx2,disst2,R,E,T,F=cv2.stereoCalibrate(objectpoints,imagepoints1,imagepoints2,cameramatrix1,dist1,cameramatrix2,dist2,img_size,flags=flags)




with open("error.pickle","wb") as file:
    pickle.dump(error,file)
with open("mtxx1.pickle","wb") as file:
    pickle.dump(mtxx1,file)
with open("mtxx2.pickle", "wb") as file:
    pickle.dump(mtxx2,file)

with open("disst1.pickle","wb") as file:
    pickle.dump(disst1,file)
with open("disst2.pickle","wb") as file:
    pickle.dump(disst2,file)
with open("R.pickle", "wb") as file:
    pickle.dump(R,file)

with open("T.pickle","wb") as file:
    pickle.dump(T,file)
with open("E.pickle","wb") as file:
    pickle.dump(E,file)
with open("F.pickle", "wb") as file:
    pickle.dump(F,file)
