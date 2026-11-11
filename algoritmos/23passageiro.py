distancia = float(input("Qual distância você deseja percorrer? (Km): "))

if distancia <= 200:
    preco_km = 0.50
else:
    preco_km = 0.45

valor = distancia * preco_km

print(f"Após cálculos, a sua passagem final ficará no valor de R${valor:.2f}")