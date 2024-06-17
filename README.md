# Reto_12
El siguiente reto tiene propuestas de solución a los puntos que componen el reto 12

## 2. Procesar el <a href="https://www.py4e.com/code3/mbox.txt">archivo</a> y extraer:
 
### 2.1 Cantidad de vocales
```python
# Se declaran variables
contenido : str
texto_vocales_minusculas : str
vocales : str
cantidad_a : int
cantidad_e : int
cantidad_i : int
cantidad_o : int
cantidad_u : int
suma : int
variables : list

# Se abre archivo 
archivo = open("archivo.txt")

def solo_vocales(archivo) -> str:
    """
    La función recibe un archivo como entrada y devuelve un string que
    contiene todas las vocales minúsculas del archivo.

    Args:
        archivo: Archivo que contiene el texto a procesar.

    Returns:
        texto_vocales_minusculas (str): Contiene todas las vocales minúsculas
        del archivo.
    """

    # Se almacena contenido del archivo en formato str
    contenido = archivo.read()

    # Se crea variable para almacenar las vocales
    texto_vocales_minusculas = ""

    # Se crea variable para filtrar contenido de variable "contenido" 
    vocales = "aeiouAEIOU"
    
    for caracter in contenido:
        # Se comprueba si caracter es una vocal
        if caracter in vocales:

            # Si se cumple condución el caracter se añade a variable
            texto_vocales_minusculas += caracter.lower()

    # Se retorna str con todas las vocales del archivo
    return texto_vocales_minusculas

def contar_vocales(texto_vocales_minusculas) -> int:
    """
    La función recibe un string que contiene vocales minúsculas y devuelve 
    una tupla que contiene la cantidad de cada vocal que se encuentran en 
    el string.

    Args:
        texto_vocales_minusculas: String que contiene vocales minúsculas.

    Returns:
        cantidad_a (int): Cantidad de vocal a en el string.

        cantidad_e (int): Cantidad de vocal e en el string. 
        
        cantidad_i (int): Cantidad de vocal i en el string.

        cantidad_o (int): Cantidad de vocal o en el string.
        
        cantidad_u (int): Cantidad de vocal u en el string.
    """

    cantidad_a = 0
    cantidad_e = 0
    cantidad_i = 0
    cantidad_o = 0
    cantidad_u = 0

    for caracter in texto_vocales_minusculas:
        # Se suman indidualmente las vocales del texto
        cantidad_a += caracter.count("a")
        cantidad_e += caracter.count("e")
        cantidad_i += caracter.count("i")
        cantidad_o += caracter.count("o")
        cantidad_u += caracter.count("u")

    # Se retorna cantidad total de cada vocal en el archivo
    return cantidad_a, cantidad_e, cantidad_i, cantidad_o, cantidad_u

if __name__ == "__main__":
    # Se llama función y se retorna texto con solo las vocales 
    texto_vocales_minusculas = solo_vocales(archivo)

    # Se llama función y se retorna la cantidad de cada vocal en el texto
    cantidad_a, cantidad_e, cantidad_i, cantidad_o, cantidad_u = contar_vocales(
                                                                                texto_vocales_minusculas)
    
    variables = [cantidad_a, cantidad_e, cantidad_i, cantidad_o, cantidad_u]

    # Se obtiene cantidad total de vocales en el texto
    suma = sum(variables)

    # Se imprimen resultados
    print(f"La vocal a aparece {cantidad_a} veces")
    print(f"La vocal e aparece {cantidad_e} veces")
    print(f"La vocal i aparece {cantidad_i} veces")
    print(f"La vocal o aparece {cantidad_o} veces")
    print(f"La vocal u aparece {cantidad_u} veces")
    print(f"La cantidad total de vocales {suma}")
    
# Se cierra archivo
archivo.close()
```

### 2.2 Cantidad de consonantes
```python
# Se declaran variables
contenido : str
consonantes_minusculas : str
vocales : str
suma : int
total_consonantes : int
variables : list

# Se abre archivo 
archivo = open("archivo.txt")

def solo_consonantes(archivo) -> str:
    """
    Esta función recibe un archivo como entrada y devuelve un string 
    que contiene todas las consonantes minúsculas del archivo.

    Args:
        archivo: Archivo que contiene el texto a procesar.

    Returns:
        consonantes_minusculas (str): Contiene todas las consonantes minúsculas
        del archivo.
    """
    
    # Se almacena contenido del archivo en formato str
    contenido = archivo.read()

    # Se crea variable para almacenar las consonantes
    consonantes_minusculas = ""

    # Se crea variable para filtrar contenido de variable "contenido" 
    vocales = "aeiouAEIOU"

    for caracter in contenido:
        # Se convierten los caracteres del archivo a minuscula
        caracter = caracter.lower()

        # Comprobación si caracter es una letra minúscula con ASCII
        if 98 <= ord(caracter) and ord(caracter) <= 122 and caracter not in  vocales:

            # Si se cumple condución el caracter se añade a variable
            consonantes_minusculas += caracter

    # Se retorna str con todas las consonantes del archivo
    return consonantes_minusculas

def contar_consonantes(consonantes_minusculas) -> int:
    """
    La función recibe un string que contiene consonantes minúsculas y 
    devuelve un entero que representa la cantidad total de consonantes 
    que se encuentran en el string.

    Args:
        consonantes_minusculas (str): Contiene consonantes minúsculas. 

    Returns:
        total_consonantes (int): Cantidad total de consonantes en el string.
    """

    # Se cuenta la cantidad todal de consonantes en el archivo
    total_consonantes = len(consonantes_minusculas)

    # Se retorna la cantidad de consonantes en el archivo
    return total_consonantes

if __name__ == "__main__":
    # Se llama función y se retorna texto con solo las consonantes 
    consonantes_minusculas = solo_consonantes(archivo)

    # Se llama función y se retorna la cantidad de consonantes en el texto
    total_consonantes = contar_consonantes(consonantes_minusculas)
    
    # Se imprime resultado con la cantidad todal de consonantes 
    print(f"La cantidad total de consonantes es {total_consonantes}")
    
# Se cierra archivo
archivo.close()
```

### 2.3 Listado de las 50 palabras que más se repiten
```python
# Se declaran variables
texto_para_lista: str
contenido: str
caracter: str
palabra_actual: str
lista: list
palabras: list
numeros: list
veces_palabras: list
i: int
contador: int
min_indice: int
max_indice: int

def palabras_archivo(contenido) -> list:
    """
    Esta función toma una cadena de texto, la procesa y devuelve una lista 
    con las palabras de la cadena.

    Args:
    contenido (str): Cadena de texto que se va a procesar.

    Returns:
    lista (list): Lista de palabras procesadas y capitalizadas.
    """

    # Se inicializan variables
    texto_para_lista = ""
    lista = []
    
    # Se recorren y minimizan caracteres de cadena de texto
    for caracter in contenido:
        caracter = caracter.lower()

        # Si caracteres son letras de alfabeto en inglés se añaden a str
        if 97 <= ord(caracter) and ord(caracter) <= 122:
            texto_para_lista += caracter

        # Si str contiene una letra este se vacía, ya que no cuenta como palabra
        elif len(texto_para_lista) == 1:
            texto_para_lista = ""

        # Se añade palabra a lista capitalizada
        elif texto_para_lista:  
            lista.append(texto_para_lista.capitalize())
            
            # Se vacía str para añadir la siguiente palabra
            texto_para_lista = ""  


    # Condicional para añadir última palabra si no hay caracteres después
    if texto_para_lista:  
        lista.append(texto_para_lista.capitalize())

        # Se vacía str para añadir la siguiente palabra
        texto_para_lista = ""  

    return lista

def contar_palabras(lista) -> list:
    """
    Cuenta las palabras más frecuentes en una lista y las devuelve en dos
    listas.
    
    Args:
        lista (list): Lista que contiene palabras de la cadena de texto.

    Returns:
        palabras (list): Contiene las 50 palabras más frecuentes
        
        numeros (list): Contiene la frecuencia de cada palabra
    """

    # Se inicializan listas 
    palabras = []
    numeros = []

    # Se ordena la para que palabras iguales estén juntas
    lista.sort()

    # Se recorren palabras de la lista
    i = 0
    while i < len(lista):
        palabra_actual = lista[i]
        contador = 0

        # Se cuenta la frecuencia de la palabra actual
        while i < len(lista) and lista[i] == palabra_actual:
            contador += 1
            i += 1

        # Se añaden hasta 50 palabras y números a listas 
        if len(palabras) < 50:
            palabras.append(palabra_actual)
            numeros.append(contador)
        
        elif contador > numeros[numeros.index(min(numeros))]:

            # Se encuentra el mínimo en numeros
            min_indice = numeros.index(min(numeros))

            # Se remplaza el mínimo y su palabra
            palabras[min_indice] = palabra_actual
            numeros[min_indice] = contador

    return palabras, numeros

def ordenar_palabras(palabras, numeros) -> list:
    """
    Ordena las palabras más frecuentes en una lista de mayor a menor frecuencia.

    Args:
        palabras (list): Lista que contiene las 50 palabras más frecuente en la
        cadena de texto.

        numeros (list): Lista que contiene la frecuencia de cada palabra en la
        lista `palabras`

    Returns:
        veces_palabras (list): Lista que contiene las 50 palabras más
        frecuentes, ordenadas de mayor a menor frecuencia.
    """

    # Se inicializan varaibles
    veces_palabras = []
    contador = 0

    while contador < 50:
        # Se extrae el índice del número máximo
        max_indice = numeros.index(max(numeros))

        # Se añade el número máximo y su palabra al final de cada fila
        veces_palabras.append(palabras[max_indice])
        veces_palabras.append(max(numeros))

        # Se remueve el máximo y se añade 0 en su posición para seguir iterando
        numeros.remove(max(numeros))
        numeros.insert(max_indice, 0)

        contador += 1
    
    return veces_palabras

def ordenar_palabras_texto_corto(palabras, numeros) -> list:
    """
    Ordena las palabras más frecuentes en una lista de mayor a menor frecuencia.

    Args:
        palabras (list): Lista que contiene las palabras más frecuente en la
        cadena de texto.

        numeros (list): Lista que contiene la frecuencia de cada palabra en la
        lista `palabras`

    Returns:
        veces_palabras (list): Lista que contiene las palabras más
        frecuentes, ordenadas de mayor a menor frecuencia.
    """

    # Se inicializan varaibles
    veces_palabras = []
    contador = 0

    while contador < len(numeros):
        # Se extrae el índice del número máximo
        max_indice = numeros.index(max(numeros))

        # Se añade el número máximo y su palabra al final de cada fila
        veces_palabras.append(palabras[max_indice])
        veces_palabras.append(max(numeros))

        # Se remueve el máximo y se añade 0 en su posición para seguir iterando
        numeros.remove(max(numeros))
        numeros.insert(max_indice, 0)

        contador += 1
    
    return veces_palabras

if __name__ == "__main__":
    # Se almacena el objeto de archivo abierto en variable
    archivo = open("archivo.txt")

    # Se lee archivo y almacena en variable "contenido" como cadena de texto
    contenido = archivo.read()

    # Se llama función para obtener las palabras del archivo
    lista = palabras_archivo(contenido)
    
    # Se llama función para contar cantidad de apariciones de cada palabra
    palabras, numeros = contar_palabras(lista)

    # Se llama función de acuerdo a cantidad de palabras tenga el archivo
    if 50 <= len(numeros):
        veces_palabras = ordenar_palabras(palabras, numeros)
    else:
        veces_palabras = ordenar_palabras_texto_corto(palabras, numeros)
    
    print("Listado de las 50 palabras que más se repiten")
    print("----------------------------------------------")

    # Se imprime palabra y su cantidad de apariciones en el archivo de texto
    for x in range(0, len(veces_palabras), 2):
        print(f"Palabra: {veces_palabras[x]} | Apariciones: {veces_palabras[x + 1]}")

    archivo.close()
```