from PyQt5.QtWidgets import QMessageBox


def show_error_window(msg):
    msgbox = QMessageBox()
    msgbox.setIcon(QMessageBox.Warning)
    msgbox.setText(msg)
    msgbox.setWindowTitle('Authorization error')
    msgbox.setStandardButtons(QMessageBox.Ok)
    msgbox.exec()