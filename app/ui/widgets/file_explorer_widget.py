from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTreeView, QFileSystemModel, QLabel
from PySide6.QtCore import QDir

class FileExplorerWdget(QWidget):
    def __init__(self, root_path):
        super().__init__()
        layout = QVBoxLayout(self)

        self.bnt_new = QPushButton("+ Novo Cenário")
        self.bnt_new.setStyleSheet("background-color: #2ecc71; color: white; padding: Box;")

        self.model = QFileSystemModel()
        self.model.setRootPath(root_path)
        self.model.setFilter(QDir.NoDoAndDotDot | QDir.AllDirs | QDir.Files)

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(root_path))

        for i in range(1, 4):
            self.tree.hideColumn(i)
        self.tree.setHeaderHidden(True)

        layout.addWidget(self.btn_new)
        layout.addWidget(QLabel("CENÁRIOS"))
        layout.addChildWidget(self.tree)