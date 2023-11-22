from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import random
import sys
from PyQt5.QtGui import QFont

class Hand(QWidget):
    def __init__(self, picture='default'):
        super().__init__()
        self.picture = picture
        self.label = QLabel(self)
        self.update_picture()

    def play(self, picture):
        self.picture = picture
        self.update_picture()

    def update_picture(self):
        self.label.setPixmap(QPixmap(f'./img/{self.picture}.png'))

class MainWindow(QMainWindow):
    def __init__(self, user_hand, app_hand):
        super().__init__()
        self.user_hand = user_hand
        self.app_hand = app_hand
        self.result_label = QLabel(self)
        self.result_label.setFont(QFont('Arial', 20, QFont.Bold))
        self.result_label.setAlignment(Qt.AlignCenter)
        self.initUI()

    def check_winner(self, user_choice, app_choice):
        if user_choice == app_choice:
            self.result_label.setText('<b>Draw!</b>')
        elif (user_choice == 'rock' and app_choice == 'scissors') or (user_choice == 'paper' and app_choice == 'rock') or (user_choice == 'scissors' and app_choice == 'paper'):
            self.result_label.setText('<b>User wins!</b>')
        else:
            self.result_label.setText('<b>App wins!</b>')

    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import random
import sys
from PyQt5.QtGui import QFont

class Hand(QWidget):
    def __init__(self, picture='default'):
        super().__init__()
        self.picture = picture
        self.label = QLabel(self)
        self.update_picture()

    def play(self, picture):
        self.picture = picture
        self.update_picture()

    def update_picture(self):
        self.label.setPixmap(QPixmap(f'./img/{self.picture}.png'))

class MainWindow(QMainWindow):
    def __init__(self, user_hand, app_hand):
        super().__init__()
        self.user_hand = user_hand
        self.app_hand = app_hand
        self.result_label = QLabel(self)
        self.result_label.setFont(QFont('Arial', 20, QFont.Bold))
        self.result_label.setAlignment(Qt.AlignCenter)
        self.initUI()

    def check_winner(self, user_choice, app_choice):
        if user_choice == app_choice:
            self.result_label.setText('<b>Empate!</b>')
        elif (user_choice == 'rock' and app_choice == 'scissors') or (user_choice == 'paper' and app_choice == 'rock') or (user_choice == 'scissors' and app_choice == 'paper'):
            self.result_label.setText('<b>Usuario gana!</b>')
        else:
            self.result_label.setText('<b>CPU gana!</b>')

    def initUI(self):
        self.setWindowTitle('Rock Paper Scissors')
        self.setGeometry(200, 200, 300, 300)

        self.rock_button = QPushButton('Rock', self)
        self.paper_button = QPushButton('Paper', self)
        self.scissors_button = QPushButton('Scissors', self)

        self.rock_button.clicked.connect(lambda: self.play('rock'))
        self.paper_button.clicked.connect(lambda: self.play('paper'))
        self.scissors_button.clicked.connect(lambda: self.play('scissors'))

        hands_layout = QHBoxLayout()
        hands_layout.addWidget(self.user_hand)
        hands_layout.addWidget(self.app_hand)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.rock_button)
        buttons_layout.addWidget(self.paper_button)
        buttons_layout.addWidget(self.scissors_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(hands_layout)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.result_label)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def play(self, choice):
        self.user_hand.play(choice)
        app_choice = random.choice(['rock', 'paper', 'scissors'])
        self.app_hand.play(app_choice)
        self.check_winner(choice, app_choice)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    user_hand = Hand()
    app_hand = Hand()
    main_win = MainWindow(user_hand, app_hand)
    main_win.showMaximized()
    sys.exit(app.exec_())