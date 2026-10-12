# Aquí creamos la clase (el molde principal para las cuentas de banco)
class BankAccount:
    """
    Este es el molde para crear cuentas de banco.
    Aquí guardamos sus características principales.
    """
    
    # Este es un atributo de clase. 
    # Lo comparten todas las cuentas que creemos por ello está declarado fuera del constructor.
    bank = "Central Bank"

    def __init__(self, balance):
        # Aquí guardamos el dinero inicial de la cuenta
        self.balance = balance

    # Este es un método normal (de instancia)
    def show_balance(self):
        """
        Muestra en pantalla cuánto dinero hay en la cuenta actual.
        """
        print(f"El balance actual es: {self.balance}")

    # Este es un método de clase 
    # Usa cls en lugar de self porque solo usa datos de la clase 
    @classmethod
    def show_bank(cls):
        print(f"El nombre del banco es: {cls.bank}")

    # Este es un método estático siempre se declara con un @ para iniciar
    # Funciona como un método aparte, que no depende de la clase ni de los objetos, pero que tiene relación con la clase.
    @staticmethod
    def convert_currency(value):
        """
        Función que convierte dólares a pesos.
        """
        exchange_rate = 17.32
        pesos = value * exchange_rate
        print(f"${value} USD equivale a ${pesos} pesos.")

        
# Mandamos a llamar el método de clase directamente sin tener que crear un objeto 
BankAccount.show_bank()

# Mandamos a llamar el método estático también de forma directa
BankAccount.convert_currency(100)

# Creamos un objeto 
cuenta_nueva = BankAccount(500)

# Usamos el método normal del objeto
cuenta_nueva.show_balance()