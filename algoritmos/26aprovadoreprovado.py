nota1 = float(input("Digite a primeira nota: ").replace(",", "."))
nota2 = float(input("Digite a segunda nota: ").replace(",", "."))

if nota1 > 10 or nota2 > 10:
    print("Erro: as notas devem ser no máximo 10.")
else:
    media = (nota1 + nota2) / 2
    print(f"A média entre {nota1} e {nota2} é igual a: {media:.2f}")

    if media <= 4.9:
        print("Reprovado")
    elif media <= 6.9:
        print("Recuperação")
    else:
        print("Aprovado")