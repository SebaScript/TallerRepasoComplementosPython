from dataclasses import dataclass


@dataclass
class Elemento:

    nombre: str

    def __eq__(self, otro):
        n1 = self.nombre
        n2 = otro.nombre
        return n1 == n2


class Conjunto:

    contador = 0

    def __init__(self, nombre: str):
        self.elementos: list[Elemento] = []
        self.nombre = nombre
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento: Elemento) -> bool:
        for e in self.elementos:
            if e.nombre == elemento.nombre:
                return True
        return False

    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for e in otro_conjunto.elementos:
            if not self.contiene(e):
                self.agregar_elemento(otro_conjunto)

    def __add__(self, otro_conjunto):
        resultado = Conjunto(f"{self.nombre} + {otro_conjunto.nombre}")
        resultado.unir(self)
        resultado.unir(otro_conjunto)
        return resultado

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nombre = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        resultado = Conjunto(nombre)
        for elemento in conjunto1.elementos:
            if conjunto2.contiene(elemento):
                resultado.agregar_elemento(elemento)
        return resultado

    def __str__(self):
        elementos_str = ""
        for e in self.elementos:
            elementos_str += f"{e.nombre}, "
        return f"Conjunto {self.nombre}: ({elementos_str})"
