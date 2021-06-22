''' Nome: Luiz Lima Cezario Ra:11201920808
    Esse programa serve para calcular o valor de um estacionamente a depende do tempo 
    dentro de um shopping sendo os valores : 
    ___________________________________________________
    |	Até 15 minutos  |	R$ 5,00                   |	
    |	De 16 minutos a |	1 hora	R$ 15,00          |	
    |	De 2 a 4 horas	|	R$ 4,00 por hora adicional|	
    |	5 horas ou mais	|	R$ 3,00 por hora adicional|
    
'''
def CalcValEstac(tempoGastoMinutos:int)-> int:
    ''' esta funcao verifica quantos minutos a pessoa ficou no estacionamento e calcula 
        quanto sera cobrado de acordo com a tabela acima  '''
    if(tempoGastoMinutos <= 15 ):
        return 5
    elif(tempoGastoMinutos <= 60):
        return 15
    elif(tempoGastoMinutos <= 240):
        valorA = (tempoGastoMinutos - 60 ) / 60 
       
        if(valorA % 1 == 0):
            return 15 + 4 * int(valorA)           
        else:
            teste = int(valorA) + 1
            return 15 + 4 * teste 
    elif(tempoGastoMinutos > 240):
        valorA = (tempoGastoMinutos - 240 ) / 60
        if(valorA % 1 == 0):
            return 27 + 3 * int(valorA) 
        else:
            teste = int(valorA) + 1
            return 27 + 3 * teste
          
    
    

def CalcularTempo(entrH:int , entrM:int, saidaH:int , saidaM:int)->int:
    ''' esta funcao transforma as horas em minutos e faz a subtracao do total de minutos no
        horario da chegada e do total de minutos no horario da saida '''
    entrEmMinutos = entrM + (entrH * 60 )
    saidaEmMinutos = saidaM + (saidaH * 60)
    DiferencaMinutos = saidaEmMinutos - entrEmMinutos
    return DiferencaMinutos
    
def Principal():
    mesada = float(input())
    entrH , entrM = input().split(':')
    saidaH , saidaM = input().split(':')
    tempoGastoMinutos = CalcularTempo(int(entrH) , int(entrM), int(saidaH) , int(saidaM))
    precoAPagar = CalcValEstac(tempoGastoMinutos)
    novaMesada = mesada - precoAPagar
    print("Você pode gastar até R$ %.2f" % novaMesada)


Principal()
