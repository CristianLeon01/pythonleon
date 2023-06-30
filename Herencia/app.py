from persona import*
from empresa import*
from producto import*

obj1=Persona(123,'Individual', 'Humilde','Roberto','robertico01@gmail.com', 300772206, 'cra1 #21-32')
print(obj1.getpersona())

pro1=Producto(1,'cocacola','alto en azucar')
print(pro1.getproducto())

obj1.agreproductos(pro1)
for producto in obj1.getlistProductos():
    print(producto.getproducto())
