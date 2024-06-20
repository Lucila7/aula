#Criando uma calculadora utilizando match/case
#solicitando os valores para o cálculo.
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação (+, -, *, /): ")

match operacao:
    case "subtracao" | "Subtracao" | "SUBTRACAO" | "":
        print(f"O resultado da subtração entre {n1} e {n2} é: {n1 - n2}")
    case "adição" | "Adição" | "ADIÇÃO" | "+":
        print(f"O resultado da adição entre {n1} e {n2} é: {n1 + n2}")
    case "multiplicacao" | "Multiplicacao" | "MULTIPLICACAO"| "*":
        print(f"O resultado da multiplicação entre {n1} e {n2} é: {n1 * n2}")
    case "divisao" | "Divisao" | "DIVISAO" | "/":
        print(f"O resultado da divisão entre {n1} e {n2} é: {n1 / n2}")
        
              
