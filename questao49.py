hora = int(input("Digite as horas: "))
minuto = int(input("Digite os minutos: "))
segundo = int(input("Digite os segundos: "))

duracao = int(input("Duração em segundos: "))

while duracao>=3600:
    hora+=1
    duracao-=3600

while duracao>=60:
    minuto+=1
    duracao-=60

segundo += duracao
while segundo>=60:
    minuto+=1
    segundo-=60

print("Termino:",hora,"horas",minuto,"minutos",segundo,"segundos")
