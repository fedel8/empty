#! /usr/bin/env python3
#Ejemplo de creacion de una gui elemental
# -*- coding: utf-8 -*-
"""
Este es un comentario
multi-
linea
"""

from tkinter import *

import math

 
window = Tk()
 
window.title("Suma Complejos")
 
window.geometry('350x200')


#Campo de entrada y etiqueta para la 
#parte real del complejo 1
lbl_re_z1 = Label(window, text="Re [z1]")
 
lbl_re_z1.grid(column=0, row=0, padx=10, pady=10)
 
re_z1 = Entry(window,width=10)
 
re_z1.grid(column=0, row=1)

#Campo de entrada y etiqueta para la 
#parte imaginaria del complejo 1
lbl_im_z1 = Label(window, text="Im [z1]")
 
lbl_im_z1 .grid(column=1, row=0, padx=10, pady=10)

im_z1  = Entry(window,width=10)
 
im_z1.grid(column=1, row=1)
 
#Campo de entrada y etiqueta para la 
#parte real del complejo 2
lbl_re_z2 = Label(window, text="Re [z2]")
 
lbl_re_z2.grid(column=0, row=2, padx=10, pady=10)
 
re_z2 = Entry(window,width=10)
 
re_z2.grid(column=0, row=3)

#Campo de entrada y etiqueta para la 
#parte imaginaria del complejo 2
lbl_im_z2 = Label(window, text="Im [z2]")
 
lbl_im_z2.grid(column=1, row=2, padx=10, pady=10)

im_z2 = Entry(window,width=10)
 
im_z2.grid(column=1, row=3)

stat_lab = Label(window, text=" z1+z2:")
stat_lab.grid(column=2, row=2, padx=10, pady=10)
stat_lab.configure(foreground="blue")

stat_lab = Label(window, text="  ")
stat_lab.grid(column=2, row=3, padx=10, pady=10)

stat_lab = Label(window, text="  ")
stat_lab.grid(column=3, row=3, padx=2, pady=10)

stat_lab = Label(window, text="  ")
stat_lab.grid(column=4, row=3, padx=10, pady=10)

def clicked():
    resultado_re = float(re_z1.get()) + float(re_z2.get())
    resultado_im = float(im_z1.get()) + float(im_z2.get())

    Label_resultado_re = Label(window, text=round(resultado_re,2))
    Label_resultado_re.grid(column=2, row=3, padx=10, pady=10)
    Label_resultado_re.configure(foreground="red")

    Label_resultado_im = Label(window, text=round(resultado_im,2))
    Label_resultado_im.grid(column=4, row=3, padx=10, pady=10)
    Label_resultado_im.configure(foreground="red")
    
    
    Label_i = Label(window, text="+ i")
    Label_i.grid(column=3, row=3, padx=2, pady=10)
    Label_i.configure(foreground="red")
    
btn = Button(window, text="Sumar", command=clicked)
 
btn.grid(column=2, row=1, padx=10, pady=10)
 
window.mainloop()
