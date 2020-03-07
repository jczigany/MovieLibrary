from PySide2.QtWidgets import QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem

data_dict = {
    "genre": [
        "action",
        "comedy",
        "thriller",
        "horror",
        "sci-fi",
    ],
    "year": [
        1970,
        1980,
        1990,
        2000,
    ],
    "language": [
        "eng",
        "hun",
        "fra",
    ]
}

class CategorySelector(QTreeWidget):
    def __init__(self):
        super(CategorySelector, self).__init__()

        self.setMaximumWidth(200)
        self.refresh()
        self.setHeaderHidden(True)

    def refresh(self):
        self.clear()
        #self.addTopLevelItem(CategoryItem(self, "Test"))

        for k, v in data_dict.items():
            top_item = CategoryItem(self, k)

            for i in v:
                CategoryItem(top_item, i)


class CategoryItem(QTreeWidgetItem):
    def __init__(self, parent, name):
        super(CategoryItem, self).__init__(parent)
        self.setText(0, str(name))

        self.setExpanded(True)


if __name__ == '__main__':
    from PySide2.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    win = CategorySelector()
    win.show()
    app.exec_()
