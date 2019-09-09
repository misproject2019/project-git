import pyrebase
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from regi_tag import *
from res_menu import *

config ={
    "apiKey": "AIzaSyAMpfbvKqf5vK-dzz5H2Osu6CJ5d1ionA0",
    "authDomain": "misproject-65629.firebaseapp.com",
    "databaseURL": "https://misproject-65629.firebaseio.com",
    "projectId": "misproject-65629",
    "storageBucket": "misproject-65629.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

class TagWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent = None):
        global category
        super(TagWindow, self).__init__(parent)
        self.setupUi(self)
        self.next_Button.clicked.connect(self.tagBox)
        category = [self.checkBox, self.checkBox_2, self.checkBox_3, 
        self.checkBox_4, self.checkBox_5, self.checkBox_6, self.checkBox_7, self.checkBox_8]
        for categories in category:
            categories.stateChanged.connect(self.categoryChange)
        
    def categoryChange(self):
        global category
        count = 0
        while count < len(category):
            if category[count].isChecked():
                counting = 0
                while counting < len(category):
                    category[counting].setChecked(False)
                    if counting == count:
                        pass
                    counting = counting +1
            count = count+1

    def tagBox(self):
        global category
        restaurant = [self.checkBox_9, self.checkBox_10, self.checkBox_11, 
        self.checkBox_12, self.checkBox_13, self.checkBox_14, self.checkBox_15, self.checkBox_16]
        for res in restaurant:
            if res.isChecked():
                res_input = res.text()
        for categories in category:
            if categories.isChecked():
                cate_input = categories.text()
        data = {"tag1":str(cate_input),
                "tag2":str(res_input)}
        db.child("restaurant").child(self.restid).update(data)
        

        self.close()
        self.m = MenuWindow()
        self.m.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TagWindow()
    window.show()
    sys.exit(app.exec_())