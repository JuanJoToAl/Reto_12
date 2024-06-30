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

def contar_vocales(texto_vocales_minusculas : str) -> int:
    """
    La función recibe un string que contiene vocales minúsculas y devuelve 
    una tupla que contiene la cantidad de cada vocal que se encuentran en 
    el string.

    Args:
        texto_vocales_minusculas (str): Contiene vocales minúsculas.

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