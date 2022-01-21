class Persona():

    def __init__(self, nombre, edad, lugar):
        self.__nombre = nombre
        self.__edad = edad
        self.__lugar = lugar

    def descripcion(self):
        print(f"mi nombre es {self.__nombre}")