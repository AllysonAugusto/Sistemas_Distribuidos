import socket
import threading
import time

requisiçao = "ADD;20;50"
clientes = 100  

def multiThread_server():
    tempo_inicial = time.time()

    threads = []
    for i in range(clientes):
        thread = threading.Thread(target=enviar_requisiçao_multi)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    tempo_final = time.time()
    print("Tempo total para o servidor multithreaded:", tempo_final - tempo_inicial, "segundos")

def singleThread_server():
    Tempo_inicial = time.time()

    for _ in range(clientes):
        enviar_requisiçao_single()

    tempo_final = time.time()
    print("Tempo total para o servidor single-threaded:", tempo_final - Tempo_inicial, "segundos")

def enviar_requisiçao_multi():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 13000))
        s.sendall(bytes(requisiçao, 'utf-8'))
        s.recv(1024)

def enviar_requisiçao_single():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 12000))
        s.sendall(bytes(requisiçao, 'utf-8'))
        s.recv(1024)


threading.Thread(target=multiThread_server).start()
singleThread_server()