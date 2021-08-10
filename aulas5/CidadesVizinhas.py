'''
Questão 1 (peso 0.8) Considere uma matriz quadrada do tipo Lógico (contendo apenas os
valores V erdadeiro e F also) que representa conexões diretas entre até 1000 cidades de
uma região. Assim, na posição (i, j) dessa matriz haverá o valor V erdadeiro se existe uma
rodovia direta entre a cidade i e a cidade j (note que isso significa que haverá também o
valor V erdadeiro na posição (j, i)).
Faça uma função que recebe uma matriz (portanto já preenchida) dessa forma e o tamanho
da dimensão da matriz. Sua função deve ler uma cidade i e deve devolver um vetor
contendo as cidades que são vizinhas diretas da cidade i e também o tamanho desse
vetor.

0 1 2 3 4

v f v f v
f v v f v
v v v v f
f f v v f
v v f f v

'''
def FindNeiboors(Cidades, city , row):
  res = []
  i = 0
  for a in range(0, row):
    if(Cidades[city][a] == "v"):
      if(city != a):
        i = i + 1
        res.append(a)
  return(res, i)


def Main():
  row , city = input().split(" ")
  Cidades = []
  if(int(row) >= 1 and int(row) <= 1000):
    for a in range(0, int(row)):
      linha = []
      linha = list(input().split(" "))
      Cidades.append(linha)
    ResList, size = FindNeiboors(Cidades, int(city), int(row))
    print("cidades vizinhas:{} \nQuantidade de cidades: {}".format(ResList, size))
  else:
    print("digite numero de colunas e linhas entre 1 e 1000")

Main()
