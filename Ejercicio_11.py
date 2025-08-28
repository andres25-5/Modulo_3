""" 
Bloque 3: Algoritmos y Proyectos de Lógica Aplicada (Ejercicios 11-15)
Estos ejercicios integran todos los conceptos del módulo en la solución de problemas algorítmicos más complejos.
Ejercicio 11: Validador de Cédula (Algoritmo Simple)
Escribe una función que valide un número de cédula (como string) basado en una regla simple: la suma de sus dígitos debe ser un número par. La función debe devolver True si es válido y False si no:
•	Adicionalmente, el programa principal debe pedir al usuario su cédula hasta que ingrese una válida, usando un bucle.
Conceptos aplicados: Funciones, bucle while, conversión de tipos (str a int), bucle for sobre un string.

"""

def validar_cedula(cedula):
    """ 
    Esta función valida un número de cédula basado en la regla de que la suma de sus dígitos debe ser un número par.
    
    Args:
        cedula (str): El número de cédula a validar.
    Returns:
        bool: True si la cédula es válida (suma de dígitos es
                par), False en caso contrario.

    """

    if not cedula.isdigit():
        print("Error: La cédula debe contener solo números.")
        return False
    suma = 0
    for digito in cedula:
        suma += int(digito)
    if suma < 10:
        print("la cedula debe tener 10 numeros")
        return False

    if suma % 2 == 0:
        return True
    else:
        print(" Cédula inválida: la suma de los dígitos no es par.")
        return False

while True:
    cedula_usuario = input("Ingrese su cédula: ")
    if validar_cedula(cedula_usuario):
        print("✅ Cédula válida")
        break

def main():
    validar_cedula(cedula_usuario)
if __name__ == "_main_":
    main()