''' Nome: Luiz Lima Cezario Ra:11201920808
    Esse programa serve para calcular o valor de um numero na base N entre as base de 2 a 10 e transformar ele em um numero de base 10     
'''
  
def TransformBase(base:int, number:list, digts:int) -> int :
  """ Esta Funcao recebe uma base um numero e o numero de digitos desse mesmo, usando essas informacoes ela troca a base do numero que esta na base dada
   para a decimal, usamos o numero em lista pois se o numero passa de 16 digitos os inteiros perder sua precisao e acabava dando erro  """
  i = 0
  res = 0
  while ( i < digts):
    index = digts - i - 1
    number[index] = int(number[index]) * (base ** i) 
    res += number[index]
    i += 1
  return  res


def Principal():
  base = int(input())
  number = list(input())
  digts = int(input())
  if(base >= 2 and base <= 10):
    changedNumber = TransformBase(base, number, digts)
    print(changedNumber)
  else:
    print("Base Invalida")


Principal()
# 9
# 13210548765215045
# 17
# 2519163320484011
# 7
# 231654454621324621
# 18
