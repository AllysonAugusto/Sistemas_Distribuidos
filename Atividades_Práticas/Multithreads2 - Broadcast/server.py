"A aplicação consiste em um user mandar mensagem pro server e ai o server replicar para todos os outros usuarios, menos de quem recebeu.Todo cliente que estabelecer conexão com o server vai ser armazenado em uma lista."

import threading
import socket

clients = [] #lista que recebe os 

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 7777)) #tupla associativa com o cliente
        server.listen() #escutando n conexões
    except:
        return print("ERROR: Não foi possível iniciar o servidor.")
    

    while True: #vai ficar sempre aceitando várias conexões e criando várias threads 
        cliente, endereco = server.recv() #pra retornar o cliente e o endereço pra saber quem é quem
        clients.append(cliente)

        #Criando threads.Para cada usuario que chegar, vai sendo armmazenado na lista e criando uma thread pra ele
        thread = threading.Thread(target=Tratamento_Mensagem, args=cliente)
        thread.start()
#Funçao que recebe a mensagem de cada usuario , onde recebe um objeto cliente


def Tratamento_Mensagem(cliente):
    while True: #cada vez que o cliente mandar mensagem pega a mensagem e manda pros outros
        try:
            msg = cliente.recv(2048)
            broadcast(cliente, msg) #mandando mensagem para todos os usuarios, passando a mensagem e o cliente
        except:
            deletandoCliente(cliente) #deeltando o cliente caso nao receba
            break #parando de ouvir a mensagem


def broadcast(msg, cliente):
    for clienteItem in clients:
        if clienteItem != cliente:  #se o cliente qfor diferente do cliente que mandou a mensagem               #manda essa mensagem pra ele
            try: #tentando mandar a mensagem pra ele
                clienteItem.send(msg)
            except: #caso nao consiga, é porque o cliente foi removido.
                deletandoCliente(clienteItem)
                break
def deletandoCliente(cliente):
    clients.remove(cliente)

    