import cv2.cv2 as cv
import numpy as np
from skimage.morphology import medial_axis
from matplotlib import pyplot as plt
from skimage.util import invert
from skimage import color



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
def imageBlurring(image):

    __img = cv.imread(image)
    __img = cv.blur(__img, (5,5))

    return __img


# filtry - rozmycie Gaussa
def GaussianBlurring(image):

    __img = cv.imread(image)
    __img = cv.GaussianBlur(__img, (5,5),0)

    return __img


#filtry - filtr medianowy
def medianBlur(image):

    __img = cv.imread(image)
    __img = cv.medianBlur(__img,5)

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


# detekcja krawędzi
def cannyEdgeDetection(image):

    __img = cv.imread(image)
    __img = cv.Canny(__img,50,200)

    return __img


# segmentacja z użyciem binaryzacji Otsu
def segmentationOtsu(image):

    __img = cv.imread(image, 0)
    __img = cv.GaussianBlur(__img,(5,5),0)
    __ret, __img = cv.threshold(__img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

    return __img


# segmentacja - wyznaczanie progów na podstawie histogramu
def segmentationBinarizationHist(image):

    __img = cv.imread(image,0)
    __img = cv.equalizeHist(__img)
    ret, __img = cv.threshold(__img, 128, 255, cv.THRESH_BINARY)

    return __img


# segmentacja - watershed algorithm
def watershedAlgorithm(image):

    img = cv.imread(image)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

    # noise removal
    kernel = np.ones((5, 5), np.uint8)
    opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)

    # sure background area
    sure_bg = cv.dilate(opening, kernel, iterations=3)

    # Finding sure foreground area
    dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
    ret, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv.subtract(sure_bg, sure_fg)

    # Marker labelling
    ret, markers = cv.connectedComponents(sure_fg)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 1

    # Now, mark the region of unknown with zero
    markers[unknown == 255] = 0

    markers = cv.watershed(img, markers)
    img[markers == -1] = [255, 0, 0]

    return img


# szkieletyzacja
def skel(image):

    img = cv.imread(image)
    img = color.rgb2gray(img)
    skel = medial_axis(img)

    for px in range(skel.shape[0]):
        for py in range(skel.shape[1]):
            if skel[px,py] == True:
                img[px,py] = 255
            else:
                img[px,py] = 0

    return img


# erozja
def erosion(image):

    img = cv.imread(image)
    kernel = np.ones((5,5),np.uint8)
    img = cv.erode(img, kernel)

    return img