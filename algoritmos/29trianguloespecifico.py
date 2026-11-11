reta1 = int(input("Digite o primeiro valor: "))
reta2 = int(input("Digite o segundo valor: "))
reta3 = int(input("Digite o terceiro valor: "))


if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):


    if reta1 == reta2 == reta3:
        print("As retas FORMAM um TRIÂNGULO EQUILÁTERO!")
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print("As retas FORMAM um TRIÂNGULO ISÓSCELES!")
    else:
        print("As retas FORMAM um TRIÂNGULO ESCALENO!")
else:
    print("As retas NÃO formam um triângulo.")