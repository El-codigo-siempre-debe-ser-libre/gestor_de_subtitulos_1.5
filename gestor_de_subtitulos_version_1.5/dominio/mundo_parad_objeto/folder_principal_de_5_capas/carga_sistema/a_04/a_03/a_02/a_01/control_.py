
""" Modulo para controlar todo el sistema """


if True:    # sistema interno
    ""
    #####################
    #                   #
    # sub_procesos      #
    #                   #
    #####################
    #
    # 0.  inicio
    # 10. regresa normalmente
    # 11. error
    #
    #####################
    #                   #
    # manejo de errores #
    #                   #
    #####################
    #
    # 0. inicio
    # 1. 
    #
    #

"================================================"

from dominio.mundo_parad_objeto.folder_principal_de_5_capas.carga_sistema.a_04.a_03.a_02.ext_del_subt_info import mi_info
from dominio.mundo_parad_objeto.folder_principal_de_5_capas.afianza.b_04.b_03.b_02.confirmo_letras import confirmando_letras
from dominio.mundo_parad_objeto.folder_principal_de_5_capas.afianza.b_04.b_03.gesta import metodo
from dominio.mundo_parad_objeto.folder_principal_de_5_capas.afianza.adicionales_docus import contrastaycrea
from dominio.mundo_parad_objeto.folder_principal_de_5_capas.carga_sistema.a_04.a_03.a_02.words_a_tradu import La_tra
from dominio.mundo_parad_objeto.folder_principal_de_5_capas.carga_sistema.dato_dela_web import go_web

from mas_bajo_nivel.super_objeto import not_way
from genericpath import exists
import os

"================================================"

class Operacion:

    def __init__(self):
        
        self.indaga= None
        self.subcontrol= 0

        self.manejo_de_errores= 0
        self.no_se= None

        self.de_ingreso= None

    def empieza(self, prendida, de_ingreso):

        self.indaga= prendida
        self.de_ingreso= de_ingreso

        while self.indaga < 100:    # Turn_Final
            while self.indaga < 14:
                while self.indaga < 12:
                    while self.indaga < 10:
                        while self.indaga < 8:
                            while self.indaga < 6:
                                while self.indaga < 4:
                                    while self.indaga < 2:

                                        self.indaga= 101
                                        continue
                                    
                                    if True:    # 3

                                        if (4 > self.indaga) and (self.indaga > 2):
                                            # opcion (MP)

                                            if (self.indaga == 3) and (self.subcontrol == 0):

                                                self.subcontrol= 1
                                                self.indaga= 9

                                                continue

                                            if (self.indaga == 3) and (self.subcontrol == 10):

                                                mi_info()
                                                metodo(True, False)

                                                contrastaycrea()

                                                self.indaga= 1
                                                continue

                                        else:
                                            break

                                if True:    # 5

                                    if (6 > self.indaga) and (self.indaga > 4):
                                        # opcion (OI)

                                        if (self.indaga == 5) and (self.subcontrol == 0):

                                            self.indaga= 11
                                            self.subcontrol= 1

                                            continue

                                        if (self.indaga == 5) and (self.subcontrol == 10):

                                            metodo(False, self.de_ingreso)

                                            self.indaga= 1
                                            continue

                                    else:
                                        break

                            if True:    # 7

                                if (8 > self.indaga) and (self.indaga > 6):
                                    # opcion (MM)

                                    if (self.indaga == 7) and (self.subcontrol == 0):

                                        self.indaga= 11
                                        self.subcontrol= 2

                                        continue
                                
                                    if (self.indaga == 7) and (self.subcontrol == 10):

                                        mi_info()
                                        metodo(True, True)
                                        
                                        if not_way == False: # por: error cancelar la invest mi_info line: 22
                                            contrastaycrea()

                                        self.indaga= 1
                                        continue

                                else:
                                    break


                        if True:    # 9

                            if (10 > self.indaga) and (self.indaga > 8):
                                # Confirmo la existencia de las carpetas en C://
                                
                                os.makedirs("c:\\study_english\\my_dictionary\\ingreso", exist_ok= True)

                                self.data= ""

                                def abriendo(opc):

                                    if opc == 1:

                                        datu= open("c:\study_english\my_dictionary\ingreso\words_learned.txt", "r")
                                        self.data= datu.read()
                                        datu.close()

                                    if opc == 2:

                                        datu= open("c:\study_english\my_dictionary\ingreso\words_learned.txt", "w")
                                        datu.write("")
                                        datu.close()

                                        date= open("c:\study_english\my_dictionary\ingreso\lo_traducido.txt", "w")
                                        date.write("")
                                        date.close()

                                try:
                                    abriendo(1)
                                
                                except FileNotFoundError:

                                    abriendo(2)
                                    abriendo(1)

                                self.subcontrol= 10
                                self.indaga= 3

                                continue
                            
                            else:
                                break

                    if True:    # 11

                        if (12 > self.indaga) and (self.indaga > 10):
                            # confirmando archivo de letras
                            
                            os.makedirs("c:\\study_english\\my_dictionary\\ingreso", exist_ok= True)
                            confirmando_letras()
                            
                            self.data= ""

                            def abriendo(opc):

                                if opc == 1:

                                    datu= open("c:\study_english\my_dictionary\ingreso\words_learned.txt", "r")
                                    self.data= datu.read()
                                    datu.close()

                                if opc == 2:

                                    datu= open("c:\study_english\my_dictionary\ingreso\words_learned.txt", "w")
                                    datu.write("")
                                    datu.close()

                                    date= open("c:\study_english\my_dictionary\ingreso\lo_traducido.txt", "w")
                                    date.write("")
                                    date.close()

                            try:
                                abriendo(1)
                            
                            except FileNotFoundError:

                                abriendo(2)
                                abriendo(1)

                            if self.subcontrol == 1:    # a ingresos
                                self.indaga= 5
                                self.subcontrol= 10
                            elif self.subcontrol == 2:  # a multiple
                                self.indaga= 7
                                self.subcontrol= 10

                            continue

                        else:
                            break


                if True:    # 13

                    if (14 > self.indaga) and (self.indaga > 12):
                        # gestiono los archivos traducidos
                        
                        os.makedirs("c:\\study_english\\set_words_study", exist_ok= True)
                        
                        trad= La_tra()
                        trad.traduce()
                        
                        self.indaga= 1
                        continue

            if True:    # 15
                
                if (16 > self.indaga) and (self.indaga > 14):
                    # administro la pagina web (que descarga los subtitulos)
                    
                    ya_viene_existiendo= None
                    
                    if not exists("c:\\study_english\\my_dictionary\\ingreso\\web_subtitle.db"):
                        
                        la_base_d= open("c:\\study_english\\my_dictionary\\ingreso\\web_subtitle.db", "w")
                        la_base_d.write("")
                        la_base_d.close()
                        
                        ya_viene_existiendo= False

                    go_web(ya_viene_existiendo)
                    
                    self.indaga= 1
                    continue
                
