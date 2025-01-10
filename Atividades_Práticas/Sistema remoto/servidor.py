# Importa o módulo rpyc para fazer RPC (Remote Procedure Call)
import rpyc
from constCS import *
from rpyc.utils.server import ForkingServer

# Classe que herda de 'rpyc.Service'
class herdar(rpyc.Service):

    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mult(self, a, b):
        return a * b
    
    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Não pode divisão por zero"
    
    def potenc(self, a, b):
        return a ** b

# inicia o servidor rpyc
if __name__ == "__main__":
    server = ForkingServer(herdar(), port=PORT, protocol_config={'allow_public_attrs': True})
    server.start()
