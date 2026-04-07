from collections import deque

# Grafo del metro
metro = {
    "Portal Norte":   ["Toberín"],
    "Toberín":        ["Portal Norte", "Calle 142"],
    "Calle 142":      ["Toberín", "Calle 127"],
    "Calle 127":      ["Calle 142", "Pepe Sierra", "Alcalá"],
    "Pepe Sierra":    ["Calle 127", "Niza"],
    "Alcalá":         ["Calle 127", "Calle 100"],
    "Niza":           ["Pepe Sierra", "Calle 100"],
    "Calle 100":      ["Alcalá", "Niza", "Virrey"],
    "Virrey":         ["Calle 100", "Centro"],
    "Centro":         ["Virrey", "Portal Sur"],
    "Portal Sur":     ["Centro"],
}

# Función BFS para ruta mínima
def ruta_minima(grafo, origen, destino):
    if origen not in grafo or destino not in grafo:
        return None

    if origen == destino:
        return [origen]

    visitados = set()
    cola = deque([[origen]])  # Cada elemento es un camino completo

    while cola:
        camino = cola.popleft()
        nodo_actual = camino[-1]

        if nodo_actual == destino:
            return camino

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            for vecino in grafo[nodo_actual]:
                if vecino not in visitados:
                    nuevo_camino = camino + [vecino]
                    cola.append(nuevo_camino)

    return None

print("Ruta 1:", ruta_minima(metro, "Portal Norte", "Centro"))

print("Ruta 1:", ruta_minima(metro, "Portal Norte", "Portal Norte"))