import sys
from pyui.auth_window import AuthWindow
from PyQt5.QtWidgets import QApplication, QMainWindow


def login():
    app = QApplication(sys.argv)
    win = AuthWindow(lambda: print('authorized!'))
    win.show()
    app.exec()


def main():
    login()


if __name__ == "__main__":
    main()
