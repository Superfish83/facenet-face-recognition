import sys
import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QTimer, QThread

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("CNSA Face ID")
        self.setGeometry(100, 100, 800, 800)

        self.image_label = QLabel(self)
        self.recButton = QPushButton('&Start Face Recognition', self)
        self.recButton.setFixedSize(400, 50)
        self.recButton.clicked.connect(self.show_recognized_face)
        
        self.setCentralWidget(self.image_label)

    # 카메라로 캡처한 사진들 표시함
    def show_recognized_face(self):
        import facenet
        vc = cv2.VideoCapture(0)
        self.recButton.setDisabled(True)

        while vc.isOpened():
            _, frame = vc.read()
            #image = frame
            image = facenet.webcam_face_recognizer(frame)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            height, width, channel = image.shape
            bytes_per_line = 3 * width
            q_image = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.image_label.setPixmap(pixmap)

            self.update()
            QApplication.processEvents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    