from tkinter import *
from pygame import mixer


# Board with Steve Brule sounds
class SteveBrule:

    def __init__(self, window):
        frame = Frame(window)
        frame.pack()

        doris = mixer.Sound('Sounds\Steve Brule\Clinic\DorisSalahari.wav')
        child = mixer.Sound('Sounds\Steve Brule\Clinic\LotsHaveEm.wav')
        letsCheck = mixer.Sound('Sounds\Steve Brule\Clinic\LetsCheckItOut.wav')
        cheers = mixer.Sound('Sounds\Steve Brule\Clinic\Cheers.wav')
        gotcha = mixer.Sound('Sounds\Steve Brule\Clinic\IGotcha.wav')
        dingus = mixer.Sound('Sounds\Steve Brule\Clinic\Dingus.wav')
        gravy = mixer.Sound('Sounds\Steve Brule\Clinic\Gravy.wav')
        orgasm = mixer.Sound('Sounds\Steve Brule\Clinic\Orgasm.wav')
        dry = mixer.Sound('Sounds\Steve Brule\Clinic\Dry.wav')
        church = mixer.Sound('Sounds\Steve Brule\Church\Church.wav')
        lonely = mixer.Sound('Sounds\Steve Brule\Church\Lonely.wav')
        jengus = mixer.Sound('Sounds\Steve Brule\Church\CallMeJengus.wav')
        sneeze = mixer.Sound('Sounds\Steve Brule\Church\Sneeze.wav')
        # ----------------------------------------------------------------------

        self.title = Label(frame, text='Steve Brule Sounds')
        self.title.grid(row=0, columnspan=3)

        self.dorisBtn = Button(frame, text='Doris Pringle-Salahari-Brule', command=doris.play)
        self.childBtn = Button(frame, text='Lots of People Have Em', command=child.play)
        self.letsCheckBtn = Button(frame, text="Let's Check It Out", command=letsCheck.play)
        self.cheersBtn = Button(frame, text='Cheers', command=cheers.play)
        self.gotchaBtn = Button(frame, text='Oh, I Gotcha', command=gotcha.play)
        self.dingusBtn = Button(frame, text='Dingus', command=dingus.play)
        self.gravyBtn = Button(frame, text='Making Gravy', command=gravy.play)
        self.orgasmBtn = Button(frame, text='*Orgasm Noises*', command=orgasm.play)
        self.dryBtn = Button(frame, text="I'm Dry", command=dry.play)
        self.churchBtn = Button(frame, text='Church!', command=church.play)
        self.lonelyBtn = Button(frame, text="It's Lonely At The Top", command=lonely.play)
        self.jengusBtn = Button(frame, text='Praise Be Gord', command=jengus.play)
        self.sneezeBtn = Button(frame, text='*Sneeze*', command=sneeze.play)
        # ----------------------------------------------------------------------

        self.dorisBtn.grid(row=1, column=0)
        self.childBtn.grid(row=1, column=1)
        self.letsCheckBtn.grid(row=1, column=2)
        self.cheersBtn.grid(row=2, column=0)
        self.gotchaBtn.grid(row=2, column=1)
        self.dingusBtn.grid(row=2, column=2)
        self.gravyBtn.grid(row=3, column=0)
        self.orgasmBtn.grid(row=3, column=1)
        self.dryBtn.grid(row=3, column=2)
        self.churchBtn.grid(row=4, column=0)
        self.lonelyBtn.grid(row=4, column=1)
        self.jengusBtn.grid(row=4, column=2)
        self.sneezeBtn.grid(row=5, column=1)
        # ----------------------------------------------------------------------