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
        '''
        mainMenu = Menu(window)
        window.config(menu=mainMenu)

        submenu = Menu(mainMenu)
        mainMenu.add_cascade(label='Soundboards', menu=submenu)
        submenu.add_command(label='All', command=lambda: makeAll(frame, window))
        submenu.add_separator()
        submenu.add_command(label='Eric Andre', command=lambda: makeAndre(frame, window))
        submenu.add_command(label='Tim and Eric', command=lambda: makeTE(frame, window))
        submenu.add_command(label='Steve Brule', command=lambda: makeBrule(frame, window))
        submenu.add_command(label='Other', command=lambda: makeMisc(frame, window))
        '''

        frame = Frame(window)
        frame.pack()

        title = Label(frame, text='Choose a soundboard!')
        allBtn = Button(frame, text='All sounds', command=lambda: makeAll(frame, window))
        andreBtn = Button(frame, text='Eric Andre sounds', command=lambda: makeAndre(frame, window))
        teBtn = Button(frame, text='Tim and Eric sounds', command=lambda: makeTE(frame, window))
        bruleBtn = Button(frame, text='Steve Brule sounds', command=lambda: makeBrule(frame, window))
        neatureBtn = Button(frame, text='Neature Walk sounds', command=lambda: makeNeature(frame, window))
        miscBtn = Button(frame, text='Misc. sounds', command=lambda: makeMisc(frame, window))

        title.grid(row=0, columnspan=2)
        allBtn.grid(row=1, column=0)
        andreBtn.grid(row=1, column=1)
        teBtn.grid(row=2, column=0)
        bruleBtn.grid(row=2, column=1)
        neatureBtn.grid(row=3, column=0)
        miscBtn.grid(row=3, column=1)


def makeAll(frame, window):
    frame.destroy()
    b = all.AllSounds(window)


def makeAndre(frame, window):
    frame.destroy()
    b = ea.EricAndre(window)


def makeTE(frame, window):
    frame.destroy()
    b = te.TimAndEric(window)


def makeBrule(frame, window):
    frame.destroy()
    b = sb.SteveBrule(window)


def makeNeature(frame, window):
    frame.destroy()
    b = neat.Neature(window)


def makeMisc(frame, window):
    frame.destroy()
    b = misc.Misc(window)

mixer.init()
pane = Tk()

s = Soundboard(pane)

pane.mainloop()
