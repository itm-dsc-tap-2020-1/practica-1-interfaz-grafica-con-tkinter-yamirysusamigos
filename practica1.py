import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk 
from tkinter import Menu
from tkinter import messagebox as mBox
def funcionR():
    print("")
def fsalir():
    ventana.quit()
    ventana.destroy()
    exit()
def fimprimir3():
    si=1
    si2=False
    imp = "Datos: \n"
    if nombre.get() == "":
        si=0
    else:
        imp += "\nNombre: " + nombre.get()
    if paterno.get() == "":
        si= 0
    else:
        imp += "\nA Paterno: " + paterno.get()
    if materno.get() == "":
        si=0
    else:
        imp += "\nA Materno: " + materno.get()
    if direc.get() == "":
        si=0
    else:
        imp += "\nDireccion: " + direc.get()
    if col.get() == "":
        si=0
    else:
        imp += "\nColonia: " + col.get()
    if ciu.get() == "":
        si=0
    else:
        imp += "\nCiudad: " + ciu.get()
    if muni.get() == "":
        si=0
    else:
        imp += "\nMunicipio: " + muni.get()
    imp += "\nPasatiempos:\n"
    if op1.get() == 1:
        imp += "- Deportes \n"
        si2 = True
    if op2.get() == 1:
        imp += "- Lectura \n"
        si2 = True
    if op3.get() == 1:
        imp += "- Videojuegos \n"
        si2 = True
    if op4.get() == 1:
        imp += "- Fiesta \n"
        si2 = True
    if op5.get() == 1:
        imp += "- Artes \n"  
        si2 = True
    if si2 == False: 
        imp += "*No tiene pasatiempos*\n"
    imp += "Estado: \n-" + op.get()
    if  si==0:
        mBox.showinfo('Error en registro','Aun no estan llenos todos los campos.\nse necesitan completos para imprimirlos.')
    else: 
       mBox.showinfo('Imprimir', imp)
def fimprimir2():
    si= False
    imp="Pasatiempos:\n"
    if op1.get() == 1:
        imp += "- Deportes \n"
        si = True
    if op2.get() == 1:
        imp += "- Lectura \n"
        si = True
    if op3.get() == 1:
        imp += "- Videojuegos \n"
        si = True
    if op4.get() == 1:
        imp += "- Fiesta \n"
        si = True
    if op5.get() == 1:
        imp += "- Artes \n"  
        si = True
    if si == False: 
        imp += "*No tiene pasatiempos*\n"
    imp += "Estado: \n-" + op.get()
    mBox.showinfo('Imprimir', imp)
def fimprimir():
    si=1
    if nombre.get() == "":
        texto1.configure(foreground='firebrick')
        si=0
    else:
        texto1.configure(foreground='black')
    if paterno.get() == "":
        texto2.configure(foreground='firebrick')
        si= 0
    else:
        texto2.configure(foreground='black')
    if materno.get() == "":
        texto3.configure(foreground='firebrick')
        si=0
    else:
        texto3.configure(foreground='black')
    if direc.get() == "":
        texto4.configure(foreground='firebrick')
        si=0
    else:
        texto4.configure(foreground='black')
    if col.get() == "":
        texto5.configure(foreground='firebrick')
        si=0
    else:
        texto5.configure(foreground='black')
    if ciu.get() == "":
        texto6.configure(foreground='firebrick')
        si=0
    else:
        texto6.configure(foreground='black')
    if muni.get() == "":
        texto8.configure(foreground='firebrick')
        si=0
    else:
        texto8.configure(foreground='black')
    if  si==0:
        mBox.showinfo('Error en registro','Llenar todos los campos')
    else:
       imp = "Nombre: "+nombre.get() + "\nA Paterno: " + paterno.get() + "\nA Materno: " + materno.get() 
       imp += "\nDireccion: " + direc.get() + "\nColonia: " + col.get() + "\nCiudad: " + ciu.get()  + "\nMunicipio: " + muni.get()  
       mBox.showinfo('Imprimir', imp)
def facerca():
    mBox.showinfo('Acerca de ','Leonardo Aldair Resendiz Pantoja\n4to Semestre\nISC\n')

#crear ventana
ventana=tk.Tk()
ventana.title("Sistema Escolar - Menu")
#crear menu
bmenu= Menu(ventana)
ventana.config(menu=bmenu)
opciones= Menu(bmenu)
opciones.add_command(label="Imprimir", command= fimprimir3)
opciones.add_separator()
opciones.add_command(label="Salir",command=fsalir)
bmenu.add_cascade(label="Sistema", menu=opciones)
#SEGUNDO MENU
menua= Menu(bmenu)
menua.add_command(label="Acerca de ", command=facerca)
bmenu.add_cascade(label="Ayuda",menu=menua) 
#pestana 1
tabcontrol = ttk.Notebook(ventana)
tab1 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1, text='Datos Personales')
tabcontrol.grid(column=1,row=0)
#datos
texto1= ttk.Label(tab1, text="Nombre: ")
texto1.grid(column=0,row=3)
texto2= ttk.Label(tab1, text="Apellido Paterno: ")
texto2.grid(column=0,row=4)
texto3= ttk.Label(tab1, text="Apellido Materno: ")
texto3.grid(column=0,row=5)
texto4= ttk.Label(tab1, text="Direccion: ")
texto4.grid(column=0,row=6)
nombre = tk.StringVar()
nombreCap = ttk.Entry(tab1, width=34, textvariable=nombre)
nombreCap.grid(column=1,row=3, columnspan=2)
paterno = tk.StringVar()
pateCap = ttk.Entry(tab1, width=34, textvariable=paterno)
pateCap.grid(column=1,row=4,columnspan=2)
materno = tk.StringVar()
mateCap = ttk.Entry(tab1, width=34, textvariable=materno)
mateCap.grid(column=1,row=5,columnspan=2)
direc = tk.StringVar()
direcCap = ttk.Entry(tab1, width=34, textvariable=direc)
direcCap.grid(column=1,row=6,columnspan=2)
#Para colonia
texto5= ttk.Label(tab1, text="Colonia: ")
texto5.grid(column=0,row=7)
col = tk.StringVar()
colonia = ttk.Combobox(tab1, width=32, textvariable=col)
colonia['values']=("","Santiaguito", "El realito" , "Torreon Nuevo")
colonia.grid(column=1,row=7,columnspan=2)
colonia.configure(state="readonly")
colonia.current(0)
#Para ciudad 
texto6= ttk.Label(tab1, text="Ciudad: ")
texto6.grid(column=0,row=8)
ciu = tk.StringVar()
ciudad = ttk.Combobox(tab1, width=32, textvariable=ciu)
ciudad['values']=("","Ciudad de Mexico", "Ciudad Juarez" , "Ciudad Hidalgo")
ciudad.grid(column=1,row=8,columnspan=2)
ciudad.configure(state="readonly")
ciudad.current(0)
#Para municipio 
texto8= ttk.Label(tab1, text="Municipio: ")
texto8.grid(column=0,row=9)
muni = tk.StringVar()
municipio = ttk.Combobox(tab1, width=32, textvariable=muni)
municipio['values']=("","Patzcuaro", "Zamora" , "Capula")
municipio.grid(column=1,row=9,columnspan=2)
municipio.configure(state="readonly")
municipio.current(0)
#boton pestana 1
accion = ttk.Button(tab1,text="Imprimir datos", command = fimprimir)
accion.grid(column=3,row=9)
#pestana 2
tab2 = ttk.Frame(tabcontrol)
tabcontrol.add(tab2, text='Datos Extras')
texto10= ttk.Label(tab2, text="Pasatiempos: ")
texto10.grid(column=0,row=10)
op1 = tk.IntVar()
cas1 = tk.Checkbutton(tab2, text="Deportes", variable=op1)
cas1.grid(column=0,row=11, sticky=tk.W)
op2 = tk.IntVar()
cas2 = tk.Checkbutton(tab2, text="Lectura", variable=op2)
cas2.grid(column=1,row=11, sticky=tk.W)
op3 = tk.IntVar()
cas3 = tk.Checkbutton(tab2, text="Videojuegos", variable=op3)
cas3.grid(column=2,row=11, sticky=tk.W)
op4 = tk.IntVar()
cas4 = tk.Checkbutton(tab2, text="Fiesta", variable=op4)
cas4.grid(column=3,row=11, sticky=tk.W)
op5 = tk.IntVar()
cas5 = tk.Checkbutton(tab2, text="Artes", variable=op5)
cas5.grid(column=4,row=11, sticky=tk.W)
#estado(RabioButton)
texto11= ttk.Label(tab2, text="Estado: ")
texto11.grid(column=0,row=12)
op = tk.StringVar()
radio1 = tk.Radiobutton(tab2, text="Soltero", variable=op,value="Soltero",command=funcionR)
radio1.grid(column=0,row=13,sticky=tk.W)
radio1.select()
radio2 = tk.Radiobutton(tab2, text="Casado", variable=op,value="Casado",command=funcionR)
radio2.grid(column=1,row=13,sticky=tk.W)
radio3 = tk.Radiobutton(tab2, text="Viudo", variable=op,value="Viudo",command=funcionR)
radio3.grid(column=2,row=13,sticky=tk.W)
radio4 = tk.Radiobutton(tab2, text="Divorciado", variable=op,value="Divorciado",command=funcionR)
radio4.grid(column=3,row=13,sticky=tk.W)
radio5 = tk.Radiobutton(tab2, text="Otro", variable=op,value="Otro",command=funcionR)
radio5.grid(column=4,row=13,sticky=tk.W)
#caja pestana 2
texto12= ttk.Label(tab2, text="Objetivo de la vida: ")
texto12.grid(column=0,row=14)
scrol_ancho = 35
scrol_alto = 3
caja = scrolledtext.ScrolledText(tab2,width=scrol_ancho, height=scrol_alto,wrap=tk.WORD)
caja.grid(column=0,row=15,columnspan=3)
#imprimir pestana 2
accion = ttk.Button(tab2,text="Imprimir datos", command = fimprimir2)
accion.grid(column=3,row=15)
ventana.mainloop() 
