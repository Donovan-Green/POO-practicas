# Aquí creamos la clase (que es como el molde principal para los carros)
class carro:
    """
    Este es el molde para crear carros. 
    Aquí guardamos sus características principales.
    """
    
    def __init__(self, brand, model, color):
        """
        Esta función sirve para recibir los datos 
        cuando creamos un carro nuevo y guardarlos.
        """
        self.brand = brand   # Guardamos la marca
        self.model = model   # Guardamos el modelo
        self.color = color   # Guardamos el color

    # Aquí están las acciones que puede hacer el carro
    def show_info(self):
        """
        Esta función imprime en la pantalla 
        la información del carro ordenada.
        """
        print(f"{self.brand} {self.model} {self.color}")

# Creamos nuestro primer carro (objeto) usando el molde
car1 = carro("toyota", "corolla", "red")
car1.show_info() 

# Creamos un segundo carro completamente diferente con el mismo molde
car2 = carro("honda", "civic", "blue")
car2.show_info()