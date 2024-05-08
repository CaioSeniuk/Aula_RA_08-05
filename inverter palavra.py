palavra_lista = []
palavra = input("\nDigite uma palavra: ")
for i in palavra:
    palavra_lista.append(i)
palavra_lista.reverse()
for x in palavra_lista:
    print(x,end="")
