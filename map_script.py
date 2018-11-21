import cv2
import numpy as np

img = cv2.imread('test2.tiff',-1)

# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
e1 = cv2.getTickCount()

for i in range(1000):
	h,w = np.shape(img)
	base = np.full((h,w,3), 255, np.uint8)

	ret1,thresh1 = cv2.threshold(img,0, 255,cv2.THRESH_BINARY)
	ret2,thresh2 = cv2.threshold(img,70,255,cv2.THRESH_BINARY)
	# cv2.cvtColor(thresh2, cv2.COLOR_BGR2GRAY)
	out = thresh2.astype(np.uint8)
	dummy = np.zeros((h+4, w+4), np.uint8)
	dummy[2:h+2,2:w+2] = out
	dummy[1,:] = 255
	dummy[h+1,:] = 255
	dummy[:,1] = 255
	dummy[:,w+1] = 255
	contours, hierarchy = cv2.findContours(dummy,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	for c in contours:
		c[:,0,:] = c[:,0,:] -2
		if cv2.pointPolygonTest(c, (5,5), False) > 0:
			cnt = c

	cv2.fillPoly(base, [cnt], (255,0,0))
	# cv2.imshow('image',base)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print time