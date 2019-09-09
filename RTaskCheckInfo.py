# encoding: utf-8
import sys
from PyQt5.QtWidgets import QWidget, QApplication
import RTaskCheckInfo_ui
import RCTWindow
from firebase import firebase
import pyrebase
import main
global restid
fb = firebase.FirebaseApplication("https://misproject-65629.firebaseio.com/", None)

class RTaskCheckInfo(QWidget, RTaskCheckInfo_ui.Ui_Form):
	RTNAME=""
	RTDISC=""
	Prerequisite=""
	pre_detail=""
	Start=""
	End=""
	def __init__(self, parent = None):
		super(RTaskCheckInfo, self).__init__(parent)
		self.setupUi(self)
		self.pushButton.clicked.connect(self.SendTaskData)
		self.pushButton_2.clicked.connect(self.BackTaskInfo)
		self.taskname.setText(self.RTNAME)
		self.label_disc.setText(self.RTDISC)
		self.label_pre.setText(self.Prerequisite)
		self.la_pre_detail.setText(self.pre_detail)
		self.valid_start.setText(self.Start)
		self.valid_end.setText(self.End)
	def SendTaskData(self):
		Rtask = fb.get('/RTask',None)
		for key,value in Rtask.items():
			fb.put('/RTask',self.RTNAME,{"rt_Name":self.RTNAME,"rt_Disc":self.RTDISC,"rt_Pre":self.Prerequisite,"rt_PreDetail":self.pre_detail,"rt_Start":self.Start,"rt_End":self.End})
		self.close()
		self.current= main.Mainwindow()
		self.current.show()
		
	def BackTaskInfo(self):
		self.hide()
		self.current= RCTWindow.RCTWindow()
		self.current.show()
		
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	RTaskCheckInfo = RTaskCheckInfo()
	RTaskCheckInfo.show()
	sys.exit(app.exec_())
	