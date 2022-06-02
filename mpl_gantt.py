#! /usr/bin/env python3


##@author  Federico Castez <federico.castez@ypftecnologia.com>

##@file

##@page mpl_gantt.py
##@brief Ejemplo de generación de diagramas de Gantt con matplotlib
#
# Importing the matplotlb.pyplot
import matplotlib.pyplot as plt

# Declaring a figure "gnt"
PixelsX =1200
PixelsY =1000
px = 1/plt.rcParams['figure.dpi']  # pixel in inches
fig, gnt = plt.subplots(figsize=(PixelsX*px, PixelsY*px))

NumTareas = 8
NumSemanas = 16
# Setting Y-axis limits
gnt.set_ylim(0, NumTareas)

# Setting X-axis limits
gnt.set_xlim(0, NumSemanas)

# Setting labels for x-axis and y-axis
gnt.set_xlabel('semana', fontsize=16)
#gnt.set_ylabel('Actividad', labelpad = 48, fontsize=16)

# Setting ticks on x-axis
gnt.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

# Setting ticks on y-axis
gnt.set_yticks([1, 2, 3, 4, 5, 5, 6, 7])
# Labelling tickes of y-axis
gnt.set_yticklabels(['', '', '', '', '', '', '', ''])

plt.tick_params(labelsize = 15)



plt.text(-1.4, 0.5, 'Unidad I', fontsize=12)
plt.text(-1.4, 1.5, 'Unidad II', fontsize=12)
plt.text(-1.4, 2.5, 'Unidad III', fontsize=12)
plt.text(-2.8, 3.5, 'rep/cons/1er parcial', fontsize=12)
plt.text(-1.4, 4.5, 'Unidad IV', fontsize=12)
plt.text(-1.4, 5.5, 'Unidad V', fontsize=12)
plt.text(-1.4, 6.5, 'Unidad VI', fontsize=12)
plt.text(-2.8, 7.5, 'rep/cons/2do parcial', fontsize=12)


# Setting graph attribute
gnt.grid(True)

# Declaring a bar in schedule
SemanaComienzo = 0
NumTarea = 0
Duracion = 2
Color = 'tab:orange'
gnt.broken_barh([(SemanaComienzo, Duracion)], (NumTarea, 1), facecolors =(Color))

SemanaComienzo = 2
NumTarea = 1
Duracion = 2
Color = 'yellow'
gnt.broken_barh([(SemanaComienzo, Duracion)], (NumTarea, 1), facecolors =(Color))


SemanaComienzo = 4
NumTarea = 2
Duracion = 2
Color = 'tab:pink'
gnt.broken_barh([(SemanaComienzo, Duracion)], (NumTarea, 1), facecolors =(Color))

SemanaComienzo = 6
NumTarea = 3
Duracion = 1
Color = 'green'
gnt.broken_barh([(SemanaComienzo, Duracion)], (NumTarea, 1), facecolors =(Color))

SemanaComienzo = 7
NumTarea = 4
Duracion = 3
Color = 'tab:gray'
gnt.broken_barh([(SemanaComienzo, Duracion)], (NumTarea, 1), facecolors =(Color))

SemanaComienzo = 10
NumTarea = 5
Duracion = 3
Color = 'tab:red'
gnt.broken_barh([(SemanaComienzo, Duracion)], (NumTarea, 1), facecolors =(Color))


SemanaComienzo = 13
NumTarea = 6
Duracion = 2
#Color = 'tab:violet'
gnt.broken_barh([(SemanaComienzo, Duracion)], (NumTarea, 1))

SemanaComienzo = 15
NumTarea = 7
Duracion = 1
Color = 'green'
gnt.broken_barh([(SemanaComienzo, Duracion)], (NumTarea, 1), facecolors =(Color))

# Declaring multiple bars in at same level and same width
#gnt.broken_barh([(8, 2), (10, 1)], (3, 5),
#						facecolors ='tab:blue')

#gnt.broken_barh([(1, 5), (11, 2), (3, 1)], (2, 9),
#								facecolors =('tab:red'))
plt.show()

plt.savefig("gantt1.png")

