from PySide2.QtWidgets import QWidget, QLineEdit, QListWidget, QListWidgetItem, QVBoxLayout, QItemDelegate
from PySide2.QtCore import QSize, Qt, QRect, QRectF, QPoint
from PySide2.QtGui import QPixmap, QPainter, QPen, QBrush, QColor, QFont
import sys, os
from utilities.dummy_data import create_dummy_data

movies_data = create_dummy_data(100)


class MovieBrowser(QWidget):
    def __init__(self):
        super(MovieBrowser, self).__init__()

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.search_field = QLineEdit()
        self.icon_view = IconView()

        main_layout.addWidget(self.search_field)
        main_layout.addWidget(self.icon_view)


class IconView(QListWidget):
    def __init__(self):
        super(IconView, self).__init__()
        # itemdelegate megadása, példányként kell megadni ()!
        self.setItemDelegate(IconViewDelegate())
        # elemek közötti nézet
        self.setSpacing(10)
        # Ikon-nézet
        self.setViewMode(QListWidget.IconMode)
        # Ablak átméretezésekor újra-rendez
        self.setResizeMode(QListWidget.Adjust)
        # Ne lehessen az elemeket mozgatni
        self.setMovement(QListWidget.Static)
        # többszörös kijelölés
        self.setSelectionMode(QListWidget.ExtendedSelection)

        self.refresh()

    def refresh(self):
        self.clear()
        for movie in movies_data:
            MovieItem(self, movie)


class IconViewDelegate(QItemDelegate):
    def __init__(self):
        super(IconViewDelegate, self).__init__()
        self.photo = QPixmap()
        self.my_painter = QPainter()
        self.my_pen = QPen(QColor("blue"))
        self.my_pen.setWidth(3)
        self.my_brush = QBrush(QColor("yellow"))
        self.font1 = QFont("Times", 12, QFont.ExtraBold)
        self.font2 = QFont("Helvetica", 6, QFont.ExtraLight)
        self.font3 = QFont("Arial", 8, QFont.ExtraLight)

        self.photo_rect = QRect()

    def paint(self, painter, option, index):
        rect = option.rect
        painter.setBrush(self.my_brush)
        painter.setPen(self.my_pen)
        painter.setPen(QColor("blue"))
        painter.drawRect(rect)
        szoveg_rect = QRectF(QPoint(rect.x() + 85, rect.y() + 40), QPoint(rect.x() + 240, rect.y() + 112))

        self.atvett_adat = index.data(Qt.UserRole)

        self.photo.load(self.atvett_adat.get("poster"))
        photo = self.photo.scaled(QSize(80, 120), Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.photo_rect.setRect(rect.x(), rect.y(), photo.width(), photo.height())
        self.photo_rect.moveTopLeft(rect.topLeft())

        painter.drawPixmap(self.photo_rect, QPixmap(photo))

        # painter.drawText(rect,self.atvett_adat.get("title"))
        painter.setPen(QColor("red"))
        painter.setFont(self.font1)
        painter.drawText(rect.x() + 85, rect.y() + 15,self.atvett_adat.get("title"))

        painter.setPen(QColor("black"))
        painter.setFont(self.font2)
        painter.drawText(rect.x() + 85, rect.y() + 30, ''.join(["(", self.atvett_adat.get("release_date"), ")"]))

        painter.setPen(QColor("blue"))
        painter.setFont(self.font3)
        # painter.drawText(rect.x() + 85, rect.y() + 40, self.atvett_adat.get("description"))
        painter.drawText(szoveg_rect, Qt.TextWordWrap, self.atvett_adat.get("description"))
        # painter.drawText(rect, Qt.TextWordWrap)


class MovieItem(QListWidgetItem):
    def __init__(self, parent, movie_data):
        super(MovieItem, self).__init__(parent)
        self.movie_data = movie_data
        self.setSizeHint(QSize(240, 120))
        self.setText(movie_data.get("title"))
        self.setData(Qt.UserRole, movie_data)


if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication

    import sys

    app = QApplication(sys.argv)
    win = MovieBrowser()
    win.show()
    app.exec_()
