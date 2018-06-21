from tkinter import *
from pygame import mixer


# Board with Time and Eric sounds
class TimAndEric:

    def __init__(self, window):
        frame = Frame(window)
        frame.pack()

        greatJob = mixer.Sound('Sounds\Tim and Eric\PoopTube\GreatJob.wav')
        bm = mixer.Sound('Sounds\Tim and Eric\PoopTube\BMFahrtz.wav')
        pTube = mixer.Sound('Sounds\Tim and Eric\PoopTube\ThePoopTube.wav')
        really = mixer.Sound('Sounds\Tim and Eric\PoopTube\ReallyWorks.wav')
        better = mixer.Sound('Sounds\Tim and Eric\PoopTube\BetterThanItUsedToo.wav')
        sell = mixer.Sound('Sounds\Tim and Eric\PoopTube\SellPoopTube.wav')
        spagett1 = mixer.Sound('Sounds\Tim and Eric\Spagett\Spagett1.wav')
        spagett2 = mixer.Sound('Sounds\Tim and Eric\Spagett\Spagett2.wav')
        gotYa = mixer.Sound('Sounds\Tim and Eric\Spagett\GotYa.wav')
        armando = mixer.Sound('Sounds\Tim and Eric\Spagett\Armando.wav')
        spagett3 = mixer.Sound('Sounds\Tim and Eric\Spagett\Spagett3.wav')
        cig = mixer.Sound('Sounds\Tim and Eric\Spagett2\CigJuice.wav')
        spagett4 = mixer.Sound('Sounds\Tim and Eric\Spagett2\Spagett4.wav')
        diah = mixer.Sound('Sounds\Tim and Eric\D Pants\DiahRihaJones.wav')
        dpants = mixer.Sound('Sounds\Tim and Eric\D Pants\DPants.wav')
        free = mixer.Sound('Sounds\Tim and Eric\FreeRealEstate.wav')
        # ----------------------------------------------------------------------

        self.title = Label(frame, text='Tim and Eric Sounds')
        self.title.grid(row=0, columnspan=4)

        self.greatJobBtn = Button(frame, text='Great Job!', command=greatJob.play)
        self.bmBtn = Button(frame, text='B.M. Fahrtz', command=bm.play)
        self.pTubeBtn = Button(frame, text='Poop Tube', command=pTube.play)
        self.reallyBtn = Button(frame, text='It Really Works!', command=really.play)
        self.betterBtn = Button(frame, text='It Smells Better...', command=better.play)
        self.sellBtn = Button(frame, text='My Dad Said...', command=sell.play)
        self.spagett1Btn = Button(frame, text='Spagett 1', command=spagett1.play)
        self.spagett2Btn = Button(frame, text='Spagett 2', command=spagett2.play)
        self.gotYaBtn = Button(frame, text='Got Ya', command=gotYa.play)
        self.armandoBtn = Button(frame, text='Armando', command=armando.play)
        self.spagett3Btn = Button(frame, text='Spagett 3', command=spagett3.play)
        self.cigBtn = Button(frame, text='Good News', command=cig.play)
        self.spagett4Btn = Button(frame, text='Spagett 4', command=spagett4.play)
        self.diahBtn = Button(frame, text='Diah Riha-Jones', command=diah.play)
        self.dpantsBtn = Button(frame, text='With D-Pants', command=dpants.play)
        self.freeBtn = Button(frame, text='Free Real Estate', command=free.play)
        # ----------------------------------------------------------------------

        self.greatJobBtn.grid(row=1, column=0)
        self.bmBtn.grid(row=1, column=1)
        self.pTubeBtn.grid(row=1, column=2)
        self.reallyBtn.grid(row=1, column=3)
        self.betterBtn.grid(row=2, column=0)
        self.sellBtn.grid(row=2, column=1)
        self.spagett1Btn.grid(row=2, column=2)
        self.spagett2Btn.grid(row=2, column=3)
        self.gotYaBtn.grid(row=3, column=0)
        self.armandoBtn.grid(row=3, column=1)
        self.spagett3Btn.grid(row=3, column=2)
        self.cigBtn.grid(row=3, column=3)
        self.spagett4Btn.grid(row=4, column=0)
        self.diahBtn.grid(row=4, column=1)
        self.dpantsBtn.grid(row=4, column=2)
        self.freeBtn.grid(row=4, column=3)
        # ----------------------------------------------------------------------