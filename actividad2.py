class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar(nodo.derecha, valor)
        return nodo

    #  a) mínimo
    def minimo(self):
        if self.raiz is None:
            return None

        actual = self.raiz

        while actual.izquierda is not None:
            actual = actual.izquierda

        return actual.valor

    #  b) máximo
    def maximo(self):
        if self.raiz is None:
            return None

        actual = self.raiz

        while actual.derecha is not None:
            actual = actual.derecha

        return actual.valor

    #  c) top N (mayores)
    def top_n(self, n):
        resultado = []

        def recorrido_inverso(nodo):
            if nodo is None or len(resultado) >= n:
                return

            # derecha → raíz → izquierda
            recorrido_inverso(nodo.derecha)

            if len(resultado) < n:
                resultado.append(nodo.valor)

            recorrido_inverso(nodo.izquierda)

        recorrido_inverso(self.raiz)
        return resultado


#  PRUEBA
torneo = BST()
puntos = [3200, 4100, 1800, 5000, 2700, 3900, 4600]

for p in puntos:
    torneo.insertar(p)

print("Mínimo:", torneo.minimo())    
print("Máximo:", torneo.maximo())    
print("Top 3:", torneo.top_n(3))