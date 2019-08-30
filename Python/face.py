from imutils import face_utils, translate, resize
import dlib
import cv2
import numpy as np
kozak1=[[[np.array([-0.9444311]), np.array([0.51524417]), np.array([-0.86076623])]], [[np.array([2.59185785]), np.array([-1.05053156]), np.array([1.51689407])]], [[np.array([-0.11953029]), np.array([1.87933391]), np.array([4.59828687])]], [[np.array([23.82093403]), np.array([23.3855359]), np.array([-7.16599031])]], [[np.array([0.83326034]), np.array([0.97167888]), np.array([-0.28417912])]], [[np.array([1.00798524]), np.array([0.43389733]), np.array([0.63365589])]], [[np.array([1.33289116]), np.array([2.13965402]), np.array([11.78509451])]], [[np.array([1.28283652]), np.array([0.61512279]), np.array([-1.2369959])]], [[np.array([-0.38173876]), np.array([1.07380049]), np.array([1.61103363])]], [[np.array([2.44797524]), np.array([2.14183264]), np.array([8.15152424])]], [[np.array([-7.69946033]), np.array([10.27520562]), np.array([5.1286794])]], [[np.array([1.53330339]), np.array([0.89436533]), np.array([-4.09401239])]], [[np.array([1.84751017]), np.array([-2.02336589]), np.array([0.49605926])]], [[np.array([-0.73176568]), np.array([0.15315361]), np.array([-2.64393626])]], [[np.array([-10.80940772]), np.array([8.73680543]), np.array([12.90050548])]], [[np.array([0.77617008]), np.array([0.06332783]), np.array([0.91561728])]], [[np.array([0.04378608]), np.array([-0.16152392]), np.array([0.35073041])]], [[np.array([-118.24116803]), np.array([-84.97617676]), np.array([89.91592428])]], [[np.array([0.36110508]), np.array([0.51897118]), np.array([1.00982286])]], [[np.array([-0.38955851]), np.array([1.88618035]), np.array([0.12859143])]], [[np.array([2.20031014]), np.array([-0.57817194]), np.array([1.80411977])]], [[np.array([-10910.043654]), np.array([-57.38713206]), np.array([57994.85125303])]], [[np.array([-2.48019918]), np.array([0.00583995]), np.array([-0.95772737])]], [[np.array([-0.02285297]), np.array([0.79143229]), np.array([-0.76067164])]], [[np.array([-4.39627379]), np.array([5.54996947]), np.array([2.09395967])]], [[np.array([-3.13062363]), np.array([1.16081503]), np.array([-2.18908672])]], [[np.array([0]), np.array([0]), np.array([-0])]], [[np.array([0.72972454]), np.array([-2.56231241]), np.array([-1.04077901])]], [[np.array([1.07059661]), np.array([-0.06793011]), np.array([-1.04369816])]], [[np.array([0.73985924]), np.array([0.98445529]), np.array([-0.08258083])]], [[np.array([-0.69977767]), np.array([0.31979703]), np.array([-0.7070492])]], [[np.array([3.9077985]), np.array([-1.73362157]), np.array([-3.18775847])]], [[np.array([0.99940502]), np.array([-1.29089915]), np.array([-1.32506239])]], [[np.array([0.84114916]), np.array([-1.18698307]), np.array([-0.99955035])]], [[np.array([1.32494597]), np.array([-0.66762979]), np.array([-1.30669456])]], [[np.array([0.02054456]), np.array([1.89877169]), np.array([0.13125742])]], [[np.array([0.25333613]), np.array([-0.39495055]), np.array([-3.09613529])]], [[np.array([-1.08050144]), np.array([0.44212955]), np.array([-0.19624235])]], [[np.array([0.23392586]), np.array([2.97619996]), np.array([2.88543732])]], [[np.array([4.17071469]), np.array([-3.55259734]), np.array([-1.26842053])]], [[np.array([0.24336847]), np.array([0.30493903]), np.array([0.61952541])]], [[np.array([0.68410238]), np.array([-0.31714123]), np.array([-0.29466357])]], [[np.array([2.18745374]), np.array([-2.59473496]), np.array([-0.4028674])]], [[np.array([1.62451494]), np.array([-1.07181552]), np.array([-2.52113675])]], [[np.array([0.30754095]), np.array([-1.55801585]), np.array([-0.35834793])]], [[np.array([-0.50507648]), np.array([0.00749654]), np.array([0.63116278])]], [[np.array([3.47679641]), np.array([-5.43076845]), np.array([-2.18180822])]], [[np.array([-0.3625339]), np.array([1.23631042]), np.array([-0.19542902])]], [[np.array([-0.76563947]), np.array([1.87740813]), np.array([-0.45569886])]], [[np.array([0.19133674]), np.array([0.32614126]), np.array([0.62829095])]], [[np.array([0.6788464]), np.array([3.57691317]), np.array([-2.62091813])]], [[np.array([0.55116258]), np.array([-0.79167587]), np.array([-0.15018793])]]]
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)
j=0
camera = cv2.VideoCapture("P3.avi")
list=[]
while True:

    _, image = camera.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 0)
    dist=np.array([[-4.31349472e-01 , 2.83291049e+01 ,-2.90680923e-03 , 1.45047909e-03,-8.00154071e+02]])
    mtx=np.array([[4.35910328e+03, 0.00000000e+00 ,1.05139738e+03],[0.00000000e+00,4.37245777e+03, 6.24011532e+02],[0.00000000e+00 ,0.00000000e+00, 1.00000000e+00]])
    gray=cv2.undistort(gray,mtx,dist)
    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        # kozak=[shape[27],shape[30],shape[31],shape[33],shape[35],shape[36],shape[39],shape[42],shape[45],shape[48],shape[54]]
        # kozak=[shape[36],shape[39],shape[27],shape[42],shape[45],shape[30],shape[31],shape[35],shape[48],shape[54]]
        # print(kozak)

        import pickle

        with open("test3.pickle", "wb") as file:
            objectpoints = pickle.dump(shape,file)

        for point in shape:
            cv2.circle(image, tuple(point), 3, (0, 255, 0), -1)
    cv2.putText(image, text=f"{kozak1[j][0]}", org=(200, 200), fontFace=20, fontScale=1, color=(0, 0, 0))

    cv2.imshow("kozak",image)
    j+=1
    if j==1:
        break
    k = cv2.waitKey(5) & 0xFF

    if k == 27:
        break

cv2.destroyAllWindows()
camera.release()
