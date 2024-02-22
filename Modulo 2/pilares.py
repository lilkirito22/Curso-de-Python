# Definição da classe Animal (abstração)
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):  # Método genérico para todos os animais
        pass

    def mover(self):  # Método genérico para todos os animais
        pass

# Definição da subclasse Cachorro (herança)
class Cachorro(Animal):
    def fazer_som(self):  # Polimorfismo: Cada animal faz um som diferente
        return "Au au!"

    def mover(self):  # Polimorfismo: Cada animal se move de uma forma diferente
        return "Correndo"

# Definição da subclasse Gato (herança)
class Gato(Animal):
    def fazer_som(self):  # Polimorfismo: Cada animal faz um som diferente
        return "Miau!"

    def mover(self):  # Polimorfismo: Cada animal se move de uma forma diferente
        return "Andando"

# Função para demonstrar o polimorfismo
def fazer_barulho(animal):
    print(animal.nome + " faz " + animal.fazer_som())

# Função para demonstrar a herança e polimorfismo
def mover_animal(animal):
    print(animal.nome + " está " + animal.mover())

# Criando instâncias das classes
cachorro = Cachorro("Rex")
gato = Gato("Whiskers")

# Chamando as funções para demonstrar o polimorfismo
fazer_barulho(cachorro)
fazer_barulho(gato)

# Chamando a função para demonstrar a herança e polimorfismo
mover_animal(cachorro)
mover_animal(gato)
