

# Interface com Modelo Bard/Gemini-pro

Este projeto consiste em uma interface gráfica desenvolvida em PyQt5 para interagir com o modelo de IA Gemini-pro do Google.

## Requisitos

- Python 3.6+
- PyQt5
- google.generativeai (biblioteca de clientes Python para API do Google)
- Chave de API para acesso aos modelos do Google (obtida no site do Google)

## Funcionamento

O programa carrega a interface desenvolvida em Qt Designer (`gemini_interface.ui`). Esta interface consiste em:

- Campo para inserir a chave de API
- Campo de texto para digitar as prompts
- Botão para enviar as prompts e receber respostas do Gemini
- Botão para ativar a conexão com o Gemini usando a chave fornecida
- Campo de texto para exibir as respostas do Gemini

Ao clicar no botão "Ativar", a chave de API é configurada e um chat é iniciado com o modelo Gemini-pro.

Ao digitar uma prompt e clicar em "Enviar", a prompt é enviada para o chat ativo com o Gemini e a resposta é formatada (quebra de linhas) antes de ser exibida na interface.

## Instalação

- Clonar repositório
- Instalar requisitos com `pip install -r requirements.txt` 
- Obter chave de API do Google
- Preencher chave em `keys.py`
- Executar `python controle.py`

