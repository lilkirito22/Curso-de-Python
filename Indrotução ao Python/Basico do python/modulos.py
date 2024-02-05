import math
try:
 numero = input("Digite um número: ")
 raiz_quadrada = math.sqrt(int(numero))
 print(f"A raiz quadrada de {numero} é {raiz_quadrada}")

except ValueError as e:
  print(f"Erro: {e}")
  print("Por favor, digite um número válido")