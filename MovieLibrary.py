from PySide2.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget
from modules.CategorySelector import CategorySelector
from modules.MovieBrowser import MovieBrowser
import sys, os

class MovieLibrary(QMainWindow):
    def __init__(self):
        super(MovieLibrary, self).__init__()
        self.resize(800, 600)
        self.setWindowTitle("Movie Library")
        # a MainWindow-nak nincs centralwidget-e, azt nekem kell létrehozni és be set-elni
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.category_selector = CategorySelector()
        self.movie_browser = MovieBrowser()
        # majd ehhez a centralwidget-hez hozzáadhatjuk a layout-unkat
        main_layout = QHBoxLayout(central_widget)
        main_layout.addWidget(self.category_selector)
        main_layout.addWidget(self.movie_browser)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MovieLibrary()
    win.show()
    app.exec_()




