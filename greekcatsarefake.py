from tkinter import *

def click():
    print("Master freed dobby! How can dobby ever repay?")




window = Tk()

slider = Scale(window,
               from_= 100,
               to=0,
               resolution=5
               )
slider.pack()
window.mainloop()