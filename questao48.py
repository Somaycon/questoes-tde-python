valor_segundos = int(input("Valor em segundos: "))
hora = 0
minuto = 0
segundo = 0
while valor_segundos>=3600:
    hora+=1
    valor_segundos-=3600
while valor_segundos>=60:
    minuto+=1
    valor_segundos-=60
segundo = valor_segundos

print(hora,"horas",minuto,"minutos",segundo,"segundos")
