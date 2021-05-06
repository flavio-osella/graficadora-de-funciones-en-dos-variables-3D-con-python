#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Graficadora 3D con derivada 
Flavio Osella.
v.1.0.0"""

from math import *
from tkinter import *
from numpy import *
from matplotlib import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
from matplotlib import style
import sympy as sy
from sympy import symbols
from sympy.plotting import plot
from sympy import integrate
from sympy import diff
from sympy.abc import x , y
from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data
from matplotlib import cm 





class Ini():
    def __init__(self,root):
        self.root=root
        self.root.title("Graficos 3D")       
        self.pantalla=Text(root,state="normal",width=20,height=3,background="black",foreground="white",font=("Helvetica",15))
        self.pantalla.grid(row=0,column=0,columnspan=4)
        self.pantalla2=Text(root,state="disabled",width=20,height=3,background="black",foreground="white",font=("Helvetica",15))
        self.pantalla2.grid(row=0,column=5,columnspan=4)        
        self.ventana3d=Toplevel(root_principal)
        self.ventana3d.title(" Grafico Función")        
        self.fig2=Figure(figsize=(8,8))
        self.ax2=self.fig2.add_subplot(111,projection='3d')
        self.ax2.set_facecolor('black')
        self.canvas2=FigureCanvasTkAgg(self.fig2,master=self.ventana3d)
        self.canvas2.draw()
        self.canvas2.get_tk_widget().pack()
        self.toolbar2 = NavigationToolbar2Tk(self.canvas2, self.ventana3d)
        self.toolbar2.pack(side=TOP)
        self.toolbar2.update()             
        self.texto=""
        self.otraVar="" 
        self.notacion=""
        self.texto2=""    
        self.ani3d=FuncAnimation(self.fig2,self.dibujar3d,interval=1000)              
        boton1=Button(self.root,text="Graficar",width=8,height=1,
                      command=lambda: [self.borrar2(),self.representar3d()])
        boton1.grid(row=1,column=0)
        self.etiqueta2=Label(master=root,text="Potencias")
        self.etiqueta2.grid(row=2,column=0)
        boton2=self.crearBoton(u"\u00B2","black")
        boton2.grid(row=3,column=0)
        boton3=self.crearBoton(u"\u00B3","black")
        boton3.grid(row=3,column=1)
        boton4=self.crearBoton(u"\u2074","black")
        boton4.grid(row=3,column=2)
        boton5=self.crearBoton(u"\u2075","black")
        boton5.grid(row=4,column=0)
        boton6=self.crearBoton(u"\u2076","black")
        boton6.grid(row=4,column=1)
        boton7=self.crearBoton(u"\u2077","black")
        boton7.grid(row=4,column=2)
        boton8=self.crearBoton(u"\u2078","black")
        boton8.grid(row=5,column=0)
        boton9=self.crearBoton(u"\u2079","black")
        boton9.grid(row=5,column=1)
        boton10=Button(root,text="d/dy",width=4,height=4,font=("Helvetica",20),command=lambda:self.derivarY())
        boton10.grid(row=3,column=5,rowspan=2)
        boton11=Button(root,text="d/dx",width=4,height=4,font=("Helvetica",20),command=lambda:self.derivarX())
        boton11.grid(row=3,column=6,rowspan=2)
        boton13=self.crearBoton(u"\u23B7","black")
        boton13.grid(row=5,column=2)
     
      
 

       
        self.funciones={"sin":"sin","e":"exp",u"\u00B2":"**2",u"\u00B3":"**3",u"\u2074":"**4",
                        u"\u2075":"**5",u"\u2076":"**6",u"\u2077":"**7",u"\u2078":"**8",
                        u"\u2079":"**9",u"\u23B7":"sqrt"}

        self.funcionesSy={"e":"sy.exp","log":"sy.log","sin":"sy.sin",u"\u00B2":"**2",
                          u"\u00B3":"**3",u"\u2074":"**4",u"\u2075":"**5",u"\u2076":"**6",
                          u"\u2077":"**7",u"\u2078":"**8",u"\u2079":"**9","cos":"sy.cos",u"\u23B7":"sy.sqrt"}

        self.vuelveNotacion={"exp":"e","**2":u"\u00B2","**3":u"\u00B3","**4":u"\u2074","**5":u"\u2075",
                       "**6":u"\u2076","**7":u"\u2077","**8":u"\u2078","**9":u"\u2079","sqrt":u"\u23B7"}



    def crearBoton(self,valor,color,ancho=3,alto=2):
        return Button(self.root,text=valor,fg=color,font=("Helvetica",15),width=ancho,
                      height=alto,command=lambda:self.escribir(valor))

    def reemplazar(self):
        if self.pantalla.get("1.0",END)!="":
            self.texto=self.pantalla.get("1.0",END)        
            for i in self.funciones:
                if i in self.texto :
                    self.texto=self.texto.replace(i,self.funciones[i])
                else:
                    pass
        else:
            self.texto="0"
        return

    def sustituir(self):
        if self.pantalla2.get("1.0",END)!="":
            self.texto2=self.pantalla2.get("1.0",END)       
            for i in self.funciones:
                if  i in self.texto2:
                    self.texto2=self.texto2.replace(i,self.funciones[i])
                else:
                    pass
        else:
            self.texto2="0"                
        return
         
             
    def escribir(self,valor):
        self.pantalla.insert(END,valor)
        return

    def reemplazar2(self):
        self.otraVar=self.pantalla.get("1.0",END)
        for i in self.funcionesSy:
            if i in self.otraVar:
                self.otraVar=self.otraVar.replace(i,self.funcionesSy[i])
            else:
                pass
        return

    def volverNotacion(self,f):
        self.notacion=str(f)
        for i in self.vuelveNotacion:
            if i in self.notacion:
                self.notacion=self.notacion.replace(i,self.vuelveNotacion[i])
            else:
                pass
        return  
        

    def derivarY(self):
        self.borrar2()
        self.reemplazar2()
        f=diff(eval(self.otraVar),y)
        self.otraVar=""
        self.volverNotacion(f)
        self.escribirPantalla2(self.notacion)
        self.notacion=""
        return          

    def derivarX(self):
        self.borrar2()
        self.reemplazar2()
        f=diff(eval(self.otraVar),x)
        self.otraVar=""
        self.volverNotacion(f)
        self.escribirPantalla2(self.notacion)
        self.notacion=""
        return

    def representar3d(self):
        self.reemplazar()
        self.ani3d.event_source.start()
        plt.show()
        return
        
    def dibujar3d(self,i):                
        try:
            x,y = meshgrid(linspace(-5,5,30),linspace(-5,5,30))
            z=eval(self.texto)
            self.texto=""
            self.ax2.clear()
            self.ax2.plot_surface(x,y,z,cmap='hot',antialiased=False)        
            self.ax2.grid()
            self.ani3d.event_source.stop()
        except:
            pass    
        return
         
    def escribirPantalla2(self,fun):
        self.pantalla2.configure(state="normal")
        self.pantalla2.insert(END,fun)
        self.pantalla2.configure(state="disabled")
        return

    def borrar2(self):
        self.pantalla2.configure(state="normal")
        self.pantalla2.delete("1.0",END)
        self.pantalla2.configure(state="disabled")
        return
        


              

                             
root_principal=Tk()
style.use( 'seaborn-ticks')
graficadora=Ini(root_principal)
root_principal.mainloop()


