
""" Gestor para el sistema """


"=================================================="

from dominio.mundo_parad_objeto.folder_principal_de_5_capas.carga_sistema.a_04.a_03.a_02.a_01.control_ import Operacion
from mas_bajo_nivel.super_objeto import pez

import tkinter as tk
import os

def reformula(cambio):

    new= (cambio * 2) + 1

    return new

"=================================================="

def entrada(dester):

    funciona= Operacion()

    if dester == 1:
        inicio_en= reformula(1)
        funciona.empieza(inicio_en, de_ingreso= None)

    if dester == 2:
        inicio_en= reformula(3)
        funciona.empieza(inicio_en, de_ingreso= None)

    if dester == 3:
        inicio_en= reformula(2)
        funciona.empieza(inicio_en, False)

    if dester == 4:
        inicio_en= reformula(2)
        funciona.empieza(inicio_en, True)

    if dester == 5:
        inicio_en= reformula(6)
        funciona.empieza(inicio_en, de_ingreso= None)
        
    if dester == 6:
        inicio_en= reformula(7)
        funciona.empieza(inicio_en, de_ingreso= None)

def procesando():   # iniciemos

    os.makedirs("c:\study_english\docus_tratados\su_fecha", exist_ok= True)

    mi_ventana= tk.Tk()
    pez.de_tk= tk
    mi_ventana.title("Gestor de Subtitulos de Videos")
    #mi_ventana.iconbitmap("c:\\mis_iconos\\g_subtitle.ico")

    if True:    # marcos

        cuadro_0= tk.LabelFrame(mi_ventana)
        cuadro_0.pack()
        
        cuadro_1= tk.LabelFrame(mi_ventana)
        cuadro_1.pack(fill= tk.X)
        
        cuadro_2= tk.LabelFrame(mi_ventana)
        cuadro_2.pack(fill= tk.X)

    if True:    # administrar la base de datos

        boton_0= tk.Button(cuadro_0, text= "Trabajar con el particular", padx= 20, pady= 60, bg= "yellow", command=lambda:entrada(1))
        boton_0.grid(row= 0, column= 0)

        boton_0= tk.Button(cuadro_0, text= "Trabajando con el abc_dario", padx= 20, pady= 60, bg= "#EB7045", command=lambda:entrada(2))
        boton_0.grid(row= 0, column= 1)

        boton_0= tk.Button(cuadro_0, text= "Ingresarlos a especifico  ", padx= 20, pady= 60, bg= "#45EBA7", command=lambda:entrada(3))
        boton_0.grid(row= 0, column= 2)

        boton_0= tk.Button(cuadro_0, text= "Ingresarlos al abc_dario", padx= 20, pady= 60, bg= "#45D0EB", command=lambda:entrada(4))
        boton_0.grid(row= 0, column= 3)

    if True:    # proceso divisor y mensajes
        
        div_words= tk.Button(cuadro_1, text= "crea sets", bg= "orange", command=lambda:entrada(5))
        div_words.config(anchor= "w", padx= 80, pady= 25)
        div_words.grid(row= 0, column= 0)
        
        mensajes= tk.Label(cuadro_1, text= "Bienvenido, empezamos trabajando en la ruta \nC:\study_english\...\nComience extrayendo, es el: 1° o 2° boton", padx= 20)
        pez.mensaje= mensajes
        mensajes.grid(row= 0, column= 1)

    if True:    # encuentro la nueva direccion web
        
        web_side= tk.Button(cuadro_2, text= "ingresa sitio web", bg= "#D145EB", command= lambda:entrada(6))
        web_side.config(anchor= "w", padx= 58, pady= 25)
        web_side.grid(row= 0, column= 0)
        
        entr= tk.Entry(cuadro_2)
        pez.entd_a_web= entr
        entr.grid(row= 0, column= 1)

    mi_ventana.mainloop()

