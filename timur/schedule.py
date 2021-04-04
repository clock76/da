# из модуля tkinter
from tkinter import *


#создаем окно root
root = Tk()
#задаем размер окна
root.geometry('400x350')

#обьявляем фрейм text_frame, с родителями root
text_frame = Frame(root, borderwidth=5, relief=GROOVE)
#размещаем фрейм используя относительные размеры
text_frame.place(x=5, y=5, relwidth=0.8, relheight=0.97)

#обьявляем текстовое поле с родителем
text_space = Text(text_frame,)
text_space.pack()
#размещаем текстовое поле
text_space.insert(0.0, 'Some text...')

#вставляем текст в текстовое поле
buttons_frame =Frame(root, borderwidth=5, relief=GROOVE)
buttons_frame.place(relx=0.72, y=5, relwidth=0.27, relheight=0.98)



btn_monday = Button(buttons_frame, text='monday', command=lambda: show_text(1) )
btn_monday.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.02)

btn_tuesday = Button(buttons_frame, text='tuesday', command=lambda: show_text(2) )
btn_tuesday.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.14)

btn_wednesday = Button(buttons_frame, text='wednesday', command=lambda: show_text(3) )
btn_wednesday.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.26)

def show_text(day):
    text_space.delete(0.0, END)

    if day == 1:
        text_space.insert(0.0, 'Monday schedule:')
    if day == 2:
        text_space.insert(0.0, 'Tuesday schedule:')




#запускаем главный цикл для окна (без него работать нэбудет!)
root.mainloop()


