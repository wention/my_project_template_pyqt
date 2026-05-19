import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from myapp.ui.mainwindow import MainWindow

def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())

