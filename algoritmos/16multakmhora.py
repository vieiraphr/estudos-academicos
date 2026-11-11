nome = str(input("Digite seu nome:"))
veiculo = str(input("Qual modelo de seu veículo?"))
velocidade = int(input("Velocidade máxima obtida:"))
multa = int(velocidade - 80) * 5
if velocidade > 80:
    print(f"Você deve pagar uma multa de R$ {multa:.2f}")
else:
    print("Obrigado por respeitar o limite da via!")