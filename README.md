# Eliminación de Recursividad Izquierda en Gramáticas

Este proyecto implementa un algoritmo para eliminar la recursividad directa por la izquierda de gramáticas. La recursividad izquierda representa un problema en los analizadores sintácticos descendentes LL(1), por lo que es esencial transformarlas en una forma que pueda ser manejada por tales analizadores.

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Cómo Funciona](#cómo-funciona)
- [Instrucciones de Uso](#instrucciones-de-uso)
- [Ejemplos de Uso](#ejemplos-de-uso)
  - [Caso de Prueba 3: Recursividad Directa Compleja](#caso-de-prueba-3-recursividad-directa-compleja)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Descripción del Proyecto

Este algoritmo toma como entrada una gramática en un archivo de texto y transforma la gramática eliminando tanto la recursividad directa como la indirecta. Los resultados se guardan en un nuevo archivo de texto, permitiendo que la gramática resultante sea utilizada en un análisis sintáctico LL(1).

## Cómo Funciona

El algoritmo se compone de las siguientes funciones clave:

1. **leer_gramatica**: Lee la gramática desde un archivo de texto y la convierte en un diccionario de producciones.
2. **escribir_gramatica**: Escribe la gramática transformada en un archivo de salida.
3. **eliminar_recursividad_izquierda**: Elimina la recursividad izquierda directa de una gramática.
4. **eliminar_recursividad_indirecta**: Elimina la recursividad indirecta de una gramática.
5. **procesar_gramatica**: Función principal que ejecuta el proceso de eliminación de recursividad.

### 1. `leer_gramatica(archivo)

**Descripción**: Esta función lee una gramática desde un archivo de texto. La gramática debe estar en el formato `A -> producciones`, donde `A` es un no terminal y `producciones` son las diferentes producciones separadas por el símbolo `|`.

**Funcionamiento**:
- Abre el archivo especificado en modo lectura.
- Lee cada línea del archivo y separa el no terminal de sus producciones.
- Almacena la información en un diccionario, donde las claves son los no terminales y los valores son listas de sus respectivas producciones.






