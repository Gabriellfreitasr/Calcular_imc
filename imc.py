peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Qual a sua altura: "))

imc = peso // (altura * altura)

print(f"O seu IMC é de {imc}")
