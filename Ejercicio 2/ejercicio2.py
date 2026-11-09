import json


class StockInvalidoError(Exception):
    pass


class DispositivoEcológico():

    def __init__(self, codigo: str, nombre: str, precio: float, stock: int):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

        self.__stock = 0
        self.asignar_stock(stock)

    def asignar_stock(self, nuevo_stock):

        if nuevo_stock < 0:
            raise StockInvalidoError("El stock no puede ser negativo")

        self.__stock = nuevo_stock

    def obtener_stock(self):

        return self.__stock

    def mostrar_ficha_tecnica(self):

        return f"Codigo: {self.codigo} | Precio: ${self.precio} | Stock: {self.obtener_stock()}"


class PanelSolar(DispositivoEcológico):

    def __init__(self, codigo, nombre, precio, stock, potencia_watts, eficiencia):
        super().__init__(codigo, nombre, precio, stock)

        self.potencia_watts = potencia_watts
        self.eficiencia = eficiencia

    def mostrar_ficha_tecnica(self):

        return f"Codigo: {self.codigo} | Precio: ${self.precio} | Stock: {self.obtener_stock()} | Potencia: {self.potencia_watts} | Eficiencia: {self.eficiencia}"


class GestorInventario():

    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):

        catalogo = []

        for dispositivo in lista_dispositivos:

            producto = {
                "codigo": dispositivo.codigo,
                "nombre": dispositivo.nombre,
                "precio": dispositivo.precio,
                "stock": dispositivo.obtener_stock(),
            }

            if type(dispositivo) == PanelSolar:

                producto["potencia_watts"] = dispositivo.potencia_watts
                producto["eficiencia"] = dispositivo.eficiencia

            catalogo.append(producto)

        with open(ruta_archivo, "w", encoding="utf-8") as file:
            json.dump(catalogo, file, indent=4)

        print("Catalogo guardado correctamente.")


# Bloque principal de prueba

panel1 = PanelSolar(
    "PS-001",
    "Panel Solar Residencial",
    250_000,
    15,
    450,
    21.5
)

panel2 = PanelSolar(
    "PS-002",
    "Panel Solar Industrial",
    420_000,
    8,
    600,
    23.5
)

equipo1 = DispositivoEcológico(
    "DE-001",
    "Controlador de Carga",
    85_000,
    5
)

try:
    panel_invalido = PanelSolar(
        "PS-003",
        "Panel Solar Defectuoso",
        400_000,
        -5,
        850,
        26.5
    )

except StockInvalidoError as error:
    print(f"Error controlado: {error}")


try:
    panel1.asignar_stock(-5)

except StockInvalidoError as error:
    print(f"Error controlado: {error}")


productos = [panel1, panel2, equipo1]

for producto in productos:
    print(producto.mostrar_ficha_tecnica())


admin_catalogo = GestorInventario()
admin_catalogo.guardar_catalogo_json(productos, "catalogo_ecotech.json")