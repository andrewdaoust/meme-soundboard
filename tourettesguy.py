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

        self.filenames = ['Ah Shit',
                          'Bitch',
                          'Bob Saget 1',
                          'Bob Saget 2',
                          'Bob Saget 3',
                          'Combs',
                          'Ouch',
                          'Puerto Rican',
                          'Shit! Damnit!',
                          'Shit! Sorry!',
                          'Star Trek',
                          'Total',
                          'Tuba',
                          'What I Like',
                          'Youre a Dick',
                          'Youre a F@&#%t',
                          'Are You Shitting Me',
                          'Bacon And Eggs',
                          'Car Alarm',
                          'Chewbacca',
                          'Chicken Shit Bullshit',
                          'Colgate',
                          'Duhuhuh',
                          'Fish Sticks',
                          'Fuck Salt',
                          'Hell Hole',
                          'Holy Fuck',
                          'I Called Her A Bitch',
                          'I Love You',
                          'Mens Asses',
                          'Mickey Mouse',
                          'My Own Ass',
                          'Out Of My Way',
                          'Shes A Bitch',
                          'Stay At Home',
                          'Thats My Ass',
                          'Wait A Minute',
                          'You Cant Do Shit']

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
