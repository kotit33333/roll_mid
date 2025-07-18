from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QMessageBox, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from logic_of_choice import game_logic
from data_base_folder import  data_base_logic

class MainWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle(f"_-_")
        self.setFixedSize(500, 400)
        self.login = username
        self.is_correct = False
        self.info_about_choice = ()
        self.predicted = 0

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        # Верхняя панель с вопросом (FAQ)
        top_bar = QHBoxLayout()
        top_bar.setAlignment(Qt.AlignLeft)

        faq_button = QPushButton("❓")
        faq_button.setFixedSize(30, 30)
        faq_button.clicked.connect(self.show_help)

        top_bar.addWidget(faq_button)
        main_layout.addLayout(top_bar)

        # Центральный QLabel (кубик)
        self.cube_label = QLabel("?")
        self.cube_label.setAlignment(Qt.AlignCenter)
        self.cube_label.setFont(QFont("Arial", 80, QFont.Bold))
        self.cube_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        main_layout.addWidget(self.cube_label)

        # Кнопки от 1 до 6
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        button_layout.setAlignment(Qt.AlignCenter)

        for i in range(1, 7):
            btn = QPushButton(str(i))
            btn.setFixedSize(50, 50)
            btn.setFont(QFont("Arial", 14))
            btn.clicked.connect(lambda _, x=i: self.user_choice(x))
            button_layout.addWidget(btn)

        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def user_choice(self, number):
        self.info_about_choice = game_logic.process_user_choice(self.login, number)
        self.predicted = self.info_about_choice[0]
        self.is_correct = self.info_about_choice[1]
        self.cube_label.setText(str(self.predicted))
        if self.is_correct:
            self.cube_label.setStyleSheet("color: green;")
        else:
            self.cube_label.setStyleSheet("color: red;")
    def show_help(self):
        QMessageBox.information(
            self,
            "Справка",
            "Выберите число от 1 до 6 — то, что вы думаете, выпадет на кубике.\n"
            "Программа тоже выберет число (в будущем — будет пытаться вас предсказать)."
        )
