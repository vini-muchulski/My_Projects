README em Português:

# Projeto de Leitura Automática de PDF com Resumo Usando Modelo de Linguagem (LLM)

Este projeto é uma aplicação em Python que automatiza a leitura de arquivos PDF e gera um resumo do conteúdo usando um modelo de Linguagem (LLM) chamado Mistral OpenOrca. Especificamente, o código extrai tabelas, texto e informações relevantes de um arquivo PDF que contém um plano de ensino e, em seguida, utiliza o modelo LLM para gerar um resumo conciso do conteúdo.
Neste projeto usei o LM Studio que gera uma API de um localhost de um modelo de linguagem que rodou localmente na minha máquina

## Funcionalidades

- Extração automática de tabelas e texto do PDF utilizando as bibliotecas `tabula` e `PyPDF2`.
- Processamento do texto extraído para separar seções importantes, como informações gerais, lista de bibliografia básica e complementar.
- Geração de um resumo conciso do conteúdo do PDF utilizando o modelo de Linguagem Mistral OpenOrca.

## Requisitos

- Python 3.x
- LM Studio
- Bibliotecas: `tabula`, `PyPDF2`, `openai`
- Acesso ao modelo de Linguagem Mistral OpenOrca (hospedado localmente ou através de uma API).

## Instalação

1. Clone este repositório ou faça o download dos arquivos.
2. Instale as bibliotecas necessárias executando o seguinte comando:

```
pip install tabula PyPDF2 openai
```

3. Configure o acesso ao modelo de Linguagem Mistral OpenOrca (instruções detalhadas podem variar dependendo da sua configuração).

## Uso

1. Coloque o arquivo PDF que deseja resumir na mesma pasta que o script Python.
2. Execute o script Python.
3. O código irá extrair e processar as informações do arquivo PDF.
4. O modelo de Linguagem Mistral OpenOrca será usado para gerar um resumo conciso do conteúdo.
5. O resumo gerado será exibido na saída do programa.





README English:

# Automated PDF Reading Project with Summary Generation Using Mistral OpenOrca

This project is a Python application that automates the reading of PDF files and generates a summary of the content using a Language Model (NLM) called Mistral OpenOrca. Specifically, the code extracts tables, text, and relevant information from a PDF file containing a course syllabus, and then uses the NLM model to generate a concise summary of the content.

## Features

- Automatic extraction of tables and text from the PDF using the `tabula` and `PyPDF2` libraries.
- Processing of the extracted text to separate important sections, such as general information, basic and complementary bibliography lists.
- Generation of a concise summary of the PDF content using the Mistral OpenOrca Language Model.

## Requirements

- Python 3.x
- Libraries: `tabula`, `PyPDF2`, `openai`
- LM Studio
- Access to the Mistral OpenOrca Language Model (hosted locally or through an API).

## Installation

1. Clone this repository or download the files.
2. Install the required libraries by running the following command:

```
pip install tabula PyPDF2 openai
```

3. Set up access to the Mistral OpenOrca Language Model (detailed instructions may vary depending on your configuration).

## Usage

1. Place the PDF file you want to summarize in the same folder as the Python script.
2. Run the Python script.
3. The code will extract and process the information from the PDF file.
4. The Mistral OpenOrca Language Model will be used to generate a concise summary of the content.
5. The generated summary will be displayed in the program output.

