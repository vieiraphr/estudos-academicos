primeiro_numero = int(input("Digite um número:"))
segundo_numero = int(input("Digite outro número:"))

if primeiro_numero > segundo_numero:
    print ("O primeiro valor é o maior!")
elif segundo_numero > primeiro_numero:
    print ("O segundo valor é o maior!")
else:
    print("Não existe valor maior ou menor, ambos são iguais!")
