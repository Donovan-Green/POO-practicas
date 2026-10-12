# Creamos una clase Engine
class Engine:
# Creamos un metodo para encender el motor 
  def start(self):
   """Este metodo enciende el motor """
print("Engine started")

# Creamos una clase carro
class Car:

  def __init__(self, engine):
    self.engine = engine  

  # Creamos un método para encender el carro
  def start_car(self):
    """Este método enciende el carro"""
    # Le decimos al motor que encienda
    self.engine.start()


# Creamos un objeto motor
engine1 = Engine()

# Creamos el carro pasándole el motor anterior
car1 = Car(engine1)

# Probamos el método de encendido
car1.start_car()

