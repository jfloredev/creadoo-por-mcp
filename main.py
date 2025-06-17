# Archivo principal creado por GitHub Copilot MCP

def calculadora():
    print("Calculadora básica")
    print("Operaciones disponibles: suma, resta, multiplicacion, division")
    op = input("Elige una operación: ")
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    if op == "suma":
        print(f"Resultado: {a + b}")
    elif op == "resta":
        print(f"Resultado: {a - b}")
    elif op == "multiplicacion":
        print(f"Resultado: {a * b}")
    elif op == "division":
        if b != 0:
            print(f"Resultado: {a / b}")
        else:
            print("Error: División por cero")
    else:
        print("Operación no válida")

print("Hola, este es el archivo main.py")

# Descomenta la siguiente línea para usar la calculadora
# calculadora()
