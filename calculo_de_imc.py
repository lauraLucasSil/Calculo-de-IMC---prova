nome = (input("Digite seu nome: "))
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

print(f"Seu IMC é: {imc: .2f}")


if 18.5 >= imc:
    print (f"{nome} Você está Abaixo do Peso ")

elif imc >=18.5 and imc <= 24.9:
    print (f"{nome} Você está com Peso Normal ")

elif imc >=25.0 and imc <= 29.9:
    print (f"{nome} Você está Sobrepeso ")

elif imc >=30.0 and imc <= 34.9:
    print (f"{nome} Você está com Obesidade Grau I ")

elif imc >=35.0 and imc <= 39.9:
    print (f"{nome} Você está com Obesidade Grau II ")

elif imc >= 40.0 :
    print (f"{nome} Você está com Obesidade Grau III (mórbida) ")

else:
    print (f"{nome} seu imc é igual a{imc: .2f}.       ✅ TUDO OK ✅")

