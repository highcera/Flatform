# https://studyingrabbit.tistory.com/69

import sys
from PyQt5.QtWidgets import *

class QTreeView(QTreeView):
    def __init__(self):
        super(QTreeView, self).__init__()

    def edit(self, index, trigger, event):
        return False


class QLineEdit(QLineEdit):
    def __init__(self):
        super(QLineEdit, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if (urls and urls[0].scheme() == 'file'):
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if (urls and urls[0].scheme() == 'file'):
            filepath = str(urls[0].path())[1:]
            self.setText(filepath)


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        root_path = "C:/"
        self.model_file_system = QFileSystemModel()
        self.model_file_system.setRootPath(root_path)
        self.model_file_system.setReadOnly(False)

        self.tree_view = QTreeView()
        self.tree_view.setModel(self.model_file_system)
        self.tree_view.setRootIndex(self.model_file_system.index(root_path))
        self.tree_view.doubleClicked.connect(lambda index : self.item_double_clicked(index))

        self.tree_view.setDragEnabled(True)
        self.tree_view.setColumnWidth(0, 300)

        lineedit = QLineEdit()

        layout.addWidget(self.tree_view)
        layout.addWidget(lineedit)

        self.setLayout(layout)
        self.resize(800, 500)
        self.show()


    def item_double_clicked(self, index):
        print(self.model_file_system.filePath(index))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())