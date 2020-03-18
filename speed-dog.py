#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
from subprocess import call
import subprocess
import subprocess as sub
import webbrowser
from PIL import Image, ImageTk
from itertools import count

call('sudo apt-get install speedtest-cli', shell=True)
call('sudo apt-get install python3', shell=True)
call('sudo apt-get install python3-tk', shell=True)

def metrica():

	p = sub.Popen(['speedtest-cli'],stdout=sub.PIPE,stderr=sub.PIPE)
	output, errors = p.communicate()
	
	text = tk.Text(v_home, width=75, height=11, highlightbackground="black", background="black", 
		foreground='orange', bd=0, font=("URW Chancery L", 16))

	text.pack()
	text.place(x=300, y=150)
	text.insert(tk.END, output)


	boton_repetir=Frame(v_home, width=50, height=100)
	boton_repetir.place(x=470, y=450)
	Button(boton_repetir, 
		command=lambda:[text.destroy(), boton_repetir.destroy(), metrica()], 
		highlightbackground="orange", text="Repetir Análisis", cursor="heart", justify="center", 
		bd=0, relief="raised", overrelief="sunken", background="black", activebackground='black', 
		activeforeground='Red', foreground='darkred', font=("URW Chancery L", 20)).pack()

	boton_volver=Frame(v_home, width=50, height=100)
	boton_volver.place(x=490, y=500)
	Button(boton_volver, 
		command=lambda:[v_home.quit()], 
		highlightbackground="orange", text="Salir de aquí", cursor="heart", justify="center", 
		bd=0, relief="raised", overrelief="sunken", background="black", activebackground='black', 
		activeforeground='Red', foreground='darkred', font=("URW Chancery L", 20)).pack()




class ImageLabel(tk.Label):
    
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)



v_home = tk.Tk()

v_home.title("OffShell System Community Software")
v_home.geometry("1124x650+75+50")
v_home.resizable(width=False, height=False)
v_home.config(bg="black", bd=0)
v_home.tk.call('wm', 'iconphoto', v_home._w, tk.PhotoImage(file='primate.gif'))


lbl = ImageLabel(v_home, highlightbackground="black", bd=0, bg='black')
lbl.pack()
lbl.place(x=325, y=130)
lbl.load('dog.gif')

lbl = ImageLabel(v_home, highlightbackground="black", bd=0, bg='black')
lbl.pack()
lbl.place(x=760, y=500)
lbl.load('mundo.gif')


L_text=Label(v_home, text="Speed-Dog", 
	highlightbackground="black", bd=0, foreground='orange', background="black", 
	activebackground="black", font=("URW Chancery L", 24))
L_text.place(x=495, y=10)

L_text2=Label(v_home, text="Tu programa fiel para analizar la conexión.", 
	highlightbackground="black", bd=0, foreground='orange', background="black", 
	activebackground="black", font=("URW Chancery L", 18))
L_text2.place(x=375, y=50)

L_text3=Label(v_home, text="Software OffShell System", 
	highlightbackground="black", bd=0, foreground='darkred', background="black", 
	activebackground="black", font=("URW Chancery L", 20))
L_text3.place(x=855, y=440)

boton_menu1=Frame(v_home)
boton_menu1.pack(fill=BOTH, expand=YES)
boton_menu1.place(x=470, y=90)
Button(boton_menu1, highlightbackground="black", command=lambda:[lbl.destroy(), boton_menu1.destroy(), metrica()],
    text="Iniciar Análisis", foreground='white', activeforeground='red',
    cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black",
    activebackground="black", font=("URW Chancery L", 20)).pack()
	

v_home.mainloop()