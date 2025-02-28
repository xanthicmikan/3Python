import cv2

im = cv2.imread('turnR.jpg')
#im = cv2.imread('turnL.jpg')#NoMatch
detector = cv2.CascadeClassifier('haar_turnR.xml')
sign = detector.detectMultiScale(im,
                                  scaleFactor=1.1,
                                  minNeighbors=2,
                                  minSize=(30, 30))
if len(sign) > 0:
    for (x, y, w, h) in sign:
        cv2.rectangle(im,
                      (x, y), (x+w, y+h),
                      (0, 0, 255), 2)
else:
    print('Nothing match')

cv2.imshow('Frame', im)
cv2.waitKey(0)
cv2.destroyAllWindows()