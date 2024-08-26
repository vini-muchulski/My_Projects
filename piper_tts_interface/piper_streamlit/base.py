import streamlit as st
import subprocess
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1" 
import pygame




def  gerar_audio(prompt,idioma):         
    demo = open("demo.txt","w",encoding="utf-8")
    demo.write(prompt)
    demo.close()

    # Comando que você quer executar
    if(idioma == "Português"):
                comando = "type  .\demo.txt | .\piper.exe -m .\pt_BR-faber-medium.onnx -f audio.wav" 
    
    elif(idioma == "Inglês"):
                comando = "type  .\demo.txt | .\piper.exe -m .\en_US-bryce-medium.onnx -f audio.wav"
                
    elif(idioma == "Espanhol"):
                comando = "type  .\demo.txt | .\piper.exe -m .\es_ES-sharvard-medium.onnx -f audio.wav"


    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    
    if resultado.returncode == 0:
            print(resultado.stdout + "gerado com sucesso!")
            
            print(prompt)
            
            # Inicializa o mixer do pygame
            pygame.mixer.init()

            # Carrega o arquivo de áudio
            pygame.mixer.music.load("audio.wav")

            # Reproduz o arquivo de áudio
            pygame.mixer.music.play()

            # Mantém o programa rodando até que o áudio termine
            while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
            
            pygame.mixer.quit()       
            audio_gerado = True
    else:
        print("Erro:", resultado.stderr)
            

st.title("Gerador de áudio")
idioma = st.selectbox("Escolha um idioma:", ["Português", "Inglês", "Espanhol"])

texto = st.text_area("Digite seu texto:", height=200)
st.write("Você digitou: ", texto)

if st.button("Reproduzir áudio"):
    gerar_audio(texto.strip(),idioma=idioma)

