from tkinter import *

window = Tk()

window.title("Hello")

window.minsize(100, 100)
window.maxsize(300, 300)

window.geometry("300x300+500+300")

my_lable = Label(window, bg="red")

my_lable["text"] = "Hello!!!"

#my_lable.pack(side="left")
my_lable.place({'x': 50, 'y': 50, "width":50, "height": 50})

window.mainloop()
