diastrabalho = int(input("numero de dias trabalhados: "))
valordia = 30.00
pagamentob = valordia * diastrabalho
imposto = 0.08 * pagamentob
pagamentol= pagamentob - imposto

print("o pagamento líquido é: R$",pagamentol)