from tkinter import *
from tkinter import ttk

from main import findHashInFile, hashWord


def addView():

    def close_window():
        janela.destroy()


    def printInput():
        T.config(state=NORMAL)
        T.delete("1.0", "end")
        inp = inputtxt.get(1.0, "end-1c")
        result = hashWord(inp)
        T.insert(END, result)
        T.config(state=DISABLED)



    rainbowY = 15
    rainbowInit = 165
    hashLabelX = 180


    janela = Tk()
    janela.title("Rainbow Table")
    janela['background'] = '#ddeded'
    janela.geometry('600x200')
    janela.resizable(0, 0)

    lblR = Label(janela, text="R", font='Helvetica 18 bold',foreground="red")
    lblR.place(x=rainbowInit, y=rainbowY)

    lblA = Label(janela, text="A", font='Helvetica 18 bold',foreground="orange")
    lblA.place(x=rainbowInit + 20, y=rainbowY)

    lblI = Label(janela, text="I", font='Helvetica 18 bold',foreground="yellow")
    lblI.place(x=rainbowInit + 40, y=rainbowY)

    lblN = Label(janela, text="N", font='Helvetica 18 bold',foreground="green")
    lblN.place(x=rainbowInit + 50, y=rainbowY)

    lblB = Label(janela, text="B", font='Helvetica 18 bold',foreground="blue")
    lblB.place(x=rainbowInit + 70, y=rainbowY)

    lblO = Label(janela, text="O", font='Helvetica 18 bold',foreground="purple")
    lblO.place(x=rainbowInit + 90, y=rainbowY)

    lblW = Label(janela, text="W", font='Helvetica 18 bold',foreground="dark blue")
    lblW.place(x=rainbowInit + 110, y=rainbowY)

    lblT = Label(janela, text="T", font='Helvetica 18 bold',foreground="red")
    lblT.place(x=rainbowInit + 140, y=rainbowY)

    lblA1 = Label(janela, text="A", font='Helvetica 18 bold',foreground="orange")
    lblA1.place(x=rainbowInit + 160, y=rainbowY)

    lblB1 = Label(janela, text="B", font='Helvetica 18 bold',foreground="yellow")
    lblB1.place(x=rainbowInit + 180, y=rainbowY)

    lblL = Label(janela, text="L", font='Helvetica 18 bold',foreground="green")
    lblL.place(x=rainbowInit + 200, y=rainbowY)

    lblE = Label(janela, text="E", font='Helvetica 18 bold',foreground="blue")
    lblE.place(x=rainbowInit + 220, y=rainbowY)

    inputtxt = Text(janela,height=1,width=20)
    inputtxt.place(x=hashLabelX + 40, y=70)

    palavraLabel = Label(janela,text="PALAVRA:")
    palavraLabel.place(x=hashLabelX-20, y=70)


    printButton = Button(janela,text="ENCRIPTAR",command=printInput)
    printButton.place(x=hashLabelX + 220, y=68)

    backButton = Button(janela,text="VOLTAR",command=close_window)
    backButton.place(x=30, y=10)

    resultLabel = Label(janela,text="RESULTADO:")
    resultLabel.place(x=65, y=130)


    T = Text(janela, height=1, width=60)
    T.place(x=65, y=150)




    janela.mainloop()

