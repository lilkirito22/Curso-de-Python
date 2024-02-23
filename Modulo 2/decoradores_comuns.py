# @classmethod
#@staticmethod


class MinhaClasse:
  valor = 10 # Atributo de classe 

  def __init__(self, nome) -> None:
    self.nome = nome #atributo da instancia
  #requer uma instancia para ser chamado
  def metodo_instancia(self):
      return f"metodo de instancia chamado para {self.nome}"
  @classmethod
  def metodo_classe(cls):
     return f"metodo de classe chamado para valor={cls.valor}"
  
  
  @staticmethod
  def metodo_estatico():
     return "metodo estico chamado"
     


obj = MinhaClasse(nome="claudio")
print(obj.metodo_instancia())
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())



class Carro:
   def __init__(self, marca, modelo, ano) -> None:
      
      self.marca = marca
      self.modelo = modelo
      self.ano = ano

   @classmethod
   def criar_carro(cls, configuracao):
      marca,modelo,ano = configuracao.split(",")
      return cls(marca,modelo, int(ano))
      


configuracao1 = "Toyota,corolla,2022"
carro1 = Carro.criar_carro(configuracao1)

print(f"marca:{carro1.marca}\nModelo: {carro1.modelo}\nAno:{carro1.ano} ")
   
  