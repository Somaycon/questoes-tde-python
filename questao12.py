# Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de conversão é:
#K = 1,61∗ M, sendo K a distância em quilômetros e M em milhas

dist_milhas=float(input("Informe um valor para conversão de distancia em milhas para km: "))

dist_km=dist_milhas * 1.61
print(f"A conversão da distancia para km é: {dist_km} km")
