# Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida
# em km/h (quilômetros por hora). A fórmula de conversão é: K = M ∗3.6, sendo K a velocidade em km/h e M em m/s.

velocidade_ms=float(input("Informe um valor para a velocidade: "))

velocidade_kmh=velocidade_ms*3.6
print(f"A velocidade em km/h é: {velocidade_kmh}km/h")
