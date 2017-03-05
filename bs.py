import numpy as np
import cv2

cap = cv2.VideoCapture('M6 Motorway Traffic-PNCJQkvALVc.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
 
    cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)
    params = cv2.SimpleBlobDetector_Params()
    #params.minThreshold = 10
    #params.maxThreshold = 200

# Filter by Area.
    params.filterByArea = True
    params.minArea = 1500
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
    else : 
	detector = cv2.SimpleBlobDetector_create(params)


# Detect blobs.
    keypoints = detector.detect(fgmask)
    im_with_keypoints = cv2.drawKeypoints(fgmask, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("Keypoints", im_with_keypoints)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()
