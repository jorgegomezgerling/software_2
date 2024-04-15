#*-------------------------------------------------------------------------
#* prototipo.py
#* Ejemplo para creación de prototipos
#*-------------------------------------------------------------------------
from abc import ABC, abstractmethod
import time
from datetime import datetime
import copy
import os

#*-------------------------------------------------------------------------
#* La clase prototipo utilizada como ejemplo puede estar en una librería
#* externa y ser importada.
#* Define los atributos mandatorios y relevantes, simula actividad por
#* medio de retardos
#*-------------------------------------------------------------------------
# Class Creation
class Prototype(ABC):
    # Constructor:
    def __init__(self):
        # Mocking an expensive call
        time.sleep(2)  # Carga simulada de procesamiento de 2 segundos
        # Base attributes
        self.height = None
        self.age = None
        self.defense = None
        self.attack = None

#*------------------------------------------------------------------------------
#* El método clone() no está definido en el prototipo y mediante @abstractmethod
#* se fuerza a que cualquier instancia que se haga de ésta clase lo tenga que
#* definir.
#*------------------------------------------------------------------------------
    # Clone Method:
    @abstractmethod
    def clone(self):
        pass 

#*------------------------------------------------------------------------------
#* Clase productiva que puedo querer usar como plantilla
#*------------------------------------------------------------------------------
class Shopkeeper(Prototype):
    def __init__(self, height, age, defense, attack):
        super().__init__()
        # Mock expensive call
        time.sleep(2)  # Carga simulada de procesamiento de 2 segundos
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        # Subclass-specific Attribute
        self.charisma = 30


    # Implementa el método de clonado mediante una copia de arbol de métodos
    def clone(self):
        return copy.deepcopy(self)    

#*-------------------------------------------------------------------------
#* clase 
#* define un atributo específico
#*-------------------------------------------------------------------------
class Warrior(Prototype):
    def __init__(self, height, age, defense, attack):
        # Call superclass constructor, time.sleep() and assign base values
        # Concrete class attribute
        self.stamina = 60
    # Overwriting Cloning Method
    def clone(self):
        return copy.deepcopy(self)  

#*--------------------------------------------------------------------------
class Mage(Prototype):
    def __init__(self, height, age, defense, attack):
    # Call superclass constructor, time.sleep() and assign base values
        self.mana = 100

    # Overwriting Cloning Method
    def clone(self):
        return copy.deepcopy(self) 

#*--------------------------------------------------------------------------
#* Punto de entrada de ejecución
#*--------------------------------------------------------------------------
os.system("clear")
print("Ejemplo de taller para patrón prototipo")

dt = datetime.now()
print('Comienzo creando un objeto Shopkeeper NPC: ', dt)
shopkeeper = Shopkeeper(180, 22, 5, 8)

dt = datetime.now()
print('Finaliza la creación del objeto Shopkeeper NPC: ', dt)
print('Atributos: ' + ', '.join("%s: %s" % item for item in vars(shopkeeper).items()))

dt = datetime.now()
print('Instanciando ahora trader: ', dt)
for i in range(20):  # Genera 20 anidamientos
    shopkeeper = shopkeeper.clone()  # Clonar el objeto existente
    dt = datetime.now()
    print(f'Creo Shopkeeper NPC {i} at: ', dt)

dt = datetime.now()
print('Finalizó de crear el grupo trader: ', dt)
