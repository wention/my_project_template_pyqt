from PyQt6.QtCore import pyqtSlot as Slot
from PyQt6.QtWidgets import QMainWindow, QPushButton

from .mainwindow_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.click_count = 0

    @Slot()
    def on_btn_test_clicked(self):
        btn: QPushButton = self.sender()

        self.click_count += 1

        print(f"Clicked {self.click_count}")
        btn.setText(f"Clicked {self.click_count}")