from tkinter import *
from pygame import mixer
from math import sqrt, floor


# Board with Generic sounds
class TourettesGuy(object):
    def __init__(self, frame):
        self.frame = frame

        self.board_name = 'Tourettes Guy Sounds'
        self.path_to = 'Sounds\Tourettes Guy'
        self.ext = 'wav'

        self.filenames = ['File1',
                          'File2',
                          'File3',
                          'File4',
                          'File5',
                          'File6',
                          'File7',
                          'File8',
                          'File9',
                          'File10',
                          'File11',
                          'File12',
                          'File13',
                          'File14',
                          'File15',
                          'File16',
                          'File17',
                          'File18',
                          'File19',
                          'File20',
                          'File21',
                          'File22',
                          'File23',
                          'File24',
                          'File25',
                          'File26',
                          'File27',
                          'File28',
                          'File29',
                          'File30',
                          'File31',
                          'File32',
                          'File33']

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
