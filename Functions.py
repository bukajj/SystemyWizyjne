import cv2.cv2 as cv
import numpy as np
from skimage.morphology import medial_axis
from matplotlib import pyplot as plt
from skimage.util import invert
from skimage import color



# funkcja wyświetlania obrazu
def show(name, img):

    cv.imshow(name, img)
    cv.waitKey(0)
    cv.destroyAllWindows()


# negatyw obrazu
def negative(img):

    __shape = img.shape

    for px in range(__shape[0]):
        for py in range(__shape[1]):
            img[px, py] = [255 - img[px, py][0], 255 - img[px, py][1], 255 - img[px, py][2]]

    return img


# konwersja do odcieni szarości wg modelu YUV
def grayedOut(img):

    __shape = img.shape

    for px in range(__shape[0]):
        for py in range(__shape[1]):
            val = img[px, py][0] * 0.299 + img[px, py][1] * 0.587 + img[px, py][2] * 0.114
            img[px, py] = [val, val, val]

    return img


# normalizacja histogramu przy użyciu biblioteki openCV
def equalizeHistogram(img):

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.equalizeHist(img)

    img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

    return img


# skalowanie
def scaling(img, scaleX, scaleY):

    img = cv.resize(img, None, fx=scaleX, fy=scaleY, interpolation=cv.INTER_CUBIC)

    return img


# progowanie (binaryzacja)
def threshBinary(img):

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret,img = cv.threshold(img,128,255,cv.THRESH_BINARY)

    img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

    return  img


# filtry - rozmycie
def imgBlurring(img):

    return cv.blur(img, (5,5))


# filtry - rozmycie Gaussa
def GaussianBlurring(img):

    img = cv.GaussianBlur(img, (5,5),0)

    return img


#filtry - filtr medianowy
def medianBlur(img):


    img = cv.medianBlur(img,5)

    return img


# zmiana przestrzeni kolorów
def changingColorSpace_BGR2GRAY(img):

    img = img
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    return img

def changingColorSpace_BGR2HSV(img):

    img = img
    img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    return img


# rotacja
def rotation(img, angle):


    __rows,__cols,__colors = img.shape

    __M = cv.getRotationMatrix2D((__cols/2,__rows/2),angle,1)
    img = cv.warpAffine(img,__M,(__cols,__rows))

    return img


# zmiana jasności
def brightnessChanging(img, isBrighter):


    __shape = img.shape

    for px in range(__shape[0]):
        for py in range(__shape[1]):
            for c in range(__shape[2]):
                if isBrighter == True:
                    img[px, py][c] = min(img[px,py][c] + 50, 255)
                else:
                    img[px, py][c] = max(img[px,py][c] - 50, 0)

    return img


# detekcja krawędzi
def cannyEdgeDetection(img):

    return cv.Canny(img,100,200)


# segmentacja z użyciem binaryzacji Otsu
def segmentationOtsu(img):


    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.GaussianBlur(img,(5,5),0)
    __ret, img = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

    return img


# segmentacja - wyznaczanie progów na podstawie histogramu
def segmentationBinarizationHist(img):


    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.equalizeHist(img)
    ret, img = cv.threshold(img, 128, 255, cv.THRESH_BINARY)
    img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

    return img


# segmentacja - watershed algorithm
def watershedAlgorithm(img):


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
def skel(img):


    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    skel = medial_axis(img)

    for px in range(skel.shape[0]):
        for py in range(skel.shape[1]):
            if skel[px,py] == True:
                img[px,py] = 255
            else:
                img[px,py] = 0

    return cv.cvtColor(img, cv.COLOR_GRAY2BGR)


# erozja
def erosion(img):

    kernel = np.ones((5,5),np.uint8)
    return cv.erode(img, kernel)


def get_grayscale(img):

    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def dilate(img):

    kernel = np.ones((5,5),np.uint8)
    return cv.dilate(img, kernel, iterations = 1)

def opening(image):

    kernel = np.ones((5,5),np.uint8)
    return cv.morphologyEx(image, cv.MORPH_OPEN, kernel)

def thresholding(image):
    # threshold the image, setting all foreground pixels to
    # 255 and all background pixels to 0
    return cv.threshold(image, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]

#skew correction
def deskew(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = cv.bitwise_not(gray)
    thresh = cv.threshold(gray, 0, 255,
        cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv.warpAffine(image, M, (w, h),
        flags=cv.INTER_CUBIC, borderMode=cv.BORDER_REPLICATE)    
    return rotated

#template matching
def match_template(image, template):
    return cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)




