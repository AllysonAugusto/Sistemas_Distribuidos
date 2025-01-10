import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#conectando com o servidor
cliente.connect(('localhost', 7777))
print("Cliente conectado.")

#pedindo para digitar o arquivo que deseja
nome_arquivo = str(input("Arquivo>"))

def enviando_arquivo(nome_arquivo):
    cliente.send(nome_arquivo.encode()) # enviando arquivo de string para bytes

with open(nome_arquivo, 'wb') as flle: #arquivo será aberto para escrita binária (foto.jpeg)
    while 1: #loop para ficar recebendo o arquivo
        dados = cliente.recv(1000000)
        if not dados: #se não tiver mais dados pra receber, fecha a conexão
            break
        flle.write(dados)
    
print(f'{nome_arquivo} recebido!\n')
