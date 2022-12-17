from math import ceil
from tkinter import *
from tkinter import ttk

tamanho = 20000000


def displayTable():

    def firstPage():
        f = open("Data/rainbowTable.txt ", "r")
        Lines = f.readlines()
        aux = 1
        T.delete("1.0", "end")

        desiredPage = 1

        for line in Lines:
            if aux > desiredPage * 25:
                break
            passw = line.split("\t")[0].split("Pass:")[1]
            hashed = line.split("Hash:")[1].split("\n")[0]
            string = passw + "\t" + hashed + '\n'
            if aux > (desiredPage * 25) - 25:
                T.insert(END, string)
            aux = aux + 1

    def closeWindow():
        janela.destroy()

    def displayAll():
        T.delete("1.0", "end")
        getTable(tamanho)

    def accesPage():
        f = open("Data/rainbowTable.txt ", "r")
        Lines = f.readlines()
        aux = 1
        T.delete("1.0", "end")

        try:
            paginaDesejada = int(pageInput.get(1.0, "end-1c"))
        except:
            displayAll()

        for line in Lines:
            if aux > paginaDesejada * 25:
                break
            passw = line.split("\t")[0].split("Pass:")[1]
            hashed = line.split("Hash:")[1].split("\n")[0]
            string = passw + "\t" + hashed + '\n'
            if aux > (paginaDesejada * 25) - 25:
                T.insert(END, string)
            aux = aux + 1

    def getTable(size):
        f = open("Data/rainbowTable.txt ", "r")
        Lines = f.readlines()
        aux = 0
        for line in Lines:
            if aux == size:
                break
            passw = line.split("\t")[0].split("Pass:")[1]
            hashed = line.split("Hash:")[1].split("\n")[0]
            string = passw + "\t" + hashed + '\n'
            T.insert(END, string)
            aux = aux + 1

    rainbowY = 15
    rainbowInit = 225

    janela = Tk()
    janela.title("Rainbow Table")
    janela['background'] = '#ddeded'
    janela.geometry('700x600')
    janela.resizable(0, 0)

    lblR = Label(janela, text="R", font='Helvetica 18 bold', foreground="red")
    lblR.place(x=rainbowInit, y=rainbowY)

    lblA = Label(janela, text="A", font='Helvetica 18 bold', foreground="orange")
    lblA.place(x=rainbowInit + 20, y=rainbowY)

    lblI = Label(janela, text="I", font='Helvetica 18 bold', foreground="yellow")
    lblI.place(x=rainbowInit + 40, y=rainbowY)

    lblN = Label(janela, text="N", font='Helvetica 18 bold', foreground="green")
    lblN.place(x=rainbowInit + 50, y=rainbowY)

    lblB = Label(janela, text="B", font='Helvetica 18 bold', foreground="blue")
    lblB.place(x=rainbowInit + 70, y=rainbowY)

    lblO = Label(janela, text="O", font='Helvetica 18 bold', foreground="purple")
    lblO.place(x=rainbowInit + 90, y=rainbowY)

    lblW = Label(janela, text="W", font='Helvetica 18 bold', foreground="dark blue")
    lblW.place(x=rainbowInit + 110, y=rainbowY)

    lblT = Label(janela, text="T", font='Helvetica 18 bold', foreground="red")
    lblT.place(x=rainbowInit + 140, y=rainbowY)

    lblA1 = Label(janela, text="A", font='Helvetica 18 bold', foreground="orange")
    lblA1.place(x=rainbowInit + 160, y=rainbowY)

    lblB1 = Label(janela, text="B", font='Helvetica 18 bold', foreground="yellow")
    lblB1.place(x=rainbowInit + 180, y=rainbowY)

    lblL = Label(janela, text="L", font='Helvetica 18 bold', foreground="green")
    lblL.place(x=rainbowInit + 200, y=rainbowY)

    lblE = Label(janela, text="E", font='Helvetica 18 bold', foreground="blue")
    lblE.place(x=rainbowInit + 220, y=rainbowY)

    T = Text(janela, height=25, width=77)
    T.place(x=40, y=70)


    pageInput = Text(janela, height=1, width=5)
    pageInput.place(x=240, y=505)

    firstPage()

    paginas = Label(janela, text="De " + str(0) + " até " + str(ceil(tamanho / 25)))
    paginas.place(x=430, y=505)

    ou = Label(janela, text="OU")
    ou.place(x=335, y=535)

    setPage = Button(janela, text="DIGITE A PAGINA", command=accesPage)
    setPage.place(x=300, y=500)

    allPages = Button(janela, text="MOSTRAR TODAS PAGINAS", command=displayAll)
    allPages.place(x=270, y=565)

    backButton = Button(janela, text="VOLTAR", command=closeWindow)
    backButton.place(x=40, y=535)

    janela.mainloop()
