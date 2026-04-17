from PySide6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QLabel
from PySide6.QtCore import Qt

class EditorContainerWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        # 1. Layout Principal
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # 2. O StackedWidget (A pilha de telas)
        self.stack = QStackedWidget()
        
        # 3. Tela 1: Boas-vindas (Placeholder)
        self.welcome_screen = QLabel("Selecione ou crie um cenário para começar")
        self.welcome_screen.setAlignment(Qt.AlignCenter)
        self.welcome_screen.setStyleSheet("color: #666; font-size: 16px;")
        
        # Adicionamos à pilha
        self.stack.addWidget(self.welcome_screen)
        
        # Colocamos a pilha no layout do container
        self.main_layout.addWidget(self.stack)