valores = input().split()
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])


AreaTriangulo = (A*C)/2
AreaCirculo = 3.14159*(C**2)
AreaTrapezio = ((A+B)*C)/2
AreaQuadrado = B**2
AreaRetangulo = A*B

print("TRIANGULO: %.3f" % AreaTriangulo)
print("CIRCULO: %.3f" % AreaCirculo)
print("TRAPEZIO: %.3f" % AreaTrapezio)
print("QUADRADO: %.3f" % AreaQuadrado)
print("RETANGULO: %.3f" % AreaRetangulo)