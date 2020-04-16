from PyQt5.QtWidgets import QHBoxLayout, QGridLayout
from PyQt5.QtWidgets import QCheckBox, QButtonGroup, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider, QLCDNumber, QSplitter
from PyQt5.QtWidgets import QRadioButton, QGroupBox
from PyQt5.QtWidgets import QComboBox, QSpinBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit

class UI(object):

    def setupUI(self, Widget):

        layoutA = QHBoxLayout()
        self.originalBtn = QPushButton('Oryginał', self)
        self.negativeBtn = QPushButton('Negatyw', self)
        self.grayedOutBtn = QPushButton('Szarość', self)
        self.histEqualizeBtn = QPushButton('Normalizacja histogramu', self)
        self.binarizationBtn = QPushButton('Binaryzacja', self)
        self.blurBtn = QPushButton('Rozmycie', self)
        self.skelBtn = QPushButton('Szkieletyzacja', self)
        self.erosionBtn = QPushButton('Erozja', self)

        layoutA.addWidget(self.originalBtn)
        layoutA.addWidget(self.negativeBtn)
        layoutA.addWidget(self.grayedOutBtn)
        layoutA.addWidget(self.histEqualizeBtn)
        layoutA.addWidget(self.binarizationBtn)
        layoutA.addWidget(self.blurBtn)
        layoutA.addWidget(self.skelBtn)
        layoutA.addWidget(self.erosionBtn)


        layoutB = QHBoxLayout()
        self.gaussBtn = QPushButton('Rozmycie Gaussa', self)
        self.medianBtn = QPushButton('Filtr medianowy', self)
        self.rgb2grayBtn = QPushButton('Przestrzeń kolorów RGB->GRAY', self)
        self.rgb2hsvBtn = QPushButton('Przestrzeń kolorów RGB->HSV',self)
        self.cannyBtn = QPushButton('Detekcja krawędzi',self)
        self.otsuBtn = QPushButton('Segmentacja Otsu', self)

        layoutB.addWidget(self.gaussBtn)
        layoutB.addWidget(self.medianBtn)
        layoutB.addWidget(self.rgb2grayBtn)
        layoutB.addWidget(self.rgb2hsvBtn)
        layoutB.addWidget(self.cannyBtn)
        layoutB.addWidget(self.otsuBtn)

        layoutC = QHBoxLayout()
        self.segHistBtn = QPushButton('Segmentacja - wyznaczanie progów na podstawie histogramu', self)
        self.watershedBtn = QPushButton('Segmentacja - watershed algorithm',self)
        self.brighterBtn = QPushButton('Jasność', self)

        layoutC.addWidget(self.segHistBtn)
        layoutC.addWidget(self.watershedBtn)
        layoutC.addWidget(self.brighterBtn)
        self.chkGroup = QButtonGroup()
        for i, v in enumerate(('Jaśniej', 'Ciemniej')):
            self.chk = QCheckBox(v)
            self.chkGroup.addButton(self.chk, i)
            layoutC.addWidget(self.chk)
        self.chkGroup.buttons()[0].setChecked(True)


        layoutD = QHBoxLayout()
        self.rotatingBtn = QPushButton('Rotacja', self)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMaximum(360)
        self.slider.setMinimum(0)
        self.lcd = QLCDNumber()
        self.lcd.setSegmentStyle(QLCDNumber.Flat)

        self.scalingBtn = QPushButton('Skalowanie', self)
        self.slider1 = QSlider(Qt.Horizontal)
        self.slider1.setMinimum(1)
        self.slider1.setMaximum(100)
        self.lcd1 = QLCDNumber()
        self.lcd1.setSegmentStyle(QLCDNumber.Flat)
        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.setMinimum(1)
        self.slider2.setMaximum(100)
        self.lcd2 = QLCDNumber()
        self.lcd2.setSegmentStyle(QLCDNumber.Flat)

        layoutD.addWidget(self.rotatingBtn)
        layoutD.addWidget(self.slider)
        layoutD.addWidget(self.lcd)
        layoutD.addWidget(self.scalingBtn)
        layoutD.addWidget(self.slider1)
        layoutD.addWidget(self.lcd1)
        layoutD.addWidget(self.slider2)
        layoutD.addWidget(self.lcd2)


        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layoutA)
        mainLayout.addLayout(layoutB)
        mainLayout.addLayout(layoutC)
        mainLayout.addLayout(layoutD)

        self.setLayout(mainLayout)  # przypisanie układu do okna głównego
        self.setWindowTitle('Przetwarzanie obrazów')
        self.resize(1366,768)
