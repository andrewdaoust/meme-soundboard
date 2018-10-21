from tkinter import *
from pygame import mixer
import allsounds as all
import ericandre as ea
import timanderic as te
import stevebrule as sb
import neature as neat
import tourettesguy as tg
import miscsounds as misc


# This class runs the soundboard
class Soundboard(object):
    def __init__(self, window):
        self.window = window
        self.mainMenu = Menu(window)
        window.config(menu=self.mainMenu)

        submenu = Menu(self.mainMenu)
        self.mainMenu.add_cascade(label='Soundboards', menu=submenu)
        submenu.add_command(label='All', command=self.make_all)
        submenu.add_separator()
        submenu.add_command(label='Eric Andre', command=self.make_andre)
        submenu.add_command(label='Tim and Eric', command=self.make_te)
        submenu.add_command(label='Steve Brule', command=self.make_brule)
        submenu.add_command(label='Neature Walk', command=self.make_neature)
        submenu.add_command(label='Tourettes Guy', command=self.make_tourettes)
        submenu.add_command(label='Misc. sounds', command=self.make_misc)

        self.frame = Frame(window)
        self.frame.pack()

        title = Label(self.frame, text='Choose a soundboard!')
        all_btn = Button(self.frame, text='All sounds', command=self.make_all)
        andre_btn = Button(self.frame, text='Eric Andre sounds', command=self.make_andre)
        te_btn = Button(self.frame, text='Tim and Eric sounds', command=self.make_te)
        brule_btn = Button(self.frame, text='Steve Brule sounds', command=self.make_brule)
        neature_btn = Button(self.frame, text='Neature Walk sounds', command=self.make_neature)
        tg_btn = Button(self.frame, text='Tourettes Guy sounds', command=self.make_tourettes)
        misc_btn = Button(self.frame, text='Misc. sounds', command=self.make_misc)

        title.grid(row=0, columnspan=3)
        all_btn.grid(row=1, column=0)
        andre_btn.grid(row=1, column=1)
        te_btn.grid(row=1, column=2)
        brule_btn.grid(row=2, column=0)
        neature_btn.grid(row=2, column=1)
        tg_btn.grid(row=2, column=2)
        misc_btn.grid(row=3, column=1)

    def make_all(self):
        self.frame.destroy()
        self.frame = Frame()
        self.frame.pack()
        all.AllSounds(self.frame)

    def make_andre(self):
        self.frame.destroy()
        self.frame = Frame()
        self.frame.pack()
        ea.EricAndre(self.frame)

    def make_te(self):
        self.frame.destroy()
        self.frame = Frame()
        self.frame.pack()
        te.TimAndEric(self.frame)

    def make_brule(self):
        self.frame.destroy()
        self.frame = Frame()
        self.frame.pack()
        sb.SteveBrule(self.frame)

    def make_neature(self):
        self.frame.destroy()
        self.frame = Frame()
        self.frame.pack()
        neat.Neature(self.frame)

    def make_tourettes(self):
        self.frame.destroy()
        self.frame = Frame()
        self.frame.pack()
        tg.TourettesGuy(self.frame)

    def make_misc(self):
        self.frame.destroy()
        self.frame = Frame()
        self.frame.pack()
        misc.Misc(self.frame)


if __name__ == '__main__':
    mixer.init()
    pane = Tk()

    s = Soundboard(pane)

    pane.mainloop()
