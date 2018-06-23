from tkinter import *
from pygame import mixer
from math import sqrt, floor


# Board with Steve Brule sounds
class SteveBrule(object):
    def __init__(self, window):
        self.frame = Frame(window)
        self.frame.pack()

        self.board_name = 'Steve Brule Sounds'
        self.path_to = 'Sounds\Steve Brule'
        self.ext = 'wav'

        self.filenames = ['DorisSalahari',
                          'LotsHaveEm',
                          'LetsCheckItOut',
                          'Cheers',
                          'IGotcha',
                          'Dingus',
                          'Gravy',
                          'Orgasm',
                          'Dry',
                          'Church',
                          'Lonely',
                          'CallMeJengus',
                          'Sneeze']

        self.count = len(self.filenames)
        self.nearest_square = int(floor(sqrt(self.count)))
        self.paths = []
        self.sounds = []
        self.buttons = []

        for name in self.filenames:
            path = '{}\{}.{}'.format(self.path_to, name, self.ext)
            self.paths.append(path)

        for path in self.paths:
            sound = mixer.Sound(path)
            self.sounds.append(sound)

        for i in range(0, self.count):
            text = self.filenames[i]
            btn = Button(self.frame, text=text, command=self.sounds[i].play)
            self.buttons.append(btn)

        self.make_grid()

    def make_grid(self):
        title = Label(self.frame, text=self.board_name)
        title.grid(row=0, columnspan=self.nearest_square)
        gridded = 0
        row = 1
        column = 0
        while gridded < self.count:
            self.buttons[gridded].grid(row=row, column=column)
            gridded += 1
            if gridded % self.nearest_square == 0:
                column = 0
                row += 1
            else:
                column += 1
