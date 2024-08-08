
""" Aqui desarrollo el ingreso y extraccion de words desde
    el archivo unico a/o los multiples """


"==================================================="

from dominio.mundo_parad_objeto.folder_principal_de_5_capas.afianza.b_04.ingresos import Metodo_de_ingreso as meti
from dominio.mundo_parad_objeto.folder_principal_de_5_capas.carga_sistema.a_04.cargando import Metodo_de_extraccion as mete

from mas_bajo_nivel.super_objeto import pez

"==================================================="

def metodo(tipo, unid): 

    if tipo  == False:  # ingresos
        agr= meti()

        if unid == True:
            agr.general()
        else:

            prima= open("c:\\study_english\\my_dictionary\\ingreso\\words_learned.txt", "r")
            lalet= prima.read()
            prima.close()

            try:    # emplear el prgma por primera vez
                la_letra= lalet[0]
            
            except IndexError:
                
                pez.mensaje.config(text= "No tienes palabras en la base_dato. dirigete a \nC:\study_english\my_dictionary\ingreso\words_learned.txt\nE ingresa algunas palabras")

                return
            
            agr.en_particular(la_letra)

    if tipo == True:    # cargar y mostrar

        ext= mete()

        if unid == True:
            ext.general()
        else:
            ext.en_particular()

