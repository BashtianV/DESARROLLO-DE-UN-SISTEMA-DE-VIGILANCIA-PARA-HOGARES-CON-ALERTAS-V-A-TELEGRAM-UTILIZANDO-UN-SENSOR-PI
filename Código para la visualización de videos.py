from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import imutils

def seleccionar_video():
    global capture
    if capture is not None:
        label_Video.image = ""
        capture.release()
        capture = None
    video_path = filedialog.askopenfilename(filetypes = [("formar", ".mp4")])
    if len(video_path) > 0:
        label_InfoVideoPath.configure(text=video_path)
        capture = cv2.VideoCapture(video_path)
        visualizar()
    else:
        label_InfoVideoPath.configure(text="Seleccione un video")

def visualizar():
    global capture
    if capture is not None:
        ret, frame = capture.read()
        if ret == True:
            frame = imutils.resize(frame, width=640)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            ima = Image.fromarray(frame)
            imag = ImageTk.PhotoImage(image=ima)
            label_Video.configure(image=imag)
            label_Video.image = imag
            label_Video.after(20, visualizar)
        else:
            label_InfoVideoPath.configure(text="Seleccione un video")
            label_Video.image = ""
            capture.release()

capture = None
Ventana = Tk()
Ventana.title("SISTEMA DE SEGURIDAD")
Ventana.configure(background="royalblue1")

boton_Visualizar = Button(Ventana, text="Selecionar video", background="royalblue3", command=seleccionar_video)
boton_Visualizar.grid(column=0, row=0, padx=5, pady=5, columnspan=2)

label_Info1 = Label(Ventana, text="Video de entrada:", background="royalblue1")
label_Info1.grid(column=0, row=1)

label_InfoVideoPath = Label(Ventana, background="royalblue1", text="Seleccione un video")
label_InfoVideoPath.grid(column=1, row=1)

label_Video = Label(Ventana, background="royalblue3")
label_Video.grid(column=0, row=2, columnspan=2)

Ventana.mainloop()