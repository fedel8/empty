#! /usr/bin/env python3


##@author  Federico Castez <federico.castez@ypftecnologia.com>

##@file

##@package

##@page print_formats.py

##@brief diversos ejemplos con print.\n
# Se puede dar formato a print con % y con {}

x = 3.2
print("x = {}".format(x)) 
print('x = {}'.format(x)) 
print('x = %d' % (x)) 
print('x = %f' % (x)) 

print("Hola" + " " + "Mundo!" )
print("Hola" , " " , "Mundo!" )


i = 12
print("x = {}  i = {}".format(x,i))
print("sum = {}".format(x+i)) 
print("sum = {}".format(x+i)) 

Lista = ["Pepe", x, i]

for item in Lista:
   print("item {}: ".format(item) , item)
   
ListaDeDiccionarios = [
{'nombre': 'Pepe', 'valor': 'NaN'},
{'nombre': 'x', 'valor': x},
{'nombre': 'i', 'valor': i}
                      ]
                      
for item in ListaDeDiccionarios:
   print("item {}: ".format(item['nombre']) , item['valor'])  
   
print(ListaDeDiccionarios[1])  
print(ListaDeDiccionarios[1]['nombre'],"->" ,ListaDeDiccionarios[1]['valor'])   

str1 = "xxx"
str2 = "yyy"
str3 = "Esto es {} una {} prueba".format(str1, str2)
str4 = str3.replace('x','_').replace('y','z')
print(str3,str4)
print(str3+str4)

ListaDeStrings = [str1, str2, str3, str4]

subcadena = 'xx'

for item in ListaDeStrings:
   if ('xx' in item):  
       print("Se encontró la subdadena {} en la cadena ".format(subcadena) 
+ '"' + item + '"')                    
