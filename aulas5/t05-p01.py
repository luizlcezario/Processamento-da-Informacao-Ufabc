'''
  Nome: Luiz Lima Cezario Ra:11201920808
  Nesse Programa o objetivo era de criar um contador de pontos para o jogo Fruit Crush
  no caso a pessoas escolhe dentre um tabuleiro cheio de frutas uma posicao apartir dessa posicao 
  a sua pontuacao sera gerada pelo numero de casas de frutas iguais que estiverem conectadas
  a fruta na mesma linha e coluna.
 
  Entrada: 
    Para a entrada deve se colocar primeiro o numero de linhas do tabuleiro depois o de colunas,
  depois o numero da linha e da coluna da jogada respectivamente 
  exemplo:
11 11 7 4
3 1 4 4 0 0 3 0 0 0 0
3 1 2 4 3 3 3 3 5 5 2
0 5 4 4 1 3 0 0 3 1 1
1 4 5 4 1 5 4 5 3 1 0
5 4 2 4 5 5 0 3 5 4 0
4 1 1 4 2 2 2 1 1 2 3
1 0 4 4 4 1 2 3 0 5 5
2 0 4 4 0 1 3 2 2 1 4
1 0 4 4 1 3 3 1 1 4 1
5 0 3 4 2 0 5 2 5 5 0
1 4 0 4 1 0 3 0 2 2 5
'''
def LoopingRow(game: list[int], row: int, col: int, fruit: int)->int:
  '''
  Esta funcao tem a responsabilidade de verificar se tem mais frutas iguais a da 
  casa escolhida conectadas a ela na mesma linha se tiver trocamos por X. 
  '''
  Score = 0
  a = 0
  while(col - a >= 0 and game[row][col - a] == fruit):
    Score = Score + 1
    game[row][col - a] = "X"
    a = a + 1
  a = 1
  while(col + a < len(game[row])  and game[row][col + a] == fruit  ):
    Score = Score + 1
    game[row][col + a] = "X"
    a = a + 1
  return Score

def LoopingCol(game: list[int] , row: int, col: int, fruit: int)-> int:
  '''Esta funcao tem a responsabilidade de verificar se tem mais frutas iguais a da 
  casa escolhida conectadas a ela na mesma coluna se tiver trocamos por X. 
  '''
  a = 1
  Score = 0
  while(row - a >= 0 and game[row - a][col] == fruit  ):
    Score = Score + 1
    game[row - a][col ] = "X"
    a = a + 1
  a = 1
  while(len(game) > row + a and game[row + a][col] == fruit ):
    Score = Score + 1
    game[row + a][col ] = "X"
    a = a + 1
  return Score



def  PrintGameEnd(game: list[int], row: int, col:int):
  ''' Esta funcao so tem a funcao de imprimir nossa tabela final'''
  for i in range(row):
    print("=",end="")
  print("")
  for i in range(row):
    for o in range(col):
      print(game[i][o],end="")
    print("")
  for i in range(row):
    print("=",end="")
  print("")
  return
def Main():
  M,N,I,J = input().split(" ")
  Score = 0
  game = []
  for a in range(0, int(M)):
    linha = []
    linha = list(input().split(" "))
    game.append(linha)
  if(int(M) >= 1 and int(N) <= 50 and int(I) >= 1 and int(I)  <= int(M)  
  and int(J) >= 1 and int(J) <= int(N) ):
    fruit = game[int(I) - 1][int(J) - 1]
    Score = LoopingRow(game, int(I) - 1 , int(J) - 1 , fruit)
    Score = Score + LoopingCol(game, int(I) - 1 , int(J) - 1 , fruit) 
    for i in range(0, int(N)):
      print("=",end="")
    print("")
    print("Score:",Score ** 2)
    PrintGameEnd( game , int(N), int(M))
Main()


"""
20 15 13 15
6 5 1 5 7 0 1 4 3 5 1 5 5 4 4
3 3 4 2 0 7 0 0 4 7 2 0 1 5 4
2 3 1 3 0 1 4 2 5 7 7 6 4 4 2
1 0 6 5 2 6 4 2 6 1 1 1 1 2 6
5 4 2 6 0 2 7 4 4 5 3 4 3 0 0
6 1 0 4 6 2 2 3 4 1 4 5 2 5 0
0 2 4 7 7 4 5 0 0 1 5 4 5 0 4
6 6 5 7 7 3 1 5 6 5 6 2 3 0 7
3 0 1 7 3 2 4 0 2 4 1 7 0 7 7
4 5 6 7 3 0 5 4 5 3 2 3 6 5 3
5 0 4 7 7 7 1 3 7 3 0 0 2 0 7
1 5 4 7 6 0 0 3 4 5 7 6 1 5 3
4 2 3 7 1 3 7 2 6 6 5 6 7 7 7
6 1 4 7 0 2 3 0 6 7 6 5 6 7 2
1 3 4 5 4 6 0 3 0 6 2 6 5 1 5
4 7 6 0 2 7 2 5 7 0 5 5 5 3 4
7 4 0 4 1 4 2 1 7 2 0 1 0 5 2
6 1 2 4 1 4 3 3 2 3 4 7 0 1 2
5 1 6 5 5 0 1 7 1 0 1 1 2 2 6
4 0 7 6 4 0 3 0 4 5 3 0 4 3 1

"""
