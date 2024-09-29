matriz = [[1, "a", 2],
          ["b", 3, 4],
          [6, 5, "c"]]
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])
print(matriz[2][1])

#fatiamento
lista = ["M", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(lista[2:])
print(lista[1:2])
print(lista[0:1:2])
print(lista[::])
print(lista[::-1])

listas = ["M", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

for lista in listas:
    print(lista)
for indice, lista in enumerate(listas):
    print(f"{indice} : {lista}")

#compressao de lista

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in numbers if num % 2 == 0]
print(pares)
for num in numbers:
    if num % 2 == 0:
        pares.append(num)
        print(f" Numeros paraes : {num}")

print("Numeros quadrados")
quadrados = [num ** 2 for num in numbers]
print(quadrados)