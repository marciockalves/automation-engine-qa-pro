import os
from PySide6.QtWidgets import QMainWindow, QSplitter, QStackedWidget
from PySide6.QtCore import Qt
from app.ui.widgets.file_explorer_widget import FileExplorerWdget
from app.ui.widgets.inspector_widget import InspectorWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AutomationEngine Qa Pro")
        self.resize(1200, 800)

        self.splitter = QSplitter(Qt.Horizontal)

        scenarios_path = os.path.join(os.getcwd(), "scenarios")
        self.left_panel = FileExplorerWdget(scenarios_path)
        self.center_panel = QStackedWidget()
        self.riqht_panel = InspectorWidget()

        self.splitter.addWidget(self.left_panel)
        self.splitter.addWidget(self.center_panel)
        self.splitter.addWidget(self.riqht_panel)

        self.setCentralWidget(self.splitter)

        