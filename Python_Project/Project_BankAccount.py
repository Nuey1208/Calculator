from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication
import sys

amount = 0
long = 0
bank = str
r = 0
textt = str
excuse = str

class Firstpage(QtWidgets.QMainWindow):
    def __init__(self):
        super(Firstpage, self).__init__()
        uic.loadUi('FirstPage.ui', self)
        self.Calculate_Button.clicked.connect(self.calculate)

    def calculate(self):
        global amount, long
        amount = float(self.lineEdit_3.text())
        long = int(self.lineEdit_4.text())
        self.window = SecondPage()
        self.window.show()
        self.hide()

class SecondPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(SecondPage, self).__init__()
        uic.loadUi('SecondPage.ui', self)
        self.SCB_Button.clicked.connect(self.goto)
        self.K_Button.clicked.connect(self.goto)
        self.BKK_Button.clicked.connect(self.goto)
        self.Krungsri_Button.clicked.connect(self.goto)
        self.PreviousPage_Button.clicked.connect(self.goto)

    def goto(self):
        global bank
        if self.sender() == self.SCB_Button:
            bank = 'SCB'
            self.window = SCB()
        elif self.sender() == self.K_Button:
            bank = 'K'
            self.window = K()
        elif self.sender() == self.BKK_Button:
            bank = "BKK"
            self.window = BKK()
        elif self.sender() == self.PreviousPage_Button:
            self.window = Firstpage()
        else:
            bank = 'Krungsri'
            self.window = Krungsri()
        Fix_Account()
        self.window.show()
        self.hide()
 
class SCB(QtWidgets.QMainWindow):
    def __init__(self):
        super(SCB, self).__init__()
        uic.loadUi('SCBPage.ui', self)
        self.label_4.setText('Interest Rate : 0.25% per year')
        self.label_5.setText('Amount of deposit : ' + str(amount) + ' Bath')
        self.label_6.setText('Net : ' + str(Saving_Account())+ ' Bath')
        self.label_7.setText('Amount of deposit : ' + str(amount) + ' Bath')
        self.label_9.setText('Net : ' + str(Fix_Account()) + " Baht")
        self.label_8.setText("Interest Rate : "+ str(r)+' %'+" per year")
        self.PreviousPage_Button.clicked.connect(self.gotoSec)
        if Fix_Account() == str(amount*long):
            self.label_10.setText("No interest rate for " + str(long) + " month with Fixed Deposit Account")
        else:
            self.label_10.setText(" ")
    def gotoSec(self):
        if self.sender() == self.PreviousPage_Button:
            self.window = SecondPage()
            self.window.show()
            self.hide()
            
class K(QtWidgets.QMainWindow):
    def __init__(self):
        super(K, self).__init__()
        uic.loadUi('KPage.ui', self)     
        self.label_4.setText('Interest Rate : 0.25% per year')
        self.label_5.setText('Amount of deposit : ' + str(amount) + ' Bath')
        self.label_6.setText('Net : ' + str(Saving_Account())+ ' Bath')
        self.label_7.setText('Amount of deposit : ' + str(amount) + ' Bath')
        self.label_9.setText('Net : '+ str(Fix_Account()) + " Baht")
        self.label_8.setText("Interest Rate : "+ str(r)+' %'+" per year")
        self.PreviousPage_Button.clicked.connect(self.gotoSec)
        if Fix_Account() == str(amount*long):
            self.label_10.setText("No interest rate for " + str(long) + " month with Fixed Deposit Account")
        else:
            self.label_10.setText(" ")
    def gotoSec(self):
        if self.sender() == self.PreviousPage_Button:
            self.window = SecondPage()
            self.window.show()
            self.hide()

class BKK(QtWidgets.QMainWindow):
    def __init__(self):
        super(BKK, self).__init__()
        uic.loadUi('BKKPage.ui', self)
        self.label_4.setText('Interest Rate : 0.25% per year')
        self.label_5.setText('Amount of deposit : ' + str(amount) + ' Bath')
        self.label_6.setText('Net : ' + str(Saving_Account())+ ' Bath')
        self.label_7.setText('Amount of deposit : ' + str(amount) + ' Bath')
        self.label_9.setText('Net : '+ str(Fix_Account()) + " Baht")
        self.label_8.setText("Interest Rate : "+ str(r)+' %'+" per year")
        self.PreviousPage_Button.clicked.connect(self.gotoSec)
        if Fix_Account() == str(amount*long):
            self.label_10.setText("No interest rate for " + str(long) + " month with Fixed Deposit Account")
        else:
            self.label_10.setText(" ")
    def gotoSec(self):
        if self.sender() == self.PreviousPage_Button:
            self.window = SecondPage()
            self.window.show()
            self.hide()

class Krungsri(QtWidgets.QMainWindow):
    def __init__(self):
        super(Krungsri, self).__init__()
        uic.loadUi('KrungsriPage.ui', self)
        self.label_4.setText('Interest Rate : 0.25% per year')
        self.label_5.setText('Amount of deposit : ' + str(amount) + ' Bath')
        self.label_6.setText('Net : ' + str(Saving_Account())+ ' Bath')
        self.label_7.setText('Amount of deposit : ' + str(amount) + ' Bath')
        self.label_9.setText('Net : '+ str(Fix_Account()) + " Baht")
        self.label_8.setText("Interest Rate : "+ str(r)+' %'+" per year")
        self.PreviousPage_Button.clicked.connect(self.gotoSec)
        if Fix_Account() == str(amount*long):
            self.label_10.setText("No interest rate for " + str(long) + " month with Fixed Deposit Account")
        else:
            self.label_10.setText(" ")
    def gotoSec(self):
        if self.sender() == self.PreviousPage_Button:
            self.window = SecondPage()
            self.window.show()
            self.hide()

def Saving_Account():
    if long/12 <= 1:
        rate = float((amount*long) * 0.0025 * (long*30)/360)
        text = str(round(((amount*long)+rate),2))
    elif 1 < long/12 <= 2:
        x = float(amount*12) + float((amount*12) * 0.0025)
        rate = float((x +(amount*(long-12))) * 0.0025 * ((long-12)*30)/360)
        text = str(round((x + amount*(long-12) + rate),2))
    elif 2 < long/12 <=3:
        x = float(amount*12) + float((amount*12) * 0.0025)
        y = x+(amount*12) + (float(x+(amount*12)) * 0.0025)
        rate = (y + (amount*float(long-24)))*(0.0025)*float((long-24)/360)
        text = str(round((y + amount*(long-24) + rate),2))
    return text

def Fix_Account():
    global r,textt,excuse
    r = 0
    month_list = [1, 3, 6, 9, 12, 24, 36]
    SCB_rate = [0.25, 0.32, 0.40, 0.40, 0.40, 0.45, 0.65]
    K_rate = [0, 0.32, 0.40, 0.40, 0.40, 0.45, 0.65]
    Krungsri_rate = [0, 0.32, 0.40, 0, 0.40, 0.45, 0.65]
    BKK_rate = [0.1, 0.375, 0.50, 0.45, 0.50, 0.50, 0.75]
    if long not in month_list:
        textt = str(amount*long)
    elif long in month_list:
        if bank == 'SCB':
            for i in range(0,len(month_list)):
                if month_list[i] == long and SCB_rate[i] != 0:
                    r = SCB_rate[i]
                    rate = round(float((amount*long)*(float(r)/100)*((long*30)/360)), 2)
                    textt = str((amount*long) + rate)
                    break
                else:
                    textt = str(amount*long)
        elif bank == 'K':
            for i in range(0,len(month_list)):
                print(K_rate[i])
                if month_list[i] == long and K_rate[i] != 0:
                    r = K_rate[i]
                    rate = round(float((amount*long) * (float(r)/100)*((long*30)/360)), 2)
                    textt = str((amount*long) + rate)
                    break
                else:
                    textt = str(amount*long)
        elif bank == 'Krungsri':
            for i in range(0,len(month_list)):
                if month_list[i] == long and Krungsri_rate[i] != 0:
                    r = Krungsri_rate[i]
                    rate = round(float((amount*long) * (float(r)/100)*((long*30)/360)), 2)
                    textt = str((amount*long) + rate)
                    break
                else:
                    textt = str(amount*long)
        elif bank == 'BKK':
            for i in range(0,len(month_list)):
                if month_list[i] == long and BKK_rate[i] != 0:
                    r = BKK_rate[i]
                    rate = round(float((amount*long) * (float(r)/100)*((long*30)/360)), 2)
                    textt = str((amount*long) + rate)
                    break
                else:
                    textt = str(amount*long)
    return textt

app = QApplication(sys.argv)
window = Firstpage()
window.show()
sys.exit(app.exec_())