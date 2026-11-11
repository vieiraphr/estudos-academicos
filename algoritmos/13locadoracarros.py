print("Bem vindo a AlugaCar! Para continuarmos seu processo primeiro preciso de alguns dados, vamos lá?")

nome = input("Primeiro me diga. Qual é o seu nome? ")
carro = input(f"Perfeito {nome}! Agora me diga o carro foi realizado a locação: ")
print(f"Excelente escolha, {nome}! O {carro} é um excelente veículo.")

km = float(input("Ao pegar o veículo, qual era a kilometragem marcada em seu painel? ").replace(".", "").replace(",", "."))
km_final = float(input("E durante a devolução do veículo para a locadora o valor marcado em seu painel era? ").replace(".", "").replace(",", "."))

km_emhaver = km_final - km
km_valor = km_emhaver * 0.20

dias = int(input("Entendido! E quantos dias foram no total de locação? "))
valor_dias = dias * 90

valor_total = valor_dias + km_valor

print(
    f"Muito obrigado, {nome}, após essas informações verificamos que com o valor de R${km_valor:.2f} "
    f"referente à kilometragem utilizada do veículo mais R${valor_dias:.2f} referente aos dias de locação. "
    f"O valor total ficou em R${valor_total:.2f}."
)