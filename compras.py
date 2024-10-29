class Producto:
    _contador = 1

    def __init__(self, nombre, precio, cantidad):
        self.codigo = f"P{Producto._contador:03}"
        Producto._contador += 1
        self.nombre = nombre  # Atributo público
        self.precio = precio  # Atributo público
        self.cantidad = cantidad  # Atributo público

    def mostrar_info(self):
        print(
            f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self.cantidad}"
        )


class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()  # Llama al método de la clase padre
        print(f"Talla: {self.talla}")


class RopaHombre(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)

    def mostrar_info(self):
        super().mostrar_info()


class RopaMujer(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)

    def mostrar_info(self):
        super().mostrar_info()


class CamisaMujer(RopaMujer):
    def __init__(self, nombre, precio, cantidad, talla, tipo_tela):
        super().__init__(nombre, precio, cantidad, talla)
        self.tipo_tela = tipo_tela

    def mostrar_info(self):
        super().mostrar_info()
        print(f"tipo_tela: {self.tipo_tela}")


class CamisaHombre(RopaHombre):
    def __init__(self, nombre, precio, cantidad, talla, tipo_tela):
        super().__init__(nombre, precio, cantidad, talla)
        self.tipo_tela = tipo_tela

    def mostrar_info(self):
        super().mostrar_info()
        print(f"tipo_tela: {self.tipo_tela}")


class PantalonMujer(RopaMujer):
    def __init__(self, nombre, precio, cantidad, talla, largor):
        super().__init__(nombre, precio, cantidad, talla)
        self.largor = largor

    def mostrar_info(self):
        super().mostrar_info()
        print(f"largor: {self.largor}")


class PantalonHombre(RopaHombre):
    def __init__(self, nombre, precio, cantidad, talla, largor):
        super().__init__(nombre, precio, cantidad, talla)
        self.largor = largor

    def mostrar_info(self):
        super().mostrar_info()
        print(f"largor: {self.largor}")


class Vestido(RopaMujer):
    def __init__(self, nombre, precio, cantidad, talla, estilo):
        super().__init__(nombre, precio, cantidad, talla)
        self.estilo = estilo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"estilo: {self.estilo}")


class Blusa(RopaMujer):
    def __init__(self, nombre, precio, cantidad, talla, estilo):
        super().__init__(nombre, precio, cantidad, talla)
        self.estilo = estilo

    def mostrar_info(self):
        super().mostrar_info()
        print(f"estilo: {self.estilo}")


class Chaqueta(RopaHombre):
    def __init__(self, nombre, precio, cantidad, talla, material):
        super().__init__(nombre, precio, cantidad, talla)
        self.material = material

    def mostrar_info(self):
        super().mostrar_info()
        print(f"material: {self.material}")


class Falda(RopaMujer):
    def __init__(self, nombre, precio, cantidad, talla, largor):
        super().__init__(nombre, precio, cantidad, talla)
        self.largor = largor

    def mostrar_info(self):
        super().mostrar_info()  # Llama al método de la clase padre
        print(f"largor: {self.largor}")


class CalzadoHombre(Producto):
    def __init__(self, nombre, precio, cantidad, calse):
        super().__init__(
            nombre, precio, cantidad
        )  # Llamada al constructor de la clase padre
        self.calse = calse  # Atributo específico de RopaHombre

    def mostrar_info(self):
        super().mostrar_info()  # Llama al método de la clase padre
        print(f"Calse: {self.calse}")


class CalzadoMujer(Producto):
    def __init__(self, nombre, precio, cantidad, calse):
        super().__init__(
            nombre, precio, cantidad
        )  # Llamada al constructor de la clase padre
        self.calse = calse  # Atributo específico de RopaHombre

    def mostrar_info(self):
        super().mostrar_info()  # Llama al método de la clase padre
        print(f"Calse: {self.calse}")


class Inventario:
    def __init__(self):
        self.prendas = []  # Lista para almacenar las prendas
        self.calzados = []  # Lista para almacenar los calzados

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)  # Agrega la prenda a la lista

    def agregar_calzado(self, calzado):
        self.calzados.append(calzado)

    def mostrar_inventario(self):
        print("##### Sistema de Compras de Prendas y Calzados #####")
        print("---- Prendas ----")
        for prenda in self.prendas:
            prenda.mostrar_info()  # Muestra la información específica de cada prenda

        print("\n---- Calzados ----")
        for calzado in self.calzados:
            calzado.mostrar_info()  # Muestra la información específica de cada calzado

    def buscar_por_codigo(self, codigo):
        for prenda in self.prendas:
            if prenda.codigo == codigo:
                print("Producto encontrado:")
                prenda.mostrar_info()
                return prenda

        for calzado in self.calzados:
            if calzado.codigo == codigo:
                print("Producto encontrado:")
                calzado.mostrar_info()
                return calzado

        print("Producto no encontrado con el código:", codigo)
        return None


class Carrito:
    def __init__(self):
        self.carrito = []
        self.compras = []

    def calcular_precio():
        pass

    def mostrar_carrito(self):
        print("##### Su Carrito #####")
        if not self.carrito:
            print("No hay nada agregado al carrito")
        else:
            for producto in self.carrito:
                producto.mostrar_info() 

    def agregar_carrito(self, prenda):
        self.carrito.append(prenda)
        print("agregado al carrito")

    def mostrar_compras(self):
        print("##### Sistema de Compras de Prendas y Calzados #####")
        print("---- Prendas ----")
        for prenda in self.prendas:
            prenda.mostrar_info()  # Muestra la información específica de cada prenda
            # print("" * 40)

        print("\n---- Calzados ----")
        for calzado in self.calzados:
            calzado.mostrar_info()  # Muestra la información específica de cada calzado
            # print("-" * 40)
            
    def finalizar_compra(self):
        if not self.carrito:
            print("El carrito está vacío. No hay nada para finalizar.")
            return

        total = sum(producto.precio for producto in self.carrito)
        print("##### Resumen de la Compra #####")
        for producto in self.carrito:
            producto.mostrar_info()  # Muestra información de cada producto
    
        print(f"\nTotal de la compra: ${total:.2f}")
        
        # Crear un resumen de la compra
        resumen = {
            "productos": [producto for producto in self.carrito],
            "total": total
        }
        
        self.compras.append(resumen)
        self.carrito.clear()  # Limpia el carrito después de finalizar la compra
        print("Compra finalizada. Gracias por su compra!")


inventario = Inventario()
carrito = Carrito()
camisa = CamisaHombre("Camisa de Hombre", 25.00, 50, "M", "seda")
pantalon = PantalonHombre("Pantalón de Hombre", 30.00, 30, "M", "capri")
chaqueta = Chaqueta("Chaqueta de Hombre", 55.00, 20, "M", "cuero")


falda = Falda("Falda de Mujer", 28.00, 15, "S", "corto")
blusa = Blusa("Blusa de Mujer", 22.00, 40, "S", "clasico")
vestido = Vestido("Vestido de Mujer", 45.00, 10, "S", "vintage")
zapatos_hombre = CalzadoHombre("Zapatos de Hombre", 60.00, 25, "45")
zapatos_mujer = CalzadoMujer("Zapatos de Mujer", 50.00, 20, "37")


inventario.agregar_prenda(camisa)
inventario.agregar_prenda(pantalon)
inventario.agregar_prenda(chaqueta)
inventario.agregar_prenda(falda)
inventario.agregar_prenda(blusa)
inventario.agregar_prenda(vestido)
inventario.agregar_calzado(zapatos_hombre)
inventario.agregar_calzado(zapatos_mujer)


def menu():
    print("Operaciones posibles a realizar")
    while True:
        print("1: Ver productos")
        print("2: Agregar a carrito")
        print("3: Ver carrito")
        print("4: Finalizar Compra")
        print("5: Salir")
        opcion = input("Selecciona una opción: ")
        if opcion.isdecimal():
            opcion = int(opcion)
            if opcion == 1:
                print("-----Estos son los productos disponibles-----")
                inventario.mostrar_inventario()
            elif opcion == 2:
                codigo = input("Ingrese codigo del producto para agregar al carrito:")
                producto = inventario.buscar_por_codigo(codigo)
                carrito.agregar_carrito(producto)
            elif opcion == 3:
                carrito.mostrar_carrito()
            elif opcion == 4:
                carrito.finalizar_compra()
            elif opcion == 5:
                # guardar_datos()
                break
            else:
                print("Por favor, selecciona una opción válida.")
        else:
            print("Por favor, ingrese numeros de 1 al 5")


menu()
