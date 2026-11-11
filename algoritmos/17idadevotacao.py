nome = input("Digite seu nome: ")
print(f"Bem vindo, {nome}! Para prosseguirmos com seu cadastro para emissão de título de eleitor preciso que me informe:")

data_nascimento = int(input("Digite o ano de seu nascimento: "))
ano_atual = 2026

idade = ano_atual - data_nascimento

if idade >= 18:
    print("Você possui obrigações eleitorais (voto obrigatório).")
elif idade >= 16:
    print("Você já pode votar (voto opcional).")
else:
    print("Você ainda não pode votar.") 