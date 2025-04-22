from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel

class AddSymbolDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add Symbol")
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()

        self.symbol_input = QLineEdit(self)
        self.symbol_input.setPlaceholderText("Enter symbol (e.g., EUR/USD)")
        layout.addWidget(self.symbol_input)

        self.add_button = QPushButton("Add Symbol")
        self.add_button.clicked.connect(self.add_symbol)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def add_symbol(self):
        symbol_name = self.symbol_input.text()
        if symbol_name:
            self.parent().add_symbol_tab(symbol_name)
            self.accept()  # Close the dialog
