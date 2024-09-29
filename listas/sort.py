linguagens = ["Python", "JS", "Ruby", "C", "Lua"]
linguagens.sort()# ordena em ordem alfabetica
print(linguagens)
linguagens.sort(reverse=True) #ordena em ordem alfabetica ao reverso
print(linguagens)
linguagens.sort(key=lambda x: len(x)) #ordena em ordem crescente
print(linguagens)
linguagens.sort(key=lambda x: len(x),reverse=True) #ordena em ordem decrescente
print(linguagens)