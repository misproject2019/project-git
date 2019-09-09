import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import *
from MTaskCheckInfo_ui import *
from firebase import firebase
import pyrebase
global restid
fb = firebase.FirebaseApplication("https://misproject-65629.firebaseio.com/", None)

class MTaskCheckInfo(QWidget, Ui_Form):
	MTNAME=""
	MTDISC=""
	Date=""
	Prerequisite=""
	def __init__(self, parent = None):
		super(MTaskCheckInfo, self).__init__(parent)
		self.setupUi(self)
		self.pushButton.clicked.connect(self.SendTaskData)
		self.pushButton_2.clicked.connect(self.BackTaskInfo)
		self.taskname.setText(self.MTNAME)
		self.label_disc.setText(self.MTDISC)
		self.label_pre.setText(self.Prerequisite)
		self.label_date.setText(self.Date)
	def SendTaskData(self):
		
		Mtask=fb.get('/MTask',None)
		for key,value in Mtask.items():
			fb.put('/MTask',self.MTNAME,{"mt_Name":self.MTNAME,"mt_Disc":self.MTDISC,"mt_ValidDate":self.Date})
	def BackTaskInfo(self):
		self.hide()
		self.current= MCTWindow()
		self.current.show()
if __name__ == "__main__":
	app = QApplication(sys.argv)
	MTaskCheckInfo = MTaskCheckInfo()
	MTaskCheckInfo.show()
	sys.exit(app.exec_())
	