numeros = input().split()
A = int(numeros[0])
B = int(numeros[1])
C = int(numeros[2])
D = int(numeros[3])

if(B > C and D > A and C+D > A+B and C > 0 and D >0 and A%2 ==0 ):
  print("Valores aceitos")
else:
  print("Valores nao aceitos")