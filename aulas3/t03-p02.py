''' Nome: Luiz Lima Cezario Ra:11201920808
    Esse programa serve para analisar se uma quantidade determinada pelo primeiro numero entrado se os proximos 
    fazem parte dos numeros de fibonacci 
'''
def FibonateAnalise(x:int)-> str:
  """ Esta funçao calcula os numeros de fibonacci, enquanto o numero fibonacci for menor que o
  numero dado apos comparo se os dois sao iguais se nao envio um 0  """
  i = 0 
  proximo = 1
  anterior = 0
  while(x > proximo):
    proximo = proximo + anterior
    anterior = proximo - anterior
  if(x == proximo):
    return str(proximo)
  return '0'


def Principal():
  y = int(input())
  i = 0 
  response = ''
  while(i < y):
    x = int(input())
    i += 1
    res = FibonateAnalise(x)
    if(res != '0'):
      response = response  +  res + " "
  if(response != ''):
    print(response)
  else:
    print("Sabia que era místico demais!")
  
Principal()
