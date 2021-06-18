''' Nome: Luiz Lima Cezario 
Exercicio para balanceamento de cargas para nave da alianca rebelde , entrara 4 cargas com pesos 
diferentes e o programa deve avisar se e posivel balancear elas ou nao.'''

def Balancear(carga1:int , carga2:int , carga3:int , carga4:int) -> bool:
  ''' Funcao balancea as cargas dadas por meio dos condicionais  '''
  if(carga1 == ( carga2 + carga3 + carga4)):
    return True
  elif((carga1 + carga2) == (carga3 + carga4)) :
    return True
  elif((carga1 + carga2 + carga3 ) == (carga4)):
    return True
  elif((carga1 + carga3 ) == (carga2 + carga4 )): 
    return True
  elif((carga1+ carga4 ) == (carga3 + carga2)):
    return True
  else:
    return False  

def Principal():
  carga1 = int(input())
  carga2 = int(input())
  carga3 = int(input())
  carga4 = int(input())
  balanceamento = Balancear(carga1 , carga2 , carga3 , carga4)
  if(balanceamento == True):
    print('Carga balanceável!')
  else :
    print('Não é possível balancear a carga.')

Principal()
