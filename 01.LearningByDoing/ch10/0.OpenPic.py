import cv2
try:
    img = cv2.imread('Lenna.jpg')             
    img_small = cv2.resize(img, (100, 100)) 
    cv2.imshow('Frame1', img)               
    cv2.imshow('Frame2', img_small)         
    cv2.waitKey(0)                          
    cv2.destroyAllWindows()                 
    try:
        cv2.imwrite('small.jpg', img_small) 
        print('saved')
    except:
        print('Error：write')
except:
    print('Error：read')
