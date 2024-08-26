import streamlit as st
import subprocess
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1" 
import pygame
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Gerador de Áudio", page_icon="🎙️", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Carregar animação do foguete
lottie_audio = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_GofK09iPAE.json")

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
            

with st.sidebar:
    st.title("Configurações")
    idioma = st.selectbox("Escolha um idioma:", ["Português", "Inglês", "Espanhol"], 
                          format_func=lambda x: {"Português": "🇧🇷", "Inglês": "🇺🇸", "Espanhol": "🇪🇸"}[x] + " " + x)


col1, col2 = st.columns([2, 1])

with col1:
    st.title("🎙️ Gerador de Áudio")
    texto = st.text_area("Digite seu texto:", height=200, 
                         placeholder="Escreva aqui o texto que você deseja converter em áudio...")
    
    if st.button("🔊 Reproduzir Áudio", type="primary"):
        with st.spinner("Gerando áudio..."):
            gerar_audio(texto.strip(), idioma=idioma)
        st.success("Áudio gerado com sucesso!")

with col2:
    st_lottie(lottie_audio, height=300, key="audio_animation")


st.markdown("---")
st.subheader("Como usar:")
st.markdown("""
1. Selecione o idioma desejado no menu lateral.
2. Digite ou cole seu texto na caixa de texto.
3. Clique no botão 'Reproduzir Áudio' para gerar e ouvir o resultado.
""")

# Footer
st.markdown("---")
st.caption("Desenvolvido por [vini-muchulski](https://github.com/vini-muchulski) usando Streamlit e Python.")
st.markdown("---")
