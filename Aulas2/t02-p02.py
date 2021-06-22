''' Nome: Luiz Lima Cezario Ra:11201920808
    Esse programa serve para descobrir qual é o dia da semana com base 
    numa data qualquer no formato DD/MM/AAAA e nos textos de Gauss 
'''
def Verificacao(DD:int , MM:int , AA:int):
  ''' Esta funcao verifica se a data existe '''
  if(AA > 0 ):
    if(MM > 0 and MM <= 12):
      if(DD > 0):
        if(MM == 2 and DD <= 29):
          return True
        elif((MM == 1 or MM == 3 or MM == 5 or MM == 7 or MM == 8 or MM == 10 or MM == 12 ) and DD <= 31):
          return True
        elif((MM == 2 or MM == 4 or MM == 6 or  MM ==9 or  MM ==11 ) and DD <= 30):
          return True 
        else:
          return False     
  else:
    return False

def FindMKey(MM :int) ->int :
  ''' Aqui iremos decobrir qual é o numero chave que 
  vai representar o mes em nossa equacao final 
  essas chaves sao dadas pela tabela de Gauss '''
  if(MM == 1):
    return 28
  elif (MM == 2):
    return 31
  elif (MM == 3):
    return 2
  elif (MM == 4):
    return 5
  elif (MM == 5):
    return 7
  elif (MM == 6):
    return 10
  elif (MM == 7):
    return 12
  elif (MM == 8):
    return 15
  elif (MM == 9):
    return 18
  elif (MM == 10):
    return 20
  elif (MM == 11):
    return 23  
  elif (MM == 12):
    return 25
  
def FindAKey(AA: int )-> int:
  ''' funcao para achar a chave que representara o ano na formula de acordo com os calculos de gauss''' 
  res = 5 * (AA % 4) + 4 * (AA % 100) + 6 * (AA % 400)
  return res

def FindDay(DD:int, ChaveMes:int, ChaveAno:int)-> str:
  ''' funcao que calcula o numero entre 0 e 6 que representa os dia da semana e retorna 
  uma string para ser impressa  '''
  dia = (DD +  ChaveMes + ChaveAno) % 7
  if(dia == 0 ):
    return 'Domingo' 
  elif( dia == 1  ):
    return 'Segunda-feira'
  elif( dia == 2 ):
    return 'Terça-feira'
  elif(dia == 3 ):
    return 'Quarta-feira'
  elif( dia == 4 ):
    return 'Quinta-feira'
  elif(dia == 5 ):
    return 'Sexta-feira'
  elif( dia == 6):
    return 'Sábado'
  else:
    return 'Data inválida!'
def Principal():
  DD , MM , AAAA = input().split('/')
  verif = Verificacao(int(DD) , int(MM) ,int(AAAA))
  if(verif == True):
    ChaveMes = FindMKey(int(MM))
    if(int(MM) == 1 or int(MM) == 2): 
      AAAA = int(AAAA) - 1
      ChaveAno = FindAKey(int(AAAA))
    else:
      ChaveAno = FindAKey(int(AAAA))
    Dia = FindDay(int(DD) , ChaveMes, ChaveAno)     
  else:
    Dia = 'Data inválida!'
  print(Dia)

Principal()
