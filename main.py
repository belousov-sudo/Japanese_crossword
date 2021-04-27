from tkinter import *


def start():  # отрисовка меню
    playButton.place(x=150, y=200)
    createButton.place(x=150, y=300)
    helpButton.place(x=150, y=400)
    exitButton.place(x=150, y=500)


def start_game():
    global FormGame, form_game_point
    form_game_point = 1
    FormGame = Toplevel(FormMenu)
    FormGame.title('Game')
    FormGame.geometry(f'{width}x{height}+250+250')
    FormGame.resizable(False, False)
    FormGame.bind("<Key>", key_processing)


def start_create():
    pass


def get_help():
    global FormHelp, form_help_point
    form_help_point = 1
    FormHelp = Toplevel(FormMenu)
    FormHelp.title('Help')
    FormHelp.geometry(f'{width}x{height}+250+250')
    FormHelp.resizable(False, False)
    FormHelp.bind("<Key>", key_processing)

    with open("help.txt", "r") as f:
        text = Text(FormHelp, width=50, height=35, bg='LightPink1', fg='blue', font=('Calibri', 12), wrap=WORD)
        text.place(x=0, y=0)
        s = f.read()
        text.insert(END, s)


def key_processing(event):
    global menu
    print(event.keycode)
    if menu:  # интересные проблемы с линуксом
        if event.keycode == 13 or event.keycode == 36:
            start_game()
        elif event.keycode == 67 or event.keycode == 54:
            start_create()
        elif event.keycode == 72 or event.keycode == 43:
            get_help()
        elif event.keycode == 27 or event.keycode == 9:
            if form_game_point:
                exit_game()
            elif form_help_point:
                exit_help()
            else:
                exit_menu()
    else:
        menu = True
        start()


def exit_menu():
    FormMenu.destroy()


def exit_game():
    global form_game_point
    FormGame.destroy()
    form_game_point = 0


def exit_help():
    global form_help_point
    FormHelp.destroy()
    form_help_point = 0


menu = False

form_game_point = 0
form_help_point = 0
form_create_point = 0

FormMenu = Tk()

FormMenu.title("Menu")
width, height = 400, 600
FormMenu.geometry(f'{width}x{height}+250+250')
FormMenu.resizable(False, False)

bg_im = PhotoImage(file="bg.png")
bg_wl = Label(FormMenu, image=bg_im)
bg_wl.place(x=0, y=0)

playButton = Button(FormMenu, text="Play[Enter]", font=('Calibri', 12), command=start_game)

createButton = Button(FormMenu, text="Create[C]", font=('Calibri', 12), command=start_create)

helpButton = Button(FormMenu, text="Help[H]", font=('Calibri', 12), command=get_help)

exitButton = Button(FormMenu, text="Exit[Esc]", font=('Calibri', 12), command=exit_menu)

FormMenu.bind("<Key>", key_processing)

FormMenu.mainloop()

'''
def clicked2(): #Функция создания и работы второго окна
    def clicked3(): #Удаление второго окна
        Form2.destroy()#удаление второго окна
    Form2=Toplevel(Form) #Создание второго окна
    Form2.title('Помощь')
    Form2.geometry('400x300+600+300')
    Button3 = Button(Form2, text="Bыход",command=clicked3) #Выход окна 2
    Button3.place(x=0, y=0)
    #Виджет Text второго окна
    text = Text(Form2,width=50, height=15,bg='LightPink1',fg='blue',font=('Calibri',12),wrap=WORD)
    text.place(x=00,y=25)
    help1=open('help.txt') #Загрузка и вывод в Text помощи из файла
    s=help1.read()
    text.insert(END,s)
    help1.close()

#Функция реализует игру
def v_next():
    global ans,stop,otvet,n
    if var.get()==otvet: #Если ответ правильный
        ans=ans+1 #Считаем количество вопросов
        var.set(4 ) #Ни одна кнопка Radiobutton не нажата
    else: #Если ответ неправильный
        Button1.configure(state='disabled')
        stop=False
        Label1.configure(text='Это неправильный ответ! \nПоищи ответ в Google')
    if ans==5: # Если
        Button1.configure(state='disabled')
        stop=False
        Label1.configure(text='Вот ты и миллионер! \nПоздравления от tkinter!')
#Продолжение v_next()
 #Задаем вопрос
    if stop==True:    
        n=n+6
        for i in range(n,n+6): #Перебираем элементы lines и удаляем символы перненоса строки
            st=lines[i]
            k=len(st)
            s=''
            for j in range(k-1):s=s+st[j]
            lines[i]=s
        for i in range(4):
            vop[i].configure(text=lines[n+i+1])#Выводим варианты ответов на Radiobuttons
        otvet=int(lines[5+n])-1#Запоминаем номер правильного ответа
        Label1.configure(text=lines[n])#Выводим вопрос в Label
def v_click():
    Form.destroy()
def v_show():#Делает кнопки и Label видимыми
    for i in range(4):
        vop[i].place(x=5,y=100+45*i)
        Label1.configure(text=lines[0])
        Button1.place(x=300,y=300)

# main program

Form.config(menu=mainmenu)
vopros=open('vopros1.txt','r')
lines=vopros.readlines()
n=0
for i in range(n,n+6): #Перебираем элементы lines и удаляем символы переноса строки
    st=lines[i]
    k=len(st)
    s=''
    for j in range(k-1): s=s+st[j]
    lines[i]=s

otvet=int(lines[5+n])-1
vopros.close()
#Создаем меню основного окна
playmenu = Menu(mainmenu, tearoff=0)
playmenu.add_command(label="New Game", command=v_show)
playmenu.add_command(label="Exit",command=v_click)
mainmenu.add_cascade(label="Игра", menu=playmenu)
mainmenu.add_command(label="Справка",command=clicked2)
var = IntVar()
var.set(4)
vop=[0]*4
ans=0
# Создаем список (массив) из 4  Radiobuttons
for i in range(4):
    vop[i] = Radiobutton(text=lines[n+i+1], variable=var, value=i,font=('Calibri',10))
    vop[i].place(x=5,y=100+45*i)
    vop[i].place_forget()#Прячем кнопки 
Button1 = Button(Form,text="Next",font=('Calibri',12),command=v_next)
stop=True
#Создаем Label
Label1=Label1 = Label(Form, text="Начнем игру?",bg="plum1",fg="blue", font=("Candara", 15),width=40)
Label1.place(x=100,y=20)
'''
