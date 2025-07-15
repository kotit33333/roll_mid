import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QFormLayout, QTabWidget, QMessageBox
)
from GUI_folder import auth_logic
from data_base_folder import data_base_logic
from PyQt5.QtCore import pyqtSignal


class AuthUI(QWidget):
    login_successful = pyqtSignal(str)


    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.setFixedSize(300, 220)

        self.tabs = QTabWidget()

        self.login_tab = QWidget()
        self.register_tab = QWidget()

        self.tabs.addTab(self.login_tab, "Вход")
        self.tabs.addTab(self.register_tab, "Регистрация")

        self.setup_login_ui()
        self.setup_register_ui()

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def setup_register_ui(self):
        """окно регистрации"""
        form = QFormLayout()

        self.input_login = QLineEdit()
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.Password)
        self.input_pass_confirm = QLineEdit()
        self.input_pass_confirm.setEchoMode(QLineEdit.Password)

        form.addRow("Логин:", self.input_login)
        form.addRow("Пароль:", self.input_pass)
        form.addRow("Повтор пароля:", self.input_pass_confirm)

        btn_register = QPushButton("Зарегистрироваться")
        btn_register.clicked.connect(self.handle_register)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(btn_register)

        self.register_tab.setLayout(layout)

    def setup_login_ui(self):
        """окно входа"""
        form = QFormLayout()

        self.login_username = QLineEdit()
        self.login_password = QLineEdit()
        self.login_password.setEchoMode(QLineEdit.Password)

        form.addRow("Логин:", self.login_username)
        form.addRow("Пароль:", self.login_password)

        btn_login = QPushButton("Войти")
        btn_login.clicked.connect(self.handle_login)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addWidget(btn_login)

        self.login_tab.setLayout(layout)

    def handle_login(self):
        """функция принимает логин и пароль, дальше отправляет их в logic user, если проверка удачная, то открывает основное окно"""
        login = self.login_username.text()
        password = self.login_password.text()

        success, message = auth_logic.login_user(login, password)
        try:
            if success:
                self.login_successful.emit(login)  #

            else:
                QMessageBox.warning(self, "Ошибка", message)
        except Exception as e:
            import traceback
            print("Ошибка при показе QMessageBox:", repr(e))
            traceback.print_exc()

    def handle_register(self):
        """передает в функцию проверки возможности регистарации, если все удачно, открывает основное окно"""
        login = self.input_login.text()
        password = self.input_pass.text()
        password_confirm = self.input_pass_confirm.text()

        success, message = auth_logic.register_user(login, password, password_confirm)
        try:
            if success:

                if data_base_logic.register_user(login, password):
                    self.login_successful.emit(login)
                else:
                    QMessageBox.warning(self, "Ошибка", 'Данный логин занят')
            else:
                QMessageBox.warning(self, "Ошибка", message)
        except Exception as e:
            import traceback
            print("Ошибка при показе QMessageBox:", repr(e))
            traceback.print_exc()

def run_gui():
    app = QApplication(sys.argv)
    window = AuthUI()
    window.show()
    sys.exit(app.exec_())
