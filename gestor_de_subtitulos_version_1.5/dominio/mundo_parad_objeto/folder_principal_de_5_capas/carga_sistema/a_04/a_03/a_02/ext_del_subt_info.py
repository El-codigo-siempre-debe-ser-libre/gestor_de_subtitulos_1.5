
""" comienzo a extraer toda la informacion
    del archivo con los subtitulos """


"==================================================="

from mas_bajo_nivel.super_objeto import sys_drive, not_way
from tkinter import filedialog
import os

"==================================================="
    
if True:    # saco todas las words de subt en una list

    def tratando_contenido_de_docu(root):
        
        try:
            texto= open(root, "r+")
            documento= texto.readlines()
            texto.close()
            
        except FileNotFoundError:
            not_way.no_continues_1= True
            return
        
        salida= []

        for ni in documento:    # quita el "\n" de los elementos

            corte= ni.replace("\n", "")
            salida += (corte,)

        "......................"

        pica= []
        for vdl in salida:  # saco por palabras...

            vd= str(vdl)
            lin= vd.split()

            for u in lin:

                pica.append(u)

        sys_drive.words_subt_enlist= pica
        
        "......................"

        sale= []
        for b in salida:    # quito lineas vacias del docu_subt

            if b != "":
                sale += (b,)

        refor_original= "\n".join(sale)

        "......................"

        compon= open(root, "w")
        compon.write(refor_original)
        compon.close()

def mi_info():

    # primer trabajo necesario (cargando atributos)
    sys_drive.root_de_subt = filedialog.askopenfilename()

    ruta= os.path.split(sys_drive.root_de_subt)
    sys_drive.solo_ruta= ruta[0]
    
    tratando_contenido_de_docu(str(sys_drive.root_de_subt))

