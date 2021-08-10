'''
Questão 3 (3 pontos) Faça um algoritmo que recebe dois números naturais m e n e determine todos os pares
de números naturais x e y, com x ≤ n e y ≤ m, para os quais o valor da expressão xy − x**2 + y
seja máximo e calcule também esse máximo.

pessoal, só para dar uma esclarecida na questão 3: quando você coloca um valor em x e outro em y, 
aquela expressão passa a ser um número, certo? daí conforme os valores de x e y vão mudando, 
esse número vai aumentando ou diminuindo. De todos os números que forem gerados,
algum vai ser máximo (ou alguns, pode ser que o máximo se repita) e a ideia é justamente encontrar
todos os valores de x e y que dão esse máximo


'''


def Maximuns(ListRes):
  Reslist = []
  numberToFind = ListRes[0][0];
  for i in range(len(ListRes)):
    if(ListRes[i][0] >= numberToFind):
      numberToFind = ListRes[i][0]
  for i in range(len(ListRes)):
    if(ListRes[i][0] == numberToFind):
      Reslist.append(ListRes[i])
  return(Reslist)

def Print(ListRes):
  for i in range (len(ListRes)):
    print("O {} maximo valor e o conjunto x e y são:".format(i + 1), end=" ")
    for a in range (len(ListRes[i])):
      print(ListRes[i][a], end=" ")
    print("")

def Main():
  a, b = list(input().split(" "))
  ListRes = []
  x = int(b)
  while(x >= 0):
    y = int(a)
    while(y >= 0):
      ListRes.append([x *y - x **2 + y , x , y])
      y = y - 1
    x = x - 1
  ListRes = Maximuns(ListRes)
  Print(ListRes)

Main()
