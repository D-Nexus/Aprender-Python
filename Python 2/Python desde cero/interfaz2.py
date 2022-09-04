#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Las dos líneas siguientes son necesaias para hacer 
# compatible el interfaz Tkinter con los programas basados 
# en versiones anteriores a la 8.5, con las más recientes. 

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

# Define la ventana principal de la aplicación

raiz = Tk()

# Define las dimensiones de la ventana, que se ubicará en 
# el centro de la pantalla. Si se omite esta línea la
# ventana se adaptará a los widgets que se coloquen en
# ella. 

raiz.geometry('300x200') # anchura x altura

# Asigna un color de fondo a la ventana. Si se omite
# esta línea el fondo será gris

raiz.configure(bg = 'beige')

# Asigna un título a la ventana

raiz.title('Aplicación')

# Define un botón en la parte inferior de la ventana
# que cuando sea presionado hará que termine el programa.
# El primer parámetro indica el nombre de la ventana 'raiz'
# donde se ubicará el botón

ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)

# Después de definir la ventana principal y un widget botón
# la siguiente línea hará que cuando se ejecute el programa
# construya y muestre la ventana, quedando a la espera de 
# que alguna persona interactúe con ella.

# Si la persona presiona sobre el botón Cerrar 'X', o bien,
# sobre el botón 'Salir' el programa llegará a su fin.

raiz.mainloop()

#La primera aplicación, orientada a objetos

#A continuación, se muestra la misma aplicación pero orientada a objetos. Aunque este tipo de programación siempre es recomendable con Python no es imprescindible. Sin embargo, si vamos a trabajar con Tkinter es lo más adecuado, sobre todo, porque facilita la gestión de los widgets y de los eventos que se producen en las aplicaciones. Desde luego, todo van a ser ventajas.

#Normalmente, cuando se ejecuta una aplicación gráfica ésta se queda a la espera de que una persona interactúe con ella, que presione un botón, escriba algo en una caja de texto, seleccione una opción de un menú, sitúe el ratón en una posición determinada, etc., o bien, se produzca un suceso en el que no haya intervención humana como que termine un proceso, que cambie el valor de una variable, etc. En cualquiera de estos casos, lo habitual será vincular estos eventos o sucesos con unas acciones a realizar, que pueden ser mejor implementadas con las técnicas propias de la programación orientada a objetos.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

# Crea una clase Python para definir el interfaz de usuario de
# la aplicación. Cuando se cree un objeto del tipo 'Aplicacion'
# se ejecutará automáticamente el método __init__() qué 
# construye y muestra la ventana con todos sus widgets: 

class Aplicacion():
    def __init__(self):
        raiz = Tk()
        raiz.geometry('300x200')
        raiz.configure(bg = 'beige')
        raiz.title('Aplicación')
        ttk.Button(raiz, text='Salir', 
                   command=raiz.destroy).pack(side=BOTTOM)
        raiz.mainloop()

# Define la función main() que es en realidad la que indica 
# el comienzo del programa. Dentro de ella se crea el objeto 
# aplicación 'mi_app' basado en la clase 'Aplicación':

def main():
    mi_app = Aplicacion()
    return 0

# Mediante el atributo __name__ tenemos acceso al nombre de un
# un módulo. Python utiliza este atributo cuando se ejecuta
# un programa para conocer si el módulo es ejecutado de forma
# independiente (en ese caso __name__ = '__main__') o es 
# importado:

if __name__ == '__main__':
    main()