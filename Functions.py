import cv2.cv2 as cv

class Functions:

    # funkcja wyświetlania obrazu
    def show(name, image):

        cv.imshow(name, image)
        cv.waitKey(0)
        cv.destroyAllWindows()


    # negatyw obrazu
    def negative(image):

        __img = cv.imread(image)
        __shape = __img.shape

        for px in range(__shape[0]):
            for py in range(__shape[1]):
                __img[px, py] = [255 - __img[px, py][0], 255 - __img[px, py][1], 255 - __img[px, py][2]]

        return __img


    # konwersja do odcieni szarości wg modelu YUV
    def grayedOut(image):

        __img = cv.imread(image)
        __shape = __img.shape

        for px in range(__shape[0]):
            for py in range(__shape[1]):
                val = __img[px, py][0] * 0.299 + __img[px, py][1] * 0.587 + __img[px, py][2] * 0.114
                __img[px, py] = [val, val, val]

        return __img


    # normalizacja histogramu przy użyciu biblioteki openCV
    def equalizeHistogram(image):

        __img = cv.imread(image, 0)
        __img = cv.equalizeHist(__img)

        return __img


    # skalowanie
    def scaling(image, scale):

        __img = cv.imread(image)
        __img = cv.resize(__img, None, fx=scale, fy=scale, interpolation=cv.INTER_CUBIC)

        return __img


    # progowanie (binaryzacja)
    def threshBinary(image):

        __img = cv.imread(image,0)
        ret,__img = cv.threshold(__img,128,255,cv.THRESH_BINARY)

        return  __img


    # filtry - rozmycie
    def imageBlurring(image, kernel):

        __img = cv.imread(image)
        __img = cv.blur(__img, (kernel,kernel))

        return __img


    # filtry - rozmycie Gaussa
    def GaussianBlurring(image,kernel):

        __img = cv.imread(image)
        __img = cv.GaussianBlur(__img, (kernel, kernel),0)

        return __img


    #filtry - filtr medianowy
    def medianBlur(image, kernel):

        __img = cv.imread(image)
        __img = cv.medianBlur(__img,kernel)

        return __img


    # zmiana przestrzeni kolorów
    def changingColorSpace_BGR2GRAY(image):

        __img = cv.imread(image)
        __img = cv.cvtColor(__img, cv.COLOR_BGR2GRAY)

        return __img

    def changingColorSpace_BGR2HSV(image):

        __img = cv.imread(image)
        __img = cv.cvtColor(__img, cv.COLOR_BGR2HSV)

        return __img


    # rotacja
    def rotation(image, angle):

        __img = cv.imread(image)
        __rows,__cols,__colors = __img.shape

        __M = cv.getRotationMatrix2D((__cols/2,__rows/2),angle,1)
        __img = cv.warpAffine(__img,__M,(__cols,__rows))

        return __img


    # zmiana jasności
    def brightnessChanging(image, isBrighter):

        __img = cv.imread(image)
        __shape = __img.shape

        for px in range(__shape[0]):
            for py in range(__shape[1]):
                for c in range(__shape[2]):
                    if isBrighter == True:
                        __img[px, py][c] = min(__img[px,py][c] + 50, 255)
                    else:
                        __img[px, py][c] = max(__img[px,py][c] - 50, 0)

        return __img




