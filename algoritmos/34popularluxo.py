print("Bem vindo(a) a AlugaCar! Você realizou um aluguel conosco e iremos lhe passar o orçamento final.")
print("Responda abaixo de acordo com o serviço realizado.")
print("1- Carro Popular")
print("2- Carro de Luxo")
servico = int(input("Qual foi o modelo do serviço realizado? "))

if servico == 1:
    print("Ok! Você alugou um Carro Popular, agora iremos te passar algumas informações.")
    print("A diária de um Carro Popular custa R$90,00 a diária.")
    print("Até 100Km percorridos: R$0,20 por Km")
    print("Acima de 100Km percorridos: R$0,10 por Km")
    dias_popular = int(input("Quantos dias você ficou com nosso veículo? "))
    valor_dias = dias_popular * 90
    km_popular = float(input("Quantos Km foram percorridos durante este período? "))
    if km_popular <= 100:
        valor_km = km_popular * 0.20
    else:
        valor_km = km_popular * 0.10
    valor_final = valor_dias + valor_km
    print(f"O valor final de todo serviço ficou em R${valor_final:.2f}")

else:
    print("Ok! Você alugou um Carro de Luxo, agora iremos te passar algumas informações.")
    print("A diária de um Carro de Luxo custa R$150,00 a diária.")
    print("Até 100Km percorridos: R$0,30 por Km")
    print("Acima de 100Km percorridos: R$0,25 por Km")
    dias_luxo = int(input("Quantos dias você ficou com nosso veículo? "))
    valor_dias = dias_luxo * 150
    km_luxo = float(input("Quantos Km foram percorridos durante este período? "))
    if km_luxo <= 100:
        valor_km = km_luxo * 0.30
    else:
        valor_km = km_luxo * 0.25
    valor_final = valor_dias + valor_km
    print(f"O valor final de todo serviço ficou em R${valor_final:.2f}")