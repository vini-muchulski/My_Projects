# YouTube Audio Downloader MP3

# Português

# YouTube Audio Downloader

Este projeto é um script em Python que baixa o áudio de vídeos do YouTube. Ele utiliza a biblioteca `pytube` para interagir com a API do YouTube e fazer o download dos arquivos de áudio.

## Requisitos

- Python 3.x
- Biblioteca `pytube` (instalada automaticamente com o `pip`)
- Biblioteca `wget` (instalada automaticamente com o `pip`)

## Como usar

1. Crie um arquivo de texto chamado `videos.txt` e adicione os links dos vídeos do YouTube que deseja baixar, um por linha.
2. Certifique-se de que o arquivo `videos.txt` está localizado no mesmo diretório que o script `yt_download.py`.
3. Execute o script `yt_download.py`.
4. Os arquivos de áudio serão baixados e salvos na pasta `Engenheiros_do_Hawaii` criada no mesmo diretório.

## Notas

- O script substitui caracteres "/" no título do vídeo por " - " para evitar problemas ao salvar o arquivo.
- Se ocorrer algum erro durante o download de um vídeo, o script exibirá uma mensagem de erro e continuará com o próximo vídeo.

# English

# YouTube Audio Downloader

This project is a Python script that downloads audio from YouTube videos. It uses the `pytube` library to interact with the YouTube API and download the audio files.

## Requirements

- Python 3.x
- `pytube` library (automatically installed with `pip`)
- `wget` library (automatically installed with `pip`)

## How to use

1. Create a text file called `videos.txt` and add the links of the YouTube videos you want to download, one per line.
2. Make sure the `videos.txt` file is located in the same directory as the `yt_download.py` script.
3. Run the `yt_download.py` script.
4. The audio files will be downloaded and saved in the `Engenheiros_do_Hawaii` folder created in the same directory.

## Notes

- The script replaces "/" characters in the video title with " - " to avoid issues when saving the file.
- If an error occurs during the download of a video, the script will display an error message and continue with the next video.
