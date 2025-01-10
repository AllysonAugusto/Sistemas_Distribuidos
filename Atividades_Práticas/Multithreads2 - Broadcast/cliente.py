import threading
import socket


def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criando o socket

    try: #verificar se vai ter ou não erro quando tiver no processo de conexão
        cliente.connect(("localhost", 7777))
    except:
        return print("\nNão foi possível se conectar ao servidor!\n")

    usuario = int('Usuário> ')
    print("\nCUsário conectado")


#Criando função para que as funções 'receber e enviar mensagem rodem ao mesmo tempo' e passar o argumento client.Depois é só dar start pra funcionar

    thread1 = threading.Thread(target=receber_mensagem, args =[cliente])
    thread2 = threading.Thread(target=enviar_mensagem, args=[cliente, usuario])

    thread1.start()
    thread2.start()


def receber_mensagem(cliente):#que vai receber o objeto cliente
    while True: #enquanto tiver conectado o servidor sempre vai ta mandando algo
        try:
            msg = cliente.recv(2048)
            codificado = (str(msg.decode('utf-8'))) #Mandar de strings para byes
            print(msg+'\n')
        except:
            print("\nNão foi possível permanecer conectado no server.")
            print('Precione <Enter> para continuar...') #enviando mensagem vai ser pego pela função send
            cliente.close() #dado que o cliente nao ta respondendo
            break

def enviar_mensagem(cliente, usuario):#que vai receber o objeto cliente
    while True:
        try:
            msg = input('Digite a sua mensagem: \n')
            cliente.send(f'<{usuario}> {msg}'.encode('utf-8')) #pegar a informação de quem mandou (user) e a mensagem.decodificar bytes em uma string.
        except: #dizer que o usuario ta desconectado, por exemplo
            return #sair da funcao


main()