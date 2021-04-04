from tkinter import *
root = Tk()
root.geometry('275x400')


from module import *
writeFileName(text = ' dream is gay')
print(readFileName())

rewriteFileName(text = ' dream is gay')
print(readFileName())



root.mainloop()