import random 
#Personagem: classe mae
#Heroi: controlado pelo usuario
#INimigo: adversario do usuario

class Personagem:
  def __init__(self, nome, vida, nivel) -> None:
    self.__nome = nome
    self.__vida = vida
    self.__nivel = nivel

  def get_nome(self):
    return self.__nome
  
  def get_vida(self):
    return self.__vida
  
  def get_nivel(self):
    return self.__nivel
  
  def exibir_Detalhes(self):
    return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}"
  
  def receber_ataque(self, dano):

      self.__vida -= dano
      if self.__vida < 0:
          self.__vida = 0


  def atacar(self, alvo):
      dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)       #baseado no nivel do jogador
      alvo.receber_ataque(dano)
      print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")

  
    
class Heroi(Personagem):
  def __init__(self, nome, vida, nivel, habilidade) -> None:
    super().__init__(nome, vida, nivel)

    self.__habilidade = habilidade

  def get_habilidade(self):
    return self.__habilidade
  
  def exibir_Detalhes(self):
    return f"{super().exibir_Detalhes()}\nHabilidade: {self.get_habilidade()}\n"
  
  def ataque_especial(self,alvo):
    dano = random.randint(self.get_nivel() *5, self.get_nivel() *7)  #Dano aumentado
    alvo.receber_ataque(dano)
    print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano")
  

class Inimigo(Personagem):
  def __init__(self, nome, vida, nivel, tipo) -> None:
    super().__init__(nome, vida, nivel)

    self.__tipo = tipo

  def get_tipo(self):
    return self.__tipo
  
  def exibir_Detalhes(self):
    return f"{super().exibir_Detalhes()}\nTipo: {self.get_tipo()}\n"
  


class Jogo:
  """Classe orquestradora do jogo"""


  def __init__(self) -> None:
    self.heroi = Heroi(nome="Daniel",vida=100, nivel=5,habilidade="Fogo" )
    self.inimigo = Inimigo(nome="Maira", vida=50, nivel=3, tipo="Cobra")
  
  def iniciar_batalha(self):
    """Fazer a gesta da batalha em turnos"""

    print("iniciando a batalha")

    while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
      print("\nDetalhes dos Personagens")
      print(self.heroi.exibir_Detalhes())
      print(self.inimigo.exibir_Detalhes())

      input("Pressione enter para atacar...")
      escolha = input("Escolha (1- Ataque Normal, 2- Ataque Especial): ")

      if escolha == '1':
        self.heroi.atacar(self.inimigo)
      elif escolha == '2':
        self.heroi.ataque_especial(self.inimigo)

      else:
          print("escolha invalida")
      
      if self.inimigo.get_vida() > 0:
        # Inimigo ataca o heroi
        self.inimigo.atacar(self.heroi)


    if self.heroi.get_vida() > 0:
      print("\nParabens, voce ganhou a batalha")
    
    else:
      print("\nVoce perdeu a batalha")


# Criar Instancia do jogo e iniciar batalha
      

jogo = Jogo()
jogo.iniciar_batalha()



   
  
  
    


