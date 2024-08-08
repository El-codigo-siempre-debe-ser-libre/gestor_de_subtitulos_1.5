
""" Confirmo los archivos que guardan las palabras
    segun su letra """


"==================================================="

from dominio.mundo_parad_objeto.folder_principal_de_5_capas.carga_sistema.utileria import abcd

"==================================================="

def saca_root(letra_actual):

        nomenc= "c:\\study_english\\my_dictionary\\words_learned_"
        termi= str(letra_actual) + ".txt"

        return nomenc + termi

def toma_la_dir(letra_actual):

    if letra_actual == "a":
        return saca_root(letra_actual)
    if letra_actual == "b":
        return saca_root(letra_actual)
    if letra_actual == "c":
        return saca_root(letra_actual)
    if letra_actual == "d":
        return saca_root(letra_actual)
    if letra_actual == "e":
        return saca_root(letra_actual)

    if letra_actual == "f":
        return saca_root(letra_actual)
    if letra_actual == "g":
        return saca_root(letra_actual)
    if letra_actual == "h":
        return saca_root(letra_actual)
    if letra_actual == "i":
        return saca_root(letra_actual)
    if letra_actual == "j":
        return saca_root(letra_actual)

    "................................"

    if letra_actual == "k":
        return saca_root(letra_actual)
    if letra_actual == "l":
        return saca_root(letra_actual)
    if letra_actual == "m":
        return saca_root(letra_actual)
    if letra_actual == "n":
        return saca_root(letra_actual)
    if letra_actual == "o":
        return saca_root(letra_actual)

    if letra_actual == "p":
        return saca_root(letra_actual)
    if letra_actual == "q":
        return saca_root(letra_actual)
    if letra_actual == "r":
        return saca_root(letra_actual)
    if letra_actual == "s":
        return saca_root(letra_actual)
    if letra_actual == "t":
        return saca_root(letra_actual)

    "................................"

    if letra_actual == "u":
        return saca_root(letra_actual)
    if letra_actual == "v":
        return saca_root(letra_actual)
    if letra_actual == "w":
        return saca_root(letra_actual)
    if letra_actual == "x":
        return saca_root(letra_actual)
    if letra_actual == "y":
        return saca_root(letra_actual)

    if letra_actual == "z":
        return saca_root(letra_actual)

def confirmando_letras():

    reto= abcd()

    for i in reto:  # sino existe algun fichero lo creo 

        root= str(toma_la_dir(i))

        try:

            vamos_1= open(root, "r")
            vamos_1.read()
            vamos_1.close()

        except FileNotFoundError:

            vamos_2= open(root, "w")
            vamos_2.write("")
            vamos_2.close()

