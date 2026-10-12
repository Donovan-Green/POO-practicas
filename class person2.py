# Aquí creamos la clase (el molde principal para las personas)
class person:
    """
    Esta es la clase para crear personas.
    Aquí guardamos sus características principales.
    """

    def __init__(self,name,age,city):  # Recibimos los datos básicos cuando creamos una persona nueva
       
        self.name = name     # name: Guarda el nombre
        self.age = age       # age: Guarda la edad
        self.city = city     # city: Guarda la ciudad donde vive

    # Aquí está la acción que puede hacer la persona (saludar)
    def greet (self):
        """
        Esta función imprime en la pantalla 
        un saludo con la información de la persona.
        """
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and I live in {self.city}") 
                                                                                                   

# Creamos nuestro primer objeto usando el molde de la clase person
person1=person("Alex","19","Tepic")
person1.greet() 

# Creamos un segundo objeto con el mismo molde
person2=person("Bryan","19","Tepic")
person2.greet() 

# Creamos un tercer objeto independiente
person3=person("Alan","19","Tepic")
person3.greet()