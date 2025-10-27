# Calculadora con historial

historial = []
salir = False

while salir == False:
    print("\n--- Calculadora ---")
    num1 = float(input("Ingresa el primer número: "))

    continuar = True
    while continuar == True:
        operacion = input("Ingresa la operación (+, -, *, /): ")

        if operacion == "+" or operacion == "-" or operacion == "*" or operacion == "/":
            num2 = float(input("Ingresa el segundo número: "))

            if operacion == "+":
                resultado = num1 + num2
            elif operacion == "-":
                resultado = num1 - num2
            elif operacion == "*":
                resultado = num1 * num2
            elif operacion == "/":
                if num2 == 0:
                    print("ERROR")
                    resultado = "error"
                else:
                    resultado = num1 / num2

            if resultado != "error":
                print("Resultado:", resultado)
                texto = str(num1) + " " + operacion + " " + str(num2) + " = " + str(resultado)
                historial.append(texto)
                num1 = resultado

            print("\nOpciones:")
            print("1. Hacer otra operación con el resultado actual")
            print("2. Reiniciar calculadora")
            print("3. Ver historial")
            print("4. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                continuar = True
            elif opcion == "2":
                continuar = False
            elif opcion == "3":
                print("\n--- Historial ---")
                for item in historial:
                    print(item)
                continuar = True
            elif opcion == "4":
                continuar = False
                salir = True
            else:
                print("Opción no válida.")
                continuar = True
        else:
            print("Operador no válido.")
