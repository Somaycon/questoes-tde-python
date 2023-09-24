valor_premio = float(input("Digite o valor do premio: "))

valor_pessoa1 = float(input("valor pessoa1: "))
valor_pessoa2 = float(input("valor pessoa2: "))
valor_pessoa3 = float(input("valor pessoa3: "))

total_investido = valor_pessoa1+valor_pessoa2+valor_pessoa3
proporcao_pessoa1 = valor_pessoa1/total_investido
proporcao_pessoa2 = valor_pessoa2/total_investido
proporcao_pessoa3 = valor_pessoa3/total_investido

premio_pessoa1 = proporcao_pessoa1*valor_premio
premio_pessoa2 = proporcao_pessoa2*valor_premio
premio_pessoa3 = proporcao_pessoa3*valor_premio

print("Premio pessoa1: ",premio_pessoa1)
print("Premio pessoa2: ",premio_pessoa2)
print("Premio pessoa3: ",premio_pessoa3)