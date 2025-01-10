
##---------SERVER---------##

import time  # Importa o módulo de tempo para lidar com atrasos
from socket import *  # Importa todas as funções necessárias do módulo socket

serverPort = 12000  # Define a porta em que o servidor irá escutar por conexões
serverSocket = socket(AF_INET, SOCK_STREAM)  # Cria um socket IPV4 , TCP/IP.Porém ele não sabe qual endereço e porta tem que escutar, então 
serverSocket.bind(('', serverPort))  # Associa o socket ao endereço e porta especificados
serverSocket.listen(1)  # Habilita o servidor para aceitar conexões, com uma conexão pendente na fila
print("Aguardando conexão com cliente...")

#Agora o servidor precisa aceitar a conexão.Basta fazer:

while True:  # Loop infinito para receber conexões continuamente
    connecao, endereco = serverSocket.accept()  # Aceita uma nova conexão e armazena o socket e o endereço
    print("Conectado em:", endereco)
    
    dados = connecao.recv(1024)  # Recebe dados da conexão (até 1024 bytes)
    
    # Quando não tiver mais dados para receber
    if not dados:
        print("Fechando conexão")
        connecao.close()  # Fecha a conexão com o cliente
        break
    
    connecao.sendall(dados)  # Envia de volta os dados para o cliente
    text = dados.decode('utf-8')  # Decodifica os dados recebidos para UTF-8
    capitalizedSentence = text.upper()  # Converte a frase recebida para letras maiúsculas
    connecao.send(capitalizedSentence.encode('utf-8'))  # Envia a frase em letras maiúsculas de volta para o cliente

