from tkinter import *

# Creating window

root = Tk()
root.title('Резюме')
root.geometry('700x500')

icon = PhotoImage(file = "./icons/briefcase.png")
root.iconphoto(True, icon)

label = Label(text='Hello world!')
label.pack()

root.mainloop()

