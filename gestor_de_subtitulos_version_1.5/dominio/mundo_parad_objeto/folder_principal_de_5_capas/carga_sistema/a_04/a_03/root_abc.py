
""" Crea un nuevo nombre para un archivo autentico y unico """


"=========================================="

from mas_bajo_nivel.super_objeto import sys_drive

"=========================================="

def saca_root(letra_actual):

        nomenc= sys_drive.ruta_d_abc + "\\words_learned_"
        termi= str(letra_actual) + ".txt"

        return nomenc + termi

def toma_la_dir(letra_ac):

    letra_act= str(letra_ac)
    letra_actual= letra_act.lower()

    if (letra_actual == "a") or (letra_actual == "A"):
        return saca_root(letra_actual)
    if (letra_actual == "b") or (letra_actual == "B"):
        return saca_root(letra_actual)
    if (letra_actual == "c") or (letra_actual == "C"):
        return saca_root(letra_actual)
    if (letra_actual == "d") or (letra_actual == "D"):
        return saca_root(letra_actual)
    if (letra_actual == "e") or (letra_actual == "E"):
        return saca_root(letra_actual)

    if (letra_actual == "f") or (letra_actual == "F"):
        return saca_root(letra_actual)
    if (letra_actual == "g") or (letra_actual == "G"):
        return saca_root(letra_actual)
    if (letra_actual == "h") or (letra_actual == "H"):
        return saca_root(letra_actual)
    if (letra_actual == "i") or (letra_actual == "I"):
        return saca_root(letra_actual)
    if (letra_actual == "j") or (letra_actual == "J"):
        return saca_root(letra_actual)

    "................................"

    if (letra_actual == "k") or (letra_actual == "K"):
        return saca_root(letra_actual)
    if (letra_actual == "l") or (letra_actual == "L"):
        return saca_root(letra_actual)
    if (letra_actual == "m") or (letra_actual == "M"):
        return saca_root(letra_actual)
    if (letra_actual == "n") or (letra_actual == "N"):
        return saca_root(letra_actual)
    if (letra_actual == "o") or (letra_actual == "O"):
        return saca_root(letra_actual)

    if (letra_actual == "p") or (letra_actual == "P"):
        return saca_root(letra_actual)
    if (letra_actual == "q") or (letra_actual == "Q"):
        return saca_root(letra_actual)
    if (letra_actual == "r") or (letra_actual == "R"):
        return saca_root(letra_actual)
    if (letra_actual == "s") or (letra_actual == "S"):
        return saca_root(letra_actual)
    if (letra_actual == "t") or (letra_actual == "T"):
        return saca_root(letra_actual)

    "................................"

    if (letra_actual == "u") or (letra_actual == "U"):
        return saca_root(letra_actual)
    if (letra_actual == "v") or (letra_actual == "V"):
        return saca_root(letra_actual)
    if (letra_actual == "w") or (letra_actual == "W"):
        return saca_root(letra_actual)
    if (letra_actual == "x") or (letra_actual == "X"):
        return saca_root(letra_actual)
    if (letra_actual == "y") or (letra_actual == "Y"):
        return saca_root(letra_actual)

    if (letra_actual == "z") or (letra_actual == "Z"):
        return saca_root(letra_actual)

