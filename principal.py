<<<<<<< HEAD
"""Demonstra o uso de saudações em diferentes idiomas.

O script define a classe :class:`Place`, que associa um nome a um idioma
e imprime uma saudação correspondente. Ao ser executado, cria um objeto
configurado para francês e exibe a saudação destinada a "Mundo".
"""


class Place:
    """Representa um lugar que receberá uma saudação."""

    def __init__(self, name):
        """Inicializa uma instância com nome e idioma padrão em inglês.

        Args:
            name: Nome usado na saudação.
        """
        self.name = name
        self.language = "English"
        
    def greet(self):
        """Imprime uma saudação com base no idioma configurado."""
        match self.language.upper():
            case "SPANISH":
                print(f"Hola, {self.name}!")
            case "FRENCH":
                print(f"Bonjour, {self.name}!")
            case "GERMAN":
                print(f"Hallo, {self.name}!")
            case "ITALIAN":
                print(f"Ciao, {self.name}!")
            case "PORTUGUESE":
                print(f"Olá, {self.name}!") 
            case _:
                print(f"Hello, {self.name}!")


place = Place("Mundo")
place.language = 'Portuguese'
print("\n\n\n\n")
place.greet()   
print("\n\n\n\n")





=======

print ("Testando git")
>>>>>>> f890cd77f11abe1e941603421438297bca02e5e8

