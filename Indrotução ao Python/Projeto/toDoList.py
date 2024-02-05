"""
To Do List

Primeira sessao sao as funções logo em seguida temos o loop com as opções para escolher, codigo bem simples mas bem estruturado e facil de entender

otima opção para primeiro programa em python para iniciantes..

"""

# Funções
def adicionar_tarefa(tarefas, nome_tarefa):

  tarefa = {"nome": nome_tarefa, "completa": False}
  tarefas.append(tarefa)

  print(f"Tarefa {nome_tarefa} adicionada com sucesso!")
  return 

def ver_tarefas(tarefas):
  print("\nLista de tarefas:")
  for indice, tarefa in enumerate(tarefas, start=1):
    status = "[✓]" if tarefa["completa"] else "[ ]"
    nome_tarfea = tarefa["nome"]
    print(f"{indice}. {status} {nome_tarfea}")

  return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):

  indice_tarefa_ajustado = int(indice_tarefa) - 1

  if int(indice_tarefa_ajustado) >= 0 and int(indice_tarefa_ajustado) < len(tarefas):
   tarefas[indice_tarefa_ajustado]["nome"] = novo_nome_tarefa
   print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")

  else:
    print("Tarefa não encontrada")
  return


def completar_tarefa(tarefas, indice_tarefa):

  indice_tarefa_ajustado = int(indice_tarefa) - 1
  tarefas[indice_tarefa_ajustado]["completa"] = True


  print(f"Tarefa {indice_tarefa} completada")

  return


def deletar_tarefas_completadas(tarefas):


  for tarefa in tarefas:
    if tarefa["completa"]:
      tarefas.remove(tarefa)

  print("Tarefas completadas deletadas")

  return

# Lista de tarefas
tarefas = []



# Loop
while True:
  print("\nMenu do To Do List")
  print("\n1 - Adicionar tarefa")
  print("2 - Ver tarefas")
  print("3 - Atualizar tarefas")
  print("4 - Completar tarefas")
  print("5 - Deletar tarefas completadas")
  print("6 - Sair")

  escolha = input("\nEscolha uma opção: ")

  if escolha == "1":
    nome_tarefa = input("Digite o nome da tarefa: ")
    adicionar_tarefa(tarefas, nome_tarefa)

  elif escolha == "2":
    ver_tarefas(tarefas)
  
  elif escolha == "3":
    ver_tarefas(tarefas)
    indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
    novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
    atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa)
  
  elif escolha == "4":
    ver_tarefas(tarefas)
    indice_tarefa = input("Digite o número da tarefa que deseja completar: ")
    completar_tarefa(tarefas, indice_tarefa)

  elif escolha == "5":
    deletar_tarefas_completadas(tarefas)
    ver_tarefas(tarefas)

  elif escolha == "6":
    break

  
print("programa finalizado")
