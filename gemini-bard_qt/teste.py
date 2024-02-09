def limit_words_per_line(text, max_words):
  #resposta_formatada = wrap(resposta, width=20)
    palavras = text.split()
    tamanho = 20
    resposta_formatada = []
    linha_atual = []
    print(palavras)
    for palavra in palavras:
        if( tamanho == len(linha_atual)):
            resposta_formatada.append(" ".join(linha_atual))
            linha_atual = []
        
        linha_atual.append(palavra)
        

    resposta_formatada.append(" ".join(linha_atual))
    #print(resposta_formatada)
    texto_final = "\n".join(resposta_formatada)
    print(texto_final)

text = "A missão foi um sucesso total: Armstrong e Aldrin pousaram o módulo lunar Eagle na Lua em 20 de julho de 1969, e Armstrong se tornou o primeiro homem a pisar na superfície lunar."
print(limit_words_per_line(text, 4))
