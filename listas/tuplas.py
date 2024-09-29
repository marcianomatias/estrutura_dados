##
# Exemplos de tuplas
#frutas = ("laranja","pera","uva",)  a virgula no final é para conhecer como tupla
#
#letras = tuple("Python")
#numeros = tuple([1,2,3,4])
#
# pais  = ("Brasil",)
# ##
from typing import TypeGuard

frutas = ("laranja","pera","uva",)
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[-1])
print(frutas[-2])
print(frutas[-0])

# tulpas aninhada
matriz = (
    (1,"a",2,),
    (2,"b",3,),
    (3,"c",4,),
)
print(matriz[0])
print(matriz[0][-1])
print(matriz[-2][0])
print(matriz[-1][-1])

# Fatiamento de tuplas

tupla = ("P","y","t","h","o","n",)
print(tupla)
print(tupla[2:])
print(tupla[:2])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[::])
print(tupla[::-1]) # realiza o reverser do fatiamento

# enterar tuplas com for

carros = ("gol","celta","palio",)
for carro in carros:
    print(carro)
for indice, carro in enumerate(carros):
    print(f"{indice}, {carro}")

#metodos da classe tuple
cores = ("branco", "azul", "amarelo", "preto", "azul", "preto", "azul",)
print(cores.count("azul"))
print(cores.count("branco"))
print(cores.count("preto"))
print(cores.count("amarelo"))
#index
print(f"Index")
print(f"Posiçao no index: {cores.index("azul")}")
print(f"Posiçao no index: {cores.index("amarelo")}")
print(f"Posiçao no index: {cores.index("branco")}")
print(f"Posiçao no index: {cores.index("preto")}")

# len
print(f"Metodo len")

print(f"elementos total da tupla: {len(cores)}")

