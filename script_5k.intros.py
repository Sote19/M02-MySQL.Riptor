import random

# Lista de valores para generar datos aleatorios
nombres_productos = ["Camiseta", "Pantalón", "Zapatillas", "Chaqueta", "Sudadera", "Gorra", "Jeans", "Botas", "Polo"]
colores = ["Negro", "Blanco", "Azul", "Gris", "Rojo", "Verde", "Amarillo"]
marcas = ["Nike", "Adidas", "Puma", "Reebok", "Under Armour"]
descripciones = ["Producto de alta calidad", "Diseño moderno", "Material resistente", "Ideal para deportes"]
categorias = ["Camisetas", "Pantalones", "Zapatillas", "Chaquetas", "Sudaderas", "Gorras_Gorros"]
materiales = ["Algodón", "Denim", "Malla", "Cuero", "Poliéster"]

# Función para generar un valor aleatorio
def valor_aleatorio(lista):
    return random.choice(lista)

# Generar el INSERT con los 20,000 registros
insert = "INSERT INTO Productos (nombre, precio, color, marca, stock, descripcion, categoria, materiales) VALUES\n"

for i in range(5000):
    nombre = valor_aleatorio(nombres_productos)
    precio = round(random.uniform(10, 100), 2)
    color = valor_aleatorio(colores)
    marca = valor_aleatorio(marcas)
    stock = random.randint(10, 100)
    descripcion = valor_aleatorio(descripciones)
    categoria = valor_aleatorio(categorias)
    material = valor_aleatorio(materiales)
    
    # Agregar los valores al INSERT
    insert += f"('{nombre}', {precio}, '{color}', '{marca}', {stock}, '{descripcion}', '{categoria}', '{material}'),\n"

# Eliminar la coma extra al final y agregar punto y coma
insert = insert[:-2] + ";"

# Imprimir el INSERT generado
print(insert)
