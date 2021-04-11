################################################
################################################
################################################
#########*******###*******####**********########
########**#####**#**#####**###**######**########
########**#####**#**#####**###**######**########
########**#####**#**#####**###**********########
########**#####**#**#####**###**################
########**#####**#**#####**###**################
########**######***######**###**################
########**###############**###**################
########**###############**###**################
################################################
########Copyright © Maresal Programming#########
################################################

from PyQt5 import  QtWidgets,QtCore
import os,sys
from CovidDesign import Ui_MainWindow

class covidApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(covidApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(open("style.css","r").read())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.ui.ExitBtn.clicked.connect(self.exitButton)
        self.ui.minimizeBtn.clicked.connect(self.minimize)
        self.ui.InstagramBtn.clicked.connect(self.instaLink)
        self.ui.FacebookBtn.clicked.connect(self.faceLink)
        self.ui.GithubBtn.clicked.connect(self.githubLink)
        self.ui.homeBtn.clicked.connect(self.anasayfa)
        self.ui.turkiyeBtn.clicked.connect(self.turkiye)
        self.ui.dunyaBtn.clicked.connect(self.dunya)
        self.ui.abdBtn.clicked.connect(self.abd)

        self.turkiyeVeri()
        self.dunyaVeri()
        self.abdVeri()

    def anasayfa(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def dunya(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def turkiye(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    
    def abd(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    
    def turkiyeVeri(self):
        from bs4 import BeautifulSoup
        import requests

        url = "https://news.google.com/covid19/map?hl=tr&gl=TR&ceid=TR%3Atr&mid=%2Fm%2F01znc_"

        req = requests.get(url).content
        soup = BeautifulSoup(req,'html.parser')

        anaBilgiler = soup.find_all("div",{"class" : "UvMayb"})
        altbilgiler = soup.find_all("strong")

        anaBilgilerList = []
        altBilgilerList = []
        for a in anaBilgiler:
            anaBilgilerList.append(a.text)
        for b in altbilgiler:
            altBilgilerList.append(b.text)

        self.ui.TToplamSayiLbl.setText(anaBilgilerList[0])
        self.ui.TVakaArtisLbl.setText("Dün bildirilen Vaka sayısı  : "+ altBilgilerList[0])
        self.ui.TVefatSayiLbl.setText(anaBilgilerList[1])
        self.ui.TVefatArtisLbl.setText("Dün bildirilen vefat sayısı : "+ altBilgilerList[2])
        self.ui.TDozSayiLbl.setText(anaBilgilerList[2])
        self.ui.TDozArtisLbl.setText("Dün bildirilen doz sayısı  : "+ altBilgilerList[3])
        self.ui.TAsiOlanSayiLbl.setText(anaBilgilerList[3])
        self.ui.TAsiOlanYuzdeLbl.setText("Nüfus yüzdesi : "+altBilgilerList[5])

        self.ui.TVakaPrgLbl.setText("Toplam Vaka Sayısı : "+anaBilgilerList[0])
        self.ui.TAsiOlanSayiPrgLbl.setText("Toplam Aşı Olan Sayısı : "+anaBilgilerList[3])

        trNufus = 83614362 
        vakaSayisi = str(anaBilgilerList[0]).replace(".","")
        
        yuzde = (int(vakaSayisi) * 100) / trNufus

        self.progressBarValue(yuzde,self.ui.VakaPrg)
        self.ui.TVakaYuzdeLbl.setText(str(int(yuzde))+" %")


        self.progressBarValue(int(altBilgilerList[5].lstrip("%").split(",")[0]),self.ui.asiPrg)
        self.ui.TAsiYuzdeLbl.setText(altBilgilerList[5].lstrip("%").split(",")[0]+" %")

    def dunyaVeri(self):
        from bs4 import BeautifulSoup
        import requests

        url = "https://news.google.com/covid19/map?hl=tr&gl=TR&ceid=TR%3Atr"

        req = requests.get(url).content
        soup = BeautifulSoup(req,'html.parser')

        anaBilgiler = soup.find_all("div",{"class" : "UvMayb"})
        altbilgiler = soup.find_all("strong")

        anaBilgilerList = []
        altBilgilerList = []
        for a in anaBilgiler:
            anaBilgilerList.append(a.text)
        for b in altbilgiler:
            altBilgilerList.append(b.text)

        if len(altBilgilerList) >= 4 :  
            self.ui.DToplamSayiLbl.setText(anaBilgilerList[0])
            self.ui.DVakaArtisLbl.setText("Dün bildirilen Vaka sayısı  : "+ altBilgilerList[0])
            self.ui.DVefatSayiLbl.setText(anaBilgilerList[1])
            self.ui.DVefatArtisLbl.setText("Dün bildirilen vefat sayısı : "+ altBilgilerList[2])
            self.ui.DDozSayiLbl.setText(anaBilgilerList[2])
            self.ui.DDozArtisLbl.setText("Dün bildirilen doz sayısı  : "+ altBilgilerList[3])
            self.ui.DToplamSayiLbl.setText(anaBilgilerList[3])
            self.ui.DAsiOlanYuzdeLbl.setText("Nüfus yüzdesi : "+altBilgilerList[5])

            self.ui.DVakaPrgLbl.setText("Toplam Vaka Sayısı : "+anaBilgilerList[0])
            self.ui.DAsiOlanSayiPrgLbl.setText("Toplam Aşı Olan Sayısı : "+anaBilgilerList[3])
        else :
            self.ui.DToplamSayiLbl.setText(anaBilgilerList[0])
            self.ui.DVakaArtisLbl.setText("Dün bildirilen Vaka sayısı  : None")
            self.ui.DVefatSayiLbl.setText(anaBilgilerList[2])
            self.ui.DVefatArtisLbl.setText("Dün bildirilen vefat sayısı : None")
            self.ui.DDozSayiLbl.setText(anaBilgilerList[3])
            self.ui.DDozArtisLbl.setText("Dün bildirilen doz sayısı  : "+ altBilgilerList[0])
            self.ui.DAsiOlanSayiLbl.setText(anaBilgilerList[4])
            self.ui.DAsiOlanYuzdeLbl.setText("Nüfus yüzdesi : "+altBilgilerList[2])

            self.ui.DVakaPrgLbl.setText("Toplam Vaka Sayısı : "+anaBilgilerList[0])
            self.ui.DAsiOlanSayiPrgLbl.setText("Toplam Aşı Olan Sayısı : "+anaBilgilerList[4])

        dNufus = 7859092000 
        vakaSayisi = str(anaBilgilerList[0]).replace(".","")
        
        yuzde = (int(vakaSayisi) * 100) / dNufus

        self.progressBarValue(yuzde,self.ui.VakaPrg_6)
        self.ui.DVakaYuzdeLbl.setText(str(int(yuzde))+" %")


        self.progressBarValue(int(altBilgilerList[2].lstrip("%").split(",")[0]),self.ui.asiPrg_6)
        self.ui.DAsiYuzdeLbl.setText(altBilgilerList[2].lstrip("%").split(",")[0]+" %")

    def abdVeri(self):
        from bs4 import BeautifulSoup
        import requests

        url = "https://news.google.com/covid19/map?hl=tr&gl=TR&ceid=TR%3Atr&mid=%2Fm%2F09c7w0"

        req = requests.get(url).content
        soup = BeautifulSoup(req,'html.parser')

        anaBilgiler = soup.find_all("div",{"class" : "UvMayb"})
        altbilgiler = soup.find_all("strong")

        anaBilgilerList = []
        altBilgilerList = []
        for a in anaBilgiler:
            anaBilgilerList.append(a.text)
        for b in altbilgiler:
            altBilgilerList.append(b.text)

        aNufus = 331002651 

        if len(altBilgilerList) >= 4 :  
            self.ui.AToplamSayiLbl.setText(anaBilgilerList[0])
            self.ui.AVakaArtisLbl.setText("Dün bildirilen Vaka sayısı  : "+ altBilgilerList[0])
            self.ui.AVefatSayiLbl.setText(anaBilgilerList[1])
            self.ui.AVefatArtisLbl.setText("Dün bildirilen vefat sayısı : "+ altBilgilerList[2])
            self.ui.ADozSayiLbl.setText(anaBilgilerList[2])
            self.ui.ADozArtisLbl.setText("Dün bildirilen doz sayısı  : "+ altBilgilerList[3])
            self.ui.AAsiOlanSayiLbl.setText(anaBilgilerList[3])
            self.ui.AAsiOlanYuzdeLbl.setText("Nüfus yüzdesi : "+altBilgilerList[5])

            self.ui.AToplamVakaPrgLbl.setText("Toplam Vaka Sayısı : "+anaBilgilerList[0])
            self.ui.AAsiOlanSayiPrgLbl.setText("Toplam Aşı Olan Sayısı : "+anaBilgilerList[3])

            vakaSayisi = str(anaBilgilerList[0]).replace(".","")
            
            yuzde = (int(vakaSayisi) * 100) / aNufus

            self.progressBarValue(yuzde,self.ui.VakaPrg_12)
            self.ui.AVakaYuzdeLbl.setText(str(int(yuzde))+" %")


            self.progressBarValue(int(altBilgilerList[5].lstrip("%").split(",")[0]),self.ui.asiPrg_12)
            self.ui.AAsiYuzdeLbl.setText(altBilgilerList[5].lstrip("%").split(",")[0]+" %")

        else :
            self.ui.AToplamSayiLbl.setText(anaBilgilerList[0])
            self.ui.AVakaArtisLbl.setText("Dün bildirilen Vaka sayısı  : None")
            self.ui.AVefatSayiLbl.setText(anaBilgilerList[2])
            self.ui.AVefatArtisLbl.setText("Dün bildirilen vefat sayısı : None")
            self.ui.ADozSayiLbl.setText(anaBilgilerList[3])
            self.ui.ADozArtisLbl.setText("Dün bildirilen doz sayısı  : "+ altBilgilerList[0])
            self.ui.AAsiOlanSayiLbl.setText(anaBilgilerList[4])
            self.ui.AAsiOlanYuzdeLbl.setText("Nüfus yüzdesi : "+altBilgilerList[2])

            self.ui.AToplamVakaPrgLbl.setText("Toplam Vaka Sayısı : "+anaBilgilerList[0])
            self.ui.AAsiOlanSayiPrgLbl.setText("Toplam Aşı Olan Sayısı : "+anaBilgilerList[4])

            vakaSayisi = str(anaBilgilerList[0]).replace(".","")
            
            yuzde = (int(vakaSayisi) * 100) / aNufus

            self.progressBarValue(yuzde,self.ui.VakaPrg_12)
            self.ui.AVakaYuzdeLbl.setText(str(int(yuzde))+" %")


            self.progressBarValue(int(altBilgilerList[2].lstrip("%").split(",")[0]),self.ui.asiPrg_12)
            self.ui.AAsiYuzdeLbl.setText(altBilgilerList[2].lstrip("%").split(",")[0]+" %")

    def instaLink(self):
        os.startfile("https://www.instagram.com/maresalp/")
    def faceLink(self):
        os.startfile("https://www.facebook.com/maresalprogramming")
    def githubLink(self):
        os.startfile("https://github.com/IMaresaLI")






    def progressBarValue(self,value,progressBar):

        styleSheet = """
        QFrame{
        border-radius:100px;
        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));}
        """

        progress = (100 - value) / 100.0

        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        newStylesheet = styleSheet.replace("{STOP_1}",stop_1).replace("{STOP_2}",stop_2)

        progressBar.setStyleSheet(newStylesheet)

# Windows Setting

    def minimize(self):
        self.showMinimized()

    def exitButton(self):
        app.exit()

    def mousePressEvent(self, event):

        if event.buttons() == QtCore.Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):

        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = covidApp()
    app.setStyle("Fusion")
    main.show()
    app.exit(app.exec_())