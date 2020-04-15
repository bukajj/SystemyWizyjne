from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from UI import UI
from PyQt5.QtGui import QColor

class Main(QWidget, UI):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUI(self)



    def execute(self):



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Main()
    window.show()

    sys.exit(app.exec_())


