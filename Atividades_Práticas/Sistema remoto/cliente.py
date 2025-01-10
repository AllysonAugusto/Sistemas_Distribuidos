# módulo rpyc para conectar ao servidor
import rpyc
from constCS import *

# Conexão com o servidor
conexao = rpyc.connect(HOST, port=PORT)

a = float(input("Digite o primeiro número (a): "))

b = float(input("Digite o segundo número (b): "))


print(a, '+', b, '=', conexao.root.add(a, b))

print(a, '-', b, '=', conexao.root.sub(a, b))

print(a, '*', b, '=', conexao.root.mult(a, b))

print(a, '/', b, '=', conexao.root.div(a, b))
