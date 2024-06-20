import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import os
from PIL import Image, ImageOps
import pickle

path = os.path.dirname(__file__)
os.chdir(path)

class MainWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # SVM Model Loaded
        self.loaded_model = pickle.load(open('svm_model.pkl', 'rb'))

        self.initUI()
        self.start_timer()
    
    def initUI(self):
        self.container = QtWidgets.QVBoxLayout()
        self.container.setContentsMargins(20, 20, 20, 20)

        # Used As Canvas Container
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(300, 300)
        canvas.fill(QtGui.QColor("black"))
        self.label.setPixmap(canvas)
        self.label.setStyleSheet("border: 2px solid #FFD700;")
        self.last_x, self.last_y = None, None

        self.prediction = QtWidgets.QLabel('Prediction: ...')
        self.prediction.setFont(QtGui.QFont('Monospace', 24))
        self.prediction.setStyleSheet("color: #FFD700; margin: 20px 0;")

        self.button_clear = QtWidgets.QPushButton('CLEAR')
        self.button_clear.setStyleSheet("""
            QPushButton {
                background-color: #FFD700;
                color: black;
                border: none;
                padding: 10px;
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #FFA500;
            }
        """)
        self.button_clear.clicked.connect(self.clear_canvas)

        self.container.addWidget(self.label, alignment=QtCore.Qt.AlignHCenter)
        self.container.addWidget(self.prediction, alignment=QtCore.Qt.AlignHCenter)
        self.container.addWidget(self.button_clear, alignment=QtCore.Qt.AlignHCenter)

        self.setLayout(self.container)
    
    def clear_canvas(self):
        self.label.pixmap().fill(QtGui.QColor('#000000'))
        self.update()

    def predict(self):
        s = self.label.pixmap().toImage().bits().asarray(300 * 300 * 4)
        arr = np.frombuffer(s, dtype=np.uint8).reshape((300, 300, 4))
        arr = np.array(ImageOps.grayscale(Image.fromarray(arr).resize((28,28), Image.LANCZOS)))

        # Check if the canvas is mostly black
        if np.mean(arr) < 10:  # Adjust this threshold as needed
            self.prediction.setText('Prediction: ...')
            return

        arr = (arr / 255.0).reshape(1, -1)
        self.prediction.setText('Prediction: ' + str(self.loaded_model.predict(arr)[0]))
    
    def mouseMoveEvent(self, e):
        if self.last_x is None:  # First event.
            self.last_x = e.x() - self.label.pos().x()
            self.last_y = e.y() - self.label.pos().y()
            return  # Ignore the first time.

        painter = QtGui.QPainter(self.label.pixmap())

        p = painter.pen()
        p.setWidth(20)
        self.pen_color = QtGui.QColor('#FFFFFF')
        p.setColor(self.pen_color)
        painter.setPen(p)

        painter.drawLine(self.last_x, self.last_y, e.x() - self.label.pos().x(), e.y() - self.label.pos().y())
        painter.end()
        self.update()

        # Update the origin for next time.
        self.last_x = e.x() - self.label.pos().x()
        self.last_y = e.y() - self.label.pos().y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    def start_timer(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.predict)
        self.timer.start(1000)  # Interval in milliseconds (e.g., 1000ms = 1s)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.mainWidget = MainWidget()
        self.setCentralWidget(self.mainWidget)
        self.setStyleSheet("background-color: #2E2E2E;")
        self.setGeometry(100, 100, 400, 450)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    mainApp = MainWindow()
    mainApp.setWindowTitle('DIGIT PREDICTOR')
    mainApp.setWindowIcon(QtGui.QIcon('icon.png'))  # Add an application icon
    mainApp.show()
    sys.exit(app.exec_())
