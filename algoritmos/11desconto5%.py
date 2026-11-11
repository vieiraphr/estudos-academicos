import random

while True:

    produto = random.randint(10, 100)
    desconto = produto * 0.05
    print(f"VALOR FINAL DE SEU PRODUTO: R${produto}")
    print ("VOCÊ GANHOU UM CUPOM DE 5% DE DESCONTO!!!")
    aplicar = str(input("Deseja aplicar? S/N:"))
    if aplicar == "S":
     preco_final = produto - desconto
     print (f"Parabéns! Você usou seu cupom e agora seu produto custa R${preco_final:.2f}!")
     break
    elif aplicar == "N":
     print (f"Seu produto continuará no valor de R${produto}.")
     break
    else:
     print ("Você precisa escolher uma das opções para finalizar sua compra!")

