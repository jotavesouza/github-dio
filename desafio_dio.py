print("Escolha o número da resolução que deseja!")
print("1 - Contatenação")
print("2 - Repetir Texto")
print("3 - Operações Matemáticas")

opcao = int(input("Qual número da solução que deseja? "))

if opcao == 1:
    word1 = input("Palavra 1: ")
    word2 = input("Palavra 2: ")
    print("As palavras concatenadas são: " + word1 + " " + word2) 

elif opcao == 2:
    palavra = input("Qual a palavra escolhida? ")
    numero = int(input("Quantas vezes quer que a palavra se repita? "))
    print((palavra + ' ') * numero)

elif opcao == 3:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    operacao = input("Escolha a operação que deseja (+,-,*,/): ")
    if operacao == '+':
        print(num1 + num2)
    elif operacao == '-':
        print(num1 - num2)
    elif operacao == '*':
        print(num1 * num2)    
    elif operacao == '/':
        print(num1 / num2)
    else:
        print("Escolha um operador válido!!")

else:
    print("Escolha um número entre as opções!!")