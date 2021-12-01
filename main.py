# classe principal
# import - importa funções, variáveis, classes de outros arquivos

# de /model/cliente.py importe Cliente (é uma classe)
from model.cliente import Cliente

# carrega o arquivo do diretório /model/cliente_dao.py
# e define um apelido chamado funcoes_clientes para prover 
# acesso as funções definidas no arquivo importado
import model.cliente_dao as funcoes_clientes

# adiciona vários clientes
for i in range(0, 15):
    novo_cliente = Cliente(i, f'Cliente-{i}', 'rua a', '75 9 8888888')
    funcoes_clientes.adicionar(novo_cliente)

funcoes_clientes.listar_todos()



