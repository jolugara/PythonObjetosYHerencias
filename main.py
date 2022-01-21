from Persona import Persona
from Empleado import Empleado

class Coche():
    def __init__(self, rueda, gasolina, color):
        self.__rueda = rueda
        self.__gasolina = gasolina
        self.__color = color


    def getRueda(self):
        return self.__rueda
    def setRueda(self, rueda):
        self.__rueda = rueda

    def getGasolina(self):
        return self.__gasolina
    def setGasolina(self, gasolina):
        self.__gasolina = gasolina

    def getColor(self):
        return self.__color
    def setColor(self, color):
        self.__color = color



ferrari = Coche(4, "gasoil", "rojo")
print(ferrari.getRueda(),ferrari.getGasolina(),ferrari.getColor())

PersonaMain = Persona("Ale", 45, "Ilerna")

PersonaMain.descripcion()

e = Empleado(1500, 2, "pepe", 20, "Sevilla")

e.descripcion()