from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

from dersOzel_PY import Ui_Form as Ui_Form9
from dersTavsiye_PY import Ui_Form as Ui_Form8
from denemeEklendi_PY import Ui_Form as Ui_Form7
from denemeEkle_PY import Ui_Form as Ui_Form6
from ogrenciBulListe_PY import Ui_Form as Ui_Form5
from ogrenciBul_PY import Ui_Form as Ui_Form4
from silmeKontrol_PY import Ui_Form as Ui_Form3
from widget_PY import Ui_Form as Ui_Form2
from login_PY import Ui_Form as Ui_Form1

from ekle_cikar_PY import Ui_MainWindow
from liste_PY import Ui_MainWindow as Ui_MainWindow1
from ogretmenDeneme_PY import Ui_MainWindow as Ui_MainWindow2
from DenemeGor_PY import Ui_MainWindow as Ui_MainWindow3
from ogrenciDeneme_PY import Ui_MainWindow as Ui_MainWindow4
import random, os
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import sqlite3 as sql

os.chdir(f"{os.path.dirname(__file__)}")

sozler = [

    ["Gelecek, bugünden hazırlanan bir yerdir.","Malcolm X"],
    ["Başarı, küçük çabaların tekrar tekrar tekrarlanmasından doğar.","Robert Collier"],
    ["Eğitimdir ki bir milleti ya özgür, bağımsız, şanlı, yüksek bir topluluk halinde yaşatır ya da esaret ve sefalete terk eder.","Mustafa Kemal Atatürk"],
    ["En büyük zafer, düşmemekte değil, her düştüğünde ayağa kalkmaktır.","Vince Lombardi"],
    ["Kendinize inanın ve ne olursa olsun devam edin.","Walt Disney"],
    ["Hayatta en hakiki mürşit ilimdir.","Mustafa Kemal Atatürk"],
    ["Zorluklar, insanın kendini keşfetmesi için bir fırsattır.","Ralph Waldo Emerson"],
    ["Hedeflerinizden asla vazgeçmeyin.","Albert Einstein"],
    ["Zafer, 'zafer benimdir' diyebilenlerindir.","Mustafa Kemal Atatürk"],
    ["Başarının sırrı, sürekli olarak öğrenmektir.","John C. Maxwell"],
    ["Yapabileceğinize inandığınızda, başaramayacağınız hiçbir şey yoktur.","Mary Kay Ash"],
    ["Milletimizin geleceği, bugünkü gençlerin doğru görüşü ve yorulmak bilmeyen çalışma azmi ile büyük ve parlak olacaktır.","Mustafa Kemal Atatürk"],
    ["Hayatınızı hayalleriniz doğrultusunda yaşayın.","Les Brown"],
    ["Kendinize bir hedef belirleyin ve ona ulaşmak için çalışın.","Bruce Lee"],
    ["Vatanını en çok seven, görevini en iyi yapandır.","Mustafa Kemal Atatürk"],
    ["Başarı, hazırlık ve fırsatın birleştiği noktadır.","Bobby Unser"],
    ["Düşüncelerinize dikkat edin; onlar sözlerinize dönüşür.","Mahatma Gandhi"],
    ["Hayatta en önemli şey, kendinizi tanımaktır.","Socrates"],
    ["Egemenlik kayıtsız şartsız milletindir.","Mustafa Kemal Atatürk"],
    ["Başarı, cesaretin ödülüdür.","George S. Patton"],
    ["Yarın, bugünden yaptıklarınızın sonucudur.","Mahatma Gandhi"],
    ["Başarı, hayallerinizin peşinden gitmekle başlar.","Paulo Coelho"],
    ["Yapabileceğiniz en büyük yatırım, kendinize yaptığınız yatırımdır.","Warren Buffett"],
    ["Yüksel Türk! Senin için yüksekliğin sınırı yoktur.","Mustafa Kemal Atatürk"],
    ["Başarı, kararlılıkla çalışmanın sonucudur.","Colin Powell"],
    ["Hayallerinizin peşinden gitmek, en büyük cesareti gerektirir.","Oprah Winfrey"],
    ["İnsanı yenilgi değil, vazgeçiş bitirir.","Richard Nixon"],
    ["Başarı, azim ve kararlılıkla gelir.","Conrad Hilton"],
    ["Hayatta en önemli şey, neyin peşinden gittiğinizdir.","Joseph Campbell"],
    ["Beni görmek demek mutlaka yüzümü görmek değildir. Benim fikirlerimi, benim duygularımı anlıyorsanız ve hissediyorsanız bu kafidir.","Mustafa Kemal Atatürk"],
    ["Başarıya giden yol, sürekli olarak bir hedefe odaklanmaktan geçer.","Vince Lombardi"],
    ["Başarı, başkalarının imkansız olduğunu düşündüğü şeyleri yapmaktır.","Walter Bagehot"],
    ["Gerçek başarı, mutluluğun peşinden gitmekle başlar.","Helen Keller"],
    ["Zorluklar, karşımıza çıkmak için değil, aşılmak için vardır.","Albert Schweitzer"],
    ["Yapabileceğinize inandığınızda, yolun yarısını zaten kat etmişsinizdir.","Theodore Roosevelt"],
    ["Kendinize inanmadıkça, hiç kimseye inanamazsınız.","Dorothy Day"],
    ["Hedefleriniz için çalıştığınızda, hayalleriniz gerçeğe dönüşür.","Les Brown"],
    ["Cesaret, korkuya rağmen devam edebilmektir.","Franklin D. Roosevelt"],
    ["Başarısızlık, başarıya giden en emin yoldur.","Thomas Edison"],
    ["Küçük adımlarla büyük işler başarılır.","Laozi"],
    ["Hayallerinizin peşinden gidin, çünkü başka bir yolunuz yok.","James Cameron"],
    ["Hayatın anlamı, neyin peşinden gittiğinizde saklıdır.","Joseph Campbell"],
    ["Düşüncelerinize dikkat edin; onlar sözlerinize dönüşür.","Mahatma Gandhi"],
    ["Başarı, hazırlık ve fırsatın birleştiği noktadır.","Bobby Unser"],
    ["Kendinize bir hedef belirleyin ve ona ulaşmak için çalışın.","Bruce Lee"],
    ["En büyük zaferimiz, hiç düşmemekte değil, her düştüğümüzde ayağa kalkmaktır.","Confucius"],
    ["Hayatta en önemli şey, kendinizi tanımaktır.","Socrates"],
    ["Başarının sırrı, pes etmemekte yatar.","Winston Churchill"],
    ["Yapabileceğinize inandığınızda, başaramayacağınız şey yoktur.","Mary Kay Ash"],
    ["Başarı, tutkularınızın peşinden gitmektir.","Oprah Winfrey"],
    ["Hayatınızı değiştirmek için asla geç değildir.","Jane Fonda"],
    ["Başarı, her gün küçük adımlar atarak gelir.","Robert Collier"],
    ["Düşünceleriniz, geleceğinizi şekillendirir.","Norman Vincent Peale"],
    ["Kendinizi sürekli geliştirerek başarıya ulaşabilirsiniz.","Tony Robbins"],
    ["Başarı, cesaretin ödülüdür.","George S. Patton"],
    ["Yarın, bugünden yaptıklarınızın sonucudur.","Mahatma Gandhi"],
    ["Başarı, hayallerinizin peşinden gitmekle başlar.","Paulo Coelho"],
    ["Yapabileceğiniz en büyük yatırım, kendinize yaptığınız yatırımdır.","Warren Buffett"],
    ["Başarı, kararlılıkla çalışmanın sonucudur.","Colin Powell"],
    ["Hayallerinizin peşinden gitmek, en büyük cesareti gerektirir.","Oprah Winfrey"],
    ["Güneşi esirgemiyorsa gökyüzü, birileri o günlerin bedelini ödediği içindir.","???"],
]



connect = sql.connect("data.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS ogrenciList(key text, ad text, soyad text, number integer)""")

app = QApplication([])

denemeGorListe = []
denemeInfoListe = []
denemeOzelListe = []

def refresRowidsInOgrenciList():
    cursor.execute("""SELECT rowid FROM ogrenciList""")
    rowids = cursor.fetchall()
    for i in range(1,len(rowids)+1):
        cursor.execute(f"""UPDATE ogrenciList SET rowid = {i} WHERE rowid = {rowids[i-1][0]}""")
        connect.commit()

class loginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.login = Ui_Form1()
        self.login.setupUi(self)
        self.loginChange = 1
        self.login.radioButton.clicked.connect(self.ogretmenSelect)
        self.login.radioButton_2.clicked.connect(self.ogrenciSelect)
        self.login.pushButton.clicked.connect(self.loginButton)
    def ogretmenSelect(self):
        self.loginChange = 1
    def ogrenciSelect(self):
        self.loginChange = 0
    def loginButton(self):
        key = self.login.lineEdit.text()
        if self.loginChange == 1:
            if key == "a":
                ogretmenM.show()
                self.close()
            else:
                self.login.label.setText("Hatalı Anahtar")
                self.login.lineEdit.setText("")
        elif self.loginChange == 0:
            cursor.execute("""SELECT name from sqlite_master""")
            keys = cursor.fetchall()
            if not (key,) in keys:
                self.login.label.setText("Hatalı Anahtar")
                self.login.lineEdit.setText("")
            else:
                self.close()
                sozX = random.choice(sozler)
                soz = sozX[0]
                soyleyen = sozX[1]
                yazi = '"' + soz + '"' + f"\n\n  - {soyleyen}"
                ogrenciM.menu.label.setText(yazi)
                ogrenciM.key = self.login.lineEdit.text()
                ogrenciM.refreshList()
                ogrenciM.show()

class ogretmenMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.menu = Ui_Form2()
        self.menu.setupUi(self)
        self.silmeModu = None
        self.menu.pushButton.clicked.connect(self.ekle_cikar_ac)
        self.menu.pushButton_2.clicked.connect(self.liste)
    def ekle_cikar_ac(self):
        ekle_cikar_menu.menu.label_4.setText("")
        ekle_cikar_menu.refreshList()
        ekle_cikar_menu.show()
    def liste(self):
        liste.refreshList()
        liste.show()
    
    def closeEvent(self,event):
        ekle_cikar_menu.close()
        liste.close()
        silmeKontrolM.close()
        filtreM.close()
        filtre2M.close()
        denemeEkleM.close()
        denemeEklendiM.close()
        liste.ogretmenDenemeControl.close()
        for i in denemeGorListe:
            del denemeGorListe[denemeGorListe.index(i)]

class ogrenciDeneme(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = Ui_MainWindow4()
        self.menu.setupUi(self)
        self.menu.listWidget.doubleClicked.connect(self.denemeGor)
    def refreshList(self):
        cursor.execute(f"""SELECT rowid,denemeAdi FROM {self.key} """)
        listOfDeneme = cursor.fetchall()
        for i in listOfDeneme:
            self.menu.listWidget.addItem(f"{i[0]}- {i[1]}")
    def denemeGor(self):
        deneme = self.menu.listWidget.currentItem().text()[0]
        cursor.execute(f"""SELECT * FROM {self.key} WHERE rowid = {deneme}""")
        denemeA = cursor.fetchall()[0]
        denemeAdi = denemeA[0]
        denemeTurkce = denemeA[1].split("-")
        denemeSosyal = denemeA[2].split("-")
        denemeDin = denemeA[3].split("-")
        denemeIng = denemeA[4].split("-")
        denemeMat = denemeA[5].split("-")
        denemeFen = denemeA[6].split("-")
        denemeGorListe.append(denemeGor())
        denemeGorListe[-1].menu.label.setText(f"Deneme Adı: {denemeAdi}")
        denemeGorListe[-1].rowid = deneme
        denemeGorListe[-1].key = self.key
        
        
        denemeGorListe[-1].menu.tableWidget.setItem(0,0, QTableWidgetItem(denemeTurkce[2]))
        denemeGorListe[-1].menu.tableWidget.setItem(1,0, QTableWidgetItem(denemeTurkce[0]))
        denemeGorListe[-1].menu.tableWidget.setItem(2,0, QTableWidgetItem(denemeTurkce[1]))
        denemeGorListe[-1].menu.tableWidget.setItem(3,0, QTableWidgetItem(str(round(int(denemeTurkce[0])-int(denemeTurkce[1])/3,2))))
        
        denemeGorListe[-1].menu.tableWidget.setItem(0,1, QTableWidgetItem(denemeSosyal[2]))
        denemeGorListe[-1].menu.tableWidget.setItem(1,1, QTableWidgetItem(denemeSosyal[0]))
        denemeGorListe[-1].menu.tableWidget.setItem(2,1, QTableWidgetItem(denemeSosyal[1]))
        denemeGorListe[-1].menu.tableWidget.setItem(3,1, QTableWidgetItem(str(round(int(denemeSosyal[0])-int(denemeSosyal[1])/3,2))))

        denemeGorListe[-1].menu.tableWidget.setItem(0,2, QTableWidgetItem(denemeDin[2]))
        denemeGorListe[-1].menu.tableWidget.setItem(1,2, QTableWidgetItem(denemeDin[0]))
        denemeGorListe[-1].menu.tableWidget.setItem(2,2, QTableWidgetItem(denemeDin[1]))
        denemeGorListe[-1].menu.tableWidget.setItem(3,2, QTableWidgetItem(str(round(int(denemeDin[0])-int(denemeDin[1])/3,2))))

        denemeGorListe[-1].menu.tableWidget.setItem(0,3, QTableWidgetItem(denemeIng[2]))
        denemeGorListe[-1].menu.tableWidget.setItem(1,3, QTableWidgetItem(denemeIng[0]))
        denemeGorListe[-1].menu.tableWidget.setItem(2,3, QTableWidgetItem(denemeIng[1]))
        denemeGorListe[-1].menu.tableWidget.setItem(3,3, QTableWidgetItem(str(round(int(denemeIng[0])-int(denemeIng[1])/3,2))))


        denemeGorListe[-1].menu.tableWidget.setItem(0,4, QTableWidgetItem(denemeMat[2]))
        denemeGorListe[-1].menu.tableWidget.setItem(1,4, QTableWidgetItem(denemeMat[0]))
        denemeGorListe[-1].menu.tableWidget.setItem(2,4, QTableWidgetItem(denemeMat[1]))
        denemeGorListe[-1].menu.tableWidget.setItem(3,4, QTableWidgetItem(str(round(int(denemeMat[0])-int(denemeMat[1])/3,2))))

        denemeGorListe[-1].menu.tableWidget.setItem(0,5, QTableWidgetItem(denemeFen[2]))
        denemeGorListe[-1].menu.tableWidget.setItem(1,5, QTableWidgetItem(denemeFen[0]))
        denemeGorListe[-1].menu.tableWidget.setItem(2,5, QTableWidgetItem(denemeFen[1]))
        denemeGorListe[-1].menu.tableWidget.setItem(3,5, QTableWidgetItem(str(round(int(denemeFen[0])-int(denemeFen[1])/3,2))))

        denemeGorListe[-1].menu.pushButton.clicked.connect(self.info)
        denemeGorListe[-1].show()
    def info(self):
        denemeInfoListe.append(dersTavsiye())
        denemeInfoListe[-1].rowid = denemeGorListe[-1].rowid
        denemeInfoListe[-1].key = denemeGorListe[-1].key
        denemeInfoListe[-1].liste()
        denemeInfoListe[-1].show()

class dersTavsiye(QWidget):
    def __init__(self):
        super().__init__()
        self.menu = Ui_Form8()
        self.menu.setupUi(self)
        self.menu.pushButton.clicked.connect(self.turkce)
        self.menu.pushButton_2.clicked.connect(self.sosyal)
        self.menu.pushButton_3.clicked.connect(self.din)
        self.menu.pushButton_4.clicked.connect(self.ingilizce)
        self.menu.pushButton_5.clicked.connect(self.matematik)
        self.menu.pushButton_6.clicked.connect(self.fen)
    def turkce(self):
        denemeOzelListe.append(dersOzel())
        denemeOzelListe[-1].setWindowTitle("Türkçe")
        cursor.execute(f"""SELECT denemeAdi FROM {self.key} WHERE rowid = {self.rowid}""")
        denemeisim = cursor.fetchall()[0][0]
        denemeOzelListe[-1].menu.label.setText(denemeisim)
        denemeOzelListe[-1].menu.label_2.setText("Türkçe")
        denemeOzelListe[-1].menu.tableWidget.setHorizontalHeaderLabels([self.denemeO[0],self.deneme[0]])
        self.O = self.denemeO[1].split("-")
        try:
            self.Net1 = float(self.O[0]) - round(float(self.O[1])/3,2)
        except:
            self.Net1 = "Yok"

        denemeOzelListe[-1].menu.tableWidget.setItem(0,0, QTableWidgetItem(self.O[2]))
        denemeOzelListe[-1].menu.tableWidget.setItem(1,0, QTableWidgetItem(self.O[0]))
        denemeOzelListe[-1].menu.tableWidget.setItem(2,0, QTableWidgetItem(self.O[1]))
        denemeOzelListe[-1].menu.tableWidget.setItem(3,0, QTableWidgetItem(str(self.Net1)))

        self.no = self.deneme[1].split("-")
        try:
            self.Net2 = float(self.no[0]) - round(float(self.no[1])/3,2)
        except:
            self.Net2 = "Yok"

        denemeOzelListe[-1].menu.tableWidget.setItem(0,1, QTableWidgetItem(self.no[2]))
        denemeOzelListe[-1].menu.tableWidget.setItem(1,1, QTableWidgetItem(self.no[0]))
        denemeOzelListe[-1].menu.tableWidget.setItem(2,1, QTableWidgetItem(self.no[1]))
        denemeOzelListe[-1].menu.tableWidget.setItem(3,1, QTableWidgetItem(str(self.Net2)))
        try:
            self.ort = [str(int(self.no[0])-int(self.O[0])),str(int(self.no[1])-int(self.O[1])),str(int(self.no[2])-int(self.O[2]))]
        except:
            self.ort = ["Yok","Yok","Yok"]
        try:
            self.NetOrt = str(self.Net2 - self.Net1)
        except:
            self.NetOrt = "Yok"

        if self.NetOrt[0] != "-" and self.NetOrt != "Yok":
            self.NetOrt = "+" + self.NetOrt
        denemeOzelListe[-1].menu.tableWidget.setItem(0,2, QTableWidgetItem(self.ort[2]))
        denemeOzelListe[-1].menu.tableWidget.setItem(1,2, QTableWidgetItem(self.ort[0]))
        denemeOzelListe[-1].menu.tableWidget.setItem(2,2, QTableWidgetItem(self.ort[1]))
        denemeOzelListe[-1].menu.tableWidget.setItem(3,2, QTableWidgetItem(str(self.NetOrt)))

        denemeOzelListe[-1].show()
    def sosyal(self):
        denemeOzelListe.append(dersOzel())
        denemeOzelListe[-1].setWindowTitle("Sosyal Bilgiler")
        cursor.execute(f"""SELECT denemeAdi FROM {self.key} WHERE rowid = {self.rowid}""")
        denemeisim = cursor.fetchall()[0][0]
        denemeOzelListe[-1].menu.label.setText(denemeisim)
        denemeOzelListe[-1].menu.label_2.setText("Sosyal Bilgiler")
        denemeOzelListe[-1].menu.tableWidget.setHorizontalHeaderLabels([self.denemeO[0],self.deneme[0]])
        self.O = self.denemeO[2].split("-")
        try:
            self.Net1 = float(self.O[0]) - round(float(self.O[1])/3,2)
        except:
            self.Net1 = "Yok"

        denemeOzelListe[-1].menu.tableWidget.setItem(0,0, QTableWidgetItem(self.O[2]))
        denemeOzelListe[-1].menu.tableWidget.setItem(1,0, QTableWidgetItem(self.O[0]))
        denemeOzelListe[-1].menu.tableWidget.setItem(2,0, QTableWidgetItem(self.O[1]))
        denemeOzelListe[-1].menu.tableWidget.setItem(3,0, QTableWidgetItem(str(self.Net1)))

        self.no = self.deneme[2].split("-")
        try:
            self.Net2 = float(self.no[0]) - round(float(self.no[1])/3,2)
        except:
            self.Net2 = "Yok"
        denemeOzelListe[-1].menu.tableWidget.setItem(0,1, QTableWidgetItem(self.no[2]))
        denemeOzelListe[-1].menu.tableWidget.setItem(1,1, QTableWidgetItem(self.no[0]))
        denemeOzelListe[-1].menu.tableWidget.setItem(2,1, QTableWidgetItem(self.no[1]))
        denemeOzelListe[-1].menu.tableWidget.setItem(3,1, QTableWidgetItem(str(self.Net2)))

        try:
            self.ort = [str(int(self.no[0])-int(self.O[0])),str(int(self.no[1])-int(self.O[1])),str(int(self.no[2])-int(self.O[2]))]
        except:
            self.ort = ["Yok","Yok","Yok"]

        try:
            self.NetOrt = str(self.Net2 - self.Net1)
        except:
            self.NetOrt = "Yok"
        if self.NetOrt[0] != "-" and self.NetOrt != "Yok":
            self.NetOrt = "+" + self.NetOrt
        denemeOzelListe[-1].menu.tableWidget.setItem(0,2, QTableWidgetItem(self.ort[2]))
        denemeOzelListe[-1].menu.tableWidget.setItem(1,2, QTableWidgetItem(self.ort[0]))
        denemeOzelListe[-1].menu.tableWidget.setItem(2,2, QTableWidgetItem(self.ort[1]))
        denemeOzelListe[-1].menu.tableWidget.setItem(3,2, QTableWidgetItem(str(self.NetOrt)))

        denemeOzelListe[-1].show()
    def din(self):
        denemeOzelListe.append(dersOzel())
        denemeOzelListe[-1].setWindowTitle("Din K. ve Ahlak B.")
        cursor.execute(f"""SELECT denemeAdi FROM {self.key} WHERE rowid = {self.rowid}""")
        denemeisim = cursor.fetchall()[0][0]
        denemeOzelListe[-1].menu.label.setText(denemeisim)
        denemeOzelListe[-1].menu.label_2.setText("Din K. ve Ahlak B.")
        denemeOzelListe[-1].menu.tableWidget.setHorizontalHeaderLabels([self.denemeO[0],self.deneme[0]])
        self.O = self.denemeO[3].split("-")
        try:
            self.Net1 = float(self.O[0]) - round(float(self.O[1])/3,2)
        except:
            self.Net1 = "Yok"

        denemeOzelListe[-1].menu.tableWidget.setItem(0,0, QTableWidgetItem(self.O[2]))
        denemeOzelListe[-1].menu.tableWidget.setItem(1,0, QTableWidgetItem(self.O[0]))
        denemeOzelListe[-1].menu.tableWidget.setItem(2,0, QTableWidgetItem(self.O[1]))
        denemeOzelListe[-1].menu.tableWidget.setItem(3,0, QTableWidgetItem(str(self.Net1)))

        self.no = self.deneme[3].split("-")
        try:
            self.Net2 = float(self.no[0]) - round(float(self.no[1])/3,2)
        except:
            self.Net2 = "Yok"
        denemeOzelListe[-1].menu.tableWidget.setItem(0,1, QTableWidgetItem(self.no[2]))
        denemeOzelListe[-1].menu.tableWidget.setItem(1,1, QTableWidgetItem(self.no[0]))
        denemeOzelListe[-1].menu.tableWidget.setItem(2,1, QTableWidgetItem(self.no[1]))
        denemeOzelListe[-1].menu.tableWidget.setItem(3,1, QTableWidgetItem(str(self.Net2)))

        try:
            self.ort = [str(int(self.no[0])-int(self.O[0])),str(int(self.no[1])-int(self.O[1])),str(int(self.no[2])-int(self.O[2]))]
        except:
            self.ort = ["Yok","Yok","Yok"]
        try:
            self.NetOrt = str(self.Net2 - self.Net1)
        except:
            self.NetOrt = "Yok"
        if self.NetOrt[0] != "-" and self.NetOrt != "Yok":
            self.NetOrt = "+" + self.NetOrt
        denemeOzelListe[-1].menu.tableWidget.setItem(0,2, QTableWidgetItem(self.ort[2]))
        denemeOzelListe[-1].menu.tableWidget.setItem(1,2, QTableWidgetItem(self.ort[0]))
        denemeOzelListe[-1].menu.tableWidget.setItem(2,2, QTableWidgetItem(self.ort[1]))
        denemeOzelListe[-1].menu.tableWidget.setItem(3,2, QTableWidgetItem(str(self.NetOrt)))

        denemeOzelListe[-1].show()
    def ingilizce(self):
        denemeOzelListe.append(dersOzel())
        denemeOzelListe[-1].setWindowTitle("İngilizce")
        cursor.execute(f"""SELECT denemeAdi FROM {self.key} WHERE rowid = {self.rowid}""")
        denemeisim = cursor.fetchall()[0][0]
        denemeOzelListe[-1].menu.label.setText(denemeisim)
        denemeOzelListe[-1].menu.label_2.setText("İngilizce")
        denemeOzelListe[-1].menu.tableWidget.setHorizontalHeaderLabels([self.denemeO[0],self.deneme[0]])
        self.O = self.denemeO[4].split("-")
        try:
            self.Net1 = float(self.O[0]) - round(float(self.O[1])/3,2)
        except:
            self.Net1 = "Yok"

        denemeOzelListe[-1].menu.tableWidget.setItem(0,0, QTableWidgetItem(self.O[2]))
        denemeOzelListe[-1].menu.tableWidget.setItem(1,0, QTableWidgetItem(self.O[0]))
        denemeOzelListe[-1].menu.tableWidget.setItem(2,0, QTableWidgetItem(self.O[1]))
        denemeOzelListe[-1].menu.tableWidget.setItem(3,0, QTableWidgetItem(str(self.Net1)))

        self.no = self.deneme[4].split("-")
        try:
            self.Net2 = float(self.no[0]) - round(float(self.no[1])/3,2)
        except:
            self.Net2 = "Yok"
        denemeOzelListe[-1].menu.tableWidget.setItem(0,1, QTableWidgetItem(self.no[2]))
        denemeOzelListe[-1].menu.tableWidget.setItem(1,1, QTableWidgetItem(self.no[0]))
        denemeOzelListe[-1].menu.tableWidget.setItem(2,1, QTableWidgetItem(self.no[1]))
        denemeOzelListe[-1].menu.tableWidget.setItem(3,1, QTableWidgetItem(str(self.Net2)))

        try:
            self.ort = [str(int(self.no[0])-int(self.O[0])),str(int(self.no[1])-int(self.O[1])),str(int(self.no[2])-int(self.O[2]))]
        except:
            self.ort = ["Yok","Yok","Yok"]
        try:
            self.NetOrt = str(self.Net2 - self.Net1)
        except:
            self.NetOrt = "Yok"
        if self.NetOrt[0] != "-" and self.NetOrt != "Yok":
            self.NetOrt = "+" + self.NetOrt
        denemeOzelListe[-1].menu.tableWidget.setItem(0,2, QTableWidgetItem(self.ort[2]))
        denemeOzelListe[-1].menu.tableWidget.setItem(1,2, QTableWidgetItem(self.ort[0]))
        denemeOzelListe[-1].menu.tableWidget.setItem(2,2, QTableWidgetItem(self.ort[1]))
        denemeOzelListe[-1].menu.tableWidget.setItem(3,2, QTableWidgetItem(str(self.NetOrt)))

        denemeOzelListe[-1].show()
    def matematik(self):
        denemeOzelListe.append(dersOzel())
        denemeOzelListe[-1].setWindowTitle("Matematik")
        cursor.execute(f"""SELECT denemeAdi FROM {self.key} WHERE rowid = {self.rowid}""")
        denemeisim = cursor.fetchall()[0][0]
        denemeOzelListe[-1].menu.label.setText(denemeisim)
        denemeOzelListe[-1].menu.label_2.setText("Matematik")
        denemeOzelListe[-1].menu.tableWidget.setHorizontalHeaderLabels([self.denemeO[0],self.deneme[0]])
        self.O = self.denemeO[5].split("-")
        try:
            self.Net1 = float(self.O[0]) - round(float(self.O[1])/3,2)
        except:
            self.Net1 = "Yok"

        denemeOzelListe[-1].menu.tableWidget.setItem(0,0, QTableWidgetItem(self.O[2]))
        denemeOzelListe[-1].menu.tableWidget.setItem(1,0, QTableWidgetItem(self.O[0]))
        denemeOzelListe[-1].menu.tableWidget.setItem(2,0, QTableWidgetItem(self.O[1]))
        denemeOzelListe[-1].menu.tableWidget.setItem(3,0, QTableWidgetItem(str(self.Net1)))

        self.no = self.deneme[5].split("-")
        try:
            self.Net2 = float(self.no[0]) - round(float(self.no[1])/3,2)
        except:
            self.Net2 = "Yok"
        denemeOzelListe[-1].menu.tableWidget.setItem(0,1, QTableWidgetItem(self.no[2]))
        denemeOzelListe[-1].menu.tableWidget.setItem(1,1, QTableWidgetItem(self.no[0]))
        denemeOzelListe[-1].menu.tableWidget.setItem(2,1, QTableWidgetItem(self.no[1]))
        denemeOzelListe[-1].menu.tableWidget.setItem(3,1, QTableWidgetItem(str(self.Net2)))

        try:
            self.ort = [str(int(self.no[0])-int(self.O[0])),str(int(self.no[1])-int(self.O[1])),str(int(self.no[2])-int(self.O[2]))]
        except:
            self.ort = ["Yok","Yok","Yok"]
        try:
            self.NetOrt = str(self.Net2 - self.Net1)
        except:
            self.NetOrt = "Yok"
        if self.NetOrt[0] != "-" and self.NetOrt != "Yok":
            self.NetOrt = "+" + self.NetOrt
        denemeOzelListe[-1].menu.tableWidget.setItem(0,2, QTableWidgetItem(self.ort[2]))
        denemeOzelListe[-1].menu.tableWidget.setItem(1,2, QTableWidgetItem(self.ort[0]))
        denemeOzelListe[-1].menu.tableWidget.setItem(2,2, QTableWidgetItem(self.ort[1]))
        denemeOzelListe[-1].menu.tableWidget.setItem(3,2, QTableWidgetItem(str(self.NetOrt)))

        denemeOzelListe[-1].show()
    def fen(self):
        denemeOzelListe.append(dersOzel())
        denemeOzelListe[-1].setWindowTitle("Fen Bilimleri")
        cursor.execute(f"""SELECT denemeAdi FROM {self.key} WHERE rowid = {self.rowid}""")
        denemeisim = cursor.fetchall()[0][0]
        denemeOzelListe[-1].menu.label.setText(denemeisim)
        denemeOzelListe[-1].menu.label_2.setText("Fen Bilimleri")
        denemeOzelListe[-1].menu.tableWidget.setHorizontalHeaderLabels([self.denemeO[0],self.deneme[0]])
        self.O = self.denemeO[6].split("-")
        try:
            self.Net1 = float(self.O[0]) - round(float(self.O[1])/3,2)
        except:
            self.Net1 = "Yok"

        denemeOzelListe[-1].menu.tableWidget.setItem(0,0, QTableWidgetItem(self.O[2]))
        denemeOzelListe[-1].menu.tableWidget.setItem(1,0, QTableWidgetItem(self.O[0]))
        denemeOzelListe[-1].menu.tableWidget.setItem(2,0, QTableWidgetItem(self.O[1]))
        denemeOzelListe[-1].menu.tableWidget.setItem(3,0, QTableWidgetItem(str(self.Net1)))

        self.no = self.deneme[6].split("-")
        try:
            self.Net2 = float(self.no[0]) - round(float(self.no[1])/3,2)
        except:
            self.Net2 = "Yok"
        denemeOzelListe[-1].menu.tableWidget.setItem(0,1, QTableWidgetItem(self.no[2]))
        denemeOzelListe[-1].menu.tableWidget.setItem(1,1, QTableWidgetItem(self.no[0]))
        denemeOzelListe[-1].menu.tableWidget.setItem(2,1, QTableWidgetItem(self.no[1]))
        denemeOzelListe[-1].menu.tableWidget.setItem(3,1, QTableWidgetItem(str(self.Net2)))

        try:
            self.ort = [str(int(self.no[0])-int(self.O[0])),str(int(self.no[1])-int(self.O[1])),str(int(self.no[2])-int(self.O[2]))]
        except:
            self.ort = ["Yok","Yok","Yok"]
        try:
            self.NetOrt = str(self.Net2 - self.Net1)
        except:
            self.NetOrt = "Yok"
        if self.NetOrt[0] != "-" and self.NetOrt != "Yok":
            self.NetOrt = "+" + self.NetOrt
        denemeOzelListe[-1].menu.tableWidget.setItem(0,2, QTableWidgetItem(self.ort[2]))
        denemeOzelListe[-1].menu.tableWidget.setItem(1,2, QTableWidgetItem(self.ort[0]))
        denemeOzelListe[-1].menu.tableWidget.setItem(2,2, QTableWidgetItem(self.ort[1]))
        denemeOzelListe[-1].menu.tableWidget.setItem(3,2, QTableWidgetItem(str(self.NetOrt)))

        denemeOzelListe[-1].show()
    def liste(self):
        cursor.execute(f"""SELECT * FROM {self.key} WHERE rowid = {self.rowid}""")
        self.deneme = cursor.fetchall()[0]
        try:
            cursor.execute(f"""SELECT * FROM {self.key} WHERE rowid = {str(int(self.rowid)-1)}""")
            self.denemeO = cursor.fetchall()[0]
        except:
            self.denemeO = ("Yok","Yok-Yok-Yok","Yok-Yok-Yok","Yok-Yok-Yok","Yok-Yok-Yok","Yok-Yok-Yok","Yok-Yok-Yok")

class dersOzel(QWidget):
    def __init__(self):
        super().__init__()
        self.menu = Ui_Form9()
        self.menu.setupUi(self)

class ekle_cikar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = Ui_MainWindow()
        self.menu.setupUi(self)
        self.chars = "1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
        self.refreshList()
        self.menu.pushButton_2.clicked.connect(self.Ekle)
        self.menu.pushButton.clicked.connect(self.Cikar)
        self.menu.action_RENC_BUL.triggered.connect(self.filtreAc)
        self.menu.actionY_NELE.triggered.connect(self.refreshList)

    def Ekle(self):
        cursor.execute("""SELECT number FROM ogrenciList""")
        numbers = cursor.fetchall()
        self.name = self.menu.lineEdit.text()
        self.surname = self.menu.lineEdit_2.text()
        self.number = self.menu.lineEdit_3.text()
        try:
            self.number = int(self.number)
        except:
            self.number = 0
        while (not (self.number,) in numbers):
            self.key = ""
            for i in random.choices(self.chars,k=10):
                self.key += i
            if self.key[0] in "1234567890":
                continue
            
            try:
                cursor.execute(f"""CREATE TABLE {self.key}(denemeAdi text, turkce text, sosyal text, din text, ing text, mat text, fen text)""")
                cursor.execute(f"""INSERT INTO ogrenciList VALUES("{self.key}","{self.name}","{self.surname}",{self.number})""")
                self.menu.lineEdit.setText("")
                self.menu.lineEdit_2.setText("")
                self.menu.lineEdit_3.setText("")
                self.menu.label_4.setText("")
                liste.refreshList()
                break
            except:
                pass

        else:
            self.menu.label_4.setText("Numara Zaten Alınmış")
            self.menu.lineEdit_3.setText("")
        self.refreshList()
        connect.commit()
    def refreshList(self):
        self.menu.listWidget.clear()
        cursor.execute("""SELECT *,rowid FROM ogrenciList""")
        self.ogrenciler = cursor.fetchall()
        for i in self.ogrenciler:
            listAddText = f"""{i[4]}. {i[1]} {i[2]}:\n    Numara: {i[3]}\n    Anahtar: {i[0]}\n"""
            self.menu.listWidget.addItem(listAddText)
    def Cikar(self):
        try:
            self.selectedkey = self.menu.listWidget.currentItem().text().split(" ")[-1].split("\n")[0]
            silmeKontrolM.show()
        except:
            pass
    def filtreAc(self):
        self.filterMod = "eç"
        filtreM.show()
    
    def closeEvent(self,event):
        filtreM.menu.lineEdit.setText("")
        filtreM.menu.lineEdit_2.setText("")
        filtreM.menu.lineEdit_3.setText("")
        self.menu.lineEdit.setText("")
        self.menu.lineEdit_2.setText("")
        self.menu.lineEdit_3.setText("")
        silmeKontrolM.close()
        filtreM.close()

class listele(QMainWindow):
    def __init__(self):
        super().__init__()
        self.liste = Ui_MainWindow1()
        self.liste.setupUi(self)
        self.ogretmenDenemeControl = ogretmenDeneme()
        self.refreshList()


        self.liste.action_RENC_BUL.triggered.connect(self.filtreleAc)
        self.liste.actionY_NELE.triggered.connect(self.refreshList)
        self.liste.listWidget.doubleClicked.connect(self.showDeneme)
    def refreshList(self):
        self.liste.listWidget.clear()
        cursor.execute("""SELECT rowid,ad,soyad,number FROM ogrenciList""")
        self.ogrenciler = cursor.fetchall()
        for i in self.ogrenciler:
            listAddText = f"""{i[0]}. {i[1]} {i[2]} - {i[3]}"""
            self.liste.listWidget.addItem(listAddText)
    def filtreleAc(self):
        filtre2M.show()
    def showDeneme(self):
        self.select = self.liste.listWidget.currentItem().text().split()[-1]
        cursor.execute(f"""SELECT key,ad,soyad,number FROM ogrenciList WHERE number = {self.select}""")
        self.ogretmenDenemeControl = ogretmenDeneme()
        denemeEkleM.close()
        self.selected = cursor.fetchall()[0]
        self.selectedkey = self.selected[0]
        self.selectedname = self.selected[1]
        self.selectedsurname = self.selected[2]
        self.selectednumber = self.selected[3]
        self.ogretmenDenemeControl.menu.label.setText(f"{self.selectednumber} - {self.selectedname} {self.selectedsurname}")
        self.refreshDenemeList()
        self.ogretmenDenemeControl.menu.pushButton.clicked.connect(self.denemeEkle)
        self.ogretmenDenemeControl.menu.listWidget.doubleClicked.connect(self.denemeGor)
        self.ogretmenDenemeControl.menu.pushButton_2.clicked.connect(self.denemeSil)
        self.ogretmenDenemeControl.show()
    def refreshDenemeList(self):
        self.ogretmenDenemeControl.menu.listWidget.clear()
        cursor.execute(f"""SELECT rowid,denemeAdi FROM {self.selectedkey}""")
        self.denemeList = cursor.fetchall()
        for i in self.denemeList:
            listAddText = f"{i[0]}- {i[1]}"
            self.ogretmenDenemeControl.menu.listWidget.addItem(listAddText)
    def denemeEkle(self):
        denemeEkleM.key = self.selectedkey
        denemeEkleM.show()
    def denemeGor(self):
        deneme = self.ogretmenDenemeControl.menu.listWidget.currentItem().text().split("-")[0]
        cursor.execute(f"""SELECT * FROM {self.selectedkey} WHERE rowid = {deneme}""")
        denemeA = cursor.fetchall()[0]
        denemeAdi = denemeA[0]
        denemeTurkce = denemeA[1].split("-")
        denemeSosyal = denemeA[2].split("-")
        denemeDin = denemeA[3].split("-")
        denemeIng = denemeA[4].split("-")
        denemeMat = denemeA[5].split("-")
        denemeFen = denemeA[6].split("-")
        denemeGorListe.append(denemeGor())
        denemeGorListe[-1].menu.label.setText(f"Deneme Adı: {denemeAdi}")
        denemeGorListe[-1].rowid = deneme
        denemeGorListe[-1].key = self.selectedkey

        denemeGorListe[-1].menu.tableWidget.setItem(0,0, QTableWidgetItem(denemeTurkce[2]))
        denemeGorListe[-1].menu.tableWidget.setItem(1,0, QTableWidgetItem(denemeTurkce[0]))
        denemeGorListe[-1].menu.tableWidget.setItem(2,0, QTableWidgetItem(denemeTurkce[1]))
        denemeGorListe[-1].menu.tableWidget.setItem(3,0, QTableWidgetItem(str(round(int(denemeTurkce[0])-int(denemeTurkce[1])/3,2))))
        
        denemeGorListe[-1].menu.tableWidget.setItem(0,1, QTableWidgetItem(denemeSosyal[2]))
        denemeGorListe[-1].menu.tableWidget.setItem(1,1, QTableWidgetItem(denemeSosyal[0]))
        denemeGorListe[-1].menu.tableWidget.setItem(2,1, QTableWidgetItem(denemeSosyal[1]))
        denemeGorListe[-1].menu.tableWidget.setItem(3,1, QTableWidgetItem(str(round(int(denemeSosyal[0])-int(denemeSosyal[1])/3,2))))

        denemeGorListe[-1].menu.tableWidget.setItem(0,2, QTableWidgetItem(denemeDin[2]))
        denemeGorListe[-1].menu.tableWidget.setItem(1,2, QTableWidgetItem(denemeDin[0]))
        denemeGorListe[-1].menu.tableWidget.setItem(2,2, QTableWidgetItem(denemeDin[1]))
        denemeGorListe[-1].menu.tableWidget.setItem(3,2, QTableWidgetItem(str(round(int(denemeDin[0])-int(denemeDin[1])/3,2))))

        denemeGorListe[-1].menu.tableWidget.setItem(0,3, QTableWidgetItem(denemeIng[2]))
        denemeGorListe[-1].menu.tableWidget.setItem(1,3, QTableWidgetItem(denemeIng[0]))
        denemeGorListe[-1].menu.tableWidget.setItem(2,3, QTableWidgetItem(denemeIng[1]))
        denemeGorListe[-1].menu.tableWidget.setItem(3,3, QTableWidgetItem(str(round(int(denemeIng[0])-int(denemeIng[1])/3,2))))


        denemeGorListe[-1].menu.tableWidget.setItem(0,4, QTableWidgetItem(denemeMat[2]))
        denemeGorListe[-1].menu.tableWidget.setItem(1,4, QTableWidgetItem(denemeMat[0]))
        denemeGorListe[-1].menu.tableWidget.setItem(2,4, QTableWidgetItem(denemeMat[1]))
        denemeGorListe[-1].menu.tableWidget.setItem(3,4, QTableWidgetItem(str(round(int(denemeMat[0])-int(denemeMat[1])/3,2))))

        denemeGorListe[-1].menu.tableWidget.setItem(0,5, QTableWidgetItem(denemeFen[2]))
        denemeGorListe[-1].menu.tableWidget.setItem(1,5, QTableWidgetItem(denemeFen[0]))
        denemeGorListe[-1].menu.tableWidget.setItem(2,5, QTableWidgetItem(denemeFen[1]))
        denemeGorListe[-1].menu.tableWidget.setItem(3,5, QTableWidgetItem(str(round(int(denemeFen[0])-int(denemeFen[1])/3,2))))

        denemeGorListe[-1].menu.pushButton.clicked.connect(self.info)
        denemeGorListe[-1].show()
    
    def info(self):
        denemeInfoListe.append(dersTavsiye())
        denemeInfoListe[-1].rowid = denemeGorListe[-1].rowid
        denemeInfoListe[-1].key = denemeGorListe[-1].key
        denemeInfoListe[-1].liste()
        denemeInfoListe[-1].show()
    def denemeSil(self):
        silmeKontrolM2.show()


    def closeEvent(self,event):
        filtre2M.menu.lineEdit.setText("")
        filtre2M.menu.lineEdit_2.setText("")
        filtre2M.menu.lineEdit_3.setText("")
        filtre2M.close()
        
class silmeKontrol(QWidget):
    def __init__(self):
        super().__init__()
        self.menu = Ui_Form3()
        self.menu.setupUi(self)
        self.menu.pushButton.clicked.connect(self.evet)
        self.menu.pushButton_2.clicked.connect(self.hayir)
    def evet(self):
        cursor.execute(f"""DROP TABLE {ekle_cikar_menu.selectedkey}""")
        cursor.execute(f"""DELETE FROM ogrenciList WHERE key = "{ekle_cikar_menu.selectedkey}" """)
        refresRowidsInOgrenciList() 
        ekle_cikar_menu.refreshList()
        liste.refreshList()
        connect.commit()
        ekle_cikar_menu.menu.label_4.setText("")
        
        self.close()
    def hayir(self):
        self.close()

class silmeKontrol2(QWidget):
    def __init__(self):
        super().__init__()
        self.menu = Ui_Form3()
        self.menu.setupUi(self)
        self.menu.pushButton.clicked.connect(self.evet)
        self.menu.pushButton_2.clicked.connect(self.hayir)
    def evet(self):
        try:
            row = liste.ogretmenDenemeControl.menu.listWidget.currentItem().text()[0]
            cursor.execute(f"""DELETE FROM {liste.selectedkey} WHERE rowid = {row}""")

            cursor.execute(f"""SELECT rowid FROM {liste.selectedkey}""")
            rowids = cursor.fetchall()
            for i in range(1,len(rowids)+1):
                cursor.execute(f"""UPDATE {liste.selectedkey} SET rowid = "{i}" WHERE rowid = {rowids[i-1][0]}""")
            connect.commit()
            liste.refreshDenemeList()
            self.close()
        except:
            self.close()
    def hayir(self):
        self.close()

class filtre(QWidget):
    def __init__(self):
        super().__init__()
        self.menu = Ui_Form4()
        self.menu.setupUi(self)
        self.menu.pushButton.clicked.connect(self.filtrele)
    def filtrele(self):
        ad = self.menu.lineEdit.text()
        soyad = self.menu.lineEdit_2.text()
        number = self.menu.lineEdit_3.text()
        cursor.execute(f"""SELECT *,rowid FROM ogrenciList WHERE ad LIKE '{ad}%' and soyad LIKE '{soyad}%' and number LIKE '{number}%' """)
        filtreList = cursor.fetchall()
        ekle_cikar_menu.menu.listWidget.clear()
        counter = 0
        for i in filtreList:
            counter += 1
            listAddText = f"""{counter}. {i[1]} {i[2]}:\n    Numara: {i[3]}\n    Anahtar: {i[0]}\n"""
            ekle_cikar_menu.menu.listWidget.addItem(listAddText)
        self.menu.lineEdit.setText("")
        self.menu.lineEdit_2.setText("")
        self.menu.lineEdit_3.setText("")
        self.close()

class filtre2(QWidget):
    def __init__(self):
        super().__init__()
        self.menu = Ui_Form4()
        self.menu.setupUi(self)
        self.menu.pushButton.clicked.connect(self.filtrele)
    def filtrele(self):
        ad = self.menu.lineEdit.text()
        soyad = self.menu.lineEdit_2.text()
        number = self.menu.lineEdit_3.text()
        cursor.execute(f"""SELECT ad,soyad,number FROM ogrenciList WHERE ad LIKE '{ad}%' and soyad LIKE '{soyad}%' and number LIKE '{number}%' """)
        filtreList = cursor.fetchall()
        liste.liste.listWidget.clear()
        counter = 0
        for i in filtreList:
            counter += 1
            listAddText = f"""{counter}. {i[0]} {i[1]} - {i[2]}"""
            liste.liste.listWidget.addItem(listAddText)
        self.menu.lineEdit.setText("")
        self.menu.lineEdit_2.setText("")
        self.menu.lineEdit_3.setText("")
        self.close()

class ogretmenDeneme(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = Ui_MainWindow2()
        self.menu.setupUi(self)
    def closeEvent(self,event):
        denemeEkleM.menu.spinBox.setValue(0)
        denemeEkleM.menu.spinBox_2.setValue(0)
        denemeEkleM.menu.spinBox_3.setValue(0)
        denemeEkleM.menu.spinBox_4.setValue(0)
        denemeEkleM.menu.spinBox_5.setValue(0)
        denemeEkleM.menu.spinBox_6.setValue(0)
        denemeEkleM.menu.spinBox_7.setValue(0)
        denemeEkleM.menu.spinBox_8.setValue(0)
        denemeEkleM.menu.spinBox_9.setValue(0)
        denemeEkleM.menu.spinBox_10.setValue(0)
        denemeEkleM.menu.spinBox_11.setValue(0)
        denemeEkleM.menu.spinBox_12.setValue(0)
        denemeEkleM.menu.lineEdit.setText("")
        denemeEkleM.close()
        denemeEklendiM.close()
        silmeKontrolM2.close()

class denemeEkleOgretmen(QWidget):
    def __init__(self):
        super().__init__()
        self.menu = Ui_Form6()
        self.menu.setupUi(self)
        self.key = None

        self.menu.pushButton.clicked.connect(self.reset)
        self.menu.pushButton_2.clicked.connect(self.ekle)

    def reset(self):
        self.menu.spinBox.setValue(0)
        self.menu.spinBox_2.setValue(0)
        self.menu.spinBox_3.setValue(0)
        self.menu.spinBox_4.setValue(0)
        self.menu.spinBox_5.setValue(0)
        self.menu.spinBox_6.setValue(0)
        self.menu.spinBox_7.setValue(0)
        self.menu.spinBox_8.setValue(0)
        self.menu.spinBox_9.setValue(0)
        self.menu.spinBox_10.setValue(0)
        self.menu.spinBox_11.setValue(0)
        self.menu.spinBox_12.setValue(0)
        self.menu.lineEdit.setText("")
    
    def ekle(self):
        turkce = f"{self.menu.spinBox.value()}-{self.menu.spinBox_2.value()}-{self.menu.spinBox.value()+self.menu.spinBox_2.value()}"
        sosyal = f"{self.menu.spinBox_4.value()}-{self.menu.spinBox_3.value()}-{self.menu.spinBox_4.value()+self.menu.spinBox_3.value()}"
        din = f"{self.menu.spinBox_6.value()}-{self.menu.spinBox_5.value()}-{self.menu.spinBox_6.value()+self.menu.spinBox_5.value()}"
        ingilizce = f"{self.menu.spinBox_8.value()}-{self.menu.spinBox_7.value()}-{self.menu.spinBox_8.value()+self.menu.spinBox_7.value()}"
        matematik = f"{self.menu.spinBox_9.value()}-{self.menu.spinBox_10.value()}-{self.menu.spinBox_9.value()+self.menu.spinBox_10.value()}"
        fen = f"{self.menu.spinBox_12.value()}-{self.menu.spinBox_11.value()}-{self.menu.spinBox_12.value()+self.menu.spinBox_11.value()}"

        if self.menu.lineEdit.text() == "":
            name = "İsimsiz"
        else:
            name = self.menu.lineEdit.text()
        
        cursor.execute(f"""INSERT INTO {self.key} VALUES("{name}", "{turkce}", "{sosyal}", "{din}", "{ingilizce}", "{matematik}", "{fen}")""")
        connect.commit()
        denemeEklendiM.menu.label.setText(f"{name[0:7]}... başarıyla eklendi.")
        liste.refreshDenemeList()
        denemeEklendiM.show()
        
    def closeEvent(self,event):
        self.menu.spinBox.setValue(0)
        self.menu.spinBox_2.setValue(0)
        self.menu.spinBox_3.setValue(0)
        self.menu.spinBox_4.setValue(0)
        self.menu.spinBox_5.setValue(0)
        self.menu.spinBox_6.setValue(0)
        self.menu.spinBox_7.setValue(0)
        self.menu.spinBox_8.setValue(0)
        self.menu.spinBox_9.setValue(0)
        self.menu.spinBox_10.setValue(0)
        self.menu.spinBox_11.setValue(0)
        self.menu.spinBox_12.setValue(0)
        self.menu.lineEdit.setText("")
        self.close()

class denemeEklendi(QWidget):
    def __init__(self):
        super().__init__()
        self.menu = Ui_Form7()
        self.menu.setupUi(self)
        self.menu.pushButton.clicked.connect(self.tamam)
    def tamam(self):
        self.close()
    def closeEvent(self,event):
        denemeEkleM.close()

class denemeGor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = Ui_MainWindow3()
        self.menu.setupUi(self)
    def closeEvent(self,event):
        del denemeGorListe[denemeGorListe.index(self)]
        self.close()
    

login = loginPage()
ogretmenM = ogretmenMenu()
ogrenciM = ogrenciDeneme()
ekle_cikar_menu = ekle_cikar()
liste = listele()
silmeKontrolM = silmeKontrol()
silmeKontrolM2 = silmeKontrol2()
filtreM = filtre()
filtre2M = filtre2()
denemeEkleM = denemeEkleOgretmen()
denemeEklendiM = denemeEklendi()

login.show()

connect.commit()
app.exec_()
connect.close()
