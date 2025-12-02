palavra = input("Digite uma palavra:").lower()

vogais = "aeiou"

contador = 0

for letras in palavra:
    if letras in vogais:
        contador += 1

print(f"A palavra {palavra} tem {contador} vogal!")
