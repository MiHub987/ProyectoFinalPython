def es_palindromo(texto):
    texto_limpio = texto.lower().replace(" ", "")
    
    return texto_limpio == texto_limpio[::-1]

print(es_palindromo("Ana"))       # True "Aunque lleve mayuscula"
print(es_palindromo("Luz azul"))  # True "Aunque lleve espacios"
print(es_palindromo("Python"))    # False
print(es_palindromo("A la gorda drogala"))
