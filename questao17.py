#Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas. A fórmula de 
#conversão é: P = C/2,54, sendo C o comprimento em centímetros e P o comprimento em polegadas

centimetros = float(input("Informe um valor para conversão de centimetros para polegadas: "))
 
polegadas = centimetros/2.54
print(f"A conversão de centimetros para polegadas é: {polegadas}polegadas")
