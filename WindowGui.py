from tkinter import *
window = Tk()
#widgets = GUI elements : buttons , lables, images
#window = serves as a container to hold or contain these widgets
window.title("Hello world")
window.config(background="black")
icon = PhotoImage(file='naruto.jpg')
window.iconphoto(True, icon)
window.mainloop()
