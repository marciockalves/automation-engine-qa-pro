from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QFormLayout, QLineEdit

class InspectorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QLabel("PROPRIEDADES DO STEP"))

        self.scroll = QScrollArea()
        self.container = QWidget()
        self.form = QFormLayout(self.container)

        self.form.addRow("Evento:", QLineEdit())
        self.form.addRow("Seletor:", QLineEdit())

        self.scroll.setWidget(self.container)
        self.scroll.setWidgetResizable(True)
        self.layout.addWidget(self.scroll)

    def clear_inspector(self):
        pass