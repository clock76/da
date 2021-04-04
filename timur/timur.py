from tkinter import*


root=Tk()
root.title("портал в другой мир")
text=Label(text="мир слов")
text.pack()
text_root=Text(width=100, height=30)
text_root.pack()
text2=Label(text="вечен")
text2.pack()
btn=Button(text="играть")
btn.pack()


root.mainloop()

