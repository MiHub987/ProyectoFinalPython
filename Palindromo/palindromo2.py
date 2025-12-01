def verificar_palindromo():
    texto_usu = input("Escribe una palabra o frase para verificar: ")
    texto_limpio = texto_usu.lower().replace(" ", "")

    # 3. Comparamos con su inverso
    if texto_limpio == texto_limpio[::-1]:
        print(f"'{texto_usu}' es un palíndromo.")
    else:
        print(f"'{texto_usu}' NO es un palíndromo.")

# Ejecutamos la función
verificar_palindromo()
