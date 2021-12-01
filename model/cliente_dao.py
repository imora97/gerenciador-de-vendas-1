# Padrão DAO (Data Access Object) 
# Centraliza o acesso aos dados dos objetos cliente

#lista que irá armazenar todos os clientes do sistema
lista_clientes = []

# adcionar novo cliente
def adicionar(novo_cliente):
    lista_clientes.append(novo_cliente)

# editar cliente
def editar():
    pass
    
# excluir cliente
def excuir():
    pass

# listar todos os cliente
def listar_todos():
    # passa por todos os clientes da lista e 
    # chama a função imprime() desses objetos
    for cliente in lista_clientes:
        cliente.imprime()

# pegar um cliente específico
def lista_cliente():
    pass