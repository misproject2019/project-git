import sys
from PyQt5.QtWidgets import QMainWindow, QApplication 
from PyQt5 import QtWebEngineWidgets 
import test23

class Ui_MainWindow(QMainWindow,test23.Ui_MainWindow):
    def __init__(self, parent = None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())