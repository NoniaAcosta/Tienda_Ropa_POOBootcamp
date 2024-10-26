class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre  # Atributo público
        self.precio = precio  # Atributo público
        self.cantidad = cantidad  # Atributo público

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self.cantidad}")
        
class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  # Llamada al constructor de la clase padre
        self.talla = talla  # Atributo específico de RopaHombre

    def mostrar_info(self):
        super().mostrar_info()  # Llama al método de la clase padre
        print(f"Talla: {self.talla}")
        
class Calzado(Prenda):
    def __init__(self, nombre, precio, cantidad, calse):
        super().__init__(nombre, precio, cantidad)  # Llamada al constructor de la clase padre
        self.calse = calse  # Atributo específico de RopaHombre

    def mostrar_info(self):
        super().mostrar_info()  # Llama al método de la clase padre
        print(f"Calse: {self.calse}")
        
class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")
        
class Inventario:
    def __init__(self):
        self.prendas = []  # Lista para almacenar las prendas

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)  # Agrega la prenda a la lista

    def mostrar_inventario(self):
        for prenda in self.prendas:
            prenda.mostrar_info()  # Muestra la información de cada prenda

inventario = Inventario()
camisa = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
pantalon = RopaHombre("Pantalón de Hombre", 30.00, 30, "M")
chaqueta = RopaHombre("Chaqueta de Hombre", 55.00, 20, "M")


falda = RopaMujer("Falda de Mujer", 28.00, 15, "S")            
blusa = RopaMujer("Blusa de Mujer", 22.00, 40, "S")            
vestido = RopaMujer("Vestido de Mujer", 45.00, 10, "S")        
zapatos_hombre = Calzado("Zapatos de Hombre", 60.00, 25, "45")     
zapatos_mujer = Calzado("Zapatos de Mujer", 50.00, 20, "37")    
        
inventario.agregar_prenda(camisa)
inventario.agregar_prenda(pantalon)
inventario.agregar_prenda(chaqueta)
inventario.agregar_prenda(falda)
inventario.agregar_prenda(blusa)
inventario.agregar_prenda(vestido)
inventario.agregar_prenda(zapatos_hombre)
inventario.agregar_prenda(zapatos_mujer)

inventario.mostrar_inventario()
