
""" Hago los ingresos correspondientes """


"================================================="

from dominio.mundo_parad_objeto.folder_principal_de_5_capas.carga_sistema.a_04.a_03.root_abc import toma_la_dir
from dominio.mundo_parad_objeto.folder_principal_de_5_capas.carga_sistema.a_04.cargando import Metodo_de_extraccion as mete
from dominio.mundo_parad_objeto.folder_principal_de_5_capas.afianza.b_04.b_03.b_02.confirmo_letras import confirmando_letras
from mas_bajo_nivel.super_objeto import sys_drive

"================================================="

class Metodo_de_ingreso:

    def saco_root_segun_letras(self, letra):
        
        self.lasrut= toma_la_dir(letra)

    def adicionando_words_a_un_txt(self, lete_iq, letra):

        self.saco_root_segun_letras(letra)
        mi_direcc= str(self.lasrut)

        try:    # al usar el prgma por primera vez
            anterior= open(mi_direcc, "r+")
            anteri= anterior.read()
            anterior.close()

        except FileNotFoundError:

            confirmando_letras()

        hola= anteri.split("\n")

        "....................................."

        actua= mete()
        actua.en_particular()
        en_base= list(sys_drive.en_basedato_word)

        "....................................."

        if lete_iq == None:
            hola.extend(en_base)
        else:
            hola.append(en_base[lete_iq])
    
        hola.sort()

        di= ""
        dime=[]
        for sa in hola: # quito todas las words repetidas

            if sa != di:

                di= sa
                dime += (sa,)

        "....................................."

        combinacion= "\n".join(dime)

        "....................................."

        aflora= open(mi_direcc, "r+")
        aflora.write(combinacion)
        aflora.close()

        "....................................."

    def general(self):
        
        toma= mete()
        toma.en_particular()

        for t, k in enumerate(sys_drive.en_basedato_word):
            self.adicionando_words_a_un_txt(t, k[0])

    def en_particular(self, la_letra):

        nada= None

        self.adicionando_words_a_un_txt(nada, la_letra)

