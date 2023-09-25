# Leia um angulo em radianos e apresente-o convertido em graus. A fórmula de conversão é: G = R ∗180/π, 
#sendo G o angulo em graus e R em radianos e π = 3.14.

radianos = float(input("Informe um valor para conversão de radianos para graus: "))
 
pi=3.14
graus = radianos *180/pi
print(f"A conversão de radianos para graus é: {graus}graus")
