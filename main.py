from tkinter import *


def start():
    FormMenu.title("Menu")
    width, height = 400, 600
    FormMenu.geometry(f'{width}x{height}+250+250')
    FormMenu.resizable(False, False)

    bg_wl.place(x=0, y=0)
    bg_wl_2.place(x=-500, y=-500)

    text_create.place(x=-500, y=-500)
    name_entry.place(x=-500, y=-500)
    size_x_entry.place(x=-500, y=-500)
    size_y_entry.place(x=-500, y=-500)
    text_x.place(x=-500, y=-500)
    text_y.place(x=-500, y=-500)
    text_name.place(x=-500, y=-500)

    text_play.place(x=-500, y=-500)
    
    playButton.place(x=150, y=200)
    createButton.place(x=150, y=300)
    helpButton.place(x=150, y=400)
    exitButton.place(x=150, y=500)


def start_game():
    global form_game_point
    form_game_point = 1
    FormMenu.title("Play")
    width, height = 400, 400
    FormMenu.geometry(f'{width}x{height}+250+250')

    bg_wl_2.place(x=0, y=0)  # заставка создания
    
    playButton.place(x=-500, y=-500)
    createButton.place(x=-500, y=-500)
    helpButton.place(x=-500, y=-500)
    exitButton.place(x=-500, y=-500)

    text_play.place(x=125, y=0)
    
    FormMenu.resizable(False, False)


def start_create():
    global form_create_point
    form_create_point = 1
    FormMenu.title("Create")
    width, height = 400, 400
    FormMenu.geometry(f'{width}x{height}+250+250')

    bg_wl_2.place(x=0, y=0)
    
    playButton.place(x=-500, y=-500)
    createButton.place(x=-500, y=-500)
    helpButton.place(x=-500, y=-500)
    exitButton.place(x=-500, y=-500)

    text_create.place(x=80, y=25)
    text_create.configure(fg='White')
    text_create.configure(text='Введите название вашего \n'
                               'кроссворда и его размеры')
    text_x.place(x=100, y=125)
    text_y.place(x=100, y=150)
    text_name.place(x=100, y=200)
    size_x_entry.place(x=175, y=125)
    size_y_entry.place(x=175, y=150)
    name_entry.place(x=175, y=200)
    
    FormMenu.resizable(False, False)


def get_help():
    global FormHelp, form_help_point
    form_help_point = 1
    FormHelp = Toplevel(FormMenu)
    FormHelp.title('Help')
    FormHelp.geometry(f'{width}x{height}+250+250')
    FormHelp.resizable(False, False)
    FormHelp.bind("<Key>", key_processing)

    with open("help.txt", "r") as f:
        text = Text(FormHelp, width=50, height=32, bg='LightPink1', fg='blue',
                    font=('Calibri', 12), wrap=WORD)
        text.place(x=0, y=0)
        s = f.read()
        text.insert(END, s)


def continue_creating():
    if size_x_entry.get() == '':
        text_create.configure(fg='Red')
        text_create.configure(text='Введите количество столбцов.')
    elif size_y_entry.get() == '':
        text_create.configure(fg='Red')
        text_create.configure(text='Введите количество строк.')
    elif name_entry.get() == '':
        text_create.configure(fg='Red')
        text_create.configure(text='Введите название.')
    elif int(size_x_entry.get()) > 20:
        text_create.configure(fg='Red')
        text_create.configure(text='Недопустимый размер. \n'
                                   'столбцов не может быть больше 20.')
    elif int(size_y_entry.get()) > 20:
        text_create.configure(fg='Red')
        text_create.configure(text='Недопустимый размер. \n'
                                   'строк не может быть больше 20.')
    elif int(size_x_entry.get()) % 5 != 0:
        text_create.configure(fg='Red')
        text_create.configure(text='Недопустимый размер. \n'
                                   'Столбцы не кратны 5.')
    elif int(size_y_entry.get()) % 5 != 0:
        text_create.configure(fg='Red')
        text_create.configure(text='Недопустимый размер. \n'
                                   'Строки не кратны 5.')
    else:
        pass


def key_processing(event):
    global menu
    if menu:  # интересные проблемы с линуксом
        if event.keycode == 13 or event.keycode == 36:
            if form_create_point:  # если в меню режима редактирования
                continue_creating()
            elif form_game_point:  # если в меню игры
                pass
            else:
                start_game()
        elif event.keycode == 67 or event.keycode == 54:
            if form_create_point:  # если в меню режима редактирования
                pass
            else:
                start_create()
        elif event.keycode == 72 or event.keycode == 43:
            if form_create_point:  # если в меню режима редактирования
                pass
            else:
                get_help()
        elif event.keycode == 27 or event.keycode == 9:
            if form_game_point:
                exit_game()
            elif form_help_point:
                exit_help()
            elif form_create_point:
                exit_create()
            else:
                exit_menu()
    else:
        menu = True
        start()


def exit_menu():
    FormMenu.destroy()


def exit_game():
    global form_game_point
    form_game_point = 0
    start()


def exit_help():
    global form_help_point
    FormHelp.destroy()
    form_help_point = 0


def exit_create():
    global form_create_point
    form_create_point = 0
    start()


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

bg_im_2 = PhotoImage(file="bg_2.png")
bg_wl_2 = Label(FormMenu, image=bg_im_2)

playButton = Button(FormMenu, text="Play[Enter]", font=('Calibri', 12),
                    command=start_game)  # виджеты в меню
createButton = Button(FormMenu, text="Create[C]", font=('Calibri', 12),
                      command=start_create)
helpButton = Button(FormMenu, text="Help[H]", font=('Calibri', 12),
                    command=get_help)
exitButton = Button(FormMenu, text="Exit[Esc]", font=('Calibri', 12),
                    command=exit_menu)

text_create = Label(FormMenu, text="", bg="Black", fg="White",
                    font=("Candara", 15), width=0, height=3)  # виджеты в меню создания
text_create.place(x=-500, y=-500)
text_x = Label(FormMenu, text="Столбцов:", bg="Black", fg="White",
               font=("Candara", 9), width=0, height=1)
text_x.place(x=-500, y=-500)
text_y = Label(FormMenu, text="Строк:", bg="Black", fg="White",
               font=("Candara", 9), width=0, height=1)
text_y.place(x=-500, y=-500)
text_name = Label(FormMenu, text="Название:", bg="Black", fg="White",
                  font=("Candara", 9), width=0, height=1)
text_name.place(x=-500, y=-500)
size_x_entry = Entry(FormMenu, width=5)
size_x_entry.place(x=-500, y=-500)
size_y_entry = Entry(FormMenu, width=5)
size_y_entry.place(x=-500, y=-500)
name_entry = Entry(FormMenu, width=15)
name_entry.place(x=-500, y=-500)

text_play = Label(FormMenu, text="Выберите уровень:", bg="Black", fg="White",
                  font=("Candara", 15), width=0, height=3)  # виджеты в меню выбора игры
text_play.place(x=-500, y=-500)

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
