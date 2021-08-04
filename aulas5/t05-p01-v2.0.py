'''
Nesse Programa o objetivo era de criar um contador de pontos para o jogo Fruit Crush
no caso a pessoas escolhe dentre um tabuleiro cheio de frutas uma posicao apartir dessa posicao 
a sua pontuacao sera gerada pelo numero de casas de frutas iguais que estiverem conectadas
no caso desse programa v2 acorreu devido ao meu entendimento errado da questao no problema 
ele so queria que verificasemos as frutas iguais que estiverem na mesma linha e coluna da 
jogada da pessoa, porem esse meu programa uma um tipo de algoritmo de back-tracking, para 
ver literalmente todas as futas que tiverem conectadas apartir da casa escolhida pelo jogador.
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

def LoopingRow(game: list[int] , row: int, col: int, Score: int)-> int:
  '''Esta funcao tem a responsabilidade de verificar se a fruta que foi escolhida na jogada
  existe mais delas em contato com a da fruta a qual esta na casa de linha row e coluna col
  caso existe ele vai somando qunatas sao essas frutas, alem disso ele verifica se nas casas adjasentes existe 
  mas frutas iguais em cima e em baixo caso exista ele chama novamente essa funcao soque agora com as coordenadas 
  daquela fruta encontrado acima ou abaixo fazendo com que ele vai procurando ao redor de toda fruta encontrada
  e para nao verificar casas ja encontradas substituimos as frutas por "X". 
   '''
  a = 0
  fruit = game[row][col]
  while(game[row][col - a] == fruit):
    Score = Score + 1
    game[row][col - a] = "X"
    if(LoopingCol(game, row + 1, col - a, fruit) == True):
      Score = LoopingRow(game, row + 1, col - a, Score )
    if(LoopingCol(game, row - 1, col - a, fruit) == True):
      Score = LoopingRow(game, row - 1, col - a, Score )
    a = a + 1
  a = 1
  while(game[row][col + a] == fruit):
    Score = Score + 1
    game[row][col + a] = "X"
    if(LoopingCol(game, row + 1, col + a, fruit) == True):
      Score = LoopingRow(game, row + 1, col + a, Score)
    if(LoopingCol(game, row - 1, col + a, fruit) == True):
      Score = LoopingRow(game, row - 1, col + a, Score)
    a = a + 1
  return Score


def LoopingCol(game: list[int], row:int , col: int, fruit: int)-> bool:
  ''' Essa funcao tem a responsabilidade de me falar se nao chegamos a borda do game 
  e se existe uma fruta na posicao que mandaram ela cai ser usada para saber se 
  existe frutas acima ou abaixo da posicao atual caso exista retorna true'''
  if(game[row][col] == fruit and len(game) - 1 > row ):
    return True
  return False


def  PrintGameEnd(game: list[int], row: int, col:int):
  ''' Esta funcao so tem a funcao de imprimir nossa tabela final'''
  for i in range(0, col):
    print("=",end="")
  print("")
  for i in range(0 , row):
    for o in range(0 , col):
      print(game[i][o],end="")
    print("")
  for i in range(0, col):
    print("=",end="")
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
    Score = LoopingRow(game, int(I) - 1 , int(J) - 1 , 0)
    for i in range(0, int(N)):
      print("=",end="")
    print("")
    print("Score:",Score ** 2)
    PrintGameEnd( game , int(M), int(N))
Main()
