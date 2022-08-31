from msilib.schema import Class


class Persona():
    """Esta Clase crea la estructura para generar objetos de tipo persona
    """
    def __init__(self, color, edad, estatura, nombre):
        self.color = color
        self.edad = edad
        self.estatura = estatura
        self.nombre = nombre
    
    def saltar(self):
        print('Estoy saltando')
        

persona = Persona('cafe', 17, 187, 'jose')

class Drink:
    
    def __init__(self, name):
        self.__name = name
    def describe(self):
        print(f'Soy una bebida de nombre: {self.__name}')
        

drink1 = Drink('Agua')
drink1.name = 'Coca Cola'


class Beer(Drink):
    
    def __init__(self, name, brand, alcohol):
        super().__init__(name)
        self.brand = brand
        self.alcohol = alcohol
    
    def describe(self):
        return super().describe() + f'de marca {self.__brand} con {self.__alcohol} de alcohol'
        

beer1 = Beer('laga', 'Aguila', 5)
print(beer1.describe())