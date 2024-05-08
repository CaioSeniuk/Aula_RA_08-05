'''palavra_lista = []
palavra = input("\nDigite uma palavra: ")
for i in palavra:
    palavra_lista.append(i)
palavra_lista.reverse()
for x in palavra_lista:
    print(x,end="")'''

def inverter_palavra(palavra):
    return palavra[::-1]

palavra = input("Digite uma palavra: ")
print("Palavra invertida:", inverter_palavra(palavra))