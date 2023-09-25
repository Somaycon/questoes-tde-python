#Leia um ângulo em graus e apresente-o convertido em radianos.
#A fórmula de conversão é: R = G ∗ π/180, sendo G o angulo em graus e R em radianos e π = 3.14.


graus = float(input("Informe um valor para conversão de graus para radianos: "))
 
pi=3.14
rad = graus * pi/180
print(f"A conversão de graus para radianos é: {rad}rad")



