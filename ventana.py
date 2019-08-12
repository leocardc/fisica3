import math
from tkinter.ttk import Combobox

import pygame
import tkinter as tk
from tkinter import *
import os

root = Tk()

w, h = 1000, 650
rojo = 255, 0, 0
azul = 0, 0, 240
NEGRO = 0, 0, 0

coeficiente = {'Aluminio': 23e-6, 'Cobre': 17e-6,
               'Acero': 11e-6, 'Vidrio': 9e-6, 'Zinc': 25e-6,
               'Plomo': 29e-6, 'Diamante': 0.9e-6}

coeficiente_Superficial = {'Aluminio': 44.8e-6, 'Cobre': 33.4e-6,
                           'Acero': 23e-6, 'Vidrio': 14.6e-6, 'Zinc': 52e-6,
                           'Plomo': 54.6e-6, 'Diamante': 1.8e-6}

coef_lineal = StringVar(root)
coef_superficial = StringVar(root)
longitud = DoubleVar()
temp_i = DoubleVar()
radio = DoubleVar()
temp_f = DoubleVar()
selected = DoubleVar()
selected2 = DoubleVar()
altura = DoubleVar()
base = DoubleVar()
lado1 = DoubleVar()
lado2 = DoubleVar()
lado3 = DoubleVar()

root.band_1 = True
root.band_2 = True
root.band_3 = True
root.bands_1 = True
root.bands_2 = True
root.bands_3 = True

embed = Frame(root, width=w, height=h)  # creates embed frame for pygame window
embed.grid(columnspan=1200, rowspan=650)  # Adds grid
embed.pack(side=LEFT)  # packs window to the left
embed.configure(bg='gray')
# buttonwin = tk.Frame(root, width = 75, height = 650)
# buttonwin.pack(side = LEFT)

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

screen = pygame.display.set_mode((w - 300, 650))
screen.fill(NEGRO)

pygame.display.init()
pygame.display.update()


def opc_lineal():
    print('lineal')
    screen.fill(pygame.Color(0, 0, 0))
    pygame.font.init()
    fuente = pygame.font.Font(None, 30)
    titulo = fuente.render('Expansión Lineal', 1, rojo)
    nombres = fuente.render('Leonardo Cardona y Juan Pablo Tinoco', 1, azul)

    screen.blit(nombres, (10, 10))
    screen.blit(titulo, (10, 30))

    root.band_1 = False

    root.long = Entry(root, textvariable=longitud, width=10)
    root.long.place(x=700, y=140)

    root.longtxt = Label(root, text='Longitud :', bg='gray')
    root.longtxt.place(x=700, y=100)

    root.listbox = Combobox(root, width=10, textvariable=coef_lineal)
    root.listbox.place(x=850, y=140)
    root.listbox['values'] = ("Aluminio", "Cobre", "Acero", "Vidrio", "Zinc", "Plomo", "Diamante")

    root.coetxt = Label(root, text='Coeficiente :', bg='gray')
    root.coetxt.place(x=850, y=100)

    root.temp_ini = Entry(root, textvariable=temp_i, width=10)
    root.temp_ini.place(x=700, y=200)

    root.temp_initxt = Label(root, text='Temperatura Inicial :', bg='gray')
    root.temp_initxt.place(x=700, y=170)

    root.temp_fin = Entry(root, textvariable=temp_f, width=10)
    root.temp_fin.place(x=850, y=200)

    root.temp_fintxt = Label(root, text='Temperatura Final :', bg='gray')
    root.temp_fintxt.place(x=850, y=170)

    root.botoncalcular = Button(root, text='calcular', command=calcular_lineal)
    root.botoncalcular.place(x=700, y=250)

    if not root.band_2:
        root.cir.destroy()
        root.cua.destroy()
        root.tri.destroy()
        root.listbox2.destroy()
        root.coetxt2.destroy()
        root.temp_fin2.destroy()
        root.temp_fintxt2.destroy()
        root.temp_initxt2.destroy()
        root.temp_ini2.destroy()
        root.botoncalcular2.destroy()
        if selected2.get() == 1:
            root.radio.destroy()
            root.radiotxt.destroy()
        elif selected2.get() == 2:
            root.basetxt.destroy()
            root.base.destroy()
            root.alturatxt.destroy()
            root.altura.destroy()
        elif selected2.get() == 3:
            root.lado1.destroy()
            root.lado1txt.destroy()
            root.lado2.destroy()
            root.lado2txt.destroy()
            root.lado3.destroy()
            root.lado3txt.destroy()
    embed.configure(bg='gray')


def opc_superficial():
    print('superficial')

    root.band_2 = False
    screen.fill(pygame.Color(0, 0, 0))
    pygame.font.init()
    fuente = pygame.font.Font(None, 30)
    titulo = fuente.render('Expansión Superficial', 1, rojo)
    nombres = fuente.render('Leonardo Cardona y Juan Pablo Tinoco', 1, azul)

    screen.blit(nombres, (10, 10))
    screen.blit(titulo, (10, 30))

    root.cir = Radiobutton(root, text='Circulo', value=1, variable=selected2, bg='gray', command=opc_circulo)
    root.cir.place(x=710, y=100)
    root.cua = Radiobutton(root, text='Cuadrado', value=2, variable=selected2, bg='gray', command=opc_cuadrado)
    root.cua.place(x=790, y=100)
    root.tri = Radiobutton(root, text='Triángulo', value=3, variable=selected2, bg='gray', command=opc_triangulo)
    root.tri.place(x=880, y=100)

    root.listbox2 = Combobox(root, width=10, textvariable=coef_superficial)
    root.listbox2.place(x=710, y=290)
    root.listbox2['values'] = ("Aluminio", "Cobre", "Acero", "Vidrio", "Zinc", "Plomo", "Diamante")

    root.coetxt2 = Label(root, text='Coeficiente :', bg='gray')
    root.coetxt2.place(x=710, y=270)

    root.temp_ini2 = Entry(root, textvariable=temp_i, width=10)
    root.temp_ini2.place(x=710, y=230)

    root.temp_initxt2 = Label(root, text='Temperatura Inicial :', bg='gray')
    root.temp_initxt2.place(x=710, y=200)

    root.temp_fin2 = Entry(root, textvariable=temp_f, width=10)
    root.temp_fin2.place(x=850, y=230)

    root.temp_fintxt2 = Label(root, text='Temperatura Final :', bg='gray')
    root.temp_fintxt2.place(x=850, y=200)

    root.botoncalcular2 = Button(root, text='calcular', command=calcular_superficial)
    root.botoncalcular2.place(x=810, y=287)
    if not root.band_1:
        root.long.destroy()
        root.longtxt.destroy()
        root.listbox.destroy()
        root.coetxt.destroy()
        root.temp_fin.destroy()
        root.temp_fintxt.destroy()
        root.temp_initxt.destroy()
        root.temp_ini.destroy()
        root.botoncalcular.destroy()
    embed.configure(bg='gray')


def opc_volumetrica():
    print('volumetrica')


def opc_circulo():
    print('circulo')
    root.bands_1 = False
    screen.fill(pygame.Color(0, 0, 0))
    pygame.font.init()
    fuente = pygame.font.Font(None, 30)
    titulo = fuente.render('Expansión Superficial', 1, rojo)
    nombres = fuente.render('Leonardo Cardona y Juan Pablo Tinoco', 1, azul)
    opcion = fuente.render('Circulo', 1, azul)

    screen.blit(nombres, (10, 10))
    screen.blit(titulo, (10, 30))
    screen.blit(opcion, (10, 50))
    if (not root.bands_2):
        root.basetxt.destroy()
        root.base.destroy()
        root.alturatxt.destroy()
        root.altura.destroy()
        root.bands_2 = True

    if (not root.bands_3):
        root.lado1.destroy()
        root.lado1txt.destroy()
        root.lado2.destroy()
        root.lado2txt.destroy()
        root.lado3.destroy()
        root.lado3txt.destroy()
        root.bands_3 = True
    embed.configure(bg='gray')

    root.radiotxt = Label(root, text='Radio :', bg='gray')
    root.radiotxt.place(x=710, y=130)
    root.radio = Entry(root, textvariable=radio, width=10)
    root.radio.place(x=710, y=160)


def opc_cuadrado():
    print('cuadrado')
    root.bands_2 = False
    screen.fill(pygame.Color(0, 0, 0))
    screen.fill(pygame.Color(0, 0, 0))
    pygame.font.init()
    fuente = pygame.font.Font(None, 30)
    titulo = fuente.render('Expansión Superficial', 1, rojo)
    nombres = fuente.render('Leonardo Cardona y Juan Pablo Tinoco', 1, azul)
    opcion = fuente.render('Cuadrilatero', 1, azul)

    screen.blit(nombres, (10, 10))
    screen.blit(titulo, (10, 30))
    screen.blit(opcion, (10, 50))
    if (not root.bands_1):
        root.radiotxt.destroy()
        root.radio.destroy()
        root.bands_1 = True

    if (not root.bands_3):
        root.lado1.destroy()
        root.lado1txt.destroy()
        root.lado2.destroy()
        root.lado2txt.destroy()
        root.lado3.destroy()
        root.lado3txt.destroy()
        root.bands_3 = True
    embed.configure(bg='gray')

    root.basetxt = Label(root, text='Base :', bg='gray')
    root.basetxt.place(x=710, y=130)
    root.base = Entry(root, textvariable=base, width=10)
    root.base.place(x=710, y=160)

    root.alturatxt = Label(root, text='Altura :', bg='gray')
    root.alturatxt.place(x=800, y=130)
    root.altura = Entry(root, textvariable=altura, width=10)
    root.altura.place(x=800, y=160)


def opc_triangulo():
    print('triangulo')
    root.bands_3 = False
    screen.fill(pygame.Color(0, 0, 0))
    pygame.font.init()
    fuente = pygame.font.Font(None, 30)
    titulo = fuente.render('Expansión Superficial', 1, rojo)
    nombres = fuente.render('Leonardo Cardona y Juan Pablo Tinoco', 1, azul)
    opcion=fuente.render('Triangulo', 1, azul)

    screen.blit(nombres, (10, 10))
    screen.blit(titulo, (10, 30))
    screen.blit(opcion, (10, 50))
    if (not root.bands_1):
        root.radiotxt.destroy()
        root.radio.destroy()
        root.bands_1 = True
    if (not root.bands_2):
        root.basetxt.destroy()
        root.base.destroy()
        root.alturatxt.destroy()
        root.altura.destroy()
        root.bands_2 = True
    embed.configure(bg='gray')

    root.lado1txt = Label(root, text='Lado 1 :', bg='gray')
    root.lado1txt.place(x=710, y=130)
    root.lado1 = Entry(root, textvariable=lado1, width=10)
    root.lado1.place(x=710, y=160)

    root.lado2txt = Label(root, text='Lado 2 :', bg='gray')
    root.lado2txt.place(x=790, y=130)
    root.lado2 = Entry(root, textvariable=lado2, width=10)
    root.lado2.place(x=790, y=160)

    root.lado3txt = Label(root, text='Lado 3 :', bg='gray')
    root.lado3txt.place(x=870, y=130)
    root.lado3 = Entry(root, textvariable=lado3, width=10)
    root.lado3.place(x=870, y=160)


def draw():
    pygame.draw.circle(screen, rojo, (200, 200), 25)

    pygame.display.update()


def calcular_lineal():
    screen.fill(pygame.Color(0, 0, 0))
    pygame.font.init()
    fuente = pygame.font.Font(None, 30)
    titulo = fuente.render('Expansión Lienal', 1, rojo)
    nombres = fuente.render('Leonardo Cardona y Juan Pablo Tinoco', 1, azul)

    screen.blit(nombres, (10, 10))
    screen.blit(titulo, (10, 30))
    if longitud.get() != '' and temp_i.get() != '' and temp_f.get() != '':
        diferencia_temp = (temp_f.get() - temp_i.get())
        exp_lineal = coeficiente.get(coef_lineal.get()) * longitud.get() * diferencia_temp
        print(exp_lineal)
        pygame.draw.line(screen, azul, (100, 200), (100 + escala_i(longitud.get()), 200), 10)
        pygame.draw.line(screen, rojo, (100, 400),
                         (100 + escala_i(longitud.get()) + exp_li(exp_lineal) + exp_lineal, 400), 10)
        pygame.draw.line(screen, azul, (100, 400), (100 + escala_i(longitud.get()), 400), 10)

        pygame.font.init()
        fuente = pygame.font.Font(None, 20)
        mensaje = fuente.render('Longitud Final: ' + str(longitud.get() + exp_lineal), 1, (255, 255, 255))
        screen.blit(mensaje, (100, 380))
        pygame.display.flip()
        pygame.display.update()


def calcular_superficial():
    screen.fill(pygame.Color(0, 0, 0))
    pygame.font.init()
    fuente = pygame.font.Font(None, 30)
    titulo = fuente.render('Expansión Superficial', 1, rojo)
    nombres = fuente.render('Leonardo Cardona y Juan Pablo Tinoco', 1, azul)


    screen.blit(nombres, (10, 10))
    screen.blit(titulo, (10, 30))

    if selected2.get() == 1:
        if radio.get() != '' and temp_i.get() != '' and temp_f.get() != '':
            opcion = fuente.render('Circulo', 1, azul)
            screen.blit(opcion, (10, 50))
            area_circulo = math.pi * (radio.get() * radio.get())
            diferencia_temp = (temp_f.get() - temp_i.get())
            expan_superficial = coeficiente_Superficial.get(coef_superficial.get()) * area_circulo * diferencia_temp
            pygame.font.init()
            fuente = pygame.font.Font(None, 20)
            mensaje_area_fin = fuente.render('Area Final: ' + str(round(area_circulo + expan_superficial, 3)), 1,
                                             (255, 255, 255))
            mensaje_area_ini = fuente.render('Area Inicial: ' + str(round(area_circulo, 3)), 1, (255, 255, 255))
            mensaje_expansion = fuente.render('La Expansion fue de : ' + str(round(expan_superficial, 3)), 1,
                                              (255, 255, 255))
            screen.blit(mensaje_area_ini, (100, 550))
            screen.blit(mensaje_expansion, (100, 570))
            screen.blit(mensaje_area_fin, (100, 590))

            pygame.draw.circle(screen, azul, (300, 150), escala_cir(int(radio.get())))
            pygame.draw.circle(screen, rojo, (300, 450), escala_cir(int(radio.get())) + expa_s(expan_superficial))
            pygame.draw.circle(screen, azul, (300, 450), escala_cir(int(radio.get())))

            pygame.display.update()
    elif selected2.get() == 2:
        if base.get() != '' and altura.get() != '' and temp_i.get() != '' \
                and temp_f.get() != '' and coef_superficial.get() != '':
            opcion = fuente.render('Cuadrilátero', 1, azul)
            screen.blit(opcion, (10, 50))
            diferencia_temp = (temp_f.get() - temp_i.get())
            area_cuadra = base.get()*altura.get()
            expan_superficial = coeficiente_Superficial.get(coef_superficial.get()) * area_cuadra * diferencia_temp

            pygame.font.init()
            fuente = pygame.font.Font(None, 20)
            mensaje_area_fin = fuente.render('Area Final: ' + str(round(area_cuadra + expan_superficial, 3)), 1,
                                             (255, 255, 255))
            mensaje_area_ini = fuente.render('Area Inicial: ' + str(round(area_cuadra, 3)), 1, (255, 255, 255))
            mensaje_expansion = fuente.render('La Expansion fue de : ' + str(round(expan_superficial, 3)), 1,
                                              (255, 255, 255))
            screen.blit(mensaje_area_ini, (500, 570))
            screen.blit(mensaje_expansion, (500, 590))
            screen.blit(mensaje_area_fin, (500, 610))

            msj_base = fuente.render('Base: ' + str(round(base.get(), 3)), 1, (255, 255, 255))
            screen.blit(msj_base, (220, 130))
            msj_altura = fuente.render('altura: ' + str(round(altura.get(), 3)), 1, (255, 255, 255))
            screen.blit(msj_altura, (110, 190))
            if base.get()> altura.get():
                pygame.draw.rect(screen, azul, ((200, 150), (200+(int(base.get()*0.05)),100+ (int(altura.get()*0.05))) ) )
                pygame.draw.rect(screen, rojo, ((195, 445), (210+(int(base.get()*0.05)),110+ (int(altura.get()*0.05))) ))
                pygame.draw.rect(screen, azul, ((200, 450), (200+(int(base.get()*0.05)),100+ (int(altura.get()*0.05))) ) )
            elif base.get()< altura.get():

                pygame.draw.rect(screen, azul, ((200, 150), (100 + (int(base.get()*0.05)), 150 + (int(altura.get()*0.05)))))
                pygame.draw.rect(screen, rojo, ((195, 445), (110 + (int(base.get()*0.05)), 160 + (int(altura.get()*0.05)))))
                pygame.draw.rect(screen, azul, ((200, 450), (100 + (int(base.get()*0.05)), 150 + (int(altura.get()*0.05)))))
            else :
                pygame.draw.rect(screen, azul, ((200, 150), (150 + (int(base.get()*0.05)), 150 + (int(altura.get()*0.05)))))
                pygame.draw.rect(screen, rojo, ((195, 445), (160 + (int(base.get()*0.05)), 160 + (int(altura.get()*0.05)))))
                pygame.draw.rect(screen, azul, ((200, 450), (150 + (int(base.get()*0.05)), 150 + (int(altura.get()*0.05)))))
            pygame.display.update()

    elif selected2.get() == 3:
        if lado1.get() != '' and lado2.get() != '' and lado3.get() != '' and temp_i.get() != '' \
                and temp_f.get() != '' and coef_superficial.get() != '':
            opcion = fuente.render('Triangulo', 1, azul)
            screen.blit(opcion, (10, 50))

            diferencia_temp = (temp_f.get() - temp_i.get())
            area_trian = base.get() * altura.get()
            expan_superficial = coeficiente_Superficial.get(coef_superficial.get()) * area_cuadra * diferencia_temp

            listapuntos = [(200, 300), (300, 180), (400, 300)]
            pygame.draw.polygon(screen, azul, listapuntos)
            listapuntos2 = [(190, 555), (300, 410), (410, 555)]
            pygame.draw.polygon(screen, rojo, listapuntos2)
            listapuntos3 = [(200, 550), (300, 420), (400, 550)]
            pygame.draw.polygon(screen, azul, listapuntos3)
            pygame.display.update()



def escala_i(longitud):
    if longitud < 15:
        return 250
    elif longitud < 30:
        return 300
    elif longitud < 45:
        return 350
    elif longitud < 60:
        return 400
    else:
        return 450


def exp_li(exp):
    if exp < 0.1e-3:
        return 22
    elif exp < 0.1e-1:
        return 22
    elif exp < 2:
        return 22
    elif exp < 5:
        return 22
    else:
        return 19


def escala_cir(radio):
    if radio < 5:
        return 25
    elif radio < 10:
        return 30
    elif radio < 15:
        return 35
    elif radio < 20:
        return 40
    elif radio < 25:
        return 45
    elif radio < 30:
        return 50
    elif radio < 35:
        return 55
    elif radio < 40:
        return 60
    elif radio < 45:
        return 65
    elif radio < 50:
        return 70
    else:
        return 65


def expa_s(exp):
    if exp < 0.05:
        return 1
    elif exp < 1:
        return 3
    elif exp < 3:
        return 5
    elif exp < 8:
        return 7
    elif exp < 20:
        return 9
    else:
        return 12


def suma():
    if (area.get() != '' and base.get() != ''):
        print(int(area.get()) + int(base.get()))
        print(selected.get())

pygame.font.init()
fuente = pygame.font.Font(None, 30)
nombres = fuente.render('Leonardo Cardona y Juan Pablo Tinoco', 1,azul)

screen.blit(nombres, (10, 10))

rad1 = Radiobutton(root, text='Exp Lineal', value=1, variable=selected, bg='gray', command=opc_lineal).place(x=750,
                                                                                                             y=10)
rad2 = Radiobutton(root, text='Exp Superficial', value=2, variable=selected, bg='gray', command=opc_superficial).place(
    x=750, y=30)
rad3 = Radiobutton(root, text='Exp Volumetrica', value=3, variable=selected, bg='gray', command=opc_volumetrica).place(
    x=750, y=50)
# botonmuestra = Button(root, text='mostrar', command=mostrar).place(x=750, y=70)
# button1 = Button(buttonwin,text = 'pintar',  command=draw)
# button1.pack(side=LEFT)

root.update()

while True:
    pygame.display.update()
    root.update()
