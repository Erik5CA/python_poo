
class Producto:
    def __init__(self,codigo ,nombre, precio, descuento=None):
        # Atributos privados
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__descuento = descuento
    # Obtener el valor (getter)
    @property
    def codigo(self):
        return self.__codigo
    # Cambiar el valor (setter)
    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor
        
    @property
    def precio(self):
        if self.__descuento == None:
            return self.__precio
        else:    
            return self.__descuento.aplicar_descuento(self.__precio)
    
    @precio.setter
    def precio(self, valor):
        self.__precio = valor
        
    def cacular_total(self, unidades):
        return self.precio * unidades
        
    # Mostrar info del objeto
    def __str__(self):
        return f'Producto[ Codigo: {self.codigo} - Nombre: {self.nombre} - Precio: {self.precio} ]'

class Pedido:
    def __init__(self):
        self.__productos = []
        self.__cantidades = []
        
    def aniadir_producto(self, producto, cantidad):
        if not isinstance(producto, Producto):
            raise Exception('Añadir Producto: el producto debe ser de la clase producto')
        
        if not isinstance(cantidad, int):
            raise Exception('Añadir Producto: la cantidad debe ser un numero')
        
        if cantidad <= 0:
            raise Exception('Añadir Producto: la cantidad debe ser mayor a 0')
        
        if producto in self.__productos:
            indice = self.__productos.index(producto)
            self.__cantidades[indice] = self.__cantidades[indice] + cantidad
        else:
            self.__productos.append(producto)
            self.__cantidades.append(cantidad)
            
    def eliminar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise Exception('Eliminar Producto: el producto debe ser de la clase producto')
        
        if producto in self.__productos:
            indice = self.__productos.index(producto)
            del self.__productos[indice]
            del self.__cantidades[indice]
        else:
            raise Exception('Eliminar Producto: el producto no se encuentra en el pedido')
    
    def total_pedido(self):
        total = 0
        for (p, c) in zip(self.__productos, self.__cantidades):
            total += p.cacular_total(c)
        return total
    
    def mostrar_pedido(self):
        for (p, c) in zip(self.__productos, self.__cantidades):
            print(f'Producto: {p.nombre}', f'Cantidad: {str(c)}')
            
TIPO_DESC_FIJO = 'Fijo'
TIPO_DESC_PORC = 'Porcentaje'
 
class Descuento:
    def __init__(self, tipo, valor):
        if not isinstance(valor, int):
            raise Exception('Constructor descuento: el valor debe ser un numero')
        if not isinstance(tipo, str):
            raise Exception('Constructor descuento: el tipo debe ser un string')
        if tipo != TIPO_DESC_PORC and tipo != TIPO_DESC_FIJO:
            raise Exception('Constructor descuento: el tipo debe ser Fijo o Porcentaje')
        if tipo == TIPO_DESC_FIJO and valor <= 0:
            raise Exception('Constructor descuento: el valor en el tipo fijo debe ser mayor a 0')
        if tipo == TIPO_DESC_PORC and (valor <= 0 or valor > 100):
            raise Exception('Constructor descuento: el valor en el tipo porcentaje debe ser mayor a 0 y menor a 100')
        self.__tipo = tipo
        self.__valor = valor
        
    @property
    def tipo(self):
        return self.__tipo
        
    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor
        
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
        
    def aplicar_descuento(self, precio):
        if self.__tipo == TIPO_DESC_FIJO:
            if precio > self.__valor:
                return precio - self.__valor
            else:
                return 0
        else:
            return precio - (precio * self.__valor / 100)

desc1 = Descuento(TIPO_DESC_FIJO, 5)
desc2 = Descuento(TIPO_DESC_PORC, 50)

p1 = Producto(1, 'Producto 1', 10)
p2 = Producto(2, 'Producto 2', 10, desc1)
p3 = Producto(3, 'Producto 3', 10, desc2)
p4 = Producto(3, 'Producto 4', 10)

# p1.nombre = 'Hola'
print(p1)
print(p2)
print(p3)

print(p1.cacular_total(5))
print(p2.cacular_total(5))
print(p3.cacular_total(5))

productos = [p1, p2, p3]
cantidades = [5, 10 ,2]

pedido = Pedido()

try:
    pedido.aniadir_producto(p1, 5)
    pedido.aniadir_producto(p2, 5)
    pedido.aniadir_producto(p3, 5)
    print(f'Total pedido: {str(pedido.total_pedido())}')
    pedido.mostrar_pedido()
    
    pedido.eliminar_producto(p4)
    print(f'Total pedido: {str(pedido.total_pedido())}')
    pedido.mostrar_pedido()
except Exception as e:
    print(e)
    
