idadeEmDias = int(input())

Anos = idadeEmDias//365
Meses = (idadeEmDias%365)//30
Dias = (idadeEmDias%365)%30

print("%d Ano(s)" %Anos)
print("%d Mes(es)" %Meses)
print("%d Dia(s)" %Dias)
