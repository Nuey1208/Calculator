from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication,QDialog, QTableWidgetItem
import sys

amount = 0
long = 0
r = 0
textt = str
excuse = str

class Firstpage(QtWidgets.QMainWindow):
    def __init__(self):
        super(Firstpage, self).__init__()
        uic.loadUi('FirstPage.ui', self)
        self.lineEdit_3.textChanged.connect(self.check)
        self.lineEdit_4.textChanged.connect(self.check)
        self.Calculate_Button.clicked.connect(self.calculate)
        self.InvalidInput.setVisible(False)

    def calculate(self):
        global amount, long
        amount = float(self.lineEdit_3.text())
        long = int(self.lineEdit_4.text())
        self.window = SecondPage()
        self.window.show()
        self.hide()


    def check(self):
        show = bool
        check = self.sender().text()
        if check == self.lineEdit_3.text():
            if len(check) > 0 and check.replace('.','',1).isdigit():
                show = False
            else:
                show = True
            self.InvalidInput.setVisible(show)
        else:
            if len(check) > 0 and check.isdigit():
                show = False
            else:
                show = True
            self.InvalidInput.setVisible(show)
           

class SecondPage(QtWidgets.QMainWindow):
    def __init__(self):
        super(SecondPage, self).__init__()
        uic.loadUi('SecondPage.ui', self)
        self.SCB_Button.clicked.connect(self.goto)
        self.K_Button.clicked.connect(self.goto)
        self.BKK_Button.clicked.connect(self.goto)
        self.Krungsri_Button.clicked.connect(self.goto)
        self.PreviousPage_Button.clicked.connect(self.goto)
        self.ComparisonTable_Button.clicked.connect(self.goto)

    def goto(self):
        global bank
        if self.sender() == self.SCB_Button:
            self.window = SCB()
        elif self.sender() == self.K_Button:
            self.window = K()
        elif self.sender() == self.BKK_Button:
            self.window = BKK()
        elif self.sender() == self.PreviousPage_Button:
            self.window = Firstpage()
        elif self.sender() == self.ComparisonTable_Button:
            Fix_SCB()
            Fix_K()
            Fix_Krungsri()
            Fix_BKK()
            self.window = Table()
        else:
            bank = 'Krungsri'
            self.window = Krungsri()
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
        self.label_9.setText('Net : ' + str(Fix_SCB()) + " Baht")
        self.label_8.setText("Interest Rate : "+ str(r)+' %'+" per year")
        self.PreviousPage_Button.clicked.connect(self.gotoSec)
        if Fix_SCB() == str(amount*long):
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
        self.label_9.setText('Net : '+ str(Fix_K()) + " Baht")
        self.label_8.setText("Interest Rate : "+ str(r)+' %'+" per year")
        self.PreviousPage_Button.clicked.connect(self.gotoSec)
        if Fix_K() == str(amount*long):
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
        self.label_9.setText('Net : '+ str(Fix_BKK()) + " Baht")
        self.label_8.setText("Interest Rate : "+ str(r)+' %'+" per year")
        self.PreviousPage_Button.clicked.connect(self.gotoSec)
        if Fix_BKK() == str(amount*long):
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
        self.label_9.setText('Net : '+ str(Fix_Krungsri()) + " Baht")
        self.label_8.setText("Interest Rate : "+ str(r)+' %'+" per year")
        self.PreviousPage_Button.clicked.connect(self.gotoSec)
        if Fix_Krungsri() == str(amount*long):
            self.label_10.setText("No interest rate for " + str(long) + " month with Fixed Deposit Account")
        else:
            self.label_10.setText(" ")
    def gotoSec(self):
        if self.sender() == self.PreviousPage_Button:
            self.window = SecondPage()
            self.window.show()
            self.hide()

###########################################################################################
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

###########################################################################################
month_list = [1, 3, 6, 9, 12, 24, 36]
SCB_rate = [0.25, 0.32, 0.40, 0.40, 0.40, 0.45, 0.65]
K_rate = [0, 0.32, 0.40, 0.40, 0.40, 0.45, 0.65]
Krungsri_rate = [0, 0.32, 0.40, 0, 0.40, 0.45, 0.65]
BKK_rate = [0.1, 0.375, 0.50, 0.45, 0.50, 0.50, 0.75]

def Fix_SCB():
    global r,textt,excuse  
    r = 0
    if long not in month_list:
        textt = str(amount*long)
    elif long in month_list:
        for i in range(0,len(month_list)):
            if month_list[i] == long and SCB_rate[i] != 0:
                r = SCB_rate[i]
                rate = round(float((amount*long)*(float(r)/100)*((long*30)/360)), 2)
                textt = str((amount*long) + rate)
                break
            else:
                textt = str(amount*long)
    return textt
def Fix_K():
    global r,textt,excuse
    r = 0
    if long not in month_list:
        textt = str(amount*long)
    elif long in month_list:
        for i in range(0,len(month_list)):
            print(K_rate[i])
            if month_list[i] == long and K_rate[i] != 0:
                r = K_rate[i]
                rate = round(float((amount*long) * (float(r)/100)*((long*30)/360)), 2)
                textt = str((amount*long) + rate)
                break
            else:
                textt = str(amount*long)
    return textt
def Fix_Krungsri():
    global r,textt,excuse
    r = 0
    if long not in month_list:
        textt = str(amount*long)
    elif long in month_list:
        for i in range(0,len(month_list)):
            if month_list[i] == long and Krungsri_rate[i] != 0:
                r = Krungsri_rate[i]
                rate = round(float((amount*long) * (float(r)/100)*((long*30)/360)), 2)
                textt = str((amount*long) + rate)
                break
            else:
                textt = str(amount*long)
    return textt
def Fix_BKK():
    global r,textt,excuse
    r = 0
    if long not in month_list:
        textt = str(amount*long)
    elif long in month_list:
        for i in range(0,len(month_list)):
            if month_list[i] == long and BKK_rate[i] != 0:
                r = BKK_rate[i]
                rate = round(float((amount*long) * (float(r)/100)*((long*30)/360)), 2)
                textt = str((amount*long) + rate)
                break
            else:
                textt = str(amount*long)
    return textt

####################################################################################################################

class Table(QtWidgets.QMainWindow):
    def __init__(self):
        super(Table, self).__init__()
        uic.loadUi('Table.ui',self)
        self.information()
        self.MonthForTable.setText('Table showing the different between 4 banks in '+ str(long)+' month.')
        self.PreviousPage_Button.clicked.connect(self.gotoSec)
        print(Fix_SCB())
        print(Fix_K())
        print(Fix_Krungsri())
        print(Fix_BKK())

    def gotoSec(self):
        if self.sender() == self.PreviousPage_Button:
            self.window = SecondPage()
            self.window.show()
            self.hide()

    def information(self):
        fix_rate = []
        if long not in month_list:
            for i in range(0, 4):
                fix_rate.append('0')
        else:
            for i in range(0,len(month_list)):
                if month_list[i] == long:
                    fix_rate.append(SCB_rate[i])
                    fix_rate.append(K_rate[i])
                    fix_rate.append(Krungsri_rate[i])
                    fix_rate.append(BKK_rate[i])
        data = {'11': '0.25', '12':str(amount), '13':Saving_Account(), '14':str(fix_rate[0]), '15':str(amount), '16': Fix_SCB(),
                '21': '0.25', '22':str(amount), '23':Saving_Account(), '24':str(fix_rate[1]), '25':str(amount), '26': Fix_K(),
                '31': '0.25', '32':str(amount), '33':Saving_Account(), '34':str(fix_rate[2]), '35':str(amount), '36': Fix_Krungsri(),
                '41': '0.25', '42':str(amount), '43':Saving_Account(), '44':str(fix_rate[3]), '45':str(amount), '46': Fix_BKK()}
        self.ComparisonTable.setItem(0, 0, QtWidgets.QTableWidgetItem(data['11']))
        self.ComparisonTable.setItem(0, 1, QtWidgets.QTableWidgetItem(data['12']))
        self.ComparisonTable.setItem(0, 2, QtWidgets.QTableWidgetItem(data['13']))
        self.ComparisonTable.setItem(0, 3, QtWidgets.QTableWidgetItem(data['14']))
        self.ComparisonTable.setItem(0, 4, QtWidgets.QTableWidgetItem(data['15']))
        self.ComparisonTable.setItem(0, 5, QtWidgets.QTableWidgetItem(data['16']))
        self.ComparisonTable.setItem(1, 0, QtWidgets.QTableWidgetItem(data['21']))
        self.ComparisonTable.setItem(1, 1, QtWidgets.QTableWidgetItem(data['22']))
        self.ComparisonTable.setItem(1, 2, QtWidgets.QTableWidgetItem(data['23']))
        self.ComparisonTable.setItem(1, 3, QtWidgets.QTableWidgetItem(data['24']))
        self.ComparisonTable.setItem(1, 4, QtWidgets.QTableWidgetItem(data['25']))
        self.ComparisonTable.setItem(1, 5, QtWidgets.QTableWidgetItem(data['26']))
        self.ComparisonTable.setItem(2, 0, QtWidgets.QTableWidgetItem(data['31']))
        self.ComparisonTable.setItem(2, 1, QtWidgets.QTableWidgetItem(data['32']))
        self.ComparisonTable.setItem(2, 2, QtWidgets.QTableWidgetItem(data['33']))
        self.ComparisonTable.setItem(2, 3, QtWidgets.QTableWidgetItem(data['34']))
        self.ComparisonTable.setItem(2, 4, QtWidgets.QTableWidgetItem(data['35']))
        self.ComparisonTable.setItem(2, 5, QtWidgets.QTableWidgetItem(data['36']))
        self.ComparisonTable.setItem(3, 0, QtWidgets.QTableWidgetItem(data['41']))
        self.ComparisonTable.setItem(3, 1, QtWidgets.QTableWidgetItem(data['42']))
        self.ComparisonTable.setItem(3, 2, QtWidgets.QTableWidgetItem(data['43']))
        self.ComparisonTable.setItem(3, 3, QtWidgets.QTableWidgetItem(data['44']))
        self.ComparisonTable.setItem(3, 4, QtWidgets.QTableWidgetItem(data['45']))
        self.ComparisonTable.setItem(3, 5, QtWidgets.QTableWidgetItem(data['46']))


app = QApplication(sys.argv)
window = Firstpage()
window.show()
sys.exit(app.exec_())