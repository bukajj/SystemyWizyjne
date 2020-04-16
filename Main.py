from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from UI import UI
from PyQt5.QtGui import QColor
from Functions import *
import cv2.cv2 as cv


class Main(QWidget, UI):

    angle = 90
    scaleX = 0.5
    scaleY = 0.5
    isBrighter = True

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUI(self)

        self.lcd.display(self.angle)
        self.slider.setSliderPosition(self.angle)

        self.lcd1.display(self.scaleX)
        self.slider1.setSliderPosition(self.scaleX*100)

        self.lcd2.display(self.scaleY)
        self.slider2.setSliderPosition(self.scaleY*100)

        self.originalBtn.clicked.connect(self.execute)
        self.negativeBtn.clicked.connect(self.execute)
        self.grayedOutBtn.clicked.connect(self.execute)
        self.histEqualizeBtn.clicked.connect(self.execute)
        self.binarizationBtn.clicked.connect(self.execute)
        self.blurBtn.clicked.connect(self.execute)

        self.gaussBtn.clicked.connect(self.execute)
        self.medianBtn.clicked.connect(self.execute)
        self.rgb2grayBtn.clicked.connect(self.execute)
        self.rgb2hsvBtn.clicked.connect(self.execute)
        self.cannyBtn.clicked.connect(self.execute)

        self.otsuBtn.clicked.connect(self.execute)
        self.segHistBtn.clicked.connect(self.execute)
        self.watershedBtn.clicked.connect(self.execute)
        self.skelBtn.clicked.connect(self.execute)
        self.erosionBtn.clicked.connect(self.execute)
        self.chkGroup.buttonClicked[int].connect(self.setBright)
        self.brighterBtn.clicked.connect(self.execute)

        self.slider.valueChanged.connect(self.changeAngle)
        self.rotatingBtn.clicked.connect(self.execute)
        self.slider1.valueChanged.connect(self.changeScaleX)
        self.slider2.valueChanged.connect(self.changeScaleY)
        self.scalingBtn.clicked.connect(self.execute)


    def execute(self):

        img = 'lenna.bmp'

        sender = self.sender()

        if sender.text() == 'Oryginał':
            image = cv.imread(img)
            show('Oryginał', image)
        elif sender.text() == 'Negatyw':
            show('Negatyw', negative(img))
        elif sender.text() == 'Szarość':
            show('Szarość',grayedOut(img))
        elif sender.text() == 'Normalizacja histogramu':
            show('Normalizacja histogramu', equalizeHistogram(img))
        elif sender.text() == 'Binaryzacja':
            show('Binaryzacja', threshBinary(img))
        elif sender.text() == 'Rozmycie':
            show('Rozmycie', imageBlurring(img))
        elif sender.text() == 'Rozmycie Gaussa':
            show('Rozmycie Gaussa',GaussianBlurring(img))
        elif sender.text() == 'Filtr medianowy':
            show('Filtr medianowy', medianBlur(img))
        elif sender.text() == 'Przestrzeń kolorów RGB->GRAY':
            show('Przestrzeń kolorów RGB->GRAY', changingColorSpace_BGR2GRAY(img))
        elif sender.text() == 'Przestrzeń kolorów RGB->HSV':
            show('Przestrzeń kolorów RGB->HSV', changingColorSpace_BGR2HSV(img))
        elif sender.text() == 'Detekcja krawędzi':
            show('Detekcja krawędzi', cannyEdgeDetection(img))
        elif sender.text() == 'Segmentacja Otsu':
            show('Segmentacja Otsu',segmentationOtsu(img))
        elif sender.text() == 'Segmentacja - wyznaczanie progów na podstawie histogramu':
            show('Segmentacja - wyznaczanie progów na podstawie histogramu', segmentationBinarizationHist(img))
        elif sender.text() == 'Segmentacja - watershed algorithm':
            show('Segmentacja - watershed algorithm', watershedAlgorithm(img))
        elif sender.text() == 'Szkieletyzacja':
            show('Szkieletyzacja', skel(img))
        elif sender.text() == 'Erozja':
            show('Erozja', erosion(img))
        elif sender.text() == 'Rotacja':
            show('Rotacja', rotation(img, self.angle))
        elif sender.text() == 'Skalowanie':
            show('Skalowanie', scaling(img, self.scaleX, self.scaleY))
        else:
            show('Jasnść', brightnessChanging(img, self.isBrighter))


    def changeAngle(self, value):

        try:
            value = int(value)
        except ValueError:
            value = 0

        self.angle = value
        self.lcd.display(self.angle)

    def changeScaleX(self, value):

        try:
            value = int(value)
        except ValueError:
            value = 0

        self.scaleX = value/100
        self.lcd1.display(self.scaleX)

    def changeScaleY(self, value):

        try:
            value = int(value)
        except ValueError:
            value = 0

        self.scaleY = value/100
        self.lcd2.display(self.scaleY)


    def setBright(self, value):

        if value == 0:
            self.isBrighter = True
        else:
            self.isBrighter = False


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Main()
    window.show()

    sys.exit(app.exec_())


