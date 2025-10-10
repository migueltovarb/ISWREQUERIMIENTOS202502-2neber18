import csv

class funcion_cine:
    def __init__(self, codigo, nombre_pelicula, hora, precio):
        self.codigo = codigo
        self.nombre_pelicula = nombre_pelicula
        self.hora = hora
        self.precio = float(precio)

    def get_id(self):
        return self.codigo
    
    def get_data(self):
        return f"""Código: {self.codigo}
Nombre Película: {self.nombre_pelicula}
Hora: {self.hora}"""

    def __str__(self):
        return f"{self.codigo} - {self.nombre_pelicula} ({self.hora} ${self.precio:.2f})"

class sistema_cine:
    def __init__(self):
        self.funciones = self.cargar_funciones()
        self.ventas = []

    def cargar_funciones(self):
        funciones = []
        try:
            with open("funciones.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row:
                        funciones.append(funcion_cine(*row))
        except FileNotFoundError:
            print("Archivo de funciones no encontrado. Se creará uno nuevo.")
        return funciones

    def guardar_funciones(self):
        with open("funciones.csv", "w", newline='') as f:
            writer = csv.writer(f)
            for funcion in self.funciones:
                writer.writerow([funcion.codigo, funcion.nombre_pelicula, funcion.hora, funcion.precio])

    def guardar_venta(self, codigo, cantidad, total):
        with open("ventas.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([codigo, cantidad, total])
        self.ventas.append((codigo, cantidad, total))

    def registrar_funcion(self):
        codigo = input("Ingresar el código de la función: ")
        nombre = input("Ingresar el nombre de la película: ")
        hora = input("Ingresar la hora de la función: ")
        precio = float(input("Ingresar el precio del boleto: "))
        nueva_funcion = funcion_cine(codigo, nombre, hora, precio)
        self.funciones.append(nueva_funcion)
        self.guardar_funciones()
        print("Función registrada exitosamente.")

    def listar_funciones(self):
        print("\nFunciones disponibles:")
        for funcion in self.funciones:
            print(funcion)
        print()

    def vender_boletos(self):
        codigo = input("Ingresar el código para ver la función: ")
        funcion = None
        for f in self.funciones:
            if f.codigo == codigo:
                funcion = f
                break

        if not funcion:
            print("Código de función no encontrado.")
            return

        try:
            cantidad = int(input("Ingresar la cantidad de boletos: "))
            if cantidad <= 0:
                raise ValueError
        except ValueError:
            print("Cantidad inválida.")
            return

        total = funcion.precio * cantidad
        self.guardar_venta(codigo, cantidad, total)
        print(f"Total a pagar: ${total:.2f}")

    def resumen_ventas(self):
        total_boletos = 0
        total_dinero = 0
        try:
            with open("ventas.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row:
                        cantidad = int(row[1])
                        monto = float(row[2])
                        total_boletos += cantidad
                        total_dinero += monto
        except FileNotFoundError:
            print("No hay ventas registradas.")
            return

        print(f"\nResumen del día:")
        print(f"- Total boletos vendidos: {total_boletos}")
        print(f"- Total dinero recaudado: ${total_dinero:.2f}\n")


def mostrar_menu():
    print("""
MovieTime - Venta de Boletos
1. Registrar nueva función
2. Listar funciones disponibles
3. Vender boletos
4. Mostrar resumen de ventas del día
5. Salir
""")


cine = sistema_cine()

while True:
    mostrar_menu()
    try:
        opcion = int(input("Seleccione una opción (1-5): "))
    except ValueError:
        print("Opción inválida. Intente de nuevo.")
        continue

    if opcion == 1:
        cine.registrar_funcion()
    elif opcion == 2:
        cine.listar_funciones()
    elif opcion == 3:
        cine.vender_boletos()
    elif opcion == 4:
        cine.resumen_ventas()
    elif opcion == 5:
        print("Gracias por usar MovieTime.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")


    
