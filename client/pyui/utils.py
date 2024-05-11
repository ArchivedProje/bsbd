from PyQt5.QtWidgets import QMessageBox
from hashlib import sha256


def show_error_window(msg):
    msgbox = QMessageBox()
    msgbox.setIcon(QMessageBox.Warning)
    msgbox.setText(msg)
    msgbox.setWindowTitle('Authorization error')
    msgbox.setStandardButtons(QMessageBox.Ok)
    msgbox.exec()


def show_success_window(msg):
    msgbox = QMessageBox()
    msgbox.setIcon(QMessageBox.Information)
    msgbox.setText(msg)
    msgbox.setStandardButtons(QMessageBox.Ok)
    msgbox.exec()


def hash_password(password):
    passwd_len = len(password)
    for i in range(passwd_len):
        password += chr((ord(password[i]) + 1) % 100)
    return sha256(password.encode('utf-8')).hexdigest()
