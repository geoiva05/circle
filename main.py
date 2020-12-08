import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from random import randrange, randint

def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, 'Error', text)
    quit()


sys.excepthook = log_uncaught_exceptions

class flex(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.center()
        self.new_paint = False
        self.btn_draw.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.new_paint:
            qp = QPainter(self)
            qp.begin(self)
            qp.setPen(Qt.yellow)
            qp.drawEllipse(100, 100, self.radius, self.radius)
            qp.drawEllipse(400, 100, self.radius, self.radius)
            qp.end()

    def paint(self):
        self.radius = randint(100, 200)
        self.new_paint = True
        self.repaint()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = flex()
    ex.show()
    sys.exit(app.exec())