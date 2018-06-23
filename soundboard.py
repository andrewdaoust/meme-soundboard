from tkinter import *
from pygame import mixer
import allsounds as all
import ericandre as ea
import timanderic as te
import stevebrule as sb
import neature as neat
import miscsounds as misc


# This class runs the soundboard
class Soundboard:

    def __init__(self, window):
        self.window = window
        self.mainMenu = Menu(window)
        window.config(menu=self.mainMenu)

        submenu = Menu(self.mainMenu)
        self.mainMenu.add_cascade(label='Soundboards', menu=submenu)
        submenu.add_command(label='All', command=self.makeAll)
        submenu.add_separator()
        submenu.add_command(label='Eric Andre', command=self.makeAndre)
        submenu.add_command(label='Tim and Eric', command=self.makeTE)
        submenu.add_command(label='Steve Brule', command=self.makeBrule)
        submenu.add_command(label='Other', command=self.makeMisc)

        self.frame = Frame(window)
        self.frame.pack()

        title = Label(self.frame, text='Choose a soundboard!')
        allBtn = Button(self.frame, text='All sounds', command=self.makeAll)
        andreBtn = Button(self.frame, text='Eric Andre sounds', command=self.makeAndre)
        teBtn = Button(self.frame, text='Tim and Eric sounds', command=self.makeTE)
        bruleBtn = Button(self.frame, text='Steve Brule sounds', command=self.makeBrule)
        neatureBtn = Button(self.frame, text='Neature Walk sounds', command=self.makeNeature)
        miscBtn = Button(self.frame, text='Misc. sounds', command=self.makeMisc)

        title.grid(row=0, columnspan=2)
        allBtn.grid(row=1, column=0)
        andreBtn.grid(row=1, column=1)
        teBtn.grid(row=2, column=0)
        bruleBtn.grid(row=2, column=1)
        neatureBtn.grid(row=3, column=0)
        miscBtn.grid(row=3, column=1)

    def makeAll(self):
        self.frame.destroy()
        self.frame = Frame()
        self.frame.pack()
        all.AllSounds(self.frame)

    def makeAndre(self):
        self.frame.destroy()
        self.frame = Frame()
        self.frame.pack()
        ea.EricAndre(self.frame)

    def makeTE(self):
        self.frame.destroy()
        self.frame = Frame()
        self.frame.pack()
        te.TimAndEric(self.frame)

    def makeBrule(self):
        self.frame.destroy()
        self.frame = Frame()
        self.frame.pack()
        sb.SteveBrule(self.frame)

    def makeNeature(self):
        self.frame.destroy()
        self.frame = Frame()
        self.frame.pack()
        neat.Neature(self.frame)

    def makeMisc(self):
        self.frame.destroy()
        self.frame = Frame()
        self.frame.pack()
        misc.Misc(self.frame)


if __name__ == '__main__':
    mixer.init()
    pane = Tk()

    s = Soundboard(pane)

    pane.mainloop()
