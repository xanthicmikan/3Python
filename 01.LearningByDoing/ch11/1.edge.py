import cv2


def get_edge(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (13, 13), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny


img = cv2.imread('road.jpg')
edge = get_edge(img)
cv2.imshow('Edge', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
