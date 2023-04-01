from manim import *

class crypto0Main(Scene):
    def construct(self):
        youText = Tex("You", color=BLUE).shift(1.8*DOWN, 5*LEFT)
        youPerson = makePerson(color=BLUE).shift(5*LEFT)
        self.play(Create(youPerson), Write(youText))

        self.wait(1)

        eveText = Tex("Eve", color=GREEN).shift(1.8*DOWN)
        evePerson = makePerson(color=GREEN)
        eveHatTriangle = Polygon([-.3,1.8,0], [.3,1.8,0], [0,2.5,0], color = GREEN)
        stripe1 = Line([-.2,2,0], [.2,2,0], color = GREEN)
        stripe2 = Line([-.13,2.2,0], [.13,2.2,0], color = GREEN)
        eveHat = VGroup(eveHatTriangle, stripe1, stripe2)
        eveList = [evePerson, eveText, eveHat]
        self.play(Create(evePerson), Write(eveText))

        self.wait(1)

        self.play(Transform(evePerson, changeMood(evePerson, "happy", GREEN)), Create(eveHat))

        self.wait(1)

        recipients = []
        for i in range(-1,2):
            recipients.append(scaleGroup(makePerson(color=RED).shift(i*1.5*UP, 5*RIGHT), .4))
        for p in recipients:
            self.play(Create(p), run_time=.3)
        
        self.wait()

        self.play(*[Transform(x, x.copy().shift(10*DOWN)) for x in eveList])
        # self.play(Transform(evePerson, evePerson.copy().shift(10*DOWN)),
        #           Transform(eveHat, eveHat.copy().shift(10*DOWN)))
        
        inviteBox = Rectangle(height=2, width=1.5)
        inviteText1 = Tex("Come to the").scale(.4)
        inviteText2 = Tex("surprise party").scale(.4)
        inviteText3 = Tex("for Eve!").scale(.4)
        inviteText1.shift(.5*UP)
        inviteText3.shift(.5*DOWN)
        inviteTextGroup = VGroup(inviteText1, inviteText2, inviteText3)
        inviteGroup = VGroup(inviteTextGroup, inviteBox)
        inviteGroup.shift(3.5*LEFT)
        self.play(Create(inviteTextGroup),
                  Create(inviteBox))

        self.wait()

        #sending notes to recipients
        newNotes = []
        oldNotes = []
        for recip in recipients:
            oldNote = inviteGroup.copy()
            self.add(oldNote)
            newNote = oldNote.copy().next_to(recip, LEFT, buff=0).scale(.6)
            newNotes.append(newNote)
            oldNotes.append(oldNote)
        self.remove(inviteTextGroup, inviteBox)
        self.play(*[ReplacementTransform(oldNotes[i], newNotes[i]) for i in range(0, len(oldNotes))])

        self.play(*[Transform(recip, changeMood(recip, "happy", RED, size=.4)) for recip in recipients])

        self.wait()

        #shift eve back up
        self.play(*[Transform(x, x.copy().shift(10*UP, 2*RIGHT)) for x in eveList])

        self.wait()

        self.play(*[Transform(recip, changeMood(recip, "sad", RED, size=.4)) for recip in recipients],
                  Transform(youPerson, changeMood(youPerson, "sad", BLUE)),
                  Transform(evePerson, changeMood(evePerson, "sad", GREEN)))
        
        self.wait()

        #ADD INTRO!!!!!

        amazonText = Tex("Amazon").scale(.4).next_to(recipients[2], RIGHT, buff=0.2)
        googleText = Tex("Google").scale(.4).next_to(recipients[1], RIGHT, buff=0.2)
        bankText = Tex("Bank of America").scale(.4).next_to(recipients[0], RIGHT, buff=0.2)
        self.play(Write(amazonText), run_time = .6)
        self.play(Write(googleText), run_time = .6)
        self.play(Write(bankText), run_time = .6)

        self.wait()

        #changing text on invites
        secretNoteBox = Rectangle(height=2, width=2)
        secretNoteText1L = Tex(r"{\bf Password}", color=YELLOW).scale(.46)
        secretNoteText1 = Tex("password123").scale(.4)
        secretNoteText2L = Tex(r"{\bf Credit Card}", color=YELLOW).scale(.46)
        secretNoteText2 = Tex("1234 5678 9101 8629").scale(.4)
        secretNoteText3L = Tex(r"{\bf Social Security}", color=YELLOW).scale(.46)
        secretNoteText3 = Tex("834-21-1234").scale(.4)
        secretNoteText1L.shift(.75*UP)
        secretNoteText1.shift(.5*UP)
        secretNoteText2L.shift(.125*UP)
        secretNoteText2.shift(.125*DOWN)
        secretNoteText3L.shift(.5*DOWN)
        secretNoteText3.shift(.75*DOWN)
        secretNoteTextGroup = VGroup(secretNoteText1, secretNoteText2, secretNoteText3,
                                     secretNoteText1L, secretNoteText2L, secretNoteText3L)
        secretNoteGroup = VGroup(secretNoteTextGroup, secretNoteBox).scale(.6)
        secretNotes = []
        for recip in recipients:
            secretNote = secretNoteGroup.copy().next_to(recip, LEFT)
            secretNotes.append(secretNote)
        self.play(*[ReplacementTransform(newNotes[i], secretNotes[i]) for i in range(0, len(newNotes))])

        self.wait()

        self.play(Transform(evePerson, changeMood(evePerson, "evil", GREEN)))

        self.wait()

        #changing message to random
        secretNoteBox = Rectangle(height=2, width=2)
        secretNoteText1L = Tex(r"{\bf Password}", color=YELLOW).scale(.46)
        secretNoteText1 = Tex("F'3UOb?V:wV").scale(.4)
        secretNoteText2L = Tex(r"{\bf Credit Card}", color=YELLOW).scale(.46)
        secretNoteText2 = Tex("gEW74?3yfRRLmN").scale(.4)
        secretNoteText3L = Tex(r"{\bf Social Security}", color=YELLOW).scale(.46)
        secretNoteText3 = Tex("A:v8VbJ-P)vn").scale(.4)
        secretNoteText1L.shift(.75*UP)
        secretNoteText1.shift(.5*UP)
        secretNoteText2L.shift(.125*UP)
        secretNoteText2.shift(.125*DOWN)
        secretNoteText3L.shift(.5*DOWN)
        secretNoteText3.shift(.75*DOWN)
        secretNoteTextGroup = VGroup(secretNoteText1, secretNoteText2, secretNoteText3,
                                     secretNoteText1L, secretNoteText2L, secretNoteText3L)
        secretNoteGroup = VGroup(secretNoteTextGroup, secretNoteBox).scale(.6)
        secretNotesEncrypted = []
        for recip in recipients:
            secretNoteEncrypted = secretNoteGroup.copy().next_to(recip, LEFT)
            secretNotesEncrypted.append(secretNoteEncrypted)
        self.play(*[Transform(secretNotes[i], secretNotesEncrypted[i]) for i in range(0, len(secretNotes))])

        self.wait()
        
        self.play(Transform(evePerson, changeMood(evePerson, "thinking", GREEN)),
                  Transform(eveHat, eveHat.copy().shift(.2*LEFT)))

        self.wait()

        self.play(*[Transform(recip, changeMood(recip, "happy", RED, size=.4)) for recip in recipients],
                  Transform(youPerson, changeMood(youPerson, "happy", BLUE)),
                  Transform(evePerson, changeMood(evePerson, "sad", GREEN)),
                  Transform(eveHat, eveHat.copy().shift(.2*RIGHT)))

        self.play(Circumscribe(VGroup(youPerson, youText)), run_time=1)

        self.wait()

        #self.play(*[Indicate(x) for x in eveList], run_time=1.5)
        eveGroup = VGroup(evePerson, eveHat, eveText)
        self.play(Circumscribe(eveGroup, run_time=1))

        self.wait()
        self.play(*[self.clearSceneFunc(obj) for obj in self.mobjects if self.clearSceneFunc(obj)!=1])

        self.wait()

        #crypto0Scene2().construct()
#class crypto0Scene2(Scene):
    #def construct(self):
        register_font("roboto_mono")
        #Cryptography, Cryptanalysis, 
        definitionsText = Text("Jargon").to_edge(UP, buff=1).scale(1.2)
        
        self.play(Write(definitionsText, run_time=1))

        self.wait()

        smallSize = .75

        cryptography = MarkupText('<gradient from="GREEN" to="BLUE"> Cryptography = code making </gradient>')
        cryptography.scale(smallSize)
        cryptography.move_to(Point([-3.55,1,0]))
        self.play(Write(cryptography, run_time=2))

        self.wait()

        cryptanalysis = MarkupText('<gradient from="RED" to="ORANGE"> Cryptanalysis = code breaking </gradient>').scale(smallSize)
        cryptanalysis.next_to(cryptography, RIGHT, buff=.4)
        self.play(Write(cryptanalysis, run_time=2))

        self.wait()

        cryptology = Text("Cryptology = both!").shift(DOWN)
        self.play(Write(cryptology, run_time=1))

        self.wait()

        self.play(Unwrite(cryptology), Unwrite(cryptography), Unwrite(cryptanalysis), run_time=1)

        self.wait()

        #pt and CT example
        plaintext = Text("plaintext", font="Courier New")
        self.play(Write(plaintext))
        
        self.wait()

        pt = Text("pt: ", font="Courier New").shift(UP)
        self.play(ReplacementTransform(plaintext, pt))

        self.wait()

        plaintextDef = MarkupText('<gradient from="GREEN" to="BLUE">this is a secret message to sub</gradient>', font="Courier New")
        pt.to_edge(LEFT)
        plaintextDef.next_to(pt, RIGHT)
        ptGroup = VGroup(pt, plaintextDef)
        self.remove(pt)
        self.play(ReplacementTransform(pt.copy().move_to(ORIGIN).shift(UP), ptGroup))
        
        self.wait()

        #without spaces
        plaintextDefNoSpace = MarkupText('<gradient from="GREEN" to="BLUE">thisasecretmessagetosub</gradient>', font="Courier New")
        plaintextDefNoSpace.next_to(pt, RIGHT)
        self.play(Transform(plaintextDef, plaintextDefNoSpace))

        self.wait()

        ciphertext = Text("Ciphertext", font="Courier New")
        self.play(Write(ciphertext))

        self.wait()

        ct = Text("CT: ", font="Courier New")
        self.play(ReplacementTransform(ciphertext, ct))

        self.wait()

        ciphertextDef = MarkupText('<gradient from="RED" to="ORANGE">TIAERTESGTSBHSSCEMSAEOU</gradient>', font="Courier New")
        ciphertextDef.next_to(ct, RIGHT)
        ctGroup = VGroup(ct.copy(), ciphertextDef.copy()).to_edge(LEFT)
        self.play(ReplacementTransform(ct, ctGroup))

        self.wait()

        smallArrow = Arrow([-2.5,.7,0], [-2.5,.7,0], color=YELLOW)
        arrow = Arrow([-2.5,.9,0], [-2.5,-1.9,0], color=YELLOW)
        self.play(Transform(ctGroup, ctGroup.copy().shift(2*DOWN)))
        self.play(Transform(smallArrow, arrow), run_time=1)
# class secretSauce(Scene):
#     def construct(self):
        secretSauce = MarkupText('<gradient from="YELLOW" to="RED">Secret Sauce??</gradient>')
        secretSauce.move_to([0, -.5, 0])
        self.play(Write(secretSauce))
        

        self.wait()
        
        self.play(*[self.clearSceneFunc(obj) for obj in self.mobjects if self.clearSceneFunc(obj)!=1])

        self.wait()

# class secretSauce(Scene):
#     def construct(self):
        teacher = makePerson(color=BLUE).shift(3*LEFT).scale(1.5)
        students=[]
        for i in range(3):
            students.append(makePerson(color=PURPLE).shift(i*2*RIGHT).align_to(teacher, DOWN))
        self.play(Create(teacher))
        for x in students:
            self.play(Create(x), run_time=.3)
        self.wait()

        self.play(Transform(teacher, changeMood(teacher.copy(), "teaching", BLUE, size=1.5)))

        self.wait()

        self.play(*[Transform(x, changeMood(x.copy(), "thinking", PURPLE)) for x in students])

        self.wait()

        self.play(Transform(teacher, changeMood(teacher.copy(), "happy", BLUE, size=1.5)))

        self.wait()

        self.play(*[Transform(x, changeMood(x.copy(), "happy", PURPLE)) for x in students])

        self.wait()
        
        self.play(Transform(teacher, changeMood(teacher.copy(), "teaching", BLUE, size=1.5)))

        self.wait()



 
        self.wait()

    def clearSceneFunc(self, obj):
        try:
            return Uncreate(obj)
        except:
            return 1

class Thumbnail(Scene):
    def construct(self):
        htks = Tex("How to keep secrets").shift(3*UP).scale(2)
        self.add(htks)
        youText = Tex("You", color=BLUE).shift(1.4*DOWN, 5*LEFT)
        youPerson = makePerson(color=BLUE).scale(.8).shift(5*LEFT)
        self.add(youPerson, youText)

        
        bobText = Tex("Bob", color=RED).shift(1.4*DOWN, 5*RIGHT)
        bobPerson = makePerson(color=RED, mood="thinking").scale(.8).shift(5*RIGHT)
        self.add(bobPerson, bobText)

        dontLike = Tex("I don't").move_to([-3.5,.2,0])
        dontLike2 = Tex("like Eve").move_to([-3.5,-.2,0])
        self.add(dontLike, dontLike2)

        a = Arrow([-2.5,0,0], [3.5,0,0])
        self.add(a)

        l=Line([.2,-2.1,0],[1,-2.1,0], color=GREEN).set_stroke(width=6)
        a2=Arrow([1,-2.38,0],[1,-.1,0], color=GREEN)
        self.add(l, a2)

        eveText = Tex("Eve", color=GREEN).shift(1.1*DOWN)
        evePerson = makePerson(color=GREEN, mood="evil").scale(.6)
        eveHatTriangle = Polygon([-.3,1.8,0], [.3,1.8,0], [0,2.5,0], color = GREEN)
        stripe1 = Line([-.2,2,0], [.2,2,0], color = GREEN)
        stripe2 = Line([-.13,2.2,0], [.13,2.2,0], color = GREEN)
        eveHat = VGroup(eveHatTriangle, stripe1, stripe2)
        eveHat.scale(.6).shift(.8*DOWN)
        eveList = [evePerson, eveText, eveHat]
        for i in eveList:
            i.shift(2.5*DOWN)
        self.add(evePerson, eveText, eveHat)

    
    


class StickFigureScene (Scene):
    def construct (self):
        
        person = makePerson(color = GREEN)
        self.play(Create(person))
        self.play(Transform(person, makePerson(color = GREEN, mood = "evil")))
        self.play(Transform(person, makePerson(color = GREEN, mood = "thinking")))
        self.play(Transform(person, makePerson(color = GREEN, mood = "happy")))
        self.play(Transform(person, makePerson(color = GREEN, mood = "sad")))
        self.play(Transform(person, makePerson(color = GREEN, mood = "teaching")))
        self.wait()

global makePerson
def makePerson(**kwargs):
    try:
        mainColor = kwargs["color"]
    except:
        color = BLUE

    try:
        mood = kwargs["mood"]
    except:
        mood = "default"
    person = VGroup()

    torso = Line([0,1,0], [0,-.3,0], color=mainColor)

    legL = Line([0,-.3,0], [-.5, -1.5, 0], color = mainColor)
    legR = Line([0,-.3,0], [.5, -1.5, 0], color = mainColor)

    arms = VGroup()
    armL = Line([0,.7,0], [-.5, .1, 0], color = mainColor)
    armR = Line([0,.7,0], [.5, .1, 0], color = mainColor)
    if mood == "happy":
        armL = Line([0,.5,0], [-.5, 1.1, 0], color = mainColor)
        armR = Line([0,.5,0], [.5, 1.1, 0], color = mainColor)
    if mood == "thinking":
        armR = Line([0,.7,0], [.9, 1.1, 0], color = mainColor)
    if mood == "teaching":
        armR = Line([0,.7,0], [.7, .9, 0], color = mainColor)
    arms.add(armL, armR)
    if mood == "thinking":
        arms.add(Line([.89, 1.09, 0], [.35, 1.65, 0], color = mainColor))

    head = Circle(radius=.4, color=mainColor).shift(UP*1.4)

    face = VGroup()
    headCenter = head.get_center()
    eyeL = Circle(.06, color=mainColor).move_to(headCenter).shift(LEFT*.15, UP*.1)
    eyeR = Circle(.06, color=mainColor).move_to(headCenter).shift(RIGHT*.15, UP*.1)
    smileWidth = .15
    mouth = ArcBetweenPoints(start=headCenter-[smileWidth,0,0], end=headCenter+[smileWidth,0,0], radius=.2, color=mainColor).shift(.12*DOWN)


    if mood == "happy":
        smileWidth = .18
        mouth = ArcBetweenPoints(start=headCenter-[smileWidth,0,0], end=headCenter+[smileWidth,0,0], radius=.19, color=mainColor).shift(.12*DOWN)
        eyebrowL = ArcBetweenPoints(end=eyeL.get_center() + [-.14,.06,0], start=eyeL.get_center() + [.02,.17,0], radius=.2, color = mainColor)
        eyebrowR = ArcBetweenPoints(start=eyeR.get_center() + [.14,.06,0], end=eyeR.get_center() + [-.02,.17,0], radius=.2, color = mainColor)
        head.add(eyebrowL, eyebrowR)
        #face.add(Line(start=headCenter-[smileWidth+.01,0,0], end=headCenter+[smileWidth+.01,0,0], color=mainColor).shift(.12*DOWN))

    elif mood == "sad":
        mouth = ArcBetweenPoints(end=headCenter-[smileWidth,0.08,0], start=headCenter+[smileWidth,-0.08,0], radius=.2, color=mainColor).shift(.12*DOWN)
        eyebrowL = ArcBetweenPoints(start=eyeL.get_center() + [-.12,.06,0], end=eyeL.get_center() + [.02,.15,0], radius=.2, color = mainColor)
        eyebrowR = ArcBetweenPoints(end=eyeR.get_center() + [.12,.06,0], start=eyeR.get_center() + [-.02,.15,0], radius=.2, color = mainColor)
        head.add(eyebrowL, eyebrowR)

    elif mood == "thinking":
        mouth = ArcBetweenPoints(end=headCenter-[smileWidth,0.08,0], start=headCenter+[smileWidth,-0.08,0], radius=100, color=mainColor).shift(.12*DOWN)
        eyebrowL = ArcBetweenPoints(end=eyeL.get_center() + [-.14,.06,0], start=eyeL.get_center() + [.02,.17,0], radius=.2, color = mainColor)
        eyebrowR = ArcBetweenPoints(end=eyeR.get_center() + [.12,.06,0], start=eyeR.get_center() + [-.02,.15,0], radius=100, color = mainColor)
        head.add(eyebrowL, eyebrowR)

    elif mood == "evil":
        eyebrowL = Line(eyeL.get_center() + [.12,.06,0], eyeL.get_center() + [-.02,.15,0], color = mainColor)
        eyebrowR = Line(eyeR.get_center() + [-.12,.06,0], eyeR.get_center() + [.02,.15,0], color = mainColor)
        head.add(eyebrowL, eyebrowR)


    head.add(eyeL, eyeR, mouth)


    person.add(torso, legL, legR, arms, head, face)
    return person

global changeMood
def changeMood(person, mood, color, **kwargs):
    try:
        size = kwargs["size"]
    except:
        size = 1
    newPerson = makePerson(color = color, mood = mood)
    newPerson.move_to(person.get_center())
    newPerson.scale(size).set_stroke(width=4*size)
    return newPerson

def scaleGroup(group, size):
    return group.copy().scale(size).set_stroke(width=4*size)