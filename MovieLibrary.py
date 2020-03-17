from PySide2.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QAction
from modules.CategorySelector import CategorySelector
from modules.MovieBrowser import MovieBrowser
import sys, os

class MovieLibrary(QMainWindow):
    def __init__(self):
        super(MovieLibrary, self).__init__()
        self.resize(800, 600)
        self.setWindowTitle("Movie Library")

        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        exit_acton = QAction("Exit", self)
        exit_acton.setShortcut("Ctrl+Q")
        self.file_menu.addAction(exit_acton)
        exit_acton.triggered.connect(self.exit_fv)

        new_file_action = QAction("New File", self)
        new_file_action.setShortcut(("Ctrl+N"))
        self.file_menu.addAction(new_file_action)

        # a MainWindow-nak nincs centralwidget-e, azt nekem kell létrehozni és be set-elni
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.category_selector = CategorySelector()
        self.movie_browser = MovieBrowser()
        # majd ehhez a centralwidget-hez hozzáadhatjuk a layout-unkat
        main_layout = QHBoxLayout(central_widget)
        main_layout.addWidget(self.category_selector)
        main_layout.addWidget(self.movie_browser)

    def exit_fv(self):
        print("Kilépés")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MovieLibrary()
    win.show()
    app.exec_()




