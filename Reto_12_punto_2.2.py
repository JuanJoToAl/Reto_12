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
        String que contiene todas las consonantes minúsculas del archivo.
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
        if 98 <= ord(caracter) and ord(caracter) <= 122:

            # Se comprueba si el caracter es una consonante
            if caracter not in  vocales:

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
        consonantes_minusculas: String que contiene consonantes minúsculas. 

    Returns:
        Entero que representa la cantidad total de consonantes en el string.
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