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
    _, contours, hierarchy = cv2.findContours(fgmask,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)	
    cv2.drawContours(fgmask, contours, -1, (0,255,0),1)
    print len(contours)
    hull = [cv2.convexHull(cnt) for cnt in contours]
    hull = np.array(hull)
    cnt = contours[0]
    if (len(cnt) == 0):
    	continue
    
    defects = cv2.convexityDefects(cnt,hull)

    for i in range(defects.shape[0]):
	s,e,f,d = defects[i,0]
	start = tuple(cnt[s][0])
	end = tuple(cnt[e][0])
	far = tuple(cnt[f][0])
	cv2.line(fgmask,start,end,[0,255,0],2)
	cv2.circle(fgmask,far,5,[0,0,255],-1)
    #params.minThreshold = 10
    #params.maxThreshold = 200
    cv2.imshow("lol",fgmask)
    
# Filter by Area.
    params.filterByArea = True
    params.minArea = 300
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
