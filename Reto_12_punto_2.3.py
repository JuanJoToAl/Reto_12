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