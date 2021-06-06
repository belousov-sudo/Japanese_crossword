from tkinter import *
import pickle
import os


def start():
    global form_game_point, choice_buttons, form_create_point, width, height
    FormMenu.title("Menu")
    width, height = 400, 600
    FormMenu.geometry(f'{width}x{height}+250+250')
    FormMenu.resizable(False, False)
    clear()
    bg_wl.place(x=0, y=0)

    playButton.place(x=150, y=200)
    createButton.place(x=150, y=300)
    helpButton.place(x=150, y=400)
    exitButton.place(x=150, y=500)


def start_game():  # меню выбора уровня
    global form_game_point, choice_buttons, width, height
    form_game_point = 1
    clear()

    files = []
    for root, dirs, file_names in os.walk("levels"):
        files += file_names
    choice_buttons = [0 for i in range(len(files))]
    for i in range(len(choice_buttons)):
        choice_buttons[i] = Button(FormMenu, bg='white', width=9, height=2, text=files[i].split('.')[0],
                                   command=lambda x=files[i]: play(x))
        choice_buttons[i].place(x=i % 5 * 100, y=i//5 * 50 + 100)
    
    FormMenu.title("Play")
    width, height = 500, 200 + len(files) // 5 * 50
    FormMenu.geometry(f'{width}x{height}+250+250')

    text_play.place(x=0, y=0)
    
    FormMenu.resizable(False, False)


def start_creating():
    global form_create_point, name_entry, size_x_entry, size_y_entry, width, height
    form_create_point = 1
    FormMenu.title("Create")
    width, height = 400, 400
    FormMenu.geometry(f'{width}x{height}+250+250')
    clear()
    bg_wl_2.place(x=0, y=0)

    text_create.place(x=80, y=25)
    text_create.configure(fg='White')
    text_create.configure(text='Введите название вашего \n'
                               'кроссворда и его размеры')
    text_x.place(x=100, y=125)
    text_y.place(x=100, y=150)
    text_name.place(x=100, y=200)
    
    size_x_entry.delete(0, 'end')
    size_y_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    
    size_x_entry.place(x=175, y=125)
    size_y_entry.place(x=175, y=150)
    name_entry.place(x=175, y=200)
    
    FormMenu.resizable(False, False)


def continue_creating():
    global cord_x, cord_y, x, crossword_name, board, form_create_point, form_create_2_point, name_entry, width, height
    global create_canvas
    try:
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
            crossword_name = name_entry.get()
            FormMenu.title("Create")
            cord_x = int(size_x_entry.get())
            cord_y = int(size_y_entry.get())
            width, height = cord_x * 30 + 150, cord_y * 30
            FormMenu.geometry(f'{width}x{height}+250+250')
            clear()
            form_create_point = 0
            form_create_2_point = 1
            FormMenu.resizable(False, False)
            
            create_canvas.configure(width=width, height=height)
            create_canvas.place(x=0, y=0)
            '''
            x = [[0 for i in range(cord_x)]
                 for j in range(cord_y)]
            '''
            board = [['white' for i in range(cord_x)]
                     for j in range(cord_y)]
            for i in range(len(board[0])):
                for j in range(len(board)):
                    if board[j][i] == 'empty':
                        create_canvas.create_rectangle(i * ((width - 150) / cord_x), j * height / cord_y, (i + 1) * ((width - 150) / cord_x),
                                                       (j + 1) * (height / cord_y), outline="black", fill="white")
                        create_canvas.create_line(i * ((width - 150) / cord_x), j * height / cord_y, (i + 1) * ((width - 150) / cord_x),
                                                  (j + 1) * (height / cord_y), width=3)
                        create_canvas.create_line(i * ((width - 150) / cord_x), (j + 1) * (height / cord_y), (i + 1) * ((width - 150) / cord_x),
                                                  j * height / cord_y, width=3)
                    else:
                        create_canvas.create_rectangle(i * ((width - 150) / cord_x), j * height / cord_y, (i + 1) * ((width - 150) / cord_x),
                                                       (j + 1) * (height / cord_y), outline="black", fill=board[j][i])

            if paint_color == 'black':
                create_canvas.create_rectangle(width - 100, 50, width - 50, 100, outline="yellow", fill="black")
                create_canvas.create_rectangle(width - 100, 150, width - 50, 200, outline="black", fill="white")
                create_canvas.create_rectangle(width - 100, 250, width - 50, 300, outline="black", fill="white")
                create_canvas.create_line(width - 100, 250, width - 50, 300, width=3)
                create_canvas.create_line(width - 100, 300, width - 50, 250, width=3)
            elif paint_color == 'white':
                create_canvas.create_rectangle(width - 100, 50, width - 50, 100, outline="black", fill="black")
                create_canvas.create_rectangle(width - 100, 150, width - 50, 200, outline="yellow", fill="white")
                create_canvas.create_rectangle(width - 100, 250, width - 50, 300, outline="black", fill="white")
                create_canvas.create_line(width - 100, 250, width - 50, 300, width=3)
                create_canvas.create_line(width - 100, 300, width - 50, 250, width=3)
            elif paint_color == 'empty':
                create_canvas.create_rectangle(width - 100, 50, width - 50, 100, outline="black", fill="black")
                create_canvas.create_rectangle(width - 100, 150, width - 50, 200, outline="black", fill="white")
                create_canvas.create_rectangle(width - 100, 250, width - 50, 300, outline="yellow", fill="white")
                create_canvas.create_line(width - 100, 250, width - 50, 300, width=3)
                create_canvas.create_line(width - 100, 300, width - 50, 250, width=3)
            '''
            blackButton.place(x=2, y=height - 50)
            whiteButton.place(x=52, y=height - 50)
            confirmButton.place(x=width - 127, y=height - 50)
            
            for j in range(cord_x):
                for i in range(cord_y):
                    x[i][j] = Button(FormMenu, bg='white', width=5, height=2,
                                     command=lambda x=i, y=j: paint(x, y))
                    x[i][j].place(x=j * 50, y=i * 50)
            '''
    except ValueError:
        text_create.configure(fg='Red')
        text_create.configure(text='Введены значения\n'
                                   'недопустимого формата.')


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


def play(name):  # игра
    global picture_canvas, f_board, play_board, play_buttons, vertical_ints, horizontal_ints, playblackButton, playclearButton
    with open(f'levels/{name}', 'rb') as f:
        f_board = pickle.load(f)
    play_board = [['white' for i in range(len(f_board[0]))] for j in range(len(f_board))]
    FormMenu.title("Play")
    width, height = len(play_board[0]) * 50 + 250, len(play_board) * 50 + 150
    FormMenu.geometry(f'{width}x{height}+250+250')
    FormMenu.resizable(False, False)
    clear()

    picture_canvas = Canvas(FormMenu, width=140, height=140, bg="gray")
    picture_canvas.place(x=0, y=0)

    play_buttons = [[0 for i in range(len(play_board[0]))] for j in range(len(play_board))]
    for i in range(len(play_board)):
        for j in range(len(play_board[0])):
            play_buttons[i][j] = Button(FormMenu, bg=play_board[i][j], width=5, height=2, command=lambda x = i, y = j: play_paint(x, y))
            play_buttons[i][j].place(x=j * 50 + 150, y=i * 50 + 150)

    vertical_ints = [0 for i in range(len(f_board))]
    tmp = []
    cnt = 0
    for i in range(len(f_board)):
        for j in range(len(f_board[0])):
            if (f_board[i][j - 1] != 'white' and f_board[i][j] != 'white' and f_board[i][j - 1] == f_board[i][j]) or (
                    cnt == 0 and f_board[i][j] != 'white'):
                cnt += 1
            elif f_board[i][j] == 'white' and f_board[i][j] != f_board[i][j - 1] and j != 0:
                tmp.append(cnt)
                cnt = 0
        if len(tmp) == 0 or cnt != 0:
            tmp.append(cnt)
        cnt = 0
        tmp = ' '.join([str(i) for i in tmp])
        vertical_ints[i] = Label(FormMenu, text=tmp, bg="White", fg="Black",
                          font=("Candara", 15), width=11, height=2)  # виджеты в меню выбора игры
        vertical_ints[i].place(x=0, y=150 + i * 50)
        tmp = []

    horizontal_ints = [0 for i in range(len(f_board[0]))]
    tmp = []
    cnt = 0
    for i in range(len(f_board[0])):
        for j in range(len(f_board)):
            if (f_board[j - 1][i] != 'white' and f_board[j][i] != 'white' and f_board[j - 1][i] ==
                f_board[j][i]) or (
                    cnt == 0 and f_board[j][i] != 'white'):
                cnt += 1
            elif f_board[j][i] == 'white' and f_board[j][i] != f_board[j - 1][i] and j != 0:
                tmp.append(cnt)
                cnt = 0
        if len(tmp) == 0 or cnt != 0:
            tmp.append(cnt)
        cnt = 0
        tmp = ' '.join([str(i) + '\n' for i in tmp])
        horizontal_ints[i] = Label(FormMenu, text=tmp, bg="White", fg="Black",
                                 font=("Candara", 15), width=2, height=4)
        horizontal_ints[i].place(x=150 + i * 50, y=0)
        tmp = []
    playblackButton.place(x=width-50, y=0)
    playclearButton.place(x=width-50, y=50)


def key_processing(event):
    global menu, crossword_name, board
    if menu:  # интересные проблемы с линуксом
        if event.keycode == 13 or event.keycode == 36:  # enter
            if form_create_point:  # если в меню режима редактирования
                continue_creating()
            elif form_create_2_point:
                save_crossword()
            elif form_game_point:  # если в меню игры
                pass
            else:
                start_game()
        elif event.keycode == 67 or event.keycode == 54:  # C
            if form_create_point:  # если в меню режима редактирования
                pass
            else:
                start_creating()
        elif event.keycode == 72 or event.keycode == 43:  # H
            if form_game_point:
                paint_picture()
            elif form_create_point:
                pass
            else:
                get_help()
        elif event.keycode == 27 or event.keycode == 9:  # esc
            if form_game_point:
                exit_game()
            elif form_help_point:
                exit_help()
            elif form_create_point or form_create_2_point:
                exit_create()
            else:
                exit_menu()
        elif event.keycode == 82 or event.keycode == 109:  # минус
            if form_game_point:
                pass
            elif form_create_2_point:
                refresh_create(-100 // len(board), -100 // len(board[0]))
        elif event.keycode == 86 or event.keycode == 107:  # плюс
            if form_game_point:
                pass
            elif form_create_2_point:
                refresh_create(100 // len(board), 100 // len(board[0]))
    else:
        menu = True
        start()


def m_pressed(event):
    global menu, width, height, paint_color, board
    if not menu:
        menu = True
        start()
    if form_game_point:
        pass
    elif form_create_2_point:
        if width - 150 <= event.x <= width - 50 and 50 <= event.y <= 100:
            paint_color = 'black'
            refresh_create(0, 0)
        elif width - 150 <= event.x <= width - 50 and 150 <= event.y <= 200:
            paint_color = 'white'
            refresh_create(0, 0)
        elif width - 150 <= event.x <= width - 50 and 250 <= event.y <= 300:
            paint_color = 'empty'
            refresh_create(0, 0)
        elif event.x < width - 150:
            board[min(len(board) - 1, event.y // (height // len(board)))][min(len(board[0]) - 1, event.x // ((width - 150) // len(board[0])))] = paint_color
            refresh_create(0, 0)


def m2_pressed(event):
    global line_painting
    if line_painting == 1:
        line_painting = 0
    else:
        line_painting = 1


def m_motion(event):
    global menu, width, height, paint_color, board, line_painting
    if line_painting == 1:
        if form_game_point:
            pass
        elif form_create_2_point:
            if event.x < width - 150:
                board[min(len(board) - 1, event.y // (height // len(board)))][min(len(board[0]) - 1, event.x // ((width - 150) // len(board[0])))] = paint_color
                refresh_create(0, 0)


def clear():
    global form_game_point, choice_buttons, playButton, createButton, helpButton, exitButton, form_create_point, cord_x, cord_y, x, crossword_name, board, name_entry
    global create_canvas, line_painting
    '''
    for j in range(cord_x):
        for i in range(cord_y):
            x[i][j].place(x=-500, y=-500)
    cord_x = 0
    cord_y = 0
    x = [[0 for i in range(cord_x)]
         for j in range(cord_y)]
    '''
    create_canvas.configure(width=0, height=0)
    create_canvas.place(x=0, y=0)

    line_painting = 0
    board = 0
    playButton.place(x=-500, y=-500)
    createButton.place(x=-500, y=-500)
    helpButton.place(x=-500, y=-500)
    exitButton.place(x=-500, y=-500)

    bg_wl.place(x=-500, y=-500)
    bg_wl_2.place(x=-500, y=-500)

    text_create.place(x=-500, y=-500)
    name_entry.place(x=-500, y=-500)
    size_x_entry.place(x=-500, y=-500)
    size_y_entry.place(x=-500, y=-500)
    text_x.place(x=-500, y=-500)
    text_y.place(x=-500, y=-500)
    text_name.place(x=-500, y=-500)

    text_play.place(x=-500, y=-500)
    '''
    confirmButton.place(x=-500, y=-500)
    blackButton.place(x=-500, y=-500)
    whiteButton.place(x=-500, y=-500)
    '''
    playButton.place(x=-500, y=-500)
    createButton.place(x=-500, y=-500)
    helpButton.place(x=-500, y=-500)
    exitButton.place(x=-500, y=-500)

    for i in range(len(play_buttons)):
        for j in range(len(play_buttons[0])):
            play_buttons[i][j].place(x=-500, y=-500)

    for i in range(len(choice_buttons)):
        choice_buttons[i].place(x=-500, y=-500)

    # на кнопках_____________
    for i in range(len(play_buttons)):
        for j in range(len(play_buttons[0])):
            play_buttons[i][j].place(x=-500, y=-500)

    for i in range(len(vertical_ints)):
        vertical_ints[i].place(x=-500, y=-500)
    for i in range(len(horizontal_ints)):
        horizontal_ints[i].place(x=-500, y=-500)
    # _______________________
    picture_canvas.place(x=-500, y=-500)


def change_color(color):
    global paint_color
    paint_color = color


def refresh_play(x, y):
    pass


def refresh_create(x, y):
    global width, height, board, paint_color
    width = max(0, width + x)
    height = max(0, height + y)
    FormMenu.geometry(f'{width}x{height}+250+250')
    create_canvas.delete("all")
    create_canvas.configure(width=width, height=height)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'empty':
                create_canvas.create_rectangle(j * ((width - 150) / cord_x), i * height / cord_y, (j + 1) * ((width - 150) / cord_x),
                                              (i + 1) * (height / cord_y), outline="black", fill="white")
                create_canvas.create_line(j * ((width - 150) / cord_x), i * height / cord_y, (j + 1) * ((width - 150) / cord_x),
                                          (i + 1) * (height / cord_y), width=3)
                create_canvas.create_line(j * ((width - 150) / cord_x), (i + 1) * (height / cord_y), (j + 1) * ((width - 150) / cord_x),
                                          i * height / cord_y, width=3)
            else:
                create_canvas.create_rectangle(j * ((width - 150) / cord_x), i * height / cord_y, (j + 1) * ((width - 150) / cord_x),
                                               (i + 1) * (height / cord_y), outline="black", fill=board[i][j])

    if paint_color == 'black':
        create_canvas.create_rectangle(width - 100, 50, width - 50, 100, outline="yellow", fill="black")
        create_canvas.create_rectangle(width - 100, 150, width - 50, 200, outline="black", fill="white")
        create_canvas.create_rectangle(width - 100, 250, width - 50, 300, outline="black", fill="white")
        create_canvas.create_line(width - 100, 250, width - 50, 300, width=3)
        create_canvas.create_line(width - 100, 300, width - 50, 250, width=3)
    elif paint_color == 'white':
        create_canvas.create_rectangle(width - 100, 50, width - 50, 100, outline="black", fill="black")
        create_canvas.create_rectangle(width - 100, 150, width - 50, 200, outline="yellow", fill="white")
        create_canvas.create_rectangle(width - 100, 250, width - 50, 300, outline="black", fill="white")
        create_canvas.create_line(width - 100, 250, width - 50, 300, width=3)
        create_canvas.create_line(width - 100, 300, width - 50, 250, width=3)
    elif paint_color == 'empty':
        create_canvas.create_rectangle(width - 100, 50, width - 50, 100, outline="black", fill="black")
        create_canvas.create_rectangle(width - 100, 150, width - 50, 200, outline="black", fill="white")
        create_canvas.create_rectangle(width - 100, 250, width - 50, 300, outline="yellow", fill="white")
        create_canvas.create_line(width - 100, 250, width - 50, 300, width=3)
        create_canvas.create_line(width - 100, 300, width - 50, 250, width=3)


def paint(a, b):
    global x, paint_color
    x[a][b].configure(bg=paint_color)
    board[a][b] = paint_color


def play_paint(a, b):
    global play_board, paint_color, play_buttons
    play_buttons[a][b].configure(bg=paint_color)
    play_board[a][b] = paint_color
    check_win()


def paint_picture():
    global picture, picture_canvas
    if picture:
        picture_canvas.delete("all")
        picture = 0
    else:
        picture = 1
        x = max(len(f_board[0]), len(f_board))
        for i in range(len(f_board[0])):
            for j in range(len(f_board)):
                picture_canvas.create_rectangle(i * (140 / x), j * (140 / x), (i + 1) * (140 / x), (j + 1) * (140 / x), outline="#fb0", fill=f_board[j][i])


def save_crossword():
    global crossword_name, board
    with open(f'levels/{crossword_name}.pickle', 'wb') as f:
        pickle.dump(board, f)


def exit_menu():
    FormMenu.destroy()


def exit_game():
    global form_game_point
    form_game_point = 0
    clear()
    start()


def exit_help():
    global form_help_point
    FormHelp.destroy()
    form_help_point = 0


def exit_create():
    global form_create_point, form_create_2_point
    form_create_point = 0
    form_create_2_point = 0
    clear()
    start()


def check_win():
    global f_board, play_board
    if f_board == play_board:
        print(1)
    else:
        print(0)


menu = False

form_game_point = 0
form_help_point = 0
form_create_point = 0
form_create_2_point = 0

line_painting = 0

picture = 0

paint_color = 'black'

crossword_name = ''

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

# menu_______________________________________
playButton = Button(FormMenu, text="Play[Enter]", font=('Calibri', 12),
                    command=start_game)  # виджеты в меню
createButton = Button(FormMenu, text="Create[C]", font=('Calibri', 12),
                      command=start_creating)
helpButton = Button(FormMenu, text="Help[H]", font=('Calibri', 12),
                    command=get_help)
exitButton = Button(FormMenu, text="Exit[Esc]", font=('Calibri', 12),
                    command=exit_menu)
# ___________________________________________

# create_____________________________________
text_create = Label(FormMenu, text="", bg="Black", fg="White",
                    font=("Candara", 15), width=0, height=3)
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
# ___________________________________________

# create_2___________________________________
create_canvas = Canvas(FormMenu, width=140, height=140, bg="gray")
create_canvas.place(x=-500, y=-500)
'''

confirmButton = Button(FormMenu, text="Confirm[Enter]", height=2,
                       font=('Calibri', 12), command=save_crossword)
blackButton = Button(FormMenu, bg='black', width=5, height=2,
                     command=lambda x='black': change_color(x))
whiteButton = Button(FormMenu, bg='white', width=5, height=2,
                     command=lambda x='white': change_color(x))
'''
# ___________________________________________

# game_______________________________________
text_play = Label(FormMenu, text="Выберите уровень:", bg="Black", fg="White",
                  font=("Candara", 15), width=0, height=3)  # виджеты в меню выбора игры
text_play.place(x=-500, y=-500)
playclearButton = Button(FormMenu, bg='white', width=5, height=2,
                         command=lambda x='white': change_color(x))
playblackButton = Button(FormMenu, bg='black', width=5, height=2,
                         command=lambda x='black': change_color(x))
picture_canvas = Canvas(FormMenu, width=140, height=140, bg="gray")
picture_canvas.place(x=-500, y=-500)

f_board = []
play_board = []
cord_x = 0
cord_y = 0
x = [[0 for i in range(cord_x)] for j in range(cord_y)]
board = 0
for i in range(cord_x):
    for j in range(cord_y):
        x[i][j] = Button(FormMenu, bg='white', width=2, height=2, command=exit_menu)
        x[i][j].place(x=i * 50, y=j * 50)
choice_buttons = []
play_buttons = []
vertical_ints = []
horizontal_ints = []
# ___________________________________________

FormMenu.bind("<Key>", key_processing)
FormMenu.bind("<Button-1>", m_pressed)
FormMenu.bind("<Button-3>", m2_pressed)
FormMenu.bind("<Motion>", m_motion)
FormMenu.mainloop()
