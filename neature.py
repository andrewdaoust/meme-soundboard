from tkinter import *
from pygame import mixer
import math


class Neature:
    def __init__(self, window):
        frame = Frame(window)
        frame.pack()

        self.sounds = {'Everyone Knows': {'path': 'Sounds\Lenny Pepperbottom\EveryoneKnows.wav'},
                       'Gun': {'path': 'Sounds\Lenny Pepperbottom\Gun.wav'},
                       'Respect': {'path': 'Sounds\Lenny Pepperbottom\Respect.wav'},
                       'How Neat is That': {'path': 'Sounds\Lenny Pepperbottom\HowNeatIsThat.wav'},
                       'Thats Pretty Neat': {'path': 'Sounds\Lenny Pepperbottom\ThatsPrettyNeat.wav'},
                       'Cuz The Way It Is': {'path': 'Sounds\Lenny Pepperbottom\CuzTheWayItIs.wav'},
                       'What A Beaut': {'path': 'Sounds\Lenny Pepperbottom\WhatABeaut.wav'},
                       'Animal Calls': {'path': 'Sounds\Lenny Pepperbottom\AnimalCalls.wav'},
                       'G Dang It': {'path'  'Sounds\Lenny Pepperbottom\GDangIt.wav'},
                       'Neature Theme': {'path': 'Sounds\Lenny Pepperbottom\Theme.wav'}
                       }

        the_keys = list(self.sounds.keys())
        _count = len(self.sounds)
        _closest_square = round(math.sqrt(_count))

        # everyone = mixer.Sound('Sounds\Lenny Pepperbottom\EveryoneKnows.wav')
        # gun = mixer.Sound('Sounds\Lenny Pepperbottom\Gun.wav')
        # respect = mixer.Sound('Sounds\Lenny Pepperbottom\Respect.wav')
        # howNeat = mixer.Sound('Sounds\Lenny Pepperbottom\HowNeatIsThat.wav')
        # prettyNeat = mixer.Sound('Sounds\Lenny Pepperbottom\ThatsPrettyNeat.wav')
        # theWayItIs = mixer.Sound('Sounds\Lenny Pepperbottom\CuzTheWayItIs.wav')
        # beaut = mixer.Sound('Sounds\Lenny Pepperbottom\WhatABeaut.wav')
        # animalCalls = mixer.Sound('Sounds\Lenny Pepperbottom\AnimalCalls.wav')
        # gDang = mixer.Sound('Sounds\Lenny Pepperbottom\GDangIt.wav')
        # theme = mixer.Sound('Sounds\Lenny Pepperbottom\Theme.wav')
        # ----------------------------------------------------------------------

        self.title = Label(frame, text='Neature Walk Sounds')
        self.title.grid(row=0, columnspan=_closest_square)
        # ----------------------------------------------------------------------
        # TODO: Write functions to create Buttons and grid
        for key in self.sounds:
            self.sounds[key]['button'] = Button(frame, text=key, command=mixer.Sound(self.sounds[key]['path']).play)

        # self.everyoneBtn = Button(frame, text='So Everyone Knows', command=everyone.play)
        # self.gunBtn = Button(frame, text='Pack A Gun', command=gun.play)
        # self.respectBtn = Button(frame, text='Respect Your Distance', command=respect.play)
        # self.howNeatBtn = Button(frame, text='How Neat Is That', command=howNeat.play)
        # self.prettyNeatBtn = Button(frame, text="That's Pretty Neat", command=prettyNeat.play)
        # self.theWayItIsBtn = Button(frame, text='Cuz The Way It Is', command=theWayItIs.play)
        # self.beautBtn = Button(frame, text='What A Beaut', command=beaut.play)
        # self.animalCallsBtn = Button(frame, text='*Animal Calls*', command=animalCalls.play)
        # self.gDangBtn = Button(frame, text='G Dang It', command=gDang.play)
        # self.themeBtn = Button(frame, text='Neature Walk Theme', command=theme.play)
        # ----------------------------------------------------------------------

        # TODO: Build the grid of buttons
        for i in range(0, _count):
            the_row = 0
            if the_row % _closest_square == 0:
                the_row += 1

            self.sounds[self.sounds[the_keys[i]]['Button']].grid(row=the_row, column=the_row % _closest_square)

        # self.everyoneBtn.grid(row=1, column=0)
        # self.gunBtn.grid(row=1, column=1)
        # self.respectBtn.grid(row=1, column=2)
        # self.howNeatBtn.grid(row=2, column=0)
        # self.prettyNeatBtn.grid(row=2, column=1)
        # self.theWayItIsBtn.grid(row=2, column=2)
        # self.beautBtn.grid(row=3, column=0)
        # self.animalCallsBtn.grid(row=3, column=1)
        # self.gDangBtn.grid(row=3, column=2)
        # self.themeBtn.grid(row=4, column=1)
        # ----------------------------------------------------------------------
