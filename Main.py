from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from UI import UI
from PyQt5.QtGui import QColor
from Functions import *
import cv2.cv2 as cv

class Main(QWidget, UI):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUI(self)

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



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Main()
    window.show()

    sys.exit(app.exec_())


