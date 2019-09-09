import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import regi_menu
import main

class MenuWindow(QMainWindow,regi_menu.Ui_PhotoWindow):
    def __init__(self, parent = None):
        super(MenuWindow, self).__init__(parent)
        self.setupUi(self)
        self.confirm_Button.clicked.connect(self.confirm)
    
    def confirm(self):
        self.close()
        self.m = main.Mainwindow()
        self.m.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuWindow()
    window.show()
    sys.exit(app.exec_())