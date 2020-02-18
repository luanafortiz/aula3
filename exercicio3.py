import random
contador = 1
numero = int(input('quantos numeros você deseja? '))
lista = []
while contador <= numero:
    lista.append (random.randrange(0,100))
    contador+=1
print(lista)
print(max(lista))
print(min(lista))