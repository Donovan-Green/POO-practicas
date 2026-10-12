# Creamos la clase Book 
class Book:
  """Clase que crea un libro con su título y número de páginas"""

  # Inicializamos los atributos del libro
  def __init__(self, title, num_pages):
    
    self.title = title  # Título del libro
    self.num_pages = num_pages  # Número total de páginas

  # Esto convierte el libro en un texto string
  def __str__(self):
    """retorna un texto en el formato necesario para el libro (string)"""
    return f"Book: {self.title}, Pages: {self.num_pages}"
    
  
  # Esto permite usar len() para saber el número de páginas
  def __len__(self):
    """Retorna la longitud del libro (numero de paginas)"""
    return self.num_pages


  
# Creamos un objeto (libro)
book1 = Book("Can't Hurt Me", 410)

# Probamos el método __str__ imprimiendo directamente el objeto (Libro)
print(book1)

# Probamos el método __len__ usando la función len()
print(f"Total de páginas: {len(book1)}")

