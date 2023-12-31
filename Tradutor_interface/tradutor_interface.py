# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tradutor_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from deep_translator import GoogleTranslator
import pyperclip
#módulo pyperclip é um módulo de terceiros que fornece uma interface simples para acessar a área de transferência em vários sistemas operacionais






class Ui_Tradutor(object):
    def setupUi(self, Tradutor):
        Tradutor.setWindowIcon(QtGui.QIcon('logo.jpeg'))
        Tradutor.setObjectName("Tradutor")
        Tradutor.resize(803, 624)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Tradutor.setFont(font)
        Tradutor.setStyleSheet("background-color: rgb(22, 72, 99);\n"
"")
        self.centralwidget = QtWidgets.QWidget(Tradutor)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_traduzir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_traduzir.setGeometry(QtCore.QRect(70, 390, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.btn_traduzir.setFont(font)
        self.btn_traduzir.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn_traduzir.setStyleSheet("background-color:rgb(66, 125, 157);\n"
" border-radius: 10px;\n"
" border-color: black;\n"
" color: white;")
        self.btn_traduzir.setObjectName("btn_traduzir")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:     rgb(221, 242, 253);\n"
"\n"
" border-radius: 15px;\n"
" border-color:white;\n"
"color: rgb(22, 72, 99);\n"
" ")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 430, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:     rgb(221, 242, 253);\n"
"\n"
" border-radius: 15px;\n"
" border-color:white;\n"
"color: rgb(22, 72, 99);\n"
" ")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 430, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:     rgb(221, 242, 253);\n"
"\n"
" border-radius: 15px;\n"
" border-color:white;\n"
"color: rgb(22, 72, 99);\n"
" ")
        self.label_3.setObjectName("label_3")
        self.btn_copiar_ctrlc = QtWidgets.QPushButton(self.centralwidget)
        self.btn_copiar_ctrlc.setGeometry(QtCore.QRect(480, 400, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.btn_copiar_ctrlc.setFont(font)
        self.btn_copiar_ctrlc.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn_copiar_ctrlc.setStyleSheet("background-color:rgb(66, 125, 157);\n"
" border-radius: 10px;\n"
" border-color: black;\n"
" color: white;")
        self.btn_copiar_ctrlc.setObjectName("btn_copiar_ctrlc")
        self.btn_fechar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fechar.setGeometry(QtCore.QRect(500, 440, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.btn_fechar.setFont(font)
        self.btn_fechar.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.btn_fechar.setStyleSheet("background-color:rgb(66, 125, 157);\n"
" border-radius: 10px;\n"
" border-color: black;\n"
" color: white;")
        self.btn_fechar.setObjectName("btn_fechar")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(210, 470, 77, 112))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ling2_ingles = QtWidgets.QPushButton(self.layoutWidget)
        self.ling2_ingles.setStyleSheet(" color: white;")
        self.ling2_ingles.setObjectName("ling2_ingles")
        self.verticalLayout.addWidget(self.ling2_ingles)
        self.ling2_pt_br = QtWidgets.QPushButton(self.layoutWidget)
        self.ling2_pt_br.setStyleSheet(" color: white;")
        self.ling2_pt_br.setObjectName("ling2_pt_br")
        self.verticalLayout.addWidget(self.ling2_pt_br)
        self.ling2_espanhol = QtWidgets.QPushButton(self.layoutWidget)
        self.ling2_espanhol.setStyleSheet(" color: white;")
        self.ling2_espanhol.setObjectName("ling2_espanhol")
        self.verticalLayout.addWidget(self.ling2_espanhol)
        self.ling2_frances = QtWidgets.QPushButton(self.layoutWidget)
        self.ling2_frances.setStyleSheet(" color: white;")
        self.ling2_frances.setObjectName("ling2_frances")
        self.verticalLayout.addWidget(self.ling2_frances)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(31, 473, 77, 112))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ling1_ingles = QtWidgets.QPushButton(self.layoutWidget1)
        self.ling1_ingles.setStyleSheet(" color: white;")
        self.ling1_ingles.setObjectName("ling1_ingles")
        self.verticalLayout_2.addWidget(self.ling1_ingles)
        self.ling1_pt_br = QtWidgets.QPushButton(self.layoutWidget1)
        self.ling1_pt_br.setStyleSheet(" color: white;")
        self.ling1_pt_br.setObjectName("ling1_pt_br")
        self.verticalLayout_2.addWidget(self.ling1_pt_br)
        self.ling1_espanhol = QtWidgets.QPushButton(self.layoutWidget1)
        self.ling1_espanhol.setStyleSheet(" color: white;")
        self.ling1_espanhol.setObjectName("ling1_espanhol")
        self.verticalLayout_2.addWidget(self.ling1_espanhol)
        self.ling1_frances = QtWidgets.QPushButton(self.layoutWidget1)
        self.ling1_frances.setStyleSheet(" color: white;")
        self.ling1_frances.setObjectName("ling1_frances")
        self.verticalLayout_2.addWidget(self.ling1_frances)
        self.texto_input = QtWidgets.QTextEdit(self.centralwidget)
        self.texto_input.setGeometry(QtCore.QRect(20, 100, 321, 281))
        self.texto_input.setStyleSheet("background-color:     rgb(221, 242, 253);")
        self.texto_input.setObjectName("texto_input")
        self.texto_traduzido = QtWidgets.QTextEdit(self.centralwidget)
        self.texto_traduzido.setGeometry(QtCore.QRect(420, 100, 321, 281))
        self.texto_traduzido.setStyleSheet("background-color:     rgb(221, 242, 253);")
        self.texto_traduzido.setObjectName("texto_traduzido")
        Tradutor.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Tradutor)
        self.statusbar.setObjectName("statusbar")
        Tradutor.setStatusBar(self.statusbar)

        self.retranslateUi(Tradutor)
        self.btn_fechar.clicked.connect(Tradutor.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Tradutor)


        
        self.linguagem_original = "auto"
        self.linguagem_traduzir = "pt"

        self.ling1_ingles.clicked.connect( self.get_english)
        self.ling1_pt_br.clicked.connect( self.get_portuguese)
        self.ling1_espanhol.clicked.connect( self.get_spanish)
        self.ling1_frances.clicked.connect( self.get_french)

        self.ling2_ingles.clicked.connect( self.set_english)
        self.ling2_pt_br.clicked.connect( self.set_portuguese)
        self.ling2_espanhol.clicked.connect( self.set_spanish)
        self.ling2_frances.clicked.connect( self.set_french)

        self.btn_traduzir.clicked.connect(self.get_texto_and_traduzir)
        self.btn_copiar_ctrlc.clicked.connect(self.copiar_texto)

        



    def retranslateUi(self, Tradutor):
        _translate = QtCore.QCoreApplication.translate
        Tradutor.setWindowTitle(_translate("Tradutor", "Tradutor"))
        self.btn_traduzir.setText(_translate("Tradutor", "Traduzir"))
        self.label.setText(_translate("Tradutor", "    Tradutor"))
        self.label_2.setText(_translate("Tradutor", " Idioma inicial:"))
        self.label_3.setText(_translate("Tradutor", " Traduzir para:"))
        self.btn_copiar_ctrlc.setText(_translate("Tradutor", "Copiar para Área de Transferência"))
        self.btn_fechar.setText(_translate("Tradutor", "Fechar"))
        self.ling2_ingles.setText(_translate("Tradutor", "Inglês"))
        self.ling2_pt_br.setText(_translate("Tradutor", "Português"))
        self.ling2_espanhol.setText(_translate("Tradutor", "Espanhol"))
        self.ling2_frances.setWhatsThis(_translate("Tradutor", "<html><head/><body><p> color: white;</p></body></html>"))
        self.ling2_frances.setText(_translate("Tradutor", "Francês"))
        self.ling1_ingles.setText(_translate("Tradutor", "Inglês"))
        self.ling1_pt_br.setText(_translate("Tradutor", "Português"))
        self.ling1_espanhol.setText(_translate("Tradutor", "Espanhol"))
        self.ling1_frances.setText(_translate("Tradutor", "Francês"))

    def get_english(self):
        self.linguagem_original = "en"
        
    def get_portuguese(self):
        self.linguagem_original = "pt"
        
    def get_spanish(self):
        self.linguagem_original = "es"
        
    def get_french(self):
        self.linguagem_original = "fr"

        
    def set_english(self):
        self.linguagem_traduzir = "en"
        
    def set_portuguese(self):
        self.linguagem_traduzir = "pt"
        
    def set_spanish(self):
        self.linguagem_traduzir = "es"
        
    def set_french(self):
        self.linguagem_traduzir = "fr"
    

    
        
    
    def get_texto_and_traduzir(self):
        texto = self.texto_input.toPlainText()
        linguagem1 = self.linguagem_original
        ling_destino = self.linguagem_traduzir

        
        print(self.linguagem_original)

        print(self.linguagem_traduzir)
        
        resultado_tradutor = GoogleTranslator(source=linguagem1, target=ling_destino)

        texto_traduzido = resultado_tradutor.translate(texto)

        self.texto_traduzido.setText(texto_traduzido)

    def copiar_texto(self):
        texto = self.texto_traduzido.toPlainText()
        pyperclip.copy(texto)

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tradutor = QtWidgets.QMainWindow()
    ui = Ui_Tradutor()
    ui.setupUi(Tradutor)
    Tradutor.show()
    sys.exit(app.exec_())
