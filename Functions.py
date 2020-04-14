import cv2.cv2 as cv

#funkcja wyświetlania obrazu
def show(name, image):

    __img = cv.imread(image)
    cv.imshow(name, __img)
    cv.waitKey(0)
    cv.destroyAllWindows()



#negatyw obrazu
def negative(image):
    __img = cv.imread(image)
    __shape = __img.shape

    for px in range(__shape[0]):
        for py in range(__shape[1]):
            __img[px,py] = [255-__img[px,py][0], 255-__img[px,py][1], 255-__img[px,py][2]]

    cv.imshow('negative', __img)
    cv.waitKey(0)
    cv.destroyAllWindows()




