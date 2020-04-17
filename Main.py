from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
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
    img = 'lenna.bmp'

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUI(self)
        
        self.lcd.display(self.angle)
        self.slider.setSliderPosition(self.angle)

        self.lcd1.display(self.scaleX)
        self.slider1.setSliderPosition(self.scaleX*200)

        self.lcd2.display(self.scaleY)
        self.slider2.setSliderPosition(self.scaleY*10)
        
        
        self.addImageBtn.clicked.connect(self.getFile)

        self.originalBtn.clicked.connect(self.execute)
        self.negativeBtn.clicked.connect(self.execute)
        self.grayedOutBtn.clicked.connect(self.execute)
        self.histEqualizeBtn.clicked.connect(self.execute)
        self.binarizationBtn.clicked.connect(self.execute)
        self.blurBtn.clicked.connect(self.execute)
        self.skelBtn.clicked.connect(self.execute)
        self.erosionBtn.clicked.connect(self.execute)

        self.gaussBtn.clicked.connect(self.execute)
        self.medianBtn.clicked.connect(self.execute)
        self.rgb2grayBtn.clicked.connect(self.execute)
        self.rgb2hsvBtn.clicked.connect(self.execute)
        self.cannyBtn.clicked.connect(self.execute)
        self.otsuBtn.clicked.connect(self.execute)
        
        self.segHistBtn.clicked.connect(self.execute)
        self.watershedBtn.clicked.connect(self.execute)
        self.brighterBtn.clicked.connect(self.execute)
        self.chkGroup.buttonClicked[int].connect(self.setBright)


        self.slider.valueChanged.connect(self.changeAngle)
        self.rotatingBtn.clicked.connect(self.execute)
        self.slider1.valueChanged.connect(self.changeScaleX)
        self.slider2.valueChanged.connect(self.changeScaleY)
        self.scalingBtn.clicked.connect(self.execute)


    def execute(self):

        sender = self.sender()

        if sender.text() == 'Oryginał':
            image = cv.imread(self.img)
            self.setImage(image)
        elif sender.text() == 'Negatyw':
            self.setImage(negative(self.img))
        elif sender.text() == 'Szarość':
            self.setImage(grayedOut(self.img))
        elif sender.text() == 'Normalizacja histogramu':
            self.setImage(equalizeHistogram(self.img))
        elif sender.text() == 'Binaryzacja':
            self.setImage(threshBinary(self.img))
        elif sender.text() == 'Rozmycie':
            self.setImage(imageBlurring(self.img))
        elif sender.text() == 'Rozmycie Gaussa':
            self.setImage(GaussianBlurring(self.img))
        elif sender.text() == 'Filtr medianowy':
            self.setImage(medianBlur(self.img))
        elif sender.text() == 'Przestrzeń kolorów RGB->GRAY':
            image = changingColorSpace_BGR2GRAY(self.img)
            image = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(image)
            self.image.setPixmap(pixmap)
        elif sender.text() == 'Przestrzeń kolorów RGB->HSV':
            image = changingColorSpace_BGR2HSV(self.img)
            cv.imwrite('hsv.jpg', image)
            pixmap = QPixmap('hsv.jpg')
            self.image.setPixmap(pixmap)
        elif sender.text() == 'Detekcja krawędzi':
            self.setImage(cannyEdgeDetection(self.img))
        elif sender.text() == 'Segmentacja Otsu':
            self.setImage(segmentationOtsu(self.img))
        elif sender.text() == 'Segmentacja - wyznaczanie progów na podstawie histogramu':
            self.setImage(segmentationBinarizationHist(self.img))
        elif sender.text() == 'Segmentacja - watershed algorithm':
            self.setImage(watershedAlgorithm(self.img))
        elif sender.text() == 'Szkieletyzacja':
            self.setImage(skel(self.img))
        elif sender.text() == 'Erozja':
            self.setImage(erosion(self.img))
        elif sender.text() == 'Rotacja':
            self.setImage(rotation(self.img, self.angle))
        elif sender.text() == 'Skalowanie':
            self.setImage(scaling(self.img, self.scaleX, self.scaleY))
        else:
            self.setImage(brightnessChanging(self.img, self.isBrighter))


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
        
    def getFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\', "Image files (*.jpg *.png *.bmp)")
        self.image.setPixmap(QPixmap(fname[0]))
        self.img = fname[0]



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Main()
    window.show()

    sys.exit(app.exec_())
