import re
import tkinter
from tkinter import messagebox
from tkinter import END

dict_baza = {}


def collor_window(collor):
    lbl_poisk.configure(bg = collor)
    # lbl_liniya.configure(bg = collor)
    # lbl.configure(bg = collor)
    lbl_out.configure(bg = collor)
    lbl_poisk.configure(bg = collor)
    # window.configure(bg = collor)
    window.configure(bg = 'white')
    frame1.configure(bg = collor)


def zagruzka():  # загрузка из файла и создание словаря
    try:
        with open("baza_avto.txt") as f:
            for line in f:
                list_sl = line.rstrip().split('\t')
                if len(list_sl) > 1:
                    dict_baza[list_sl[0]] = list_sl[1]
                else:
                    dict_baza[list_sl[0]] = list_sl[0]
    except FileNotFoundError:
        my_file = open("baza_avto.txt", "w")
        my_file.write('TEST\ttest1')
        my_file.close()
        zagruzka()


def vigruzka():
    with open("baza_avto.txt", "w") as f:
        for item in dict_baza:
            text = item + '\t' + dict_baza[item] + '\n'
            f.write(text)


def poisk(event=0):
    input_text = txt_poisk.get()
    if len(input_text) == 0:
        collor_window('grey')
        lbl_out.configure(text = "Введите номер")
        text_out.delete('1.0', END)
        return
    text_out.delete('1.0', END)
    input_text_upper = input_text.upper().strip()
    if input_text_upper in dict_baza:
        text_out.delete('1.0', END)
        lbl_out.configure(text = "Есть: ")
        text_out.insert(1.0, str(dict_baza[input_text_upper] + '\n'))
        collor_window('green')
    else:
        lbl_out.configure(text = "------Нет информации----")
        collor_window('red')
        pattern = '(.*' + input_text + '.*)|(.*' + input_text.upper() + '.*)'
        for key, value in dict_baza.items():
            po = str(key + value)
            if re.search(pattern, po):
                collor_window('blue')
                lbl_out.configure(text = "__Есть похожее__ ")
                txt_vivod = str(key + ' ' + value + '\n')
                text_out.insert(1.0, txt_vivod)


def add_baza():
    list_sl = txt_add_nomber.get()
    inf1 = txt_add_info.get()
    txt_add_nomber.delete(0, len(list_sl))  # стирание введенных символов
    txt_add_info.delete(0, len(inf1))
    if len(list_sl) == 0:
        return
    list_sl = list_sl.upper().strip()

    if inf1 == '':
        inf1 = '-без описания-'
    dict_baza[list_sl] = inf1
    messagebox.showinfo('Добавлена новая запись в базу: ', list_sl)
    vigruzka()


def dell_baza():
    input_text = txt_poisk.get()
    if len(input_text) == 0:
        return
    text_out.delete('1.0', END)
    input_text = input_text.upper().strip()
    if input_text in dict_baza:
        answer = messagebox.askyesno(title = "Внимание!", message = "Удалить авто из базы автомобилей?")
        if answer:
            a = dict_baza.pop(input_text)
            lbl_out.configure(text = "Удалено!" + str(a))

            vigruzka()

    else:
        lbl_out.configure(text = "Нет записи")
        collor_window('red')


zagruzka()
window = tkinter.Tk()
window.title('База автомобилей')
window.geometry('300x380+100+100')  # ширина=600, высота=600, x=100, y=100
window.configure(bg = '')

frame1 = tkinter.Frame(window, bg = 'green', bd = 8)
frame2 = tkinter.Frame(window, bg = 'grey', bd = 5)
# кнопка с указанием родительского виджета и несколькими аргументами
frame1.grid(column = 1, row = 1)
frame2.grid(column = 1, row = 2)
lbl_poisk = tkinter.Label(frame1, text = 'Поиск авто в базе ', font = 'Arial 16')
lbl_poisk.grid(column = 1, row = 1, columnspan = 3, rowspan = 1)

lbl_out = tkinter.Label(frame1, text = "Ведите номер авто", font = 'Arial 16')
lbl_out.grid(column = 1, row = 2, columnspan = 2)

txt_poisk = tkinter.Entry(frame1, width = 19, font = 'Arial 20')
txt_poisk.bind('<Return>', poisk)
txt_poisk.grid(column = 1, row = 3, columnspan = 2)

btn_poisk = tkinter.Button(frame1, text = "Искать!", command = poisk)
btn_poisk.grid(column = 1, row = 4)

btn_dell_1 = tkinter.Button(frame1, text = "Удалить авто из базы!", command = dell_baza)
btn_dell_1.grid(column = 2, row = 4)

text_out = tkinter.Text(frame1, height = 5, width = 22, font = 'Arial 14')
text_out.grid(column = 1, row = 5, columnspan = 3)

lbl = tkinter.Label(frame2, text = "Добавление авто!", font = 'Arial 16')
lbl.grid(column = 1, row = 6, columnspan = 2)

txt_add_nomber = tkinter.Entry(frame2, width = 22, font = 'Arial 18')
txt_add_nomber.grid(column = 1, row = 7, columnspan = 2)

lbl_add_info = tkinter.Label(frame2, text = "Описание:", font = 'Arial 16')
lbl_add_info.grid(column = 1, row = 9)

txt_add_info = tkinter.Entry(frame2, width = 15, font = 'Arial 16')
txt_add_info.grid(column = 2, row = 9)

btn = tkinter.Button(frame2, text = "Добавить!", command = add_baza)
btn.grid(column = 1, row = 10, columnspan = 2)

window.mainloop()
