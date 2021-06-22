''' Nome: Luiz Lima Cezario 
 Exercio para ordenar 3 numeros do maior para o menor e do menor para o maior '''
def Principal():
  num = str(input(''))
  a,b,c = num.split(' ')
  a, b ,c =  Maior(int(a),int(b),int(c))
  print(("{} {} {}".format(a, b ,c)))
  print(("{} {} {}".format(c, b ,a)))


Principal()


def Maior(x:int , y:int, z:int) -> int:
  maior1 = max(x, y)
  menor1 = x + y - maior1
  maiorFinal = max(maior1, z)
  menor2 = maior1 + z - maiorFinal
  meioFinal = max(menor2, menor1)
  menorFinal = menor2 + menor1 - meioFinal

  return maiorFinal, meioFinal, menorFinal
  
