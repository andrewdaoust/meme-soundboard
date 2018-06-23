from tkinter import *
from pygame import mixer
from math import sqrt, floor


# Board with all sounds
class AllSounds:
    def __init__(self, window):
        self.frame = Frame(window)
        self.frame.pack()

        self.board_name = 'All Sounds'
        self.ext = 'wav'
        self.path_tos = ['Sounds\Eric Andre',
                         'Sounds\Tim and Eric',
                         'Sounds\Steve Brule',
                         'Sounds\Lenny Pepperbottom',
                         'Sounds\Misc']

        self.paths = []
        self.sounds = []
        self.buttons = []

        ea_filenames = ['yahBoobay',
                        'LRon',
                        'Xenu',
                        'DiploSong',
                        'SecondComing',
                        'PoopIntoWine',
                        'ImSaladMan',
                        'LettuceGuy',
                        'WorstShow',
                        'Osama',
                        'BirdUp',
                        'OhOh',
                        'Time4Ranch',
                        'Convention',
                        'BurningMan',
                        'EhYa',
                        'Legalize',
                        'PizzaBall',
                        'PizzaBallSong',
                        'Revolution',
                        'StephNuggz',
                        'Brotendo',
                        'RanchItUp',
                        'CherokeeChicks',
                        'BuzzMe',
                        'MellowMike',
                        'LittleSquirt',
                        'Daddy',
                        'ArtProject']

        te_filenames = ['GreatJob',
                        'BMFahrtz',
                        'ThePoopTube',
                        'ReallyWorks',
                        'BetterThanItUsedToo',
                        'SellPoopTube',
                        'Spagett1',
                        'Spagett2',
                        'Spagett3',
                        'Spagett4',
                        'GotYa',
                        'Armando',
                        'CigJuice',
                        'DiahRihaJones',
                        'DPants',
                        'FreeRealEstate']

        sb_filenames = ['DorisSalahari',
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

        nw_filenames = ['EveryoneKnows',
                        'Gun',
                        'Respect',
                        'HowNeatIsThat',
                        'ThatsPrettyNeat',
                        'CuzTheWayItIs',
                        'WhatABeaut',
                        'AnimalCalls',
                        'GDangIt',
                        'Theme']

        misc_filenames = ['Yee',
                          'Yee2',
                          'Chilis',
                          'Windows',
                          'WarioWhisper',
                          'WaluigiWhisper',
                          'PoopWa',
                          'CoolWas',
                          'FancyWa',
                          'AngryWa',
                          'LuigiWa',
                          'memes',
                          'JustOne1',
                          'JustOne2',
                          'JustOne3',
                          'JustOne4',
                          'JustOne5',
                          'JustOne6',
                          'FriendsDisappoint',
                          'WeirdQuestion',
                          'Touches',
                          'AsuhDude',
                          'DudeSuh',
                          'FuckBees',
                          'Bees',
                          'Fuck',
                          'KrustyKrab',
                          'WhatTheEff',
                          'SueYou',
                          'ShitOnOurBodies',
                          'FuckingDemon',
                          'Cheezits1',
                          'Cheezits2']

        all_filenames = ea_filenames + te_filenames + sb_filenames + nw_filenames + misc_filenames

        self.filenames = [ea_filenames, te_filenames, sb_filenames, nw_filenames, misc_filenames]
        for i in range(0, len(self.path_tos)):
            for name in self.filenames[i]:
                path = '{}\{}.{}'.format(self.path_tos[i], name, self.ext)
                self.paths.append(path)

        self.count = len(self.paths)
        self.nearest_square = int(floor(sqrt(self.count)))

        for path in self.paths:
            sound = mixer.Sound(path)
            self.sounds.append(sound)

        for i in range(0, self.count):
            text = all_filenames[i]
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
