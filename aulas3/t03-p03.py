''' Nome: Luiz Lima Cezario Ra:11201920808
    Este programa analisa o dano em uma partida de Viddeogame onde vc entra com todos os danos causados na partida 
    e depois de 2 rounds quem foi vencedor para isso e so entra com os danos que o personagem ryu deu com valores positivos e 
    os danos do personagem ken como valores negativos no final quem ganahr mais rounds ganharam a luta acabado digitando 0 
'''
def CalculateDamage(ryu:int , ken:int , damage:int, RoundCounter:int)->int:
  """ Esta funcao verifica se o ryu levou o nao dano e se sua vida esta abaixo de zero, se estiver adiciona ao contador 
  no final se o contador for positvo ryu tera vencido se for 0 empate e negativo ken tera vencido"""
  if(damage < 0):
    ryu += damage

    if(ryu <= 0):
      RoundCounter -= 1
      ryu = 100
      ken = 100
  else:
    ken -= damage
    if(ken <= 0):
      
      RoundCounter += 1
      ryu = 100
      ken = 100
  return ryu, ken, RoundCounter


def Principal(): 
  endF = True
  ryu=100
  ken=100
  RoundCounter = 0
  while endF:
    damage = int(input())
    ryu, ken,RoundCounter  = CalculateDamage(ryu , ken , damage , RoundCounter)
    if(damage == 0):
      endF = False
  if(RoundCounter >= 1):
    print('Ryu venceu')
  elif(RoundCounter <= -1):
    print('Ken venceu')
  elif(RoundCounter == 0):
    print('Houve empate')
 
Principal()
