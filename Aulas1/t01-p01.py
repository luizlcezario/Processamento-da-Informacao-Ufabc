''' Nome: Luiz Lima Cezario 
 Exercio para gerar a Circunferencia de um planeta medindo em KM e em Estadios 
 '''

def Calculator(Dis :float, Ang:float):
  CircunEs =  float(Dis * (360 / Ang))
  CircunKm = CircunEs * 0.1764
  return CircunEs , CircunKm

def Principal ():
  DistanciaEs = float(input())
  AnguloGrau = float(input())
  CircunEs , CircunKm = Calculator(DistanciaEs,AnguloGrau)
  print ("%.1f" % CircunEs)   
  print( "%.1f" % CircunKm) 

Principal()
