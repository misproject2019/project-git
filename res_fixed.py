import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
import regi_fixed
import res_info

class FixedWindow(QMainWindow,regi_fixed.Ui_FixedWindow):
    def __init__(self, parent = None):
        super(FixedWindow, self).__init__(parent)
        self.setupUi(self)
        self.back_Button.clicked.connect(self.backInfo)
        self.next_Button.clicked.connect(self.fixedInfo)
        cities = ["縣/市", "基隆市", "台北市", "新北市", "桃園市", "新竹縣", "新竹市"
        , "苗栗縣", "南投縣", "台中市", "彰化縣", "雲林縣", "嘉義縣"
        , "嘉義市", "台南市", "高雄市", "屏東縣", "宜蘭縣"
        , "花蓮縣", "台東縣", "金門縣", "連江縣", "澎湖縣"]
        self.comboBox_cities.addItems(cities)
        self.comboBox_cities.currentTextChanged.connect(self.dropbox)
        self.timeEdit_start.setDisplayFormat("HH:mm")
        self.timeEdit_end.setDisplayFormat("HH:mm")
    def dropbox(self):
        if self.comboBox_cities.currentText() == "基隆市":
            self.comboBox_area.clear()
            Keelung = ["中正", "信義", "仁愛", "中山", '安樂', '暖暖', '七堵' ]
            self.comboBox_area.addItems(Keelung)
            self.label_pa.setText("(02)")
        elif self.comboBox_cities.currentText() == "台北市":
            self.comboBox_area.clear()
            Taipei = ['松山', '大同', '內湖', '士林', '信義', '萬華', '大安', '中山',
             '南港', '北投', '中正', '文山']
            self.comboBox_area.addItems(Taipei)
            self.label_pa.setText("(02)")
        elif self.comboBox_cities.currentText() == "新北市":
            self.comboBox_area.clear()
            NTaipei = ['三重', '永和', '新莊', '新店', '土城', '汐止', '樹林', '三峽', '淡水', 
            '坪林', '林口', '板橋', '石門', '八里', '五股', '蘆洲', '泰山', '中和', '鶯歌', 
            '深坑', '金山', '三芝', '烏來', '石碇', '萬里', '瑞芳', '平溪', '雙溪', '貢寮' ]
            self.comboBox_area.addItems(NTaipei)  
            self.label_pa.setText("(02)") 
        elif self.comboBox_cities.currentText() == "桃園市":
            self.comboBox_area.clear()
            Taoyuan = ['中壢', '復興', '大園', '新屋', '楊梅', '桃園', '大溪'
            , '蘆竹', '八德', '龍潭', '平鎮', '觀音', '龜山' ]
            self.comboBox_area.addItems(Taoyuan)
            self.label_pa.setText("(03)")
        elif self.comboBox_cities.currentText() == "新竹縣":
            self.comboBox_area.clear()
            HsinchuC = ['尖石', '竹北', '竹東', '寶山', '峨眉', '五峰', '橫山', '新豐'
            , '湖口', '新埔', '北埔', '芎林', '關西']
            self.comboBox_area.addItems(HsinchuC)
            self.label_pa.setText("(03)")
        elif self.comboBox_cities.currentText() == "新竹市":
            self.comboBox_area.clear()
            Hsinchu = ['北區', '東區', '香山' ]
            self.comboBox_area.addItems(Hsinchu)    
            self.label_pa.setText("(03)")
        elif self.comboBox_cities.currentText() == "苗栗縣":
            self.comboBox_area.clear()
            Miaoli = ['苗栗', '苑裡', '通宵', '竹南', '頭份', '後龍', '卓蘭',
             '大湖', '公館', '銅鑼', '南庄', '頭屋', '三義', '西湖', '造橋', '三灣', '獅潭', '泰安' ]
            self.comboBox_area.addItems(Miaoli)  
            self.label_pa.setText("(037)")
        elif self.comboBox_cities.currentText() == "南投縣":
            self.comboBox_area.clear()
            Nantou = ['埔里', '集集', '竹山', '南投', '名間', '草屯', '國姓'
            , '中寮', '魚池', '鹿谷', '水里', '信義', '仁愛' ]
            self.comboBox_area.addItems(Nantou)  
            self.label_pa.setText("(049)")
        elif self.comboBox_cities.currentText() == "台中市":
            self.comboBox_area.clear()
            Taichung = ['南區', '東區', '中區', '西區', '北區', '南屯', '北屯'
            , '西屯', '豐原', '大里', '太平', '大甲', '清水', '梧棲', '沙鹿'
            , '東勢', '神岡', '大雅', '潭子', '后里', '外埔', '大安', '龍井'
            , '大肚', '烏日', '霧峰', '石岡', '新社', '和平'  ]
            self.comboBox_area.addItems(Taichung) 
            self.label_pa.setText("(04)")
        elif self.comboBox_cities.currentText() == "彰化縣":
            self.comboBox_area.clear()
            Changhua = ['鹿港', '二林', '彰化', '秀水', '二水', '溪洲',
             '竹塘', '大城', '埤頭', '田中', '社頭', '員林', '埔心', '溪湖',
              '芳苑', '埔鹽', '大村', '芬園', '花壇', '福興', '和美', '線西',
               '伸港', '北斗', '田尾', '永靖' ]
            self.comboBox_area.addItems(Changhua) 
            self.label_pa.setText("(04)")
        elif self.comboBox_cities.currentText() == "雲林縣":
            self.comboBox_area.clear()
            Yunlin = ['水林', '麥寮', '台西', '東勢', '四湖', '口湖', 
            '北港', '褒忠', '崙背', '元長', '土庫', '二崙', '西螺', 
            '虎尾', '大埤', '莿桐', '林內', '斗六', '斗南', '古坑'  ]
            self.comboBox_area.addItems(Yunlin) 
        elif self.comboBox_cities.currentText() == "嘉義縣":
            self.comboBox_area.clear()
            Chiayi = ['東石', '布袋', '義竹', '朴子', '鹿草', '六腳', '太保'
            , '新港', '溪口', '大林', '民雄', '水上', '梅山', '竹崎', '中埔'
            , '番路', '阿里山', '大埔'   ]
            self.comboBox_area.addItems(Chiayi) 
            self.label_pa.setText("(05)")
        elif self.comboBox_cities.currentText() == "嘉義市":
            self.comboBox_area.clear()
            ChiayiC = ['西區', '東區'  ]
            self.comboBox_area.addItems(ChiayiC) 
            self.label_pa.setText("(05)")
        elif self.comboBox_cities.currentText() == "台南市":
            self.comboBox_area.clear()
            Tainan = ['安南', '安平', '東區', '中西區', '南區', '北區',
             '新營', '六甲', '西港', '七股', '佳里', '麻豆', '將軍', '北門',
              '學甲', '鹽水', '後壁', '下營', '柳營', '官田', '善化', '安定',
               '新市', '大內', '山上', '新化', '永康', '仁德', '歸仁', '關廟',
                '龍崎', '左鎮', '南化', '玉井', '楠西', '東山', '白河' ]
            self.comboBox_area.addItems(Tainan)
            self.label_pa.setText("(06)")
        elif self.comboBox_cities.currentText() == "高雄市":
            self.comboBox_area.clear()
            Kaohsiung = ['左營', '楠梓', '三民', '新興', '苓雅', '前金', '前鎮',
             '旗津', '小港', '鹽埕', '鼓山', '那瑪夏', '桃源', '茂林', '甲仙', '六龜',
              '杉林', '美濃', '內門', '仁武', '田寮', '旗山', '梓官', '阿蓮', '湖內',
               '岡山', '茄萣', '路竹', '鳥松', '永安', '燕巢', '大樹', '大寮', '林園',
                '彌陀', '橋頭', '大社', '鳳山' ]
            self.comboBox_area.addItems(Kaohsiung)  
            self.label_pa.setText("(07)")
        elif self.comboBox_cities.currentText() == "屏東縣":
            self.comboBox_area.clear()
            Pingtung = ['屏東', '潮州', '東港', '恆春', '萬丹', '長治', '麟洛', '九如',
             '里港', '鹽埔', '高樹', '萬巒', '內埔', '竹田', '新埤', '新園', '崁頂', 
             '林邊', '南州', '佳冬', '琉球', '車城', '枋山', '枋寮', '三地門', '霧台',
              '瑪家', '泰武', '來義', '春日', '獅子', '牡丹', '滿洲']
            self.comboBox_area.addItems(Pingtung)  
            self.label_pa.setText("(08)")
        elif self.comboBox_cities.currentText() == "宜蘭縣":
            self.comboBox_area.clear()
            Yilan = ['礁溪', '冬山', '蘇澳', '頭城', '五結', '羅東', '員山'
            , '大同', '南澳', '壯圍', '三星', '宜蘭' ]
            self.comboBox_area.addItems(Yilan) 
            self.label_pa.setText("(03)")
        elif self.comboBox_cities.currentText() == "花蓮縣":
            self.comboBox_area.clear()
            Hualien = ['秀林', '玉里', '富里', '花蓮', '壽豐', '吉安', 
            '鳳林', '光復', '豐濱', '瑞穗', '新城', '萬榮', '卓溪']
            self.comboBox_area.addItems(Hualien) 
            self.label_pa.setText("(03)")
        elif self.comboBox_cities.currentText() == "台東縣":
            self.comboBox_area.clear()
            Taitung = ['東河', '台東', '長濱', '成功', '池上', '關山',
             '鹿野', '太麻里', '大武', '綠島', '蘭嶼', '海端', '延平', 
             '卑南', '金峰', '達仁' ]
            self.comboBox_area.addItems(Taitung) 
            self.label_pa.setText("(089)")
        elif self.comboBox_cities.currentText() == "金門縣":
            self.comboBox_area.clear()
            Kinmen = ['烈嶼', '金城', '金寧', '金湖', '金沙', '烏坵' ]
            self.comboBox_area.addItems(Kinmen) 
            self.label_pa.setText("(082)")
        elif self.comboBox_cities.currentText() == "連江縣":
            self.comboBox_area.clear()
            Lienchiang = ['莒光', '南竿', '北竿', '東引' ]
            self.comboBox_area.addItems(Lienchiang) 
            self.label_pa.setText("(0836)")
        else :
            self.comboBox_area.clear()
            Penghu = ['七美', '望安', '湖西', '馬公', '西嶼', '白沙' ]
            self.comboBox_area.addItems(Penghu) 
            self.label_pa.setText("(06)")

    def backInfo(self):
        self.hide()
        self.i=res_info.InfoWindow()
        self.i.show()

    def fixedInfo(self):
        if self.lineEdit_name.text() != "" and self.lineEdit_pn.text() != "" and self.lineEdit_road.text() != "":
            address = str(self.comboBox_cities.currentText())+str(self.comboBox_area.currentText())+"區"+str(self.lineEdit_road.text())
            phone = str(self.label_pa.text())+str(self.lineEdit_pn.text())
            time = self.timeEdit_start.time().toString() + "~" +self.timeEdit_end.time().toString()
            db.child("restaurant").child(610234).update({"name": str(self.lineEdit_name.text()), "phone":phone, "address":address, "time":time})
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FixedWindow()
    window.show()
    sys.exit(app.exec_())

