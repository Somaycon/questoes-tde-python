#Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula de conversão é: L = 
#K/0,45, sendo K a massa em quilogramas e L a massa em libras.

kg = float(input("Informe um valor para conversão de quilogramas para libras: "))
 
libras = kg/0.45
print(f"A conversão de quilogramas para libras é: {libras} lib")
 
