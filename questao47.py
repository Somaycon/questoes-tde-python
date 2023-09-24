numero = int(input("Digite um numero de 4 digitos de 1000 a 9999: "))
if numero >= 1000 and numero <= 9999:
    numero = str(numero)
    for letra in numero:
        print(letra)
else:
    print("numero não entra em 1000 a 9999 ")