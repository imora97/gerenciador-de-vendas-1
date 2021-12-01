# Padrão DAO (Data Access Object) 
# Centraliza o acesso aos dados dos objetos cliente

#lista que irá armazenar todos os clientes do sistema
lista_clientes = []

# Adcionar novo cliente
def adicionar(novo_cliente):
    lista_clientes.append(novo_cliente)

# Editar cliente - Dado um objeto cliente, buscar na 
#lista através do seu ID e atualizá-lo
def editar(cliente):
    pass
    
# Excluir cliente - Dado o ID do cliente, removê-lo da lista
def excuir(id_cliente):
    pass

# Listar todos os cliente
def listar_todos():
    # passa por todos os clientes da lista e 
    # chama a função imprime() desses objetos
    for cliente in lista_clientes:
        cliente.imprime()

# Listar um cliente específico
# Dado o ID do cliente, imprimir seus dados
def lista_cliente(id):
    pass