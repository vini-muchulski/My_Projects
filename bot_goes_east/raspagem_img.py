from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
#navegador = webdriver.Chrome()

# Passo 1:
link = "https://www.ssec.wisc.edu/data/geo/#/animation?satellite=goes-east&end_datetime=latest&n_images=1&coverage=fd&channel=rgbstr"
#link =   "https://www.ssec.wisc.edu/data/geo/#/animation?satellite=himawari09&end_datetime=latest&n_images=1&coverage=fd&channel=rgb"
navegador.get(link)
time.sleep(3)

navegador.find_element('xpath', 
                       '//*[@id="downloadButtonsContainer"]/button[1]').click()

time.sleep(3)
janelas = navegador.window_handles
navegador.switch_to.window(janelas[1])
nova_url = navegador.current_url
#print(nova_url)

# Encontrar o elemento da imagem
imagem_elemento = navegador.find_element('xpath',"/html/body/img")

# Obtém o valor do atributo "src"
url_imagem = imagem_elemento.get_attribute("src")


nome_arquivo = "imagem1.png"  # Nome do arquivo de destino
with open(nome_arquivo, 'wb') as arquivo:
    resposta = requests.get(url_imagem)
    arquivo.write(resposta.content)
    #print(requests.get(url_imagem))
