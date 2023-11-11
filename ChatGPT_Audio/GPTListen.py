# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GPTListen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from gtts import gTTS
import os
import requests
import json



class Ui_GPTListen(object):
    def setupUi(self, GPTListen):
        GPTListen.setObjectName("GPTListen")
        GPTListen.resize(931, 717)
        GPTListen.setStyleSheet("background: rgb(243, 238, 234)")
        self.centralwidget = QtWidgets.QWidget(GPTListen)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_api_gpt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_api_gpt.setGeometry(QtCore.QRect(30, 30, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_api_gpt.sizePolicy().hasHeightForWidth())
        self.btn_api_gpt.setSizePolicy(sizePolicy)
        self.btn_api_gpt.setStyleSheet("QPushButton{\n"
"\n"
"    \n"
"    background-color: rgb(85, 170, 127);\n"
"    \n"
"    color: rgb(0, 85, 0);\n"
"\n"
"border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(85, 170, 0);\n"
"\n"
"    \n"
"    \n"
"}")
        self.btn_api_gpt.setObjectName("btn_api_gpt")
        self.api_gpt = QtWidgets.QLineEdit(self.centralwidget)
        self.api_gpt.setGeometry(QtCore.QRect(130, 30, 251, 21))
        self.api_gpt.setObjectName("api_gpt")
        self.btn_sair = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sair.setGeometry(QtCore.QRect(30, 530, 121, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sair.sizePolicy().hasHeightForWidth())
        self.btn_sair.setSizePolicy(sizePolicy)
        self.btn_sair.setStyleSheet("QPushButton{\n"
"\n"
"    \n"
"    background-color: rgb(85, 170, 127);\n"
"    \n"
"    color: rgb(0, 85, 0);\n"
"\n"
"border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(85, 170, 0);\n"
"\n"
"    \n"
"    \n"
"}")
        self.btn_sair.setObjectName("btn_sair")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(330, 80, 441, 471))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.gpt_texto = QtWidgets.QTextBrowser(self.layoutWidget)
        self.gpt_texto.setObjectName("gpt_texto")
        self.verticalLayout_2.addWidget(self.gpt_texto)
        self.btn_ouvir_resposta = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ouvir_resposta.setGeometry(QtCore.QRect(30, 360, 241, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ouvir_resposta.sizePolicy().hasHeightForWidth())
        self.btn_ouvir_resposta.setSizePolicy(sizePolicy)
        self.btn_ouvir_resposta.setStyleSheet("QPushButton{\n"
"\n"
"    \n"
"    background-color: rgb(85, 170, 127);\n"
"    \n"
"    color: rgb(0, 85, 0);\n"
"\n"
"border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(85, 170, 0);\n"
"\n"
"    \n"
"    \n"
"}")
        self.btn_ouvir_resposta.setObjectName("btn_ouvir_resposta")
        self.btn_enviar_prompt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_enviar_prompt.setGeometry(QtCore.QRect(31, 308, 241, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_enviar_prompt.sizePolicy().hasHeightForWidth())
        self.btn_enviar_prompt.setSizePolicy(sizePolicy)
        self.btn_enviar_prompt.setStyleSheet("QPushButton{\n"
"\n"
"    \n"
"    background-color: rgb(85, 170, 127);\n"
"    \n"
"    color: rgb(0, 85, 0);\n"
"\n"
"border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(85, 170, 0);\n"
"\n"
"    \n"
"    \n"
"}")
        self.btn_enviar_prompt.setObjectName("btn_enviar_prompt")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(31, 81, 258, 213))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("QPushButton{\n"
"\n"
"    \n"
"    background-color: rgb(85, 170, 127);\n"
"    \n"
"    color: rgb(0, 85, 0);\n"
"\n"
"border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(85, 170, 0);\n"
"\n"
"    \n"
"    \n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.texto_prompt = QtWidgets.QTextEdit(self.widget)
        self.texto_prompt.setObjectName("texto_prompt")
        self.verticalLayout.addWidget(self.texto_prompt)
        GPTListen.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(GPTListen)
        self.statusbar.setObjectName("statusbar")
        GPTListen.setStatusBar(self.statusbar)

        self.retranslateUi(GPTListen)
        self.btn_sair.clicked.connect(GPTListen.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(GPTListen)

        self.btn_api_gpt.clicked.connect(self.get_api)

        self.btn_enviar_prompt.clicked.connect(self.get_and_send_prompt)
        self.btn_ouvir_resposta.clicked.connect(self.rodar_audio)




    def get_api(self):
        api_key = str(self.api_gpt.text())
        return api_key
    
    

    def get_and_send_prompt(self):
        prompt = str(self.texto_prompt.toPlainText())

        headers = {"Authorization": f"Bearer {self.get_api()}","Content-Type" : "application/json"}

        id_modelo = "gpt-3.5-turbo-0613"

        link = "https://api.openai.com/v1/chat/completions"
        body_msg = {
        "model" : id_modelo ,
        "messages": [{"role": "user", "content" : f"{prompt}"}]
        }

        body_msg = json.dumps(body_msg)

        requisicao = requests.post(link, headers=headers,data=body_msg)
        resposta = requisicao.json()
        #print(resposta)
        mensagem_resposta = resposta["choices"][0]["message"]["content"]

       

        self.gpt_texto.setText(mensagem_resposta)


    def rodar_audio(self):
        linguagem = "pt"
        texto = self.gpt_texto.toPlainText()

        text_to_sound = gTTS(texto, lang=linguagem)
        text_to_sound.save("audio.mp3")
        os.system('ffplay -autoexit -nodisp audio.mp3')

        

    def retranslateUi(self, GPTListen):
        _translate = QtCore.QCoreApplication.translate
        GPTListen.setWindowTitle(_translate("GPTListen", "GPTListen"))
        self.btn_api_gpt.setText(_translate("GPTListen", "Ativar API"))
        self.btn_sair.setText(_translate("GPTListen", "Sair"))
        self.label_2.setText(_translate("GPTListen", "GPT:"))
        self.btn_ouvir_resposta.setText(_translate("GPTListen", "Ouvir Resposta"))
        self.btn_enviar_prompt.setText(_translate("GPTListen", "Enviar Prompt"))
        self.label.setText(_translate("GPTListen", "Digite aqui: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GPTListen = QtWidgets.QMainWindow()
    ui = Ui_GPTListen()
    ui.setupUi(GPTListen)
    GPTListen.show()
    sys.exit(app.exec_())