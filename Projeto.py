print("Minha primeira calculadora")

print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Multiplicação e divisão")
print("6. Adição e subtração")

opcao = int(input("Escolha uma opção: "))
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))

if opcao == 1:
    resultado = x + y 
elif opcao == 2:
    resultado = x - y
elif opcao == 3:
    resultado = x * y
elif opcao == 4:
    resultado = x / y
elif opcao == 5:
    u = int(input("Digite o número para divisão: "))
elif opcao == 6: 
    u = int(input("Digite outro número para a subtração"))

    if u != 0 and x > u and y > u:
        resultado = x+y-u
    else: "resultado inválido pois y e x > u"

    if u != 0 and x > u:
        resultado = x * y / u
    else:
        resultado = "Não foi possível realizar a operação."
else:
    resultado = "Opção inválida."



print(resultado)