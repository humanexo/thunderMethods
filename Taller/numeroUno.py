from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.__id = Conjunto.contador
        Conjunto.contador += 1
        self.nombre = nombre
        self.elementos = []

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento: Elemento) -> bool:
        return elemento in self.elementos

    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.elementos:
            self.agregar_elemento(elemento)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNION {otro_conjunto.nombre}")
        nuevo_conjunto.unir(self)
        nuevo_conjunto.unir(otro_conjunto)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):

        elementos_comunes = []
        for elemento in conjunto1.elementos:
            if elemento in conjunto2.elementos:
                elementos_comunes.append(elemento)
        nuevo_conjunto = Conjunto(f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}")
        for elemento in elementos_comunes:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto


    def __str__(self):

        elementos_str = ', '.join([elem.nombre for elem in self.elementos])
        return f"Conjunto: ({elementos_str})"
