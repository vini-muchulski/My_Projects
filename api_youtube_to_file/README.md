
##Português

# Extração de títulos e links de playlists do Youtube

Este projeto extrai os títulos e links de playlists do Youtube a partir de uma lista de IDs de playlist. 

## Funcionamento

- As playlists são fornecidas em um arquivo txt, uma playlist por linha
- Expressões regulares são usadas para extrair o ID da playlist a partir dos links
- A API do Youtube é consultada para obter o título e link de cada playlist
- Os resultados são escritos em um arquivo txt  no formato:

   ```
   Título da Playlist -> Link da Playlist

   Título da Playlist 2 -> Link da Playlist 2
   ```

- Playlists que não puderam ser processadas são listadas no final

## Tecnologias

- Python
- Expressões regulares (re)
- API do Youtube 
- Google API Client

## Uso

1. Obter uma chave de API do Youtube e adicioná-la no código
2. Preencher o arquivo "playlists_opera.txt" com links para as playlists
3. Rodar o script main_version.py
4. Os resultados estarão no "arquivo_playlists.txt"

---
##English

# Youtube Playlist Titles and Links Scraper

This project scrapes the titles and links of Youtube playlists from a list of playlist IDs.

## How it works

- Playlists are provided in a txt file, one playlist per line
- Regular expressions are used to extract the playlist ID from the links
- The Youtube API is queried to get the title and link for each playlist
- Results are written to a txt file in the format:

   ```
   Playlist Title -> Playlist Link

   Playlist Title 2 -> Playlist Link 2
   ```

- Playlists that could not be processed are listed at the end

## Technologies

- Python
- Regular expressions (re)  
- Youtube API
- Google API Client

## Usage 

1. Get a Youtube API key and add it to the code
2. Populate the "playlists_opera.txt" file with links to playlists
3. Run the main_version.py script
4. Results will be in the "arquivo_playlists.txt" file
