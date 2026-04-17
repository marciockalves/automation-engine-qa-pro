from PySide6.QtWidgets import (QWidget, QVBoxLayout, QFormLayout, QLineEdit, 
                             QPushButton, QLabel, QComboBox)
from PySide6.QtCore import Signal
from app.core.schemas import ProjectMetadata

class ScenarioWizardWidget(QWidget):

    scenario_created = Signal(ProjectMetadata)

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        
        self.header = QLabel("🚀 Criar Novo Cenário")
        self.header.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.header)


        self.form = QFormLayout()
        self.input_app = QLineEdit()
        self.input_app.setPlaceholderText("Ex: E-commerce Alpha")
        
        self.input_category = QComboBox()
        self.input_category.addItems(["Checkout", "Login", "Perfil", "Busca"])
        
        self.input_title = QLineEdit()
        self.input_title.setPlaceholderText("Ex: compra_cartao_sucesso")

        self.form.addRow("Nome do App:", self.input_app)
        self.form.addRow("Categoria:", self.input_category)
        self.form.addRow("Título do Teste:", self.input_title)
        
        self.layout.addLayout(self.form)

        self.btn_create = QPushButton("Próximo: Adicionar Steps")
        self.btn_create.clicked.connect(self._on_submit)
        self.layout.addWidget(self.btn_create)
        self.layout.addStretch()

    def _on_submit(self):
        
        metadata = ProjectMetadata(
            app_name=self.input_app.text(),
            scenario_category=self.input_category.currentText(),
            test_title=self.input_title.text()
        )
        self.scenario_created.emit(metadata)