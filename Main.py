import cv2.cv2 as cv
from Functions import Functions

def main():

#przykładowy obraz:
    img = 'lenna.bmp'
    Functions.show('original image', cv.imread(img))
    Functions.show('negative',Functions.negative(img))
    Functions.show('grayed out',Functions.grayedOut(img))
    Functions.show('histogram equalizing',Functions.equalizeHistogram(img))
    Functions.show('scaling',Functions.scaling(img,0.5))
    Functions.show('thresh binary', Functions.threshBinary(img))
    Functions.show('blurring', Functions.imageBlurring(img, 5))
    Functions.show('Gaussian blurring', Functions.GaussianBlurring(img, 5))
    Functions.show('median blurring', Functions.medianBlur(img, 5))


if __name__ == "__main__":
    main()