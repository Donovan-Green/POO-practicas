# Aquí creamos la clase principal para los empleados básicos
class Employee:
    """Esta clase representa a un empleado básico."""
    
    def __init__(self, name, salary):
        # Guardamos el nombre y el sueldo base del empleado
        self.name = name 
        self.salary = salary

    def show_info(self):
        """Método para mostrar el nombre y el salario."""
        # Imprimimos los datos básicos en pantalla
        print(f"Name: {self.name}, Salary: {self.salary}")


# Creamos la clase Manager que hereda todo lo de Employee ademas agrega el departamento
class Manager(Employee):
    """Clase Manager que hereda de Employee y agrega un departamento."""
    
    def __init__(self, name, salary, department):
        # Usamos super() para traer los datos del papá (Employee) y no repetirlos
        super().__init__(name, salary)  
        # Aquí guardamos el departamento 
        self.department = department

    def show_info(self):
        """Sobrescribimos show_info() para mostrar también el departamento."""
        # Modificamos el método para que ahora sí saque también el departamento
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")


    
# Creamos un objeto de la clase Employee y probamos su método
empleado1 = Employee("Pinto",6000)
empleado1.show_info()  # Imprime los datos normales

 
 
 
 # Creamos un objeto de la clase Manager y probamos su método con el departamento aagregado

manager1 = Manager("Bryan", 10000, "Ventas")
manager1.show_info()  # Imprime los datos heredados más el departamento