HoraInicial,MinutoInicial,HoraFinal,MinutoFinal = [int(x) for x in input().split()]
Hora = int(HoraFinal - HoraInicial)
Minuto = int(MinutoFinal - MinutoInicial)
if Hora > 0:
    if Minuto == 0:
        Minuto = 0
    elif Minuto > 0:
        pass
    else:
        Hora -= 1
        Minuto +=60
elif Hora == 0:
   if Minuto > 0:
     Hora = 0
   elif Minuto == 0:
       Hora = 24
       Minuto = 0
   elif Minuto < 0:
       Hora = 23
       Minuto+=60
else:
    Hora += 24
    if Minuto == 0:
        Minuto = 0
    elif Minuto > 0:
        pass
    else:
        Hora -= 1
        Minuto +=60

if Hora < 24 and Minuto >= 1:
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(Hora,Minuto))
if Hora == 24 and Minuto == 0:  
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(Hora,Minuto))

      
