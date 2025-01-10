import socket
import threading

def Calculo(client_socket,  tipo):
    request = client_socket.recv(1024).decode()
    operator, n1, n2 = request.split(";")
    
    if operator == "ADD":
        print(f"{tipo}:{n1} + {n2} =",int(n1) + int(n2))
    elif operator == "SUB":
        print(f"{n1} - {n2} =",int(n1) - int(n2))
    elif operator == "MUL":
        print(f"{n1} * {n2} =",int(n1) * int(n2))
    elif operator == "DIV":
        if int(n2) != 0:
            print(f"{n1} / {n2} =",int(n1) / int(n2))
        else:
            print(f"{tipo}: ERRO Divisão  por zero")


    client_socket.close()

def multiThread_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 13000))
    server_socket.listen(5)

    print("Servidor multiThreads TCP esperando conexões...")

    while True:
        client_socket, _ = server_socket.accept()
        tipo = "Multi Threads"
        client_handler = threading.Thread(target=Calculo, args=(client_socket,tipo))
        client_handler.start()

def singleThread_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12000))
    server_socket.listen(5)

    print("Servidor singleThread TCP esperando conexões...")

    while True:
        client_socket, _ = server_socket.accept()
        tipo = "Single Thread"
        Calculo(client_socket, tipo)



threading.Thread(target= multiThread_server).start()
singleThread_server()