# Escrever um programa que armazene as informações de três carros
# e apresente-as na tela para o usuário

class Carro:
    def __init__(self, modelo, ano, placa, marca, cor): # método construtor
        self.modelo = modelo # declaração de atributo e atribuição de um valor
        self.ano = ano # variáveis de instância 
        self.placa = placa 
        self.marca = marca
        self.cor = cor
    def __str__(self):
        return f'{self.modelo} da empresa {self.marca}, ano {self.ano}, cor {self.cor} e placa {self.placa}'

Clio= Carro('Clio', 2015,'ABC1234','Renault','Cinza')# instanciamento de um objeto
Classic = Carro('Classic', 2015,'BCF2345','Chevrolet', 'Vermelho')
Fiesta = Carro('Fiesta', 2002,'GHJ3456', 'Ford', 'preto')
Fusca = Carro('Fusca', 1991,'HJK6897','Volksvagen', 'branco')

print(Clio)
print(Classic)
print(Fiesta)

print(f'Cor carro 2: {Classic.cor}')
print(f'Marca do carro 3: {Fiesta.marca}')