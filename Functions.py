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
                __img[px, py] = [256 - __img[px, py][0], 256 - __img[px, py][1], 256 - __img[px, py][2]]

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


