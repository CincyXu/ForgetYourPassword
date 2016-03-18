# 2016/01/28 22:09
# __author__ = 'Cindy'
# coding:utf-8


import sys
from hashlib import sha256
from PyQt5.QtCore import QCoreApplication, pyqtSignal
from PyQt5.QtWidgets import (QLabel, QLineEdit, QTextEdit, QGridLayout, QWidget,
                             QPushButton, QHBoxLayout, QVBoxLayout, QApplication)


class ForgetYourPassword:
    """"""
    def __init__(self, key, salt, password_length=10):
        self.key = key
        self.salt = salt
        self.password_length = int(password_length)

    def single_ele(self, n):
        if 0 <= n <= 9:
            return str(n)
        elif 10 <= n <= 35:
            return chr(n+55)
        elif 36 <= n <= 61:
            return chr(n+61)

    def make_password(self):
        ele = ""
        sha = sha256("{}{}{}".format(self.key, "\U000E0031", self.salt).encode("utf-8"))
        hexadecimal_num = sha.hexdigest()
        decimal_num = int(hexadecimal_num, 16)
        for i in range(self.password_length):
            ele += self.single_ele(int(decimal_num % 62))
            decimal_num = int(decimal_num/62)
        return ele


class Password(QWidget):
    """用pyqt5制作界面"""
    def __init__(self):
        super().__init__()

        key = QLabel("Key:")
        salt = QLabel("Salt:")
        length = QLabel("Length:")
        pass_str = QLabel("password:")
        self.key_line = QLineEdit(self)
        self.salt_line = QLineEdit(self)
        self.len_line = QLineEdit(self)
        self.result = QTextEdit(self)

        gridLayout = QGridLayout()
        gridLayout.addWidget(key, 0, 0, 1, 1)
        gridLayout.addWidget(salt, 1, 0, 1, 1)
        gridLayout.addWidget(length, 2, 0, 1, 1)
        gridLayout.addWidget(pass_str, 3, 0, 1, 1)
        gridLayout.addWidget(self.key_line, 0, 1, 1, 3)
        gridLayout.addWidget(self.salt_line, 1, 1, 1, 3)
        gridLayout.addWidget(self.len_line, 2, 1, 1, 3)
        gridLayout.addWidget(self.result, 3, 1, 1, 3)

        ok_btn = QPushButton("Ok", self)
        # cancel_btn = QPushButton("")
        btnLayout = QHBoxLayout()

        btnLayout.setSpacing(60)
        btnLayout.addWidget(ok_btn)
        # btnLayout.addWidget(cancelBtn)

        passwordLayout = QVBoxLayout()
        passwordLayout.setContentsMargins(40, 40, 40, 40)
        passwordLayout.addLayout(gridLayout)
        passwordLayout.addStretch(40)
        passwordLayout.addLayout(btnLayout)

        self.setLayout(passwordLayout)
        ok_btn.clicked.connect(self.on_changed)
        # cancelBtn.clicked.connect(self.reject)

        self.setWindowTitle("Password")
        self.resize(500, 400)

    def on_changed(self):

        key = self.key_line.text().strip()
        salt = self.salt_line.text().strip()
        length = self.len_line.text().strip()
        pwd = ForgetYourPassword(key, salt, length)
        self.result.setText(pwd.make_password())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    password = Password()
    password.show()
    sys.exit(app.exec_())




