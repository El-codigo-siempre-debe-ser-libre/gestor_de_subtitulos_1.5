
""" Hago pasar por filtro para desarrollar la salida """


"==================================================="

from dominio.mundo_parad_objeto.folder_principal_de_5_capas.carga_sistema.utileria import abcd
from dominio.mundo_parad_objeto.folder_principal_de_5_capas.carga_sistema.a_04.a_03.root_abc import toma_la_dir

from mas_bajo_nivel.super_objeto import sys_drive

"==================================================="

class Metodo_de_extraccion:

    def general(self):

        sys_drive.en_basedato_word= self.apoyo_suma_g()

    def apoyo_suma_g(self):
        
        carps= abcd()

        plus= []
        for ex in carps:    # meto todas las words en una list

            this_root= str(toma_la_dir(ex))

            jala= open(this_root, "r")
            mina= jala.read()

            plus += (mina,)

        jala.close()

        androm= []
        for tifa in plus:   # los vacios los descarto
            
            if tifa == "" or tifa == " ":
                pass
            else:
                androm += (tifa,)
        
        mani= ""
        for tulu in androm: # creo un solo streamg con los elemt
            
            mani += tulu
            mani += " "
            
        mani= mani[:-1]
        mani.replace(" ", "\n")
        excelente= mani.split("\n")
                
        final= []
        for reco in excelente:  # cuento y agrego a final
            
            nabo= reco
            nabo= nabo.split(" ")
            
            cuan= len(nabo)
            exite= ""
            if cuan == 1:
                exite= nabo[0]
                final.append(exite)

            if cuan == 2:
                
                exite= nabo[0]
                final.append(exite)
                
                exite= nabo[1]
                final.append(exite)
            
        return final

    def en_particular(self):

        root= "c:\\study_english\\my_dictionary\\ingreso\\words_learned.txt"

        datu= open(root, "r")
        data= datu.read()
        datu.close()
        
        dante= data.replace("\n", " ")

        mis_elemen= []
        mis_elemen= dante.split(" ")
        
        new_list= []
        for mi in mis_elemen:   # corto los espacios vacios
            
            if (mi == "") or (mi == " "):
                pass
            else:
                new_list += (mi,)

        sys_drive.en_basedato_word= new_list

