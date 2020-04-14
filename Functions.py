import cv2.cv2 as cv

#funkcja wyświetlania obrazu
def show(name, image):

    img = cv.imread(image)
    cv.imshow(name, img)
    cv.waitKey(0)
    cv.destroyAllWindows()



#negatyw obrazu
def negative(image):
    img 
