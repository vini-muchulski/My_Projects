import tweepy
from keys import api_key, api_key_secret, access_token, access_token_secret, bearer_token



client = tweepy.Client(
    bearer_token,api_key,api_key_secret,access_token,access_token_secret
)

auth = tweepy.OAuth1UserHandler(api_key,api_key_secret,access_token,access_token_secret)
api= tweepy.API(auth)

#client.create_tweet(text="teste 25 01 20:33hrs")


imagem = "imagem.jpg"
tweet_titulo = ""

with open("infos.txt","r",encoding="utf-8") as arquivo:
    tweet_titulo = arquivo.read()

"""media = client.media_upload(imagem)
client.update_status(status=tweet_titulo,media_ids=[media.media_id])"""

media = api.simple_upload(filename=imagem)
media_id = media.media_id

client.create_tweet(text=tweet_titulo,media_ids=[media_id])