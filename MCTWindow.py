import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import *
from MCTWindow_ui import *
from firebase import firebase
import pyrebase
global restid
fb = firebase.FirebaseApplication("https://misproject-65629.firebaseio.com/", None)
class MCTWindow(QMainWindow, Ui_MainWindow):
	global restid
	def __init__(self, parent = None):
		super(MCTWindow, self).__init__(parent)
		self.setupUi(self)
		self.pushButton.clicked.connect(self.confirmInfo)
		self.pushButton_2.clicked.connect(self.resetInfo)

	def confirmInfo(self):
		Mtask=fb.get('/MTask',None)
		Combotext = str(self.comboBox.currentText())
		if not (self.lineEdit.text()=="") & (self.lineEdit_2.text() ==""):
			if self.lineEdit_2.text().isdigit() & (int(self.lineEdit_2.text())>=50)& (int(self.lineEdit_2.text())<=95):
				if self.lineEdit.text() not in Mtask:
					print("Task Name: "+self.lineEdit.text()+"\n"+"Discount: "+self.lineEdit_2.text())
					mvalid = self.MValidDate.date().toString("yyyy-MM-dd")
					print(mvalid) 
					if (Combotext=="出示優惠畫面"):
						print("Prerequisite: Show Discount DM")
					elif (Combotext=="打卡"):
						print("Prerequisite: HashTag")
					elif (Combotext=="加入會員"):
						print("Prerequisite: Membership")
					MTaskCheckInfo.MTNAME=self.lineEdit.text()
					MTaskCheckInfo.MTDISC=self.lineEdit_2.text()
					MTaskCheckInfo.Date=self.MValidDate.date().toString("yyyy-MM-dd")
					MTaskCheckInfo.Prerequisite=str(self.comboBox.currentText())
					self.hide()
					self.current = MTaskCheckInfo()
					self.current.show()
				else:
					self.show_MSG("提示","已有相同任務名稱")
			else:
				self.show_MSG("提示","優惠請輸入數字(50~95)")
		else:
			self.show_MSG("提示","請輸入任務名稱")
			self.lineEdit.setText("")

		self.lineEdit.setText("")
		self.lineEdit_2.setText("")

	def resetInfo(self):
		self.lineEdit.setText("")
		self.lineEdit_2.setText("")

	def show_MSG(self,title,message):
		QMessageBox.information(None,title,message)
if __name__ == "__main__":
	app = QApplication(sys.argv)
	ManagerCTWin = MCTWindow()
	ManagerCTWin.show()
	sys.exit(app.exec_())