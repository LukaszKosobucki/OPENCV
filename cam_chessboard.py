import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Display the resulting frame
    ret2, corners = cv2.findChessboardCorners(frame, (5, 8),None)
    cv2.drawChessboardCorners(frame,(5,8),corners,ret)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
