from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class MainApp(QMainWindow):
    def __init__(self, parent = None, *args):
        super(MainApp, self).__init__(parent = parent)

        self.setFixedSize(500, 300)
        self.setWindowTitle("First App")

        self.user_input = QLineEdit(self)
        self.user_input.setPlaceholderText("Usuario")
        self.user_input.setClearButtonEnabled(True)
        self.user_input.setGeometry(200, 50, 100, 30)

        self.user_pass = QLineEdit(self)
        self.user_pass.setPlaceholderText("Contraseña")
        self.user_pass.setClearButtonEnabled(True)
        self.user_pass.setGeometry(200, 100, 100, 30)
        #self.user_pass.setEchoMode(QLineEdit.echoMode)

        self.login_btn = QPushButton("Login", self)
        self.login_btn.setGeometry(200, 150, 100, 30)

        # Triggers

        #self.user_input.returnPressed.connect(self.show_text)
        #self.user_pass.returnPressed.connect(self.show_text)
        self.login_btn.clicked.connect(self.show_text)


    def show_text(self):
        print(self.user_input.text())
        print(self.user_pass.text())

if __name__ == '__main__':
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec()