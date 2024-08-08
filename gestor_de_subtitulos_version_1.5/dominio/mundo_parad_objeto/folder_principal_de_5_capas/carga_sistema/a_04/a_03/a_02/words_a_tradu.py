
""" le ubica las traducciones al lado a cada palabra """


"============================================="

from mas_bajo_nivel.super_objeto import pez, not_way

class Entradas:
    
    def __init__(self):
        
        self.desconocidas= None
        self.traducidas= None
        
    def extraccion_de_los_dos(self):
        
        try:
            wu= open("c:\study_english\desconocidas.txt", "r")
            dato_1= wu.read()
            wu.close()

        except FileNotFoundError:
            pez.mensaje.config(text= "El archivo 'desconocidas.txt' no se encuentra en la direccion \nC:\study_english\desconocidas.txt")
            not_way.no_continues_3= True
            return
        
        wo= open("c:\study_english\my_dictionary\ingreso\lo_traducido.txt", "r")
        dato_2= wo.read()
        wo.close()
        
        salida_1= dato_1.split("\n")
        salida_2= dato_2.split("\n")
        
        self.desconocidas= salida_1
        self.traducidas= salida_2
        
fuente= Entradas()

"============================================="

class La_tra:
    
    def __init__(self):
        
        self.lista_empar= []
    
    def emparejando(self):
        
        play= []
        for e, l in enumerate(fuente.desconocidas):
            
            seg_data= fuente.traducidas[e]
            new_str= l + " - " + seg_data
            
            play.append(new_str)
            
        return play

    def haber_y_limpiar(self):
        
        fuente.extraccion_de_los_dos()
        
        if not_way.no_continues_3 == True:
            # por: error del cliente al mover el fichero
            # en linea: 24 de este modulo
            return
        
        def compara():
            
            dista_1= len(fuente.desconocidas)
            dista_2= len(fuente.traducidas)
            
            #print(dista_1, dista_2)
            
            if dista_1 != dista_2:
                return False
            else:
                return None
                    
        filtro= compara()
        if filtro == False:
            
            pez.mensaje.config(text= "Desconocidas & Traducidas no tienen la misma cantidad de palabras \nEllas deben tener la misma cantidad")
            
            return
    
        self.lista_empar= self.emparejando()
                
    def traduce(self):

        self.haber_y_limpiar()
    
        lis= self.lista_empar

        lista= ""
        mano= 0
        pase= 0
        salida= False
        while True:
            
            conjunto= 20    # se resetea

            while conjunto != 0:
                
                if lista == "":
                    try:
                        lista += lis[mano]
                        
                    except IndexError:
                        
                        salida= True
                        break
                else:
                    try:
                        lista= lista + "\n" + lis[mano]
                    
                    except IndexError:
                        
                        salida= True
                        break
                
                mano += 1
                conjunto -= 1
            
            numer= len(lista)
            
            if numer != 0:
                self.guardando(lista, pase)
            
            lista= ""
            pase += 1

            if salida == True:  # antes... evaluo si salgo
                break

    def guardando(self, saliendo, numeracion):
        
        root= "c:\study_english\set_words_study\grupo_" + str(numeracion) + "_.txt"
                
        juli= open(root, "w")
        juli.write(saliendo)
        juli.close()

