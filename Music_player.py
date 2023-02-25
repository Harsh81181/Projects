from pygame import mixer
from tkinter import Button, Tk,Label
from tkinter.filedialog import askopenfile
from tkinter import messagebox as msg
mixer.init()
a, b = 3000, 3000
file = []


def asd():
    w = askopenfile(mode='r', filetypes=[('Audio', '*.mp3')])
    if w is not None:
        file.append(w.name)
        l1.grid(row=1,column=1)
        l2.grid(row=1,column=0)
        l3.grid(row=1,column=2)
        l4.grid(row=2,column=1)
    else:
        msg.showerror("Error", "Open correct file")


def ply():
    mixer.music.load(file[len(file)-1])
    mixer.music.play()


def cnl():
    l1.place(x=a, y=b)
    l2.place(x=a, y=b)
    l4.place(x=85, y=100)
    l3.place(x=a, y=b)
    file.remove(file[len(file)-1])
    ps()


def ps():
    mixer.music.pause()


top = Tk()

top.geometry("500x500+300+200")
lb=Label(top,text="<<<This program is written by Harsh Bhardwaj.>>>",bg="pink")
lb.grid(row=3,column=0,columnspan=3)
top.title("Music_Player")
l1 = Button(text="Play", activeforeground="black", activebackground="white",
            background="black", foreground="white", font=("Calibri", "15"), command=ply)
l2 = Button(text="Pause", activeforeground="black", activebackground="white",
            background="grey", foreground="white", font=("Calibri", "15"), command=ps)
l3 = Button(text="Cancel", activeforeground="black", activebackground="white",
            background="red", foreground="white", font=("Calibri", "15"), command=cnl)

top.title("Music player")
top.geometry("300x300")

l4 = Button(text="Open file", command=asd,
            background="white", font=("Calibri", "15"))
l4.grid(row=2,column=1)

top.mainloop()

#written by Harsh Bhardwaj
