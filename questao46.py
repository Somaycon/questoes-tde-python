numero = int(input("Digite um numero de 100 a 999: "))
if numero >=100 and numero <=999:
    numero = str(numero)
    numero_reverso = []
    for letra in numero:
        numero_reverso.append(letra)
    numero_reverso.reverse()
    numero_reverso = "".join(numero_reverso)
    numero_reverso = int(numero_reverso)
    print(numero_reverso)
else:
    print("numero não entra entre 100 a 999")