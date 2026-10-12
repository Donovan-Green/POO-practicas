# Creamos la clase de un empleado de tiempo completo 
class FullTimeEmployee:
    """
    Clase que representa a un empleado de tiempo completo con un salario fijo.
    
    """

    def __init__(self, name, salary):
        """
        Inicializa los atributos del empleado de tiempo completo
        """
        self.name = name  # Nombre del empleado
        self.salary = salary  # Salario fijo 

    def payment(self):
        """Imprime el nombre y el salario fijo del empleado."""
        print(f"Name: {self.name}, El salario es: {self.salary}")

# Creamos la clase de un empleado por horas 
class HourlyEmployee:
    """Clase de un empleado contratado por horas trabajadas."""

    def __init__(self, name, hours_worked, salary_hours):
        """
        Inicializa los atributos del empleado por horas
        
        """
        self.name = name # Nombre del empleado
        self.hours_worked = hours_worked # Horas trabajadas
        self.salary_hours = salary_hours # Salario por hora

    def payment(self):
        """
        Calcula el pago total multiplicando las horas trabajadas por el salario por hora
        
        """
        total_payment = self.hours_worked * self.salary_hours
        print(f"Name: {self.name}, El salario es {total_payment}")


def calculate_payment(employee):
    # Llama al pago del empleado que reciba ya sea por salario fijo o por horas 
    employee.payment()

# Creamos dos objetos uno de cada clase 
Employee1 = FullTimeEmployee("Pinto", 15000)
Employee2 = HourlyEmployee("Bryan", 10, 100)


# Calculamos el pago de cada uno
calculate_payment(Employee1)
calculate_payment(Employee2)