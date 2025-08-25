""" 
Estos ejercicios refuerzan la toma de decisiones complejas y el uso de bucles para validación y repetición controlada.
Ejercicio 1: Sistema de Precios de Entradas de Cine
Crea un programa que calcule el precio de una entrada de cine basándose en la edad del cliente y si es estudiante: 
Reglas:
•	Niños (menores de 12 años): $10.000.
•	Jóvenes (12 a 17 años): $15.000.
•	Adultos (18 años en adelante): $20.000.
•	Si el cliente es estudiante (independientemente de la edad), tiene un 10% de descuento.
El programa debe pedir la edad y si es estudiante ('si' o 'no').
Conceptos aplicados: if/elif/else anidados, operadores lógicos (and, or), input(), int(), lower(), f-strings.

"""

def main():
    def pedir_entero(mensaje, minimo=None, maximo=None):
        """ 
        Esta función solicita un número entero al usuario, validando que esté dentro de los límites especificados.
        
        Args:
            mensaje (str): mensaje que se muestra al usuario para pedir el valor.
            minimo (int, opcional): valor mínimo permitido para el número entero.
            maximo (int, opcional): valor máximo permitido para el número entero.
        Returns:
            int: el valor introducido por el usuario.   
            
        """
        while True:
            entrada = input(mensaje).strip()

            if not entrada:
                print("\n⚠️  No puede dejar el campo vacío.")
                continue

            if not entrada.isdigit():
                print("⚠️ Solo se permiten números enteros positivos.")
                continue

            valor = int(entrada)

            if minimo is not None and valor < minimo:
                print(f"\n⚠️  El valor no puede ser menor a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"\n⚠️  El valor no puede ser mayor a {maximo}.")
                continue

            return valor


    def pedir_si_no(mensaje):
        """
        Esta función solicita una respuesta al usuario, validando que sea 'si' o 'no'.
        
        Args:
            mensaje (str): mensaje que se muestra al usuario para pedir la respuesta.
        Returns:
            bool: True si la respuesta es 'si', False si la respuesta es 'no'.
        """
        while True:
            entrada = input(mensaje).strip().lower()

            if not entrada:
                print("⚠️  No puede dejar la respuesta vacía.")
                continue

            if entrada in ["si"]:
                return True
            elif entrada in ["no"]:
                return False
            else:
                print("⚠️  Respuesta inválida. Escriba 'si' o 'no'.")

    def calcular_precio(edad):
        """
        Esta función calcula el precio de la entrada según la edad del cliente.
        
        Args:
            edad (int): edad del cliente.
        Returns:
            int: el precio de la entrada.
        """
        if edad < 12:
            print("Categoría: Niño")
            return 10000
        elif 12 <= edad < 18:
            print("Categoría: Joven")
            return 15000
        else:
            print("Categoría: Adulto")
            return 20000

    print("-" * 40)
    print(" Bienvenido al sistema del cine 🎬 ")
    print("-" * 40)

    cantidad = pedir_entero("Digite la cantidad de personas a ingresar: ", minimo=1, maximo=20)

    total_general = 0

    for i in range(cantidad):
        print(f"\n Persona número {i + 1}")

        edad = pedir_entero("Digite su edad: ", minimo=1, maximo=90)
        precio = calcular_precio(edad)

        if pedir_si_no("¿Es estudiante? (si/no): "):
            descuento = precio * 0.10
            precio -= descuento
            print(f"✅ Descuento aplicado: ${descuento:.0f}")
        else:
            print("❌ No aplica descuento.")

        print(f"💵 Precio final: ${precio:.0f}")
        total_general += precio

    print("\n" + "-" * 50)
    print(f"🏷️ Total a pagar por todas las entradas: ${total_general:.0f}")
    print("-" * 50)


if __name__ == "__main__":
    main()
