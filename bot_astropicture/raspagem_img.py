from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import wget
import requests
from bs4 import BeautifulSoup
import os


link = "https://apod.nasa.gov/apod/astropix.html"
headers =  {"User-Agent" : 
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}
requisicao = requests.get(link,headers=headers)
site = BeautifulSoup(requisicao.text, "html.parser")


def baixar_img(nome_arquivo):
    # Configurar as opções do Chrome para modo headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")  
    chrome_options.add_argument("--window-size=1920x1080")  


    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico, options=chrome_options)


    link = "https://apod.nasa.gov/apod/astropix.html"
    navegador.get(link)
    
    try:
        img_link = navegador.find_element(By.XPATH, '/html/body/center[1]/p[2]/a')
        href_value = img_link.get_attribute('href')
        print(href_value)


        
        output_path = r"D:\Codigos\Projects\bot_astropicture\imagem.jpg"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        if os.path.exists(output_path):
            os.remove(output_path)
            print(f"Arquivo antigo removido: {output_path}")
            
        wget.download(href_value,out=output_path)
        
    except:
        nome_imagem = "imagem.jpg"
        print("Erro ao baixar a imagem - possivelmente é video")
        os.remove(nome_imagem)
        



def get_titulo_img(site):
    titulo_da_imagem = site.find_all("b")
    titulo_da_imagem = titulo_da_imagem[0].text.strip()

    return titulo_da_imagem


def get_explicacao(site):
    explicacao = site.find_all("p")
    explicacao = str(explicacao[2].text.strip())
    
    #busca a posicao onde termina a explicacao da imagem
    try:
        posicao_fim_da_explicacao = explicacao.find("Tomorrow's picture:")
        

    except: 
        posicao_fim_da_explicacao = explicacao.find("Explore Your Universe:")


    explicacao = explicacao[:posicao_fim_da_explicacao].strip()
    explicacao = explicacao.replace('\n', ' ')

    return explicacao



baixar_img("imagem.jpg")
titulo_da_imagem = get_titulo_img(site)
explicacao = get_explicacao(site)

with open("infos.txt","w", encoding="utf-8") as arquivo:
    
    arquivo.write(titulo_da_imagem + "  #APOD" + " #NASA" + " #Astronomy" + "\n")
    

arquivo.close()

#print(url_imagem)
#print(titulo_da_imagem)
#print(explicacao)



