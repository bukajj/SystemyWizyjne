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

        layoutA.addWidget(self.originalBtn)
        layoutA.addWidget(self.negativeBtn)
        layoutA.addWidget(self.grayedOutBtn)
        layoutA.addWidget(self.histEqualizeBtn)
        layoutA.addWidget(self.binarizationBtn)
        layoutA.addWidget(self.blurBtn)


        layoutB = QHBoxLayout()
        self.gaussBtn = QPushButton('Rozmycie Gaussa', self)
        self.medianBtn = QPushButton('Filtr medianowy', self)
        self.rgb2grayBtn = QPushButton('Przestrzeń kolorów RGB->GRAY', self)
        self.rgb2hsvBtn = QPushButton('Przestrzeń kolorów RGB->HSV',self)
        self.cannyBtn = QPushButton('Detekcja krawędzi',self)

        layoutB.addWidget(self.gaussBtn)
        layoutB.addWidget(self.medianBtn)
        layoutB.addWidget(self.rgb2grayBtn)
        layoutB.addWidget(self.rgb2hsvBtn)
        layoutB.addWidget(self.cannyBtn)


        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layoutA)
        mainLayout.addLayout(layoutB)

        self.setLayout(mainLayout)  # przypisanie układu do okna głównego
        self.setWindowTitle('Przetwarzanie obrazów')
        self.resize(1366,768)
