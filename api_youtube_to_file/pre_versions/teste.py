import re

# Sua string de exemplo
sua_string = 'https://www.youtube.com/playlist?list=ABCDE12345'

# Use uma expressão regular para encontrar a parte 'list=' seguida por qualquer sequência de caracteres
match = re.search(r'list=([A-Za-z0-9_-]+)', sua_string)

# Verifique se houve uma correspondência
print(match)
