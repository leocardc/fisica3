from tkinter.ttk import Combobox

import pygame
import tkinter as tk
from tkinter import *
import os

root = Tk()
w,h = 1000, 650
rojo = 255, 0, 0
azul = 0, 0, 240
NEGRO = 0, 0, 0

coeficiente = {'Aluminio': 23e-6 ,'Cobre': 17e-6,
               'Acero': 11e-6,'Vidrio': 9e-6, 'Zinc': 25e-6,
               'Plomo': 29e-6,'Diamante': 0.9e-6}

coef_lineal = StringVar(root)
longitud = IntVar(root)
temp_i = IntVar(root)
temp_f = IntVar(root)
selected = IntVar(root)
area = StringVar(root)
base=StringVar(root)

embed = Frame(root, width = w, height = h) #creates embed frame for pygame window
embed.grid(columnspan = (1200), rowspan = 650) # Adds grid
embed.pack(side = LEFT) #packs window to the left

buttonwin = tk.Frame(root, width = 75, height = 650)
buttonwin.pack(side = LEFT)

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

screen = pygame.display.set_mode((w-300,650))
screen.fill(NEGRO)

pygame.display.init()
pygame.display.update()

def mostrar():

    if selected.get() == 1:

        long = Entry(root, textvariable=longitud, width=10)
        long.place(x=700, y=140)

        longtxt = Label(root, text='Longitud :')
        longtxt.place(x=700, y=100)

        listbox = Combobox(root, width=10,textvariable=coef_lineal)
        listbox.place(x=850, y=140)
        listbox['values'] = ("Aluminio", "Cobre", "Acero", "Vidrio","Zinc","Plomo","Diamante")

        coetxt = Label(root, text='Coeficiente :')
        coetxt.place(x=850, y=100)

        temp_ini = Entry(root, textvariable=temp_i, width=10)
        temp_ini.place(x=700, y=200)

        temp_initxt = Label(root, text='Temperatura Inicial :')
        temp_initxt.place(x=700, y=170)

        temp_fin = Entry(root, textvariable=temp_f, width=10)
        temp_fin.place(x=850, y=200)

        root.temp_fintxt = Label(root, text='Temperatura Final :')
        root.temp_fintxt.place(x=850, y=170)

        root.botoncalcular = Button(root, text='calcular', command=calcular_lineal)
        root.botoncalcular.place(x=700, y=250)


    elif selected.get() == 2:

        Entry(root, textvariable=area, width=10).place(x=750, y=100)
        tex3 = Label(root, text='leo :').place(x=700, y=100)
        Entry(root, textvariable=base, width=10).place(x=750, y=120)
        tex4 = Label(root, text='tino :').place(x=700, y=120)

    elif selected.get() == 3:
        Entry(root, textvariable=area, width=10).place(x=750, y=100)
        Label(root, text='lucas :').place(x=700, y=100)
        Entry(root, textvariable=base, width=10).place(x=750, y=120)
        Label(root, text='Payan :').place(x=700, y=120)

def draw():

    pygame.draw.circle(screen, rojo, (200,200), 25)

    pygame.display.update()
def calcular_lineal():
    screen.fill(pygame.Color(0, 0, 0))
    if longitud.get() != '' and temp_i.get() != '' and temp_f.get() != '':
        exp_lineal= coeficiente.get(coef_lineal.get()) * longitud.get()* (temp_f.get()-temp_i.get())
        print(exp_lineal)
        pygame.draw.line(screen,azul,(100,200),(100+escala_i(longitud.get()),200),10)
        pygame.draw.line(screen, rojo, (100, 400), (100 +escala_i(longitud.get())+exp_li(exp_lineal)+exp_lineal, 400), 10)
        pygame.draw.line(screen, azul, (100, 400), (100+escala_i(longitud.get()), 400), 10)

        pygame.font.init()
        fuente = pygame.font.Font(None, 20)
        mensaje = fuente.render('Longitud Final: '+str(longitud.get()+exp_lineal), 1, (255, 255, 255))
        screen.blit(mensaje, (100, 380))
        pygame.display.flip()
        pygame.display.update()

def escala_i(longitud):
    if longitud < 15:
        return 250
    elif longitud < 30:
        return 300
    elif longitud < 45:
        return  350
    elif longitud < 60:
        return 400
    else:
        return 450
def exp_li(exp):
    if exp < 0.1e-3:
        return 22
    elif exp < 0.1e-1 :
        return 22
    elif exp < 2:
        return 22
    elif exp < 5:
        return 22
    else:
        return 19
    pass
def suma():
    if (area.get() != '' and base.get() != ''):

        print( int(area.get())+int(base.get()))
        print(selected.get())

rad1 = Radiobutton(root, text='Exp Lineal', value=1, variable=selected).place(x=750, y=10)
rad2 = Radiobutton(root, text='Exp Superficial', value=2, variable=selected).place(x=750, y=30)
rad3 = Radiobutton(root, text='Exp Volumetrica', value=3, variable=selected).place(x=750, y=50)
botonmuestra = Button(root, text='mostrar', command=mostrar).place(x=750, y=70)
button1 = Button(buttonwin,text = 'pintar',  command=draw)
button1.pack(side=LEFT)

root.update()

while True:
    pygame.display.update()
    root.update()