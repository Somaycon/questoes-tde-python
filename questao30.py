valor_em_reais = float(input("Digite o valor em reais: "))

cotacao_dolar = float(input("Digite a cotação do dólar: "))

valor_em_dolares = valor_em_reais / cotacao_dolar

print(f"O valor correspondente em dólares é: {valor_em_dolares:.2f} dólares")
