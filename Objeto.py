class Meu_Objeto:


    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f'Chamando o Construtor {self.nome}')


    def imprime(self):
        print(f'Olá meu nome é {self.nome} e eu tenho {self.idade} anos')


