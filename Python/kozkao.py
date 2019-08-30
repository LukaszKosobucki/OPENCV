import numpy as np
import cv2
#macierz R|T
rotacjaitranslacja=np.array([[ 3.11664586e-02 ,-5.32364646e-04, -9.99514066e-01,1253.72176163],
 [ 1.54623293e-01 , 9.87964164e-01 , 4.29519045e-03,-32.04345308],
 [ 9.87481792e-01, -1.54682022e-01,  3.08736602e-02,974.11997952]])
#camera matrix
kamera1=np.array([[4.56094516e+03, 0.00000000e+00,8.29290621e+02],
 [0.00000000e+00, 4.28301037e+03, 6.30447644e+02],
 [0.00000000e+00 ,0.00000000e+00 ,1.00000000e+00]])
#punkt w pixelach na klatce video
x=np.array([[1146],
            [544],
            [1]])
x2=np.array([[1298],
                [663],
                [1]])
kamera2=np.array([[4.46479976e+03 ,0.00000000e+00, 1.03132561e+03],
 [0.00000000e+00, 4.47554747e+03, 6.85670509e+02],
 [0.00000000e+00 ,0.00000000e+00 ,1.00000000e+00]])
#macierze projekcji
projekcji2=kamera2@rotacjaitranslacja
projekcji=kamera1@rotacjaitranslacja
#odwrocone macierze projekcji
projekcjinv=cv2.invert(projekcji,flags=cv2.DECOMP_SVD)
projekcjinv2=cv2.invert(projekcji2,flags=cv2.DECOMP_SVD)
print(projekcjinv)
#wektor 4x1 z punktami i skalarem
punkt2=projekcjinv2[1]@x2
punkt=projekcjinv[1]@x
punkt2=punkt2/punkt2[3]
punkt=punkt/punkt[3]
print(punkt)
#wysrednienie 1 punktu z 2 kamer
punktsredni=(punkt+punkt2)/2
print(np.sqrt(punktsredni[0]**2+punktsredni[1]**2+punktsredni[2]**2))
kozak3=[np.array([[926], [520], [1]]), np.array([[936], [592], [1]]), np.array([[955], [658], [1]]), np.array([[974], [723], [1]]), np.array([[997], [785], [1]]), np.array([[1030], [843], [1]]), np.array([[1072], [895], [1]]), np.array([[1123], [937], [1]]), np.array([[1182], [947], [1]]), np.array([[1244], [934], [1]]), np.array([[1302], [894], [1]]), np.array([[1352], [841], [1]]), np.array([[1393], [780], [1]]), np.array([[1419], [709], [1]]), np.array([[1433], [632], [1]]), np.array([[1442], [553], [1]]), np.array([[1444], [474], [1]]), np.array([[936], [499], [1]]), np.array([[966], [470], [1]]), np.array([[1008], [467], [1]]), np.array([[1052], [477], [1]]), np.array([[1095], [495], [1]]), np.array([[1187], [490], [1]]), np.array([[1232], [468], [1]]), np.array([[1282], [452], [1]]), np.array([[1332], [452], [1]]), np.array([[1376], [472], [1]]), np.array([[1147], [545], [1]]), np.array([[1150], [600], [1]]), np.array([[1151], [655], [1]]), np.array([[1153], [711], [1]]), np.array([[1107], [731], [1]]), np.array([[1131], [741], [1]]), np.array([[1159], [748], [1]]), np.array([[1188], [738], [1]]), np.array([[1212], [725], [1]]), np.array([[991], [551], [1]]), np.array([[1020], [545], [1]]), np.array([[1052], [545], [1]]), np.array([[1085], [559], [1]]), np.array([[1052], [568], [1]]), np.array([[1018], [568], [1]]), np.array([[1230], [551], [1]]), np.array([[1260], [533], [1]]), np.array([[1294], [530], [1]]), np.array([[1329], [533], [1]]), np.array([[1298], [551], [1]]), np.array([[1264], [556], [1]]), np.array([[1079], [809], [1]]), np.array([[1109], [798], [1]]), np.array([[1138], [789], [1]]), np.array([[1161], [794], [1]]), np.array([[1186], [786], [1]]), np.array([[1220], [790], [1]]), np.array([[1257], [798], [1]]), np.array([[1223], [828], [1]]), np.array([[1191], [842], [1]]), np.array([[1164], [846], [1]]), np.array([[1140], [845], [1]]), np.array([[1109], [834], [1]]), np.array([[1093], [810], [1]]), np.array([[1139], [810], [1]]), np.array([[1162], [813], [1]]), np.array([[1187], [808], [1]]), np.array([[1241], [801], [1]]), np.array([[1187], [809], [1]]), np.array([[1162], [815], [1]]), np.array([[1138], [812], [1]])]


print(x)
punktowania=[]
for i in range (len(kozak3)):
    kalamarnica=projekcjinv[1]@kozak3[i]
    kozakooo=kalamarnica / kalamarnica[3]
    punktowania.append([kozakooo[:3]])
print(punktowania)

