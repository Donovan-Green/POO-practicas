# Creamos una clase llamada Account que contendra un metodo llamado generate_report
class  Account:

 def generate_report(self):
  """
  Este metodo genera un reporte financiero
  """
  print("Generating financial report") 

# Creamos una clase llamada Technician que contendra un metodo llamado repair_machine
class Technician:
    def repair_machine(self):
     """
     Este metodo asemeja la reparacion de una maquina 
     """
     print("Reparing machine")

class Boss (Account, Technician):
     """
     Esta clase hereda los metodos de la clase Account y Technician

    """
   
     pass

jefe = Boss()
jefe.generate_report() # Usamos el metodo generate_report de la clase Account
jefe.repair_machine()  # Usamos el metodo repair_macine de la clase Technician 
