from tkinter import *
from random import randint


window = Tk()
window.title("Ну дарова ")
window.geometry('800x600')
window["bg"] = "black"



def vxod():
    vivodChislaSummaNaKubikax.place(x=coordinatX7, y=coordinatY7)
    textSummaNaKubikax.place(x=coordinatX, y=coordinatY)
    WinLose.place(x = coordinatX2, y = coordinatY2)
    More.place(x = coordinatX3, y = coordinatY3, height=30, width=65,)
    Menshe.place(x = coordinatX4, y = coordinatY4, height=30, width=65,)
    Ravno.place(x = coordinatY4, y = coordinatY4, height=30, width=65,)
    BrosaiteKubiki.place(relx = coordinatX6, rely = coordinatY6, height=40, width=140,)
    textSpisok.place(x=coordinatX9, y=coordinatY9)
    Play.place_forget()


def vixod():
    vivodChislaSummaNaKubikax.place_forget()
    textSummaNaKubikax.place_forget()
    WinLose.place_forget()
    More.place_forget()
    Menshe.place_forget()
    Ravno.place_forget()
    BrosaiteKubiki.place_forget()
    textSpisok.place_forget()
    Play.place(relx = 0.45, rely = 0.45 )


def RandomNumber():
    global CymmaKubikov, Spisok, textSpisok, WinLose, Money

    Kubik2=randint(1, 6)
    Kubik1=randint(1, 6)
    CymmaKubikov = Kubik1+Kubik2
    CymmaKubikov2 = str(CymmaKubikov)
    vivodChislaSummaNaKubikax.configure(text=CymmaKubikov2)

    Spisok.append(CymmaKubikov)
    textSpisok.configure(text=Spisok)
    textSpisok.place(x=coordinatX9, y=coordinatY9)
    NumberOfElements = len(Spisok)

    NewSumma = NumberOfElements - 1
    OldSumma = NumberOfElements - 2
    #NewSummaTxt = Label(window, text=Spisok[NewSumma], font=("Arial", 12))
    #NewSummaTxt.place(x=200, y=200, width=120, )
    #NewSummaTxt.configure(text=CymmaKubikov)
    #OldSummaTxt = Label(window, text=Spisok[OldSumma], font=("Arial", 12))
    #OldSummaTxt.place(x=250, y=250, height=30)
    #OldSummaTxt.configure(text=Spisok[OldSumma])

    raznica= "0"
    if Spisok[NewSumma] < Spisok[OldSumma]:
        raznica = "<"
    elif Spisok[NewSumma] > Spisok[OldSumma]:
        raznica = ">"
    elif Spisok[NewSumma] == Spisok[OldSumma]:
        raznica = "="

    #textraznica = Label(window, text=raznica, font=("Arial", 12))
    #textraznica.place(x=200, y=70, width=270, )
    #textraznica.configure(text=raznica)

    #textZNAK = Label(window, text=ZNAK, font=("Arial", 12))
    #textZNAK.place(x=200, y=30, width=270, )
    #textZNAK.configure(text=ZNAK)

    if raznica != ZNAK:
        WinLose.configure(text="Вы проиграли, с чем мы вас поздравляем!")
        Money = Money-10
        yourMoney.configure(text=Money)

    elif raznica == ZNAK:
        WinLose.configure(text="Вы ВЫйграли, мы очень огорчены!")
        Money = Money+10
        yourMoney.configure(text=Money)



def Bolshe():
    global More, ZNAK, Ravno, Menshe
    More.configure(bg = "white")
    Ravno.configure(bg = "grey")
    Menshe.configure(bg = "grey")
    ZNAK = "<"
    return ZNAK


def Menshe():
    global More, ZNAK, Ravno, Menshe
    Menshe.configure(bg = "white")
    Ravno.configure(bg = "grey")
    More.configure(bg = "grey")
    ZNAK = ">"
    return ZNAK


def Ravno():
    global More, ZNAK, Ravno, Menshe
    Ravno.configure(bg = "white")
    More.configure(bg = "grey")
    Menshe.configure(bg = "grey")
    ZNAK = "="
    return ZNAK


# вычисляем первое случайное значение кубиков и их сумму
Kubik1=randint(1, 6)
Kubik2=randint(1, 6)
CymmaKubikov = Kubik1+Kubik2
CymmaKubikov2 = str(CymmaKubikov)

# выводим полученную сумму кубиков после текста и прячем ее
vivodChislaSummaNaKubikax =Label(window, text=CymmaKubikov2,font=(20), fg="grey")
coordinatY7=400
coordinatX7=505
vivodChislaSummaNaKubikax.place(x=coordinatX7, y=coordinatY7)
vivodChislaSummaNaKubikax.place_forget()


Spisok=[]
Spisok.append(CymmaKubikov)
textSpisok= Label(window, text=Spisok, font=(20), fg="grey")
coordinatX9=100
coordinatY9=100
textSpisok.place(x=coordinatX9, y=coordinatY9)
textSpisok.place_forget()

# выводим текст и прячем его
textSummaNaKubikax = Label(window, text="Сумма на гранях кубиков....",font=(20), fg="grey")
coordinatY=400
coordinatX=300
textSummaNaKubikax.place(x=coordinatX, y=coordinatY)
textSummaNaKubikax.place_forget()


WinLose = Label(window, text = "Начало!",)#при правильном значении на гранях кубиков будет писаться "ВЫЙГРЫШ" ри неправильном "ПРОЙГРЫШ"
coordinatY2=500
coordinatX2=300
WinLose.place(x = coordinatX2, y = coordinatY2)
WinLose.place_forget()


More = Button(window, text = "Больше!",font=(20), bg="#999",borderwidth=0,  command = Bolshe)
coordinatY3=450
coordinatX3=270
More.place(x = coordinatX3, y = coordinatY3, height=30, width=65,)
More.place_forget()


Menshe = Button(window, text = "Меньше!",font=(20), bg="#999",borderwidth=0, command= Menshe)
coordinatY4=450
coordinatX4=365
Menshe.place(x = coordinatX4, y = coordinatY4, height=30, width=65,)
Menshe.place_forget()


Ravno = Button(window, text = "Равно!",font=(20), bg="#999",borderwidth=0, command= Ravno)
coordinatY5=450
coordinatX5=430
Ravno.place(x = coordinatX4, y = coordinatY4, height=30, width=65,)
Ravno.place_forget()


# выводим кнопку "Бросить кубики." и прячем ее
BrosaiteKubiki = Button(window, text = "Бросить кубики.",font=("Arial",12), command = RandomNumber)
coordinatY6=0.8
coordinatX6=0.8
BrosaiteKubiki.place(relx = coordinatX6, rely = coordinatY6, height=40, width=140,)
BrosaiteKubiki.place_forget()





ZNAK = "."

Money = 100
yourMoney= Label(window, text=Money,font=(20))
yourMoney.place(x=110, y=80)




yourMoneyTxt = Label(window, text="Ваши деньги:",font=(20))
yourMoneyTxt.place(x=10, y=80)

#кнопка отвечающая за вход в игру
Play = Button(window, text = "Играть",font=("Arial",25),
            command = vxod,
            )
  
Play.place(relx = 0.45, rely = 0.4, height=50, width=120,)
  
#кнопка отвечающая за вход в "меню"
Exit = Button(window, text = "Выход!",
            command = vixod,
            )
Exit.place(x = 2, y = 2)









  
window.mainloop()

