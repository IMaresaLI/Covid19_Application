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
import os,sys,time,requests
from CovidDesign import Ui_MainWindow
import DatabaseManager
from bs4 import BeautifulSoup

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
        self.worker()


    def anasayfa(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    def dunya(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.dunyaVeri()
    def turkiye(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.turkiyeVeri()
    def abd(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.abdVeri()

    def turkiyeVeri(self):
        data = DatabaseManager.sqliteData("Turkiye_Data")
        trVeri = data.getData()
        print(trVeri[-1])

        trNufus = 83614362 

        self.ui.TToplamSayiLbl.setText(trVeri[-1][1])
        self.ui.TVakaArtisLbl.setText("Dün bildirilen Vaka sayısı  : "+ trVeri[-1][2])
        self.ui.TVefatSayiLbl.setText(trVeri[-1][3])
        self.ui.TVefatArtisLbl.setText("Dün bildirilen vefat sayısı : "+ trVeri[-1][4])
        self.ui.TDozSayiLbl.setText(trVeri[-1][5])
        self.ui.TDozArtisLbl.setText("Dün bildirilen doz sayısı  : "+ trVeri[-1][6])
        self.ui.TAsiOlanSayiLbl.setText(trVeri[-1][7])
        self.ui.TAsiOlanYuzdeLbl.setText("Nüfus yüzdesi : "+trVeri[-1][8])

        self.ui.TVakaPrgLbl.setText("Toplam Vaka Sayısı : "+trVeri[-1][1])
        self.ui.TAsiOlanSayiPrgLbl.setText("Toplam Aşı Olan Sayısı : "+trVeri[-1][7])

        vakaSayisi = trVeri[-1][1].replace(".","")
        
        yuzde = (int(vakaSayisi) * 100) / trNufus

        self.progressBarValue(yuzde,self.ui.VakaPrg)
        self.ui.TVakaYuzdeLbl.setText(str(int(yuzde))+" %")


        self.progressBarValue(int(trVeri[-1][8].lstrip("%").split(",")[0]),self.ui.asiPrg)
        self.ui.TAsiYuzdeLbl.setText(trVeri[-1][8].lstrip("%").split(",")[0]+" %")

    def dunyaVeri(self):
        data = DatabaseManager.sqliteData("Global_Data")
        trVeri = data.getData()
        print(trVeri[-1])

        dNufus = 7859092000 

        self.ui.DToplamSayiLbl.setText(trVeri[-1][1])
        self.ui.DVakaArtisLbl.setText("Dün bildirilen Vaka sayısı  : "+ trVeri[-1][2])
        self.ui.DVefatSayiLbl.setText(trVeri[-1][3])
        self.ui.DVefatArtisLbl.setText("Dün bildirilen vefat sayısı : "+ trVeri[-1][4])
        self.ui.DDozSayiLbl.setText(trVeri[-1][5])
        self.ui.DDozArtisLbl.setText("Dün bildirilen doz sayısı  : "+ trVeri[-1][6])
        self.ui.DAsiOlanSayiLbl.setText(trVeri[-1][7])
        self.ui.DAsiOlanYuzdeLbl.setText("Nüfus yüzdesi : "+trVeri[-1][8])

        self.ui.DVakaPrgLbl.setText("Toplam Vaka Sayısı : "+trVeri[-1][1])
        self.ui.DAsiOlanSayiPrgLbl.setText("Toplam Aşı Olan Sayısı : "+trVeri[-1][7])

        vakaSayisi = trVeri[-1][1].replace(".","")
        
        yuzde = (int(vakaSayisi) * 100) / dNufus

        self.progressBarValue(yuzde,self.ui.VakaPrg_6)
        self.ui.DVakaYuzdeLbl.setText(str(int(yuzde))+" %")


        self.progressBarValue(int(trVeri[-1][8].lstrip("%").split(",")[0]),self.ui.asiPrg_6)
        self.ui.DAsiYuzdeLbl.setText(trVeri[-1][8].lstrip("%").split(",")[0]+" %")

    def abdVeri(self):
        data = DatabaseManager.sqliteData("ABD_Data")
        trVeri = data.getData()

        aNufus = 331002651 

        self.ui.AToplamSayiLbl.setText(trVeri[-1][1])
        self.ui.AVakaArtisLbl.setText("Dün bildirilen Vaka sayısı  : "+ trVeri[-1][2])
        self.ui.AVefatSayiLbl.setText(trVeri[-1][3])
        self.ui.AVefatArtisLbl.setText("Dün bildirilen vefat sayısı : "+ trVeri[-1][4])
        self.ui.ADozSayiLbl.setText(trVeri[-1][5])
        self.ui.ADozArtisLbl.setText("Dün bildirilen doz sayısı  : "+ trVeri[-1][6])
        self.ui.AAsiOlanSayiLbl.setText(trVeri[-1][7])
        self.ui.AAsiOlanYuzdeLbl.setText("Nüfus yüzdesi : "+trVeri[-1][8])

        self.ui.AToplamVakaPrgLbl.setText("Toplam Vaka Sayısı : "+trVeri[-1][1])
        self.ui.AAsiOlanSayiPrgLbl.setText("Toplam Aşı Olan Sayısı : "+trVeri[-1][7])

        vakaSayisi = trVeri[-1][1].replace(".","")
            
        yuzde = (int(vakaSayisi) * 100) / aNufus

        self.progressBarValue(yuzde,self.ui.VakaPrg_12)
        self.ui.AVakaYuzdeLbl.setText(str(int(yuzde))+" %")


        self.progressBarValue(int(trVeri[-1][8].lstrip("%").split(",")[0]),self.ui.asiPrg_12)
        self.ui.AAsiYuzdeLbl.setText(trVeri[-1][8].lstrip("%").split(",")[0]+" %")

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

    def worker(self):
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.finished.connect(self.workerStop)

    def workerStop(self):
        print("Bitti")


class WorkerThread(QtCore.QThread):
    def run(self):

        links = ["https://news.google.com/covid19/map?hl=tr&gl=TR&ceid=TR%3Atr","https://news.google.com/covid19/map?hl=tr&gl=TR&ceid=TR%3Atr&mid=%2Fm%2F01znc_","https://news.google.com/covid19/map?hl=tr&gl=TR&ceid=TR%3Atr&mid=%2Fm%2F09c7w0"]
        table = ["Global_Data","Turkiye_Data","ABD_Data"]
        n=0
        for link in links :
            req = requests.get(link).content
            soup = BeautifulSoup(req,'html.parser')

            anaBilgiler = soup.find_all("div",{"class" : "UvMayb"})
            altbilgiler = soup.find_all("strong")

            anaBilgilerList = []
            altBilgilerList = []
            for a in anaBilgiler:
                anaBilgilerList.append(a.text)
            for b in altbilgiler:
                altBilgilerList.append(b.text)

            if len(altBilgilerList) > 4 :
                data = DatabaseManager.sqliteData(table[n])
                data.Add(anaBilgilerList[0],altBilgilerList[0],anaBilgilerList[1],altBilgilerList[2],anaBilgilerList[2],altBilgilerList[3],anaBilgilerList[3],altBilgilerList[5])
                n+=1
            else :
                data = DatabaseManager.sqliteData(table[n])
                data.Add(anaBilgilerList[0],"None",anaBilgilerList[2],"None",anaBilgilerList[3],altBilgilerList[0],anaBilgilerList[4],altBilgilerList[2])
                n+=1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = covidApp()
    app.setStyle("Fusion")
    main.show()
    app.exit(app.exec_())
