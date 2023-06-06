from PySide6.QtWidgets import QDialog, QTextEdit, QVBoxLayout

class ArrayDialog(QDialog):
    def __init__(self, array):
        super().__init__()
        self.setWindowTitle("Array Dialog")
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: #1c007c; color: white; font-size: 20px; font-family: Arial; font-weight: bold;")
        self.setup_ui(array)

    def setup_ui(self, array):
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        array_text = ', '.join(str(num) for num in array)
        self.text_edit.setPlainText(array_text)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)

        self.setLayout(layout)
