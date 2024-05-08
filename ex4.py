def calcular_media(x):
    soma = 0
    for nota in x:
        soma += nota    
    media = soma/len(x)
    return media

lista_notas = []
nota = 0
while nota != -1:
    nota = int(input("\nInforme a nota ou digite -1 para encerrar...\n\n->"))
    if nota == -1:
        continue
    elif nota<0 or nota>10:
        print("\nNota inválida!")
        continue
    else:
        lista_notas.append(nota)
print(f"\nA média é: {calcular_media(lista_notas)}\n")