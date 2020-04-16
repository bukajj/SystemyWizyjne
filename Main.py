from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from UI import UI
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPixmap, QImage
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
        self.slider1.setSliderPosition(self.scaleX*200)

        self.lcd2.display(self.scaleY)
        self.slider2.setSliderPosition(self.scaleY*10)

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
            self.setImage(image)
        elif sender.text() == 'Negatyw':
            self.setImage(negative(img))
        elif sender.text() == 'Szarość':
            self.setImage(grayedOut(img))
        elif sender.text() == 'Normalizacja histogramu':
            self.setImage(equalizeHistogram(img))
        elif sender.text() == 'Binaryzacja':
            self.setImage(threshBinary(img))
        elif sender.text() == 'Rozmycie':
            self.setImage(imageBlurring(img))
        elif sender.text() == 'Rozmycie Gaussa':
            self.setImage(GaussianBlurring(img))
        elif sender.text() == 'Filtr medianowy':
            self.setImage(medianBlur(img))
        elif sender.text() == 'Przestrzeń kolorów RGB->GRAY':
            image = changingColorSpace_BGR2GRAY(img)
            image = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(image)
            self.image.setPixmap(pixmap)
        elif sender.text() == 'Przestrzeń kolorów RGB->HSV':
            show('BGR2HSV',changingColorSpace_BGR2HSV(img))
        elif sender.text() == 'Detekcja krawędzi':
            self.setImage(cannyEdgeDetection(img))
        elif sender.text() == 'Segmentacja Otsu':
            self.setImage(segmentationOtsu(img))
        elif sender.text() == 'Segmentacja - wyznaczanie progów na podstawie histogramu':
            self.setImage(segmentationBinarizationHist(img))
        elif sender.text() == 'Segmentacja - watershed algorithm':
            self.setImage(watershedAlgorithm(img))
        elif sender.text() == 'Szkieletyzacja':
            self.setImage(skel(img))
        elif sender.text() == 'Erozja':
            self.setImage(erosion(img))
        elif sender.text() == 'Rotacja':
            self.setImage(rotation(img, self.angle))
        elif sender.text() == 'Skalowanie':
            self.setImage(scaling(img, self.scaleX, self.scaleY))
        else:
            self.setImage(brightnessChanging(img, self.isBrighter))


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

        self.scaleX = (value//50)*0.5
        self.lcd1.display(self.scaleX)

    def changeScaleY(self, value):

        try:
            value = int(value)
        except ValueError:
            value = 0

        self.scaleY = value/10
        self.lcd2.display(self.scaleY)


    def setBright(self, value):

        if value == 0:
            self.isBrighter = True
        else:
            self.isBrighter = False

    def setImage(self, image):

        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        image = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image)
        self.image.setPixmap(pixmap)



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Main()
    window.show()

    sys.exit(app.exec_())


