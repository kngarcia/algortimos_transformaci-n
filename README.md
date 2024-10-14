# Eliminación de Recursividad Izquierda en Gramáticas

Este proyecto implementa un algoritmo para eliminar la recursividad directa por la izquierda de gramáticas. La recursividad izquierda representa un problema en los analizadores sintácticos descendentes LL(1), por lo que es esencial transformarlas en una forma que pueda ser manejada por tales analizadores.

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Cómo Funciona](#cómo-funciona)
- [Instrucciones de Uso](#instrucciones-de-uso)
- [Ejemplo de Uso](#ejemplos-de-uso)

## Descripción del Proyecto

Este algoritmo toma como entrada una gramática en un archivo de texto y transforma la gramática eliminando tanto la recursividad directa como la indirecta. Los resultados se guardan en un nuevo archivo de texto, permitiendo que la gramática resultante sea utilizada en un análisis sintáctico LL(1).

## Cómo Funciona

El algoritmo se compone de las siguientes funciones clave:

1. **leer_gramatica**: Lee la gramática desde un archivo de texto y la convierte en un diccionario de producciones.
2. **escribir_gramatica**: Escribe la gramática transformada en un archivo de salida.
3. **eliminar_recursividad_izquierda**: Elimina la recursividad izquierda directa de una gramática.
4. **eliminar_recursividad_indirecta**: Elimina la recursividad indirecta de una gramática.
5. **procesar_gramatica**: Función principal que ejecuta el proceso de eliminación de recursividad.

### 1. `leer_gramatica(archivo)`

**Descripción**: Esta función lee una gramática desde un archivo de texto. La gramática debe estar en el formato `A -> producciones`, donde `A` es un no terminal y `producciones` son las diferentes producciones separadas por el símbolo `|`.

**Funcionamiento**:
- Abre el archivo especificado en modo lectura.
- Lee cada línea del archivo y separa el no terminal de sus producciones.
- Almacena la información en un diccionario, donde las claves son los no terminales y los valores son listas de sus respectivas producciones.

### 2. `escribir_gramatica(gramatica, archivo_salida)`
**Descripción**: Esta función guarda la gramática transformada en un archivo de salida.

**Funcionamiento**:
- Abre el archivo especificado en modo escritura.
- Recorre el diccionario que representa la gramática.
- Para cada no terminal, escribe sus producciones en el formato A -> producciones, separando múltiples producciones con el símbolo |.

### 3. `eliminar_recursividad_izquierda(gramatica, no_terminal)`

**Descripción**: Elimina la recursividad directa por la izquierda de un no terminal específico en la gramática.

**Funcionamiento**:
- Obtiene las producciones del no terminal.
- Clasifica las producciones en recursivas (que empiezan con el mismo no terminal) y no recursivas.
- Si hay producciones recursivas, crea un nuevo no terminal (por ejemplo, A') y redefine las producciones del no terminal original para que incluyan las nuevas         producciones sin recursión.
- Las producciones recursivas se transforman en un formato que utiliza el nuevo no terminal y se agrega una producción que representa el caso base (generalmente una producción vacía).

### 4. `eliminar_recursividad_indirecta(gramatica)`

**Descripción**: Elimina la recursividad indirecta de toda la gramática.

**Funcionamiento**:

- Recorre la lista de no terminales.
- Para cada no terminal, verifica si tiene producciones que comienzan con otros no terminales, lo que puede llevar a una recursión indirecta.
- Si se encuentra una recursión indirecta, reemplaza la producción del no terminal que contiene la recursión con las producciones de los no terminales implicados,      ajustando las producciones para eliminar la recursión.
- Llama a eliminar_recursividad_izquierda después de procesar las recursiones indirectas para asegurarse de que no haya recursividad directa restante.

### 5. procesar_gramatica(archivo_entrada, archivo_salida)

**Descripción**: Esta es la función principal que coordina todo el proceso de transformación de la gramática.

**Funcionamiento**:

- Llama a leer_gramatica para cargar la gramática desde un archivo.
- Llama a eliminar_recursividad_indirecta para eliminar cualquier tipo de recursividad.
- Finalmente, llama a escribir_gramatica para guardar la gramática transformada en un nuevo archivo.

## Instrucciones de Uso

Para utilizar el algoritmo de eliminación de recursividad en gramáticas, sigue estos pasos:

1. **Prepara la Gramática**:
   - Crea un archivo de texto (por ejemplo, `gramatica.txt`) que contenga la gramática que deseas procesar.
   - Asegúrate de que la gramática esté en el formato correcto, con cada producción en una nueva línea. Por ejemplo:
     ```
     E -> E + T | E - T | T
     T -> T * F | T / F | F
     F -> ( E ) | id
     ```

2. **Ejecuta el Script**:
   - Asegúrate de tener Python instalado en tu sistema.
   - Abre una terminal o línea de comandos.
   - Navega hasta el directorio donde se encuentra el archivo Python (por ejemplo, `eliminar_recursividad.py`).
   - Ejecuta el script con el siguiente comando:
     ```bash
     python eliminar_recursividad.py
     ```
   - El script procesará la gramática y generará un archivo de salida (por ejemplo, `gramatica_sin_recursividad.txt`), que contendrá la gramática transformada sin recursión.

3. **Revisa la Salida**:
   - Abre el archivo de salida generado para ver la gramática sin recursividad.
   - La salida mostrará la gramática en un formato adecuado para el análisis sintáctico descendente LL(1).

## Ejemplo de Uso

### Paso 1: Preparar la Gramática

Crea un archivo de texto llamado `gramatica.txt` y añade de la carpeta de `casos_de_prueba` alguna gramática con recursión izquierda directa, para este ejemplo utilizaremos el caso de prueba 3:
```
E -> E + T | E - T | T
T -> T * F | T / F | F
F -> ( E ) | id
```
### Paso 2: Ejecutar el Script

Una vez que hayas creado el archivo, abre una terminal y navega hasta el directorio donde se encuentra el archivo `eliminar_recursividad.py`. Ejecuta el script con el siguiente comando:

```bash
python eliminar_recursividad.py
```

### Paso 3: Revisar el Archivo de Salida

Después de ejecutar el script, se generará un archivo llamado gramatica_sin_recursividad.txt. Abre este archivo para ver la gramática transformada, que debería verse así:
```
E -> T E'
E' -> + T E' | - T E' | λ
T -> F T'
T' -> * F T' | / F T' | λ
F -> ( E ) | id
``

