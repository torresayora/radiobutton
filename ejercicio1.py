import tkinter 
from tkinter import ttk

def seleccionar():
    seleccion.config(text=servicio.get())

def reset():
    servicio.set(None)
    seleccion.config(text="")

root=tkinter.Tk()
root.config(bd=15)
servicio = tkinter.IntVar()

ttk.Label(root, text="Selecciona una opción\n",justify="center").pack()

ttk.Radiobutton(root, text= "Fotografía", variable = servicio, value=1, command=seleccionar).pack()
ttk.Radiobutton(root, text= "Diseño      ", variable = servicio, value= 2, command=seleccionar).pack()
ttk.Radiobutton(root, text= "Video       ", variable = servicio, value= 3, command=seleccionar).pack()

seleccion=ttk.Label(root)
seleccion.pack(pady=8)

ttk.Button(root, text="reset", command=reset).pack(pady=10)

root.mainloop()
