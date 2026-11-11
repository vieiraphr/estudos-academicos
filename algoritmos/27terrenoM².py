largura = float(input("Digite a largura (m): "))
comprimento = float(input("Digite o comprimento (m): "))

area = largura * comprimento

print(f"A área do terreno é {area:.2f}m²")

if area < 100:
    print("TERRENO POPULAR")
elif area <= 500:
    print("TERRENO MASTER")
else:
    print("TERRENO VIP")