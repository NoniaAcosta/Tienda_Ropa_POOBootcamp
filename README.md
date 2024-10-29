## Carrito de compras
El carrito de compras al iniciarse se carga los productos de prendas y calzados.
# Menú para elegir las acciones
El menú disponible es el siguiente:
        1: Ver productos
        2: Agregar a carrito
        3: Ver carrito
        4: Finalizar Compra
        5: Salir
# Opciones
La opción 1 es para vizualizar los productos disponible, la opción 2 es para agregar al carrito los productos, esto se logra ingresando el código del producto, la opción 3 se puede vizualizar lo que se ha añadido al carrito y la opción 4 al finalizar la compra se puede ver el total.
El archivo principal es compras.py, una vez ejecutado ya se cargan los productos y se puede vizualizar con la Opción del menú.

## Clases utilizadas.
### class Producto: 
Es la clase pricipal, que tiene los atributos por defecto de nombre, precio, cantidad.
### class Ropa(Producto):
Esta clase hereda de productos y se agrega un atributo mas que sería la Talla. Tiene la función de mostrar_info.
### class RopaHombre(Ropa):
Esta clase hereda de Ropa. Tiene la función de mostrar_info.
### class RopaMujer(Ropa):
Esta clase hereda de Ropa. Tiene la función de mostrar_info.
### class CamisaMujer(RopaMujer):
Esta clase hereda de RopaMujer. Tiene la función de mostrar_info. Se agrega el atributo de tipo_tela.
### class CamisaHombre(RopaHombre):
Esta clase hereda de RopaHombre. Tiene la función de mostrar_info. Se agrega el atributo de tipo_tela.
### PantalonMujer(RopaMujer):
Esta clase hereda de RopaMujer. Tiene la función de mostrar_info. Se agrega el atributo de largor.
### class PantalonHombre(RopaHombre):
Esta clase hereda de RopaHombre. Tiene la función de mostrar_info. Se agrega el atributo de largor.
### class Vestido(RopaMujer):
Esta clase hereda de RopaMujer. Tiene la función de mostrar_info. Se agrega el atributo de estilo.
### class Blusa(RopaMujer):
Esta clase hereda de RopaMujer. Tiene la función de mostrar_info. Se agrega el atributo de estilo.
### class Chaqueta(RopaHombre):
Esta clase hereda de RopaHombre. Tiene la función de mostrar_info. Se agrega el atributo de material.
### class Falda(RopaMujer):
Esta clase hereda de RopaMujer. Tiene la función de mostrar_info. Se agrega el atributo de largor.
### class CalzadoHombre(Producto):
Esta clase hereda de Producto. Tiene la función de mostrar_info. Se agrega el atributo de calse.
### class CalzadoMujer(Producto):
Esta clase hereda de Producto. Tiene la función de mostrar_info. Se agrega el atributo de calse.
### class Inventario:
Se tiene la lista para almacenar las prendas y los calzados del inventario.
Tiene las funciones de: agregar_prenda, agregar_calzado, mostrar_inventario, buscar_por_codigo.
### class Carrito:
Se tiene la lista del carrito agregado y las compras confirmadas. Tiene las funciones de: mostrar_carrito, agregar_carrito, mostrar_compras, finalizar_compra.
