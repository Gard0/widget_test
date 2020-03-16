from tkinter import *

window = Tk()

window.title("Hello")

window.minsize(100, 100)
window.maxsize(300, 300)

window.geometry("300x300+500+300")

my_lable = Label(window, bg="red")

my_lable["text"] = "0"

button = Button()

button["text"] = "click"

button.place({'x': 0, 'y': 0, "width": 100, "height": 30})

my_lable.place({'x': 125, 'y': 125, "width": 50, "height": 50})


def click():
    current_number = int(my_lable["text"])
    my_lable["text"] = str(current_number + 1)


button["command"] = click
window.mainloop()
