print("Bem vindo ao site de alistamento militar, para prosseguir insira seus dados.")

nome = input("Nome completo: ")
idade = int(input("Idade: "))

if idade < 18:
    tempo_falta = 18 - idade
    print(f"Você ainda tem {tempo_falta} ano(s) para realizar seu alistamento militar.")

elif idade == 18:
    print("Está na hora de se alistar! Compareça à Junta Militar.")

else:
    tempo_passou = idade - 18
    print(f"Você já passou {tempo_passou} ano(s) do prazo de alistamento!")