# Calculadora básica 

repetir = True

while repetir == True:
    print("\n--- Calculadora ---")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    operacion = input("Ingresa la operación (+, -, *, /): ")

    if operacion == "+":
        resultado = num1 + num2
        print("Resultado:", resultado)
    elif operacion == "-":
        resultado = num1 - num2
        print("Resultado:", resultado)
    elif operacion == "*":
        resultado = num1 * num2
        print("Resultado:", resultado)
    elif operacion == "/":
        if num2 != 0:
            resultado = num1 / num2
            print("Resultado:", resultado)
        else:
            print("Error: no se puede dividir entre cero.")
    else:
        print("Operación no válida.")

    respuesta = input("¿Quieres hacer otra operación? (s/n): ").lower()
    if respuesta == "s":
        repetir = True
    else:
        repetir = False

print("Programa terminado.")
