nome = str(input("Bem vindo(a) ao LifeCalculator. Qual é seu nome?"))
quant = int(input(f"Prazer, {nome}! Para continuarmos nossa simulação, me diga. Quantos cigarros você fuma por dia?"))
quantanos = int(input(f"Entendido. E há quantos anos você é fumante?"))

cigarros_totais = quant * (quantanos * 365)
minutos_perdidos = cigarros_totais * 10
dias_perdidos = minutos_perdidos / 1440

print(f"{nome}, você infelizmente perdeu aproximadamente {dias_perdidos:.2f} dias de vida ;(")