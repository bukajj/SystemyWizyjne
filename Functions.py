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


#konwersja do odcieni szarości wg modelu YUV
def grayedOut(image):

    __img = cv.imread(image)
    __shape = __img.shape

    for px in range(__shape[0]):
        for py in range(__shape[1]):
            val = __img[px,py][0] * 0.299 + __img[px,py][1] * 0.587 + __img[px,py][2]*0.114
            __img[px, py] = [val, val, val]

    cv.imshow('grayed out', __img)
    cv.waitKey(0)
    cv.destroyAllWindows()


#normalizacja histogramu przy użyciu biblioteki openCV
def equalizeHistogram(image):

    __img = cv.imread(image,0)
    __img = cv.equalizeHist(__img)

    cv.imshow('histogram equalization', __img)
    cv.waitKey(0)
    cv.destroyAllWindows()
