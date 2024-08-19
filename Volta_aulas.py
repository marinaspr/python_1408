import os
os.system('cls')

 
print("Exercíio 1\n")
fr = str(input("Digite uma frase: "))
car = input("\nDigite um caractere para ser substituido: ")
nvcar = input("Digite o caractere que ira substitutir o outro: ")

nvfr = fr.replace(car,nvcar)

print(nvfr)

print("Exercício 2\n")
lista = [45, 5.7, "Férias", True, False, 99, 34]
listaInt = []
listaFloat = [] 
listaStr = []
listaBool = []

for i in range (len(lista)):
    if type(lista[i]) == int:
        listaInt.append(lista[i])
    elif type(lista[i]) == float:
        listaFloat.append(lista[i])
    elif type(lista[i]) == str:
        listaStr.append(lista[i])
    elif type(lista[i]) == bool:
        listaBool.append(lista[i])

print("lista originial: ", lista)
print("Lista de int: ", listaInt)
print("Lista de float: ", listaFloat)
print("Lista de string: ", listaStr)
print("Lista de boolean: ", listaBool)

print("Exercício 3\n")

lista10 = []

print("Digite 10 elementos")
for i in range (10):
    Elemento = input(f"Elemento {i + 1}: ")
    lista10.append(Elemento)

print(lista10)