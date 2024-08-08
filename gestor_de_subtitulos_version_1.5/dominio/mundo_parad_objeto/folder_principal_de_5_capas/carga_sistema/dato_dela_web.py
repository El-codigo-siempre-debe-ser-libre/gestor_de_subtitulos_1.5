
""" Aqui estoy manejando la entrada a la paguina web de apoyo
    de esta aplicacion """
    
    
"=================================================="

from mas_bajo_nivel.super_objeto import pez
import sqlite3
import os

"=================================================="

def go_web(existe):
    
    contenido= str(pez.entd_a_web.get())
    
    fuselaje= sqlite3.connect("c:\\study_english\\my_dictionary\\ingreso\\web_subtitle.db")
    puerta= fuselaje.cursor()
    
    def insert_ruta():
                    
        tuelement= list([
            (1, "www.google.com"),
            (2, "www.google.com")
            ])
        
        puerta.executemany("INSERT INTO web VALUES (?,?)", tuelement)
        fuselaje.commit()
    
    puerta.execute("CREATE TABLE IF NOT EXISTS web (pos INTEGER, pag TEXT)")
    
    if existe == False:
        insert_ruta()
    
        
    if contenido == "":             # vacia (extrae y entra)
        
        def recoje():
            
            puerta.execute("SELECT * FROM web")
            conte= puerta.fetchall()
            fuselaje.commit()
            
            return conte

        try:
            conte= recoje()
            
        except:
            
            insert_ruta()
            
            puerta.execute("SELECT * FROM web")
            conte= puerta.fetchall()
            fuselaje.commit()
        
        fuselaje.close()
        
        pieza= conte[1]
        os.system("start " + str(pieza[1]))
        
        pez.mensaje["text"]= "Si usted escribe una ruta URL, debajo, \nPodra siempre acceder a ella"
        
    elif contenido == "reset":      # restablece
        
        puerta.execute("SELECT * FROM web")
        conte= puerta.fetchall()
        fuselaje.commit()
        
        pieza= conte[0]
        root= pieza[1]

        puerta.execute("UPDATE web SET pag= '{}' WHERE pos= 2".format(root))
        fuselaje.commit()
        
        fuselaje.close()
        
        pez.entd_a_web.delete(0, 5)
        
        pez.mensaje["text"]= "Si ahora presiona el boton podrá ir a su pagina"
        
    elif not (contenido == "") or (contenido == "reset"):   # tiene otra URL (guarda/borra)
        
        try:
            puerta.execute("SELECT * FROM web")
            conte= puerta.fetchall()
            fuselaje.commit()
            
        except:
            insert_ruta()

        puerta.execute("UPDATE web SET pag= '{}' WHERE pos= 2".format(contenido))
        fuselaje.commit()
        
        fuselaje.close()
        
        pez.mensaje["text"]= "Si usted escribe 'reset' \nVolvera a tener la direccion web por defecto"
        
        pez.entd_a_web.delete(0, pez.de_tk.END)
        
