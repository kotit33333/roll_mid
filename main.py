from PyQt5.QtWidgets import QApplication
from GUI_folder.auth_window import AuthUI
from GUI_folder.main_window import MainWindow  # создашь это
import sys


class AppController:
    def __init__(self):
        self.auth_window = AuthUI()
        self.auth_window.login_successful.connect(self.show_main_window)
        self.main_window = None

    def show_main_window(self, username):
        self.main_window = MainWindow(username)
        self.auth_window.close()
        self.main_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = AppController()
    controller.auth_window.show()
    sys.exit(app.exec_())