# Función para leer la gramática desde un archivo de texto
def leer_gramatica(archivo):
    gramatica = {}
    with open(archivo, 'r') as file:
        for linea in file:
            linea = linea.strip()
            if '->' in linea:
                no_terminal, producciones = linea.split('->')
                no_terminal = no_terminal.strip()
                producciones = [p.strip() for p in producciones.split('|')]
                gramatica[no_terminal] = producciones
    return gramatica

# Función para escribir la gramática transformada en un archivo
def escribir_gramatica(gramatica, archivo_salida):
    with open(archivo_salida, 'w') as file:
        for no_terminal, producciones in gramatica.items():
            producciones_str = " | ".join(producciones)
            file.write(f"{no_terminal} -> {producciones_str}\n")

# Función para eliminar recursividad por la izquierda directa
def eliminar_recursividad_izquierda(gramatica, no_terminal):
    producciones = gramatica[no_terminal]
    recursivas = []
    no_recursivas = []
    
    # Clasificar las producciones en recursivas y no recursivas
    for produccion in producciones:
        if produccion.startswith(no_terminal):
            recursivas.append(produccion[len(no_terminal):])  # α
        else:
            no_recursivas.append(produccion)  # β

    # Si hay producciones recursivas por la izquierda
    if recursivas:
        nuevo_no_terminal = no_terminal + "'"
        gramatica[no_terminal] = [b + nuevo_no_terminal for b in no_recursivas]
        gramatica[nuevo_no_terminal] = [a + nuevo_no_terminal for a in recursivas] + ['lambda']

# Función para eliminar recursividad indirecta
def eliminar_recursividad_indirecta(gramatica):
    no_terminales = list(gramatica.keys())
    
    for i in range(len(no_terminales)):
        nt_i = no_terminales[i]
        
        # Reemplazar recursiones indirectas
        for j in range(i):
            nt_j = no_terminales[j]
            nuevas_producciones = []
            
            for produccion in gramatica[nt_i]:
                if produccion.startswith(nt_j):  # Recursividad indirecta
                    # Reemplazar nt_j en nt_i
                    for produccion_j in gramatica[nt_j]:
                        nuevas_producciones.append(produccion_j + produccion[len(nt_j):])
                else:
                    nuevas_producciones.append(produccion)
            gramatica[nt_i] = nuevas_producciones
        
        # Luego de eliminar recursividad indirecta, eliminamos recursividad directa
        eliminar_recursividad_izquierda(gramatica, nt_i)

# Función para procesar la gramática y preservar la jerarquía de operaciones
def procesar_gramatica(archivo_entrada, archivo_salida):
    # Leer la gramática desde el archivo
    gramatica = leer_gramatica(archivo_entrada)
    
    # Eliminar recursividad indirecta
    eliminar_recursividad_indirecta(gramatica)

    # Ahora, aplicamos la reestructuración necesaria
    for no_terminal in list(gramatica.keys()):
        eliminar_recursividad_izquierda(gramatica, no_terminal)

    # Escribir la gramática transformada en el archivo de salida
    escribir_gramatica(gramatica, archivo_salida)

# Ejecución del programa
if __name__ == "__main__":
    archivo_entrada = "gramatica.txt"
    archivo_salida = "gramatica_sin_recursividad.txt"
    
    procesar_gramatica(archivo_entrada, archivo_salida)
    print(f"Gramática procesada guardada en {archivo_salida}")
