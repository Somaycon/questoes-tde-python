valor_total = float(input("Valor total: "))
total_a_pagar = valor_total-(valor_total*0.10)
valor_parcela = total_a_pagar/3
comissao_vendedor_a_vista = total_a_pagar-(total_a_pagar*0.10)
comissao_vendedor_parcelado = valor_total-(valor_total*0.05)

print("Total a pagar: ", total_a_pagar)
print("Valor da parcela: ", valor_parcela)
print("Comissão do Vendador a vista: ",comissao_vendedor_a_vista)
print("Comissão do Vendedor parcelado: ", comissao_vendedor_parcelado)

