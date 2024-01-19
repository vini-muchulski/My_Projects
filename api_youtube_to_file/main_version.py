#pip install --upgrade google-api-python-client

#expressoes regulares
#api youtube
#arquivo

from googleapiclient.discovery import build
import re


yt_key = "api_key"
youtube = build('youtube','v3', developerKey=yt_key)
sucesso = 0


with open("playlists_opera.txt","r") as file:
    links = file.readlines()


with open("arquivo_playlists.txt","w",encoding="utf-8") as arquivo_playlists:
     arquivo_playlists.write("Titulo do video -> Link\n\n")


tamanho = len(links)
nao_processadas = []


#print(links)

for playlist in links:
    match = re.search(r'list=([A-Za-z0-9_-]+)', playlist)

    if(match):
        id = match.group(1)
        print(id)

        res = youtube.playlists().list(
            part="snippet",
            id=id).execute()
        
        playlist_title = res['items'][0]['snippet']['title']
        playlist_link = f'https://www.youtube.com/playlist?list={id}'

        resultado = f"{playlist_title} -> {playlist_link}\n"

        with open("arquivo_playlists.txt","a",encoding="utf-8") as arquivo_playlists:
            arquivo_playlists.write(resultado)
        
        

        print(resultado)
        sucesso+=1

    else:
        nao_processadas.append(playlist)

print(f"\n{sucesso} videos de um total de {tamanho} foram adicionados ao arquivo com sucesso")
print(f"nao processados => {nao_processadas}")


