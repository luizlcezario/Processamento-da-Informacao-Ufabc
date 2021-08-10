'''
Questão 4 (2.5 pontos) O tabuleiro do jogo de campo minado consiste em uma matriz de
N linhas e M colunas. Cada célula da matriz contém uma mina ou o número de minas
que existem nas células adjacentes a ela. Uma célula é adjacente a outra se estiver
imediatamente à esquerda, à direita, acima ou abaixo da célula. Note que, se não contiver
uma mina, uma célula deve obrigatoriamente conter um número entre 0 e 4, inclusive.
Faça uma função que recebe a matriz de minas, recebe suas dimensões, e que devolve a
matriz contendo o tabuleiro do jogo.
A matriz de minas tem dimensões N × M (com 1 ≤ N, M ≤ 1000), e a posição (i, j)
contém 1 se existe uma mina nessa posição ou contém 0 caso contrário.
A matriz do tabuleiro também deve ter dimensões N × M e deve conter o caractere ‘*’
nas posições que contêm minas ou um caractere entre 0 e 4 nas posições que não contêm
minas, indicando o número de minas das células adjacentes.
Veja um exemplo de matriz de minas (esquerda) e de matriz do tabuleiro (direita) abaixo.


Minas    
0 0 1 1 0 0 1
0 1 0 1 0 0 1 
0 0 1 0 1 0 0
1 1 0 1 0 0 1
0 1 0 1 0 0 0
0 0 1 0 1 0 1
Tabuleiro
0 2 * *
1 * 4 *
1 3 * 3
* * 3 *

'''

def CreateTable(Minas: list[int], row :int, col: int):
  Table = []
  for i in range(0, row):
    line = [] 
    for a in range(0, col):
      if(Minas[i][a] == "0"):
        num = 0
        if(i > 0 and Minas[i - 1][a] == "1"):
          num = num + 1
        if(i < row - 1 and Minas[i + 1][a] == "1"):
          num = num + 1
        if(a > 0 and Minas[i][a - 1] == "1"):
          num = num + 1
        if(a < col - 1 and Minas[i][a + 1] == "1"):
          num = num + 1
        line.append(num)
      elif(Minas[i][a] == "1"):
        line.append("*")
    Table.append(line)
  return Table


def  PrintTable(game: list[int], row: int, col:int):
  for i in range(row):
    print("=",end="")
  print("")
  for i in range(row):
    for o in range(col):
      print(game[i][o],end=" ")
    print("")
  for i in range(row):
    print("=",end="")
  print("")

def Main():
  row ,col = input().split(" ")
  Minas = []
  if(row >= "1" and row <= "1000" and col >= "1" and col <= "1000"):
    for a in range(0, int(row)):
      linha = []
      linha = list(input().split(" "))
      Minas.append(linha)
    Tabluleiro = CreateTable(Minas, int(row) , int(col))
    PrintTable(Tabluleiro,int(row) , int(col))
  else:
    print("digite numero de colunas e linhas entre 1 e 1000")

Main()
