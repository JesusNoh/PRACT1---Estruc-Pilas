class Pila:
    def __init__(self, capacidad=8):
        self.capacidad = capacidad
        self.elementos = []
        self.tope = 0

    def insertar(self, elemento):
        if self.tope < self.capacidad:
            self.elementos.append(elemento)
            self.tope += 1
            print(f'Insertar({elemento}): {self.elementos} | TOPE={self.tope}')
        else:
            print(f'Error: Desbordamiento al intentar insertar {elemento}')

    def eliminar(self):
        if self.tope > 0:
            elemento = self.elementos.pop()
            self.tope -= 1
            print(f'Eliminar(): {elemento} | Estado: {self.elementos} | TOPE={self.tope}')
        else:
            print('Error: Subdesbordamiento al intentar eliminar')

# Crear pila
pila = Pila()

# Realiza las operaciones
pila.insertar('X')  # a
pila.insertar('Y')  # b
pila.eliminar()      # c
pila.eliminar()      # d
pila.eliminar()      # e (subdesbordamiento)
pila.insertar('V')   # f
pila.insertar('W')   # g
pila.eliminar()      # h
pila.insertar('R')   # i

# Estado final de la pila
print(f'Número de elementos en la pila: {pila.tope}')