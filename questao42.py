salario_base = float(input("Digite o salario base: "))

gratificacao = 0.05*salario_base
imposto = 0.07*salario_base

salario_receber = (salario_base-imposto)+gratificacao

print("Salario a receber: ",salario_receber)