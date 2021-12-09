#%%  Kalkulyator  uy ishi
import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Kalkulator(QWidget):
    def __init__(self):
        super().__init__()
        self.son=[]
        self.Amal()
        self.son1=0
    def Amal(self):
        
        self.ekran=QLineEdit(self)
        self.ekran.setGeometry(15, 5, 510, 70)
        self.ekran.setFont(QFont("MS PGothic",25))
        self.ekran.setPlaceholderText("88888888888888888888888")
        self.setStyleSheet("background-color: silver;")
        self.ekran.setStyleSheet("background-color : white;border : 2px solid black; border-radius : 10px;")
        self.message=QMessageBox()
        
        self.push1=QPushButton(self)
        self.push1.setGeometry(15, 80, 90, 90)
        self.push1.setFont(QFont("Segoe UI Black",30))
        self.push1.setText("7")
        self.push1.clicked.connect(self.f7)
        self.push1.setStyleSheet("background-color : wheat;border : 2px solid chocolate; border-radius : 45px;")
        
        self.push2=QPushButton(self)
        self.push2.setGeometry(120, 80, 90, 90)
        self.push2.setFont(QFont("Segoe UI Black",30))
        self.push2.setText("8")
        self.push2.clicked.connect(self.f8)
        self.push2.setStyleSheet("background-color : wheat;border : 2px solid chocolate; border-radius : 45px;") 
        
        self.push3=QPushButton(self)
        self.push3.setGeometry(225, 80, 90, 90)
        self.push3.setFont(QFont("Segoe UI Black",30))
        self.push3.setText("9")
        self.push3.clicked.connect(self.f9)
        self.push3.setStyleSheet("background-color : wheat;border : 2px solid chocolate; border-radius : 45px;") 
        
        self.push4=QPushButton(self)
        self.push4.setGeometry(15, 185, 90, 90)
        self.push4.setFont(QFont("Segoe UI Black",30))
        self.push4.setText("4")
        self.push4.clicked.connect(self.f4) 
        self.push4.setStyleSheet("background-color : wheat;border : 2px solid chocolate; border-radius : 45px;") 
        
        self.push5=QPushButton(self)
        self.push5.setGeometry(120, 185, 90, 90)
        self.push5.setFont(QFont("Segoe UI Black",30))
        self.push5.setText("5")
        self.push5.clicked.connect(self.f5)
        self.push5.setStyleSheet("background-color : wheat;border : 2px solid chocolate; border-radius : 45px;") 
        
        self.push6=QPushButton(self)
        self.push6.setGeometry(225, 185, 90, 90)
        self.push6.setFont(QFont("Segoe UI Black",30))
        self.push6.setText("6")
        self.push6.clicked.connect(self.f6)
        self.push6.setStyleSheet("background-color : wheat;border : 2px solid chocolate; border-radius : 45px;") 
        
        self.push7=QPushButton(self)
        self.push7.setGeometry(15, 290, 90, 90)
        self.push7.setFont(QFont("Segoe UI Black",30))
        self.push7.setText("1")
        self.push7.clicked.connect(self.f1)
        self.push7.setStyleSheet("background-color : wheat;border : 2px solid chocolate; border-radius : 45px;") 
        
        self.push8=QPushButton(self)
        self.push8.setGeometry(120, 290, 90, 90)
        self.push8.setFont(QFont("Segoe UI Black",30))
        self.push8.setText("2")
        self.push8.clicked.connect(self.f2)
        self.push8.setStyleSheet("background-color : wheat;border : 2px solid chocolate; border-radius : 45px;") 
        
        self.push9=QPushButton(self)
        self.push9.setGeometry(225, 290, 90, 90)
        self.push9.setFont(QFont("Segoe UI Black",30))
        self.push9.setText("3")
        self.push9.clicked.connect(self.f3)
        self.push9.setStyleSheet("background-color : wheat;border : 2px solid chocolate; border-radius : 45px;") 
        
        self.pushf=QPushButton(self)
        self.pushf.setGeometry(15, 395, 90, 90)
        self.pushf.setFont(QFont("Segoe UI Black",30))
        self.pushf.setText("%")
        self.pushf.clicked.connect(self.ff)
        self.pushf.setStyleSheet("background-color : wheat;border : 2px solid blue; border-radius : 25px;") 
            
        self.push0=QPushButton(self)
        self.push0.setGeometry(120, 395, 90, 90)
        self.push0.setFont(QFont("Segoe UI Black",30))
        self.push0.setText("0")
        self.push0.clicked.connect(self.f0)
        self.push0.setStyleSheet("background-color : wheat;border : 2px solid chocolate; border-radius : 45px;") 
        
        self.pushn=QPushButton(self)
        self.pushn.setGeometry(225, 395, 90, 90)
        self.pushn.setFont(QFont("Segoe UI Black",30))
        self.pushn.setText(".")
        self.pushn.clicked.connect(self.fn)
        self.pushn.setStyleSheet("background-color : wheat;border : 2px solid blue; border-radius : 25px;") 
        

        self.pushp=QPushButton(self)
        self.pushp.setGeometry(330, 80, 90, 90)
        self.pushp.setFont(QFont("Segoe UI Black",30))
        self.pushp.setText("/")
        self.pushp.clicked.connect(self.fb)
        self.pushp.setStyleSheet("background-color : wheat; border : 2px solid blue; border-radius : 25px;") 
        

        self.pushm=QPushButton(self)
        self.pushm.setGeometry(330, 185, 90, 90)
        self.pushm.setFont(QFont("Segoe UI Black",30))
        self.pushm.setText("*")
        self.pushm.clicked.connect(self.fk)
        self.pushm.setStyleSheet("background-color : wheat;border : 2px solid blue; border-radius : 25px;") 
        

        self.pushk=QPushButton(self)
        self.pushk.setGeometry(330, 290, 90, 90)
        self.pushk.setFont(QFont("Segoe UI Black",30))
        self.pushk.setText("-")
        self.pushk.clicked.connect(self.fm)
        self.pushk.setStyleSheet("background-color : wheat;border : 2px solid blue; border-radius : 25px;") 
        

        self.pushb=QPushButton(self)
        self.pushb.setGeometry(330, 395, 90, 90)
        self.pushb.setFont(QFont("Segoe UI Black",30))
        self.pushb.setText("+")
        self.pushb.clicked.connect(self.fp)
        self.pushb.setStyleSheet("background-color : wheat;border : 2px solid blue; border-radius : 25px;") 
        
        self.pushc=QPushButton(self)
        self.pushc.setGeometry(435, 80, 90, 90)
        self.pushc.setFont(QFont("Segoe UI Black",30))
        self.pushc.setText("<")
        self.pushc.clicked.connect(self.fc)
        self.pushc.setStyleSheet("background-color : wheat;border : 2px solid blue; border-radius : 25px;") 

        self.pushce=QPushButton(self)
        self.pushce.setGeometry(435, 185, 90, 90)
        self.pushce.setFont(QFont("Segoe UI Black",30))
        self.pushce.setText("CE")
        self.pushce.clicked.connect(self.fce)
        self.pushce.setStyleSheet("background-color : wheat;border : 2px solid blue; border-radius : 25px;") 

        self.pusht=QPushButton(self)
        self.pusht.setGeometry(435, 290, 90, 195)
        self.pusht.setFont(QFont("Segoe UI Black",30))
        self.pusht.setText("=")
        self.pusht.clicked.connect(self.ft)
        self.pusht.setStyleSheet("background-color : salmon; border : 2px solid blue; border-radius : 25px;") 
        self.t=QGraphicsColorizeEffect()
        #self.t.setColor(Qt.blue)
        self.pusht.setGraphicsEffect(self.t)
        self.show()
    
    def f1(self):
        self.ekran.setText(self.ekran.text()+"1")
        self.son.append("1")
        self.ekran.setPlaceholderText("88888888888888888888888")

    def f2(self):
        self.ekran.setText(self.ekran.text()+"2")
        self.son.append("2")
        self.ekran.setPlaceholderText("88888888888888888888888")

    def f3(self):
        self.ekran.setText(self.ekran.text()+"3")
        self.son.append("3")
        self.ekran.setPlaceholderText("88888888888888888888888")

    def f4(self):
        self.ekran.setText(self.ekran.text()+"4")
        self.son.append("4")
        self.ekran.setPlaceholderText("88888888888888888888888")

    def f5(self):
        self.ekran.setText(self.ekran.text()+"5")
        self.son.append("5")
        self.ekran.setPlaceholderText("88888888888888888888888")

    def f6(self):
        self.ekran.setText(self.ekran.text()+"6")
        self.son.append("6")
        self.ekran.setPlaceholderText("88888888888888888888888")

    def f7(self):
        self.ekran.setText(self.ekran.text()+"7")
        self.son.append("7")
        self.ekran.setPlaceholderText("88888888888888888888888")

    def f8(self):
        self.ekran.setText(self.ekran.text()+"8")
        self.son.append("8")
        self.ekran.setPlaceholderText("88888888888888888888888")

    def f9(self):
        self.ekran.setText(self.ekran.text()+"9")
        self.son.append("9")
        self.ekran.setPlaceholderText("88888888888888888888888")

    def f0(self):
        self.ekran.setText(self.ekran.text()+"0")
        self.son.append("0")
        self.ekran.setPlaceholderText("88888888888888888888888")
        if  self.son[0]=="0"  and self.son1==0:
            self.ekran.setText(self.ekran.text()+".")
            self.son.append(".")
            self.pushn.setEnabled(False)
            self.son1=+1
            
        elif self.son[-1]=="0" and self.son1==1:
            if  self.son[-2]=="1" or self.son[-2]=="2" or self.son[-2]=="3" or self.son[-2]=="4" or self.son[-2]=="5" or self.son[-2]=="6" or self.son[-2]=="7" or self.son[-2]=="8" or self.son[-2]=="9" or self.son[-2]=="." or self.son[-2]=="0":
                pass
            else:
                self.ekran.setText(self.ekran.text()+".")
                self.son.append(".")
                self.pushn.setEnabled(False)
                self.son1=+1
            
    def ff(self):
        if self.son[-1]!="%" and self.son[-1]!="+" and self.son[-1]!="-" and self.son[-1]!="%" and self.son[-1]!="*" and self.son[-1]!="/" and self.son[-1]!=".":
            print(self.son[-1])
            self.ekran.setText(self.ekran.text()+"%")
            self.son.append("%")
            self.pushn.setEnabled(True)
            self.son1=1

    def fn(self):
        if self.son[-1]!="%" and self.son[-1]!="+" and self.son[-1]!="-" and self.son[-1]!="%" and self.son[-1]!="*" and self.son[-1]!="/" and self.son[-1]!=".":
            self.pushn.setEnabled(False)             
            if self.son[-1]=="1" or self.son[-1]=="2" or self.son[-1]=="3" or self.son[-1]=="4" or self.son[-1]=="5" or self.son[-1]=="6" or self.son[-1]=="7" or self.son[-1]=="8" or self.son[-1]=="9" or self.son[-1]=="0" and self.son[-1]!="." :
                self.ekran.setText(self.ekran.text()+".")
                self.son.append(".")
                 
    def fb(self):
        if self.son[-1]!="%" and self.son[-1]!="+" and self.son[-1]!="-" and self.son[-1]!="%" and self.son[-1]!="*" and self.son[-1]!="/" and self.son[-1]!=".":
            self.ekran.setText(self.ekran.text()+"/")
            self.son.append("/")
            self.pushn.setEnabled(True)
            self.son1=1

    def fk(self):
        if self.son[-1]!="%" and self.son[-1]!="+" and self.son[-1]!="-" and self.son[-1]!="%" and self.son[-1]!="*" and self.son[-1]!="/" and self.son[-1]!=".":
            self.ekran.setText(self.ekran.text()+"*")
            self.son.append("*")
            self.pushn.setEnabled(True)
            self.son1=1

    def fm(self):
        if self.son[-1]!="%" and self.son[-1]!="+" and self.son[-1]!="-" and self.son[-1]!="%" and self.son[-1]!="*" and self.son[-1]!="/" and self.son[-1]!=".":
            self.ekran.setText(self.ekran.text()+"-")
            self.son.append("-")
            self.pushn.setEnabled(True)
            self.son1=1

    def fp(self):
        if self.son[-1]!="%" and self.son[-1]!="+" and self.son[-1]!="-" and self.son[-1]!="%" and self.son[-1]!="*" and self.son[-1]!="/" and self.son[-1]!=".":
            self.ekran.setText(self.ekran.text()+"+")
            self.son.append("+")
            self.pushn.setEnabled(True)
            self.son1=1

    def fc(self):
        s=self.ekran.text()
        self.ekran.setText(s[:len(s)-1])
        nuqta=self.son.pop()
        if nuqta==".":
            self.pushn.setEnabled(True)
            self.son1=0
            
    def fce(self):
        self.ekran.setText("")
        self.son=[]
        self.pushn.setEnabled(True)
        self.son1=0
        self.ekran.setPlaceholderText("88888888888888888888888")

    def ft(self):
        x=self.ekran.text()
        try:
            xisob=eval(self.ekran.text())
            self.ekran.setText(str(xisob))
            
        except:
            self.ekran.setText("")
            self.ekran.setPlaceholderText("Error")
            self.message.setWindowTitle("Xato")
            
            m_box=QMessageBox(self)
            m_box.setWindowTitle("Error")
            m_box.setText("Xatolikni tekshiring")
            m_box.setIcon(QMessageBox.Critical)
            m_box.setStandardButtons(QMessageBox.Ok)
            m_box.buttonClicked.connect(self.ft)
            m_box.exec_()
            
            
            
            
      
app=QApplication(sys.argv)
bb=Kalkulator()
bb.resize(540, 500)
bb.setWindowTitle("KALKULYATOR")
bb.setFixedSize(540, 500)
bb.show()
sys.exit(app.exec_())
