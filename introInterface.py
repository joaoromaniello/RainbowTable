from tkinter import *

from addEntryView import addView
from interface import openHashInterface
from tablesView import displayTable


def intro():

    janela = Tk()
    janela.resizable(0, 0)
    janela['background'] = '#ddeded'
    janela.title("Rainbow Table")
    janela.geometry('600x200')
    photo = PhotoImage(file="rainbow.png")
    janela.iconphoto(False, photo)

    lblR = Label(janela, text="MENU DE OPÇÕES", font='Helvetica 18 bold', foreground="blue",background='#ddeded')
    lblR.place(x=200, y=15)

    hashSearch = Button(janela, text="PROCURAR HASH", command= openHashInterface)
    hashSearch.place(x=400, y=100)

    tableVisualizer = Button(janela, text="VISUALIZAR TABELA",command=displayTable)
    tableVisualizer.place(x=250, y=100)

    addHash = Button(janela, text="GERAR HASH ",command=addView)
    addHash.place(x=130, y=100)

    janela.mainloop()


intro()
