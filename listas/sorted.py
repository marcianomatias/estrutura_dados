linguagens = ["Python", "JS", "Ruby", "C", "Lua", "C#"]

print(sorted(linguagens, key=lambda x: len(x)))
print(sorted(linguagens, key=lambda x: len(x), reverse=True))
print(sorted(linguagens))
