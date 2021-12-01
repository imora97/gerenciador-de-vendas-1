# Descrição: Classe Cliente
# Contém os atributos (dados) do cliente

class Cliente():
    def __init__(self, id, nome, endereco, telefone):
        #atributos da classe
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
    
    #função da minha classe
    # imprime os dados do cliente 
    def imprime(self):
        print(f'{self.id}, {self.nome}, {self.endereco}, {self.telefone}')
