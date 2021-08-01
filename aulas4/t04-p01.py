# GGAGGGAGAA = CCUCGCUGAA
# AAGAGGAAGAGGGAGGGAAG =AACUCGUUCAGCGAGGCUAG

def ChangeLetters(tochange:list):
  for i in range(len(tochange)):
    if(tochange[i] == 'C'):
      tochange[i] = 'G'
    elif(tochange[i] == 'U'):
      tochange[i] = 'A'
    i = i + 1
  return tochange

def Comparar(mRNA : list , oligo: list):
  a = 0;
  for i in range(len(mRNA)):
    if(mRNA[a + i] == oligo[a]):
      if(a == range(len(oligo))):
        return i 
      a = a + 1
    else:
      i = i + 1;
      a = 0;
  return -1

def Inverter(x : list):
  for i in range(len(x)):
    y = len(x) - i -1
    x[i] = x[y]
    
  return x 

def Principal():
  mRNA = list(input())
  oligo = list(input())
  oligo = Inverter(oligo)
  mRNA = ChangeLetters(mRNA)
  oligo = ChangeLetters(oligo)
  compar = Comparar(mRNA, oligo)
  if(compar != -1):
    print("Silenciado em %i", compar)
  else :
    print("Não silenciado")
    
 
Principal()
