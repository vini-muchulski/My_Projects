#pip install --upgrade google-api-python-client

from googleapiclient.discovery import build

yt_key = "API_KEY"
youtube = build('youtube','v3', developerKey=yt_key)


playlist_id = "PLP_dh3S9H39nSDKOZCtR3Hj98ZVUg-_sj"

res = youtube.playlists().list(
    part="snippet",
    id=playlist_id).execute()


playlist_title = res['items'][0]['snippet']['title']
playlist_link = f'https://www.youtube.com/playlist?list={playlist_id}'


print(f'Título da Playlist: {playlist_title}')
print(f'Link da Playlist: {playlist_link}')