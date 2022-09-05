import tkinter as tk 
from tkinter import ttk


app=tk.Tk()
app.title("LOGIN")
app.geometry("300x150")
app.resizable(width=False, height=False)
app.configure(background="royalblue1")

def ingresar():
    
    if user.get()=="August" and pas.get()=="august124":
        app.title("Correcto")

    else:
        app.title("Incorrecto")


label1=ttk.Label(app,textvariable="", font=("Arial Bold", 12), text="Ingrese nombre de usuario:", background='royalblue1')
label1.pack()

user=tk.StringVar()
euser=ttk.Entry(app, width=30, textvariable=user)
euser.pack()

lpas=ttk.Label(app, textvariable="", font=("Arial Bold", 12), text="Password:", background='royalblue1')
lpas.pack()

pas=tk.StringVar()
epas=ttk.Entry(app, width=30, textvariable=pas, show="*")
epas.pack()

button1=ttk.Button(app, textvariable="", text="Entrar", command=ingresar)
button1.place(x=110, y=100)

    
app.mainloop()