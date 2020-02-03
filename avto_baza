from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

dict_baza = {}

def zagruzka(): # загрузка из файла и создание словаря
    with open ("baza_avto.txt") as f:
        for line in f:
            list_sl = line.rstrip ().split ('\t')
            if len (list_sl) > 1:
                dict_baza[list_sl[0]] = list_sl[1]
            else:
                dict_baza[list_sl[0]] = list_sl[0]

def vigruzka():
    with open ("baza_avto.txt", "w") as f:
        for item in dict_baza:
            text = item + '\t' + dict_baza[item] + '\n'
            f.write (text)

def poisk():
    input_text = txt_poisk.get ()
    if len (input_text) == 0:
        return
    input_text = input_text.upper ().strip ()
    if input_text in dict_baza:
        lbl_out.configure (text="Есть: " + str (dict_baza[input_text]))
        lbl_poisk.configure (bg='green')
        lbl_liniya.configure (bg='green')
        lbl.configure(bg='green')
        window.configure (bg='green')

    else:
        lbl_out.configure (text="Нет")
        lbl_poisk.configure (bg='red')
        lbl_liniya.configure (bg='red')
        lbl.configure (bg='red')
        window.configure (bg='red')

def add_baza():
    list_sl = txt_add_nomber.get ()
    inf1 = txt_add_info.get ()
    txt_add_nomber.delete (0, len (list_sl)) # стирание введенных символов
    txt_add_info.delete (0, len (inf1))
    if len (list_sl) == 0:
        return
    list_sl = list_sl.upper ().strip ()
    txt_vivid = 'Добавлена машина: ' + list_sl + '\n'
    txt.insert (INSERT, txt_vivid)
    if inf1 == '':
        inf1 = '-без описания-'
    dict_baza[list_sl] = inf1
    messagebox.showinfo ('Добавлена новая запись в базу: ', list_sl)
    vigruzka ()

def dell_baza():
    input_text = txt_poisk.get ()
    if len (input_text) == 0:
        return
    input_text = input_text.upper ().strip ()
    if input_text in dict_baza:
        a = dict_baza.pop (input_text)
        lbl_out.configure (text="Удалено!" + str (a))
        lbl_poisk.configure (bg='yellow')
        lbl_liniya.configure (bg='yellow')
        lbl.configure (bg='yellow')
        txt_vivid = 'Удален номер машины:' + input_text + '\n'
        txt.insert (INSERT, txt_vivid)
        vigruzka ()

    else:
        lbl_out.configure (text="Нет записи")
        lbl_poisk.configure (bg='red')
        lbl_liniya.configure (bg='red')

zagruzka ()
window = Tk ()
window.title ('База автомобилей')
window.geometry ('700x700+100+100')  # ширина=600, высота=600, x=100, y=100
window.configure(bg='')

# кнопка с указанием родительского виджета и несколькими аргументами
lbl_poisk = Label (text='Поиск авто в базе ', font='Arial 16')
lbl_poisk.grid (column=1, row=1)

lbl_out = Label (text="Ведите номер авто", font='Arial 16')
lbl_out.grid (column=1, row=2)

txt_poisk = Entry (window, width=15, font='Arial 20')
txt_poisk.grid (column=1, row=3)

btn_poisk = Button (text="Искать!", command=poisk)
btn_poisk.grid (column=1, row=4)

btn_dell = Button (text="Удалить!", command=dell_baza)
btn_dell.grid (column=2, row=3)

lbl_liniya = Label (text = "_______________________________", font='Arial 16')
lbl_liniya.grid(column = 1, row = 5)

lbl = Label (text="Добавление авто в базу автомобилей!", font='Arial 16')
lbl.grid (column=1, row=6)

txt_add_nomber = Entry (window, width=15, font='Arial 18')
txt_add_nomber.grid (column=1, row=7)

lbl_add_info = Label (text="Описание:", font='Arial 16')
lbl_add_info.grid (column=2, row=7)

txt_add_info = Entry (window, width=15, font='Arial 16')
txt_add_info.grid (column=3, row=7)

btn = Button (text="Добавить!", command=add_baza)
btn.grid (column=1, row=8)

txt = scrolledtext.ScrolledText (window, width=40, height=25)
txt.grid (column=1, row=9)

window.mainloop ()
