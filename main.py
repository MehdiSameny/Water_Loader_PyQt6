# ///////////////////////////////////////////////////////////////
# Developer: Mehdi Sameni
# Designer: Mehdi Sameni
# PyQt6
# Python 3.10
# other module : perlin_noise
# ///////////////////////////////////////////////////////////////

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QGraphicsDropShadowEffect
from PyQt6.QtCore import pyqtSlot, QTimer, QSizeF, Qt, QRectF, QPointF, QRect, QPoint, QSize, QTimer
from PyQt6.QtGui import QImage, QColor, QPainter, QLinearGradient, QGradient, QPainterPath, QPixmap, QBrush, QPen
from WaterProgress import DWaterProgress


class WaterProgressWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super(WaterProgressWindow, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)

        self.progress = DWaterProgress(self)
        self.progress.setFixedSize(200,200)
        self.progress.setValue(0)
        self.progress.start()

        layout.addWidget(self.progress)

        self.timer = QTimer(self, timeout=self.updateProgress)
        self.timer.start(50)

    def updateProgress(self):
        value = self.progress.value()
        if value == 100:
            self.progress.setValue(0)
        else:
            self.progress.setValue(value + 1)


if __name__ == '__main__':
    import cgitb

    cgitb.enable(format='text')
    app = QApplication(sys.argv)
    w = WaterProgressWindow()
    w.show()
    sys.exit(app.exec())


