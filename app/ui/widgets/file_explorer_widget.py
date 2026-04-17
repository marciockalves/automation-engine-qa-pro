import os
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTreeView, 
    QLabel, QFileSystemModel
)
from PySide6.QtCore import QDir, Qt

class FileExplorerWidget(QWidget):
    def __init__(self, root_path=None):
        super().__init__()
        
        # Se não passarmos um caminho, usamos o diretório atual
        self.root_path = root_path or os.getcwd()
        
        # 1. Configuração do Layout Interno
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSpacing(8)

        # 2. Componentes da UI
        self._setup_header()
        self._setup_tree_view()

    def _setup_header(self):
        """Cria o botão de ação e o rótulo do explorador"""
        # Botão "+ Novo Cenário"
        self.btn_new = QPushButton("+ NOVO CENÁRIO")
        self.btn_new.setCursor(Qt.PointingHandCursor)
        
        # Label para identificar a seção
        self.label_title = QLabel("EXPLORER")
        self.label_title.setStyleSheet("font-weight: bold; color: #858585; font-size: 10px;")

        self.main_layout.addWidget(self.btn_new)
        self.main_layout.addWidget(self.label_title)

    def _setup_tree_view(self):
        """Configura a árvore de ficheiros do sistema"""
        # Modelo de dados do sistema de ficheiros
        self.model = QFileSystemModel()
        self.model.setRootPath(self.root_path)
        
        # Filtros: Não mostrar os pontos (..), mostrar pastas e ficheiros
        self.model.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files)
        
        # A View (Árvore)
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(self.root_path))
        
        # Esconder colunas desnecessárias para um visual "VS Code" (Tamanho, Tipo, Data)
        self.tree.setHeaderHidden(True)
        for i in range(1, self.model.columnCount()):
            self.tree.hideColumn(i)
            
        self.main_layout.addWidget(self.tree)