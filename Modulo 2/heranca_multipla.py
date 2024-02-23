class animal:
  def __init__(self, nome) -> None:
    self.nome = nome

  def emitir_som(self):
    pass


class Mamifero(animal):
  def amamentar(self):
    return f"{self.nome} esta amamentando"
  

class Ave(animal):
  def voar(self):
      return f"{self.nome} esta voando"
  
class Aquatico(animal):
  def nadar(self):
      return f"{self.nome} esta nandando"

  
class Baleia(Mamifero, Aquatico):
  def emitir_som(self):
      return "Baleia emitem som"
  

baleia = Baleia(nome="roberto")

# Acessando metodos da classe base animal

print("Nome da baleia:", baleia.nome)
print("som da baleia", baleia.emitir_som())

# acessando meotodos das classe filhas (mamifero e aquatico)

print("Baleia amamentando", baleia.amamentar())
print("Baleia nandando", baleia.nadar())
     