from PySide2.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget

import sys, os

class MovieLibrary(QMainWindow):
    def __init__(self):
        super(MovieLibrary, self).__init__()
        self.resize(800, 600)
        self.setWindowTitle("Movie Library")
        # a MainWindow-nak nincs centralwidget-e, azt nekem kell létrehozni és be set-elni
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        # majd ehhez a centralwidget-hez hozzáadhatjuk a layout-unkat
        main_layout = QVBoxLayout(central_widget)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MovieLibrary()
    win.show()
    app.exec_()




