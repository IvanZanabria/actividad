def retroceder(historial, pasos):
    
    # Caso base 1: ya no hay pasos que retroceder
    if pasos == 0:
        return historial
    
    # Caso base 2: historial vacío
    if len(historial) == 0:
        return historial
    
    # Sacar la última página visitada
    pagina = historial.pop()
    print("Retrocediendo desde:", pagina)
    
    # Caso base 3: si encontramos Error 404
    if "Error 404" in pagina:
        print("Se encontró una página de Error 404. Proceso detenido.")
        return historial
    
    # Llamada recursiva
    return retroceder(historial, pasos - 1)


# Historial de navegación
mi_navegacion = [
    "google.com",
    "uniminuto.edu",
    "Error 404: Campus Virtual",
    "github.com",
    "stackoverflow.com"
]

# Ejecutar
resultado = retroceder(mi_navegacion, 3)

print("\nHistorial final:")
print(resultado)