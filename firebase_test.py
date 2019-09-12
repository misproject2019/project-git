import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import regi_info
import pyrebase


config ={
    "apiKey": "AIzaSyAMpfbvKqf5vK-dzz5H2Osu6CJ5d1ionA0",
    "authDomain": "misproject-65629.firebaseapp.com",
    "databaseURL": "https://misproject-65629.firebaseio.com",
    "projectId": "misproject-65629",
    "storageBucket": "misproject-65629.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

class InfoWindow(QMainWindow,regi_info.Ui_InfoWindow):
    restid = "745638"
    restna=""
    def __init__(self, parent = None):
        super(InfoWindow, self).__init__(parent)
        self.setupUi(self)
        self.label.setText(db.child("restaurant").child(self.restid).child("name").get().val())
        self.add_label.setText(db.child("restaurant").child(self.restid).child("address").get().val())
        time = db.child("restaurant").child(self.restid).child("time").get().val()
        opening_time = "\n".join(time)
        self.time_label.setText(opening_time)
        self.pn_label.setText(db.child("restaurant").child(self.restid).child("phone").get().val())
        self.tag_label.setText(db.child("restaurant").child(self.restid).child("tag").get().val())
        self.score_label.setText(str(db.child("restaurant").child(self.restid).child("rating").get().val()))
        self.pushButton_arrow.setStyleSheet('QPushButton{border-image:url(arrow.png)}')
        png=QtGui.QPixmap('https://lh3.googleusercontent.com/p/AF1QipNjg5Hb-MGhpOKA6fdKZsrM9WyloFySz7X5g0Kc=s1600-w400')
    # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        label.setPixmap(png)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InfoWindow()
    window.show()
    sys.exit(app.exec_())