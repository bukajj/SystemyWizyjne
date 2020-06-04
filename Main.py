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
            image = cv.imread(self.img)
            self.setImage(negative(image))
        elif sender.text() == 'Szarość':
            image = cv.imread(self.img)
            self.setImage(grayedOut(image))
        elif sender.text() == 'Normalizacja histogramu':
            image = cv.imread(self.img)
            self.setImage(equalizeHistogram(image))
        elif sender.text() == 'Binaryzacja':
            image = cv.imread(self.img)
            self.setImage(threshBinary(image))
        elif sender.text() == 'Rozmycie':
            image = cv.imread(self.img)
            self.setImage(imgBlurring(image))
        elif sender.text() == 'Rozmycie Gaussa':
            image = cv.imread(self.img)
            self.setImage(GaussianBlurring(image))
        elif sender.text() == 'Filtr medianowy':
            image = cv.imread(self.img)
            self.setImage(medianBlur(image))
        elif sender.text() == 'Przestrzeń kolorów RGB->GRAY':
            image = cv.imread(self.img)
            image = changingColorSpace_BGR2GRAY(image)
            image = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(image)
            self.image.setPixmap(pixmap)
        elif sender.text() == 'Przestrzeń kolorów RGB->HSV':
            image = cv.imread(self.img)
            image = changingColorSpace_BGR2HSV(image)
            cv.imwrite('hsv.jpg', image)
            pixmap = QPixmap('hsv.jpg')
            self.image.setPixmap(pixmap)
        elif sender.text() == 'Detekcja krawędzi':
            image = cv.imread(self.img)
            self.setImage(cannyEdgeDetection(image))
        elif sender.text() == 'Segmentacja Otsu':
            image = cv.imread(self.img)
            self.setImage(segmentationOtsu(image))
        elif sender.text() == 'Segmentacja - wyznaczanie progów na podstawie histogramu':
            image = cv.imread(self.img)
            self.setImage(segmentationBinarizationHist(image))
        elif sender.text() == 'Segmentacja - watershed algorithm':
            image = cv.imread(self.img)
            self.setImage(watershedAlgorithm(image))
        elif sender.text() == 'Szkieletyzacja':
            image = cv.imread(self.img)
            self.setImage(skel(image))
        elif sender.text() == 'Erozja':
            image = cv.imread(self.img)
            self.setImage(erosion(image))
        elif sender.text() == 'Rotacja':
            image = cv.imread(self.img)
            self.setImage(rotation(image, self.angle))
        elif sender.text() == 'Skalowanie':
            image = cv.imread(self.img)
            self.setImage(scaling(image, self.scaleX, self.scaleY))
        else:
            image = cv.imread(self.img)
            self.setImage(brightnessChanging(image, self.isBrighter))


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


