#importar as bibliotecas necessarias
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

class splash:
    def __init__(self):
        self.splashmainw = Tk()
        self.splashmainw.title("PONTO DE VENDAS EM PYTHON RGV:")
        width = 1000
        height = 680

        self.splashmainw.iconbitmap(r'C:\Sistema_vendas_tkinter_copia\images\icon.ico')

        self.splashmainw.config(bg="darkorange")
        tela_largura = self.splashmainw.winfo_screenwidth()
        tela_altura = self.splashmainw.winfo_screenheight()
        x = (tela_largura / 2 ) - (width /2 )
        y = (tela_altura / 2 ) - (height /2 )
        self.splashmainw.geometry("%dx%d+%d+%d" % (width,height,x,y))
        self.splashmainw.resizable(0,0)
        path ="images/intro.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        