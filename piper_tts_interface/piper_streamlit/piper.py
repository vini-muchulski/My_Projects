import subprocess

# Comando que você quer executar
comando = "type  .\demo.txt | .\piper.exe -m .\pt_BR-faber-medium.onnx -f audio.wav" 
#print(comando)

resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)


# Verificando se ocorreu algum erro durante a execução do comando
if resultado.returncode == 0:
    print(resultado.stdout)
    print("gerado com sucesso!")
else:
    print("Erro:", resultado.stderr)