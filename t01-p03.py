''' Nome: Luiz Lima Cezario 
 Exercio para mostrar qunatos notas e quais notas 
 devem ser sacadas de um caixa eletronico a depender do valor inserido'''

def CedDiv(valor:int, div:int):

  res = int(valor/div) 
  newvalor = valor - div*res
  return res , newvalor

def Principal():
  valor = int(input(''))
  ced100 , valorN = CedDiv(valor, 100)
  ced50, valorN = CedDiv(valorN, 50)
  ced10 , valorN = CedDiv(valorN, 10)
  ced5 , valorN = CedDiv(valorN, 5)
  ced1 , valorN = CedDiv(valorN, 1)

  print("	Saque de {} notas:".format(ced100+ced50+ced10+ced5+ced1) )
  print( "{} notas de 1".format(ced1))
  print( "{} notas de 5".format(ced5))
  print( "{} notas de 10".format(ced10))
  print( "{} notas de 50".format(ced50))
  print("{} notas de 100".format(ced100))

Principal()
