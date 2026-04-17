import os
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QSplitter, QFrame
from PySide6.QtCore import Qt

from app.ui.widgets.editor_container_widget import EditorContainerWidget
from app.ui.widgets.file_explorer_widget import FileExplorerWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AutomationEngine QA Pro")
        self.resize(1280, 720)

        
        self.scenarios_path = os.path.abspath("scenarios")
        os.makedirs(self.scenarios_path, exist_ok=True)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.setup_ui()

    def setup_ui(self):
        """Ponto de entrada para construir a interface"""
        self._init_columns()

    def _init_columns(self):
        """Cria especificamente o QSplitter e as 3 colunas de widgets"""
        self.splitter = QSplitter(Qt.Horizontal)
        
        self.left_panel = FileExplorerWidget(self.scenarios_path)
        
        self.center_panel = EditorContainerWidget()
        self.center_panel.setStyleSheet("background-color: #1e1e1e;") 
        
        self.right_panel = QFrame()
        self.right_panel.setStyleSheet("background-color: #252526;") 

        self.splitter.addWidget(self.left_panel)
        self.splitter.addWidget(self.center_panel)
        self.splitter.addWidget(self.right_panel)
        
        self.splitter.setSizes([260, 720, 300])
        
        self.main_layout.addWidget(self.splitter)