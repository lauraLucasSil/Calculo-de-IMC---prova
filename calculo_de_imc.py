try:
    nome = input("Digite seu nome: ")
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite sua altura: "))
    
    imc = peso / (altura * altura)

    print(f"Seu IMC é: {imc: .2f}")

    if imc <= 18.5:
        print(f"{nome}, você está Abaixo do Peso.")
    elif imc <= 24.9:
        print(f"{nome}, você está com Peso Normal.")
    elif imc <= 29.9:
        print(f"{nome}, você está com Sobrepeso.")
    elif imc <= 34.9:
        print(f"{nome}, você está com Obesidade Grau I.")
    elif imc <= 39.9:
        print(f"{nome}, você está com Obesidade Grau II.")
    elif imc >= 40.0:
        print(f"{nome}, você está com Obesidade Grau III (mórbida).")
    else:
        print(f"{nome}, seu IMC é igual a {imc:.2f}. ✅ TUDO OK ✅")

except ValueError:
    print("Erro: Por favor, digite apenas números válidos para peso e altura.")
except ZeroDivisionError:
    print("Erro: A altura não pode ser zero.")

with open ("cadastro_imc.txt", "a") as arquivo:
    arquivo.write(f"Nome: {nome}\nIMC:{imc:.2f}")
    arquivo.write("\n-----------------------------------")