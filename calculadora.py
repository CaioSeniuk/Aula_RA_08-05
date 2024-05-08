def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b
    
def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    return a/b

print(f"\nCalculadora" + "\n\n" + ("-"*60))
op = 0
while op!= 5:
    op = int(input("\nEscolha uma opção:\n1-adição\n2-subtração\n3-multiplicação\n4-divisão\n5-sair\n\n->"))
    if op == 5:
        continue
    num1=int(input("\nInsira o 1º número: "))
    num2=int(input("\nInsira o 2º número: "))
    if op== 1:
        print(f"\nA soma é igual a: {soma(num1,num2)}")
        continue
    elif op== 2:
        print(f"\nA subtração é igual a: {subtracao(num1,num2)}")
        continue
    elif op== 3:
        print(f"\nA multiplicação é igual a: {multiplicacao(num1,num2)}")
        continue
    elif op== 4:
        while num2 == 0:
            print("\nImpossível dividir por 0, insira outro número")
            num1=int(input("\nInsira o 1º número: "))
            num2=int(input("\nInsira o 2º número: "))
        print(f"\nA divisão é igual a: {divisao(num1,num2)}")
    elif op <= 0 or op > 5:
        print("\nErro ! Insira um valor válido\n" + ("-"*60))
        continue