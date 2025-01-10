##---------CLIENTE---------##

# Importação das funções necessárias do módulo socket
from socket import *

# Definição do endereço e porta do servidor
serverName = 'localhost'  # Endereço do servidor (localhost representa o próprio computador)
serverPort = 12000  # Porta em que o servidor está escutando por conexões

# Criação do socket do cliente
clientSocket = socket(AF_INET, SOCK_STREAM)  # Criação de um socket TCP/IP
# Conexão com o servidor
clientSocket.connect((serverName, serverPort))  # Conexão com o endereço e porta especificados

# Solicitação de entrada ao usuário
sentence = input('Digite alguma coisa:')  # Solicita ao usuário que insira uma frase

# Envio da frase para o servidor após codificação em UTF-8
clientSocket.sendall(str.encode('utf-8'))

# Recebimento de dados do servidor (até 1024 bytes) e armazenando-os na variavel 'dados'
dados = clientSocket.recv(1024)

print("Mensagem ecoada:", dados.decode()) #dados recebidos de UTF-8 para string legível

# Fechamento do socket do cliente
clientSocket.close()  # Libera os recursos do socket após a comunicação

