from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from io import open
import os

root = Tk()
root.geometry("628x500")
root.resizable(0,0)
titulo_documento = "Sin título"
root.title(titulo_documento+".txt")

barra = Scrollbar(root)
barra.pack(side=RIGHT,fill=Y)
texto = Text(root,height=29,width=78,selectbackground="blue",yscrollcommand=barra.set)
texto.pack(pady=3)
barra.config(command=texto.yview)
estado_barra = "Barra de estado"
contador = 0

def barra_estado(counter):
	counter=+1
	global estado_barra
	if counter%2!=0:
		estado = Label(frame,text=estado_barra,height=1,bg="light gray",width=150)
		estado.grid(row=0,column=0)
	else:
		estado.destroy()
		estado.grid_remove()
		estado1 = Label(frame,text="",height=1,bg="white")
		estado1.grid(row=0,column=0)
		
def abrir():
	global estado_barra
	if texto.get(1.0,END) != "":
		opcion = messagebox.askquestion("Advertencia","¿Desea guardar este archivo antes de abrir uno nuevo?")
		if opcion == "yes":
			guardar_como()
			texto.delete(1.0,END)
		else:
			texto.delete(1.0,END)
			abrir_archivo = filedialog.askopenfilename(initialdir=r"C:\Users\KAREN RIERA\Documents\DANIEL",title="Abrir",filetypes=(("Text files","*.txt"),("All files","*.*")))
			if abrir_archivo:
				archivo_abierto = open(abrir_archivo,"r")
				texto_archivo = archivo_abierto.read()
				texto.insert(INSERT,texto_archivo)
				head,titulo_documento = os.path.split(abrir_archivo.name)
				root.title(titulo_documento)
				abrir_archivo.close()
	estado_barra = "Archivo abierto"
	barra_estado(contador)
				
def guardar_como():
	global estado_barra
	guardar_texto_como = filedialog.asksaveasfilename(initialdir=r"C:\Users\KAREN RIERA\Documents\DANIEL",title="Guardar como",defaultextension=".txt",filetypes=(("Text files","*.txt"),("All files","*.*")))
	if guardar_texto_como:
		texto_guardado = open(guardar_texto_como,"w")
		texto_guardado.write(texto.get(1.0,END))
		texto_guardado.close()
		head,titulo_documento = os.path.split(guardar_texto_como)
		root.title(titulo_documento)
		estado_barra = "Guardado"
		barra_estado(contador)
	
def guardar():
	global guardar_texto_como
	global estado_barra
	global titulo_documento
	if titulo_documento == "Sin título":
		guardar_como()
	else:
		texto_escrito = open(guardar_texto_como,"wr")
		texto_escrito.write(texto.get(1.0,END))
		texto_escrito.close()
		estado_barra = "Guardado"
		barra_estado(contador)
		
def nuevo():
	global estado_barra
	if texto.get(1.0,END) != "":
		opcion = messagebox.askquestion("Advertencia","¿Desea guardar los cambios?")
		if opcion == "yes":
			guardar_como()
			estado_barra = "Nuevo"
			barra_estado(contador)
			texto.delete(1.0,END)
		elif opcion == "no":
			texto.delete(1.0,END)
			root.title(titulo_documento+".txt")
			estado_barra = "Nuevo"
			barra_estado(contador)
		else:
			pass

def salir():
	if texto.get(1.0,END) == "":
		root.quit()
	else:
		opcion = messagebox.askquestion("Advertencia","¿Desea guardar los cambios antes de salir?")
		if opcion == "yes":
			guardar_texto_como = filedialog.asksaveasfilename(initialdir=r"C:\Users\KAREN RIERA\Documents\DANIEL",title="Guardar como",defaultextension=".txt",filetypes=(("Text files","*.txt"),("All files","*.*")))
			if guardar_texto_como:
				texto_guardado = open(guardar_texto_como,"w")
				texto_guardado.write(texto.get(1.0,END))
				texto_guardado.close()
			root.quit()
		else:
			root.quit()
			
		root.quit()
			
def ayuda():
	messagebox.showinfo("Información","Desarrollado por Daniel Mejias como motivo de práctica para ser mejor programador. ¡ÁNIMO!")

def deshacer():
	global estado_barra
	texto.delete(1.0,END)
	root.title(titulo_documento+".txt")
	estado_barra = "Deshecho"
	barra_estado(contador)
	
def copy_text():
	texto.clipboard_clear()
	texto.clipboard_append(texto.selection_get())
	estado_barra = "Texto copiado"

def cut_text():
	copy_text()
	texto.delete("sel.first","sel.last")
	estado_barra = "Texto cortado"

def paste_text():
	texto.insert(INSERT,texto.clipboard_get())
	estado_barra = "Texto pegado"

frame = Frame(root)
frame.pack(fill=X)

barramenu = Menu(root)
root.config(menu=barramenu)

archivo_menu = Menu(barramenu,tearoff=0)
edicion_menu = Menu(barramenu,tearoff=0)
estado_menu = Menu(barramenu,tearoff=0)
ayuda_menu = Menu(barramenu,tearoff=0)

barramenu.add_cascade(label="Archivo",menu=archivo_menu)
archivo_menu.add_command(label="Nuevo",command=nuevo)
archivo_menu.add_command(label="Abrir",command=abrir)
archivo_menu.add_command(label="Guardar",command=guardar)
archivo_menu.add_command(label="Guardar como...",command=guardar_como)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir",command=salir)

barramenu.add_cascade(label="Edición",menu=edicion_menu)
edicion_menu.add_command(label="Deshacer",command=deshacer)
edicion_menu.add_separator()
edicion_menu.add_command(label="Copiar",command=copy_text)
edicion_menu.add_command(label="Cortar",command=cut_text)
edicion_menu.add_command(label="Pegar",command=paste_text)

barramenu.add_cascade(label="Ver",menu=estado_menu)
estado_menu.add_command(label="Barra de estado",command=lambda:barra_estado(contador))

barramenu.add_cascade(label="Ayuda",menu=ayuda_menu)
ayuda_menu.add_command(label="Acerca de",command=ayuda)

root.mainloop()
