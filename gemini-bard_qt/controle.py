import google.generativeai as genai


from PyQt5 import uic,QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget

chat_global = None

def start_gemini():
    global chat_global
    api = formulario.api_input.text()
    
    genai.configure(api_key=api)
    model = genai.GenerativeModel('gemini-pro')
    chat_global = model.start_chat(history=[])
    #print(api)
    pass

def enviar_msg():
    #prompt = formulario.box_prompt.text()
    prompt = formulario.box_prompt.toPlainText()
    print(prompt)

    response = chat_global.send_message(prompt)
                        
    #resposta_formatada = formatar_resposta(response.text)
    resposta_formatada = formatar_resposta(response.text)
    #formulario.box_resposta.addItem(response.text)
    #print(resposta_formatada)
    formulario.box_resposta.addItem(resposta_formatada)

def formatar_resposta(resposta):
    #print(resposta)
    palavras = resposta.split()
    #print(palavras)
    tamanho = 20
    resposta_formatada = []
    linha_atual = []
    for palavra in palavras:
        if( tamanho == len(linha_atual)):
            resposta_formatada.append(" ".join(linha_atual))
            linha_atual = []
        
        linha_atual.append(palavra)
        

    resposta_formatada.append(" ".join(linha_atual))
    #print(resposta_formatada)
    texto_final = "\n".join(resposta_formatada)
    #print(texto_final)
    return  texto_final
            

app = QtWidgets.QApplication([])

formulario = uic.loadUi("gemini_interface.ui")

formulario.setWindowIcon(QtGui.QIcon('logo.png'))
formulario.setWindowTitle("Interface with Gemini")
formulario.btn_enviar.clicked.connect(enviar_msg)
formulario.btn_ativar.clicked.connect(start_gemini)

formulario.show()
app.exec()
