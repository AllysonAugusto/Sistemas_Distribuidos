import socket

def server():
    try: #tratamento de erro
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criando socket
        server.bind(('localhost', 7777)) #associando endereço e porta
        server.listen(1) #ouvindo só uma conexão
        print("Servidor TCP iniciado. Aguardando conexões....")
        
        while True:  # Loop para aceitar conexões continuamente
            connection, address = server.accept()  # Aceita uma nova conexão e armazena o socket e o endereço
            print("Conexão estabelecida com", address)
            
    except Exception as error: #tratamento de erro
        print("Erro durante a execução do servidor:", error)

def armazenamento_informacao(connection):
    try:
        nome_arquivo = connection.recv(1024).decode()  # Recebendo o nome do arquivo enviado pelo cliente
        with open(nome_arquivo, 'rb') as file: # Abrindo o arquivo em modo de leitura binária
            for dado in file.readlines():# Lendo cada linha do arquivo e enviando para o cliente
                connection.send(dado)
                
        print("Arquivo enviado!")
    except Exception as error:
        print("Erro durante o armazenamento e envio do arquivo:", error)

# Iniciando o servidor
server()
