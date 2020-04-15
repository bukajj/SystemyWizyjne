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

        layout = QHBoxLayout()
        self.groupA = QButtonGroup()
        self.groupA.setExclusive(False)
        for v in ('Original', 'Negative', 'Grayed Out', 'Histogram Equalization', 'Thresh', 'Blur'):
            self.btn = QPushButton(v)
            self.groupA.addButton(self.btn)
            layout.addWidget(self.btn)

        self.groupABtn = QGroupBox()
        self.groupABtn.setLayout(layout)



        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.groupABtn)

        self.setLayout(mainLayout)  # przypisanie układu do okna głównego
        self.setWindowTitle('')
        self.resize(1366,768)
