
""" Creando el resto de documentos de
    palabras que no coinciden 
    y el texto con las word desconocidas señaladas """


"==================================================="

from mas_bajo_nivel.super_objeto import sys_drive, not_way

"==================================================="

def hago_el_docu_de_palabras_desconocidas():

    ubicaciones= sys_drive.ubica_las_contr 

    largo_sc= 5
    while largo_sc != 0:

        if largo_sc == 5:   # hallo las words lost y ordeno

            lost_3= []
            for w in ubicaciones:

                lost_3 += (sys_drive.words_subt_enlist[w],)

            lost_3.sort()
            
            #print(lost_3)
            largo_sc= 4

        elif largo_sc == 4: # quito las que se repiten

            ultimo= ""
            lost_2= []
            for g in lost_3:

                if g != ultimo:
                    
                    ultimo= g
                    lost_2 += (g,)

            #print(lost_2)
            largo_sc= 3

        elif largo_sc == 3: # dejo solo las streamg

            la_cla= None
            lost_1= []
            for p in lost_2:

                word= str(p)

                "......................."

                for f in word:      # veamos si la ult es "-"
                    finish = f

                if finish == "-":
                    word= word[:-1]

                "......................."

                la_cla= word.isalpha()

                if la_cla == True:
                    lost_1 += (word,)

            largo_sc= 2

        elif largo_sc == 2: # similares, si resto (s) quita

            txto= ""
            lost= []
            for g in lost_1:
                    
                if txto != "":

                    for n in g:
                        ultim_letra= n
                    
                    ensayo= g[:-1]
                    if (ultim_letra == "s") and (txto == ensayo):
                        continue
                    else:
                        txto= g
                        lost += (g,)

                else:
                    txto= g
                    lost += (g,)

            largo_sc= 1

        elif largo_sc == 1: # write en el txt verticalmente

            tex_lost= "\n".join(lost)

            mis_words_desco= sys_drive.solo_ruta + "/desconocidas.txt"
            
            try:
                avisando= open(mis_words_desco, "w+")
                avisando.write(tex_lost)
                avisando.close()
                
            except PermissionError:
                not_way.no_continues_2= True
                return

            largo_sc= 0

def ahora_formando_one():

    ubicaciones= sys_drive.ubica_las_contr 

    for k in ubicaciones:   # pone los simbolos (-)

        lamedusa_1= sys_drive.words_subt_enlist[k]

        mini= ""
        for a in lamedusa_1:
            mini= a

        valida= lamedusa_1.isalpha()

        if (mini != "-") and (valida == True):
            lamedusa_2= str(lamedusa_1) + "-"
        else:
            lamedusa_2= str(lamedusa_1)

        sys_drive.words_subt_enlist[k]= lamedusa_2

    new_tex= " ".join(sys_drive.words_subt_enlist)

    direc= sys_drive.solo_ruta + "/new_documento.txt"

    el_conte= open(direc, "w")
    el_conte.write(new_tex)
    el_conte.close()

def contrastaycrea():

    if True:    # Filtrando...
        
        for y, e in enumerate(sys_drive.words_subt_enlist):  # ¿coinciden?

            if e in sys_drive.en_basedato_word:
                pass
            else:
                sys_drive.contrastados += (e,)
                sys_drive.ubica_las_contr += (y,)

    if True:    # creando...

        hago_el_docu_de_palabras_desconocidas()
        
        if not_way.no_continues_2 == False:
            # por: error de cancelacion de extraccion conte_subt
            # en linea: 105 de este modulo
            ahora_formando_one()

