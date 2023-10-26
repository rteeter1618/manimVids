from manim import *
# can i import makePerson??
class Crypto1Main(Scene):
    def construct(self):
        pt = Text("pt: ", font="Courier New").shift(UP)
        pt.to_edge(LEFT)
        plaintextDefNoSpace = MarkupText('<gradient from="GREEN" to="BLUE">thisisasecretmessagetosub</gradient>', font="Courier New")
        plaintextDefNoSpace.next_to(pt, RIGHT)
        ptGroup = VGroup(pt, plaintextDefNoSpace)

        self.play(Write(ptGroup), run_time = 1)

        ct = Text("CT: ", font="Courier New").shift(2*DOWN)
        ciphertextDef = MarkupText('<gradient from="RED" to="ORANGE">TIIAERTESGTSBHSSSCEMSAEOU</gradient>', font="Courier New")
        ciphertextDef.next_to(ct, RIGHT)
        ctGroup = VGroup(ct, ciphertextDef).to_edge(LEFT)
        self.play(Write(ctGroup), run_time = 1)


        smallArrow = Arrow([-2.5,.7,0], [-2.5,.7,0], color=YELLOW)
        arrow = Arrow([-2.5,.9,0], [-2.5,-1.9,0], color=YELLOW)

        secretSauce = MarkupText('<gradient from="YELLOW" to="RED">Secret Sauce??</gradient>')
        secretSauce.move_to([0, -.5, 0])
        self.play(Write(secretSauce), Transform(smallArrow, arrow), run_time=1)
        
        self.wait()
        
        self.play(*[self.clearSceneFunc(obj) for obj in self.mobjects if self.clearSceneFunc(obj)!=1])

        self.wait()

        #classroom scene

        studentsL = []
        studentsL.append(makePerson(color=PURPLE).shift(2*DOWN, 3*LEFT))
        studentsL.append(makePerson(color=PURPLE).shift(2*DOWN))
        studentsL.append(makePerson(color=PURPLE).shift(2*DOWN, 3*RIGHT))
        studentsL.append(makePerson(color=PURPLE).shift(1.5*LEFT))
        studentsL.append(makePerson(color=PURPLE).shift(1.5*RIGHT))
        teacher = makePerson(color=BLUE).scale(1.5).shift(UP, 5*RIGHT)
        for stud in studentsL:
            stud.shift(LEFT)
        studentsG = VGroup(*studentsL)
        classG = VGroup(teacher, studentsG)
        self.play(Create(classG))

        self.wait()

        bubble = speechBubble(text="igpay atinlay")
        bubble2 = speechBubble(text="onay omeworkhay!")
        bubble.scale(.5).shift([-.9, 2.15, 0])
        bubble2.scale(.5).shift([-.9, 2.15, 0])
        #student says igpay atinlay
        self.play(*[Create(i) for i in bubble])

        self.wait()

        #others confused
        preConfusedPeople = [[studentsL[i], PURPLE] for i in range(0,3)]
        preConfusedPeople.append([teacher, BLUE])
        confusedPeople = [changeMood(person[0], "thinking", person[1]) for person in preConfusedPeople]
        self.play(*[Transform(preConfusedPeople[i][0], confusedPeople[i]) for i in range(0, len(confusedPeople))])


        self.wait()

        #student says onay omeworkhay
        self.play(Transform(bubble, bubble2))

        self.wait()

        #student and friend happy
        preHappyPeople = studentsL[3:]
        happyPeople = [changeMood(person, "happy", PURPLE) for person in preHappyPeople]
        self.play(*[Transform(preHappyPeople[i], happyPeople[i]) for i in range(0, len(preHappyPeople))])

        self.wait()

        self.clearAll()

        self.wait()

        pigLatinTitle = Text("Pig Latin", color=PINK).shift(3*UP)
        self.play(Write(pigLatinTitle))

        self.wait()

        learnPigLatinText = MarkupText('<gradient from="GREEN" to="BLUE"> subscribe to learn how to speak pig latin</gradient>', font="Courier New", font_size=20)
        self.play(Write(learnPigLatinText))

        self.wait()


    def clearSceneFunc(self, obj):
        try:
            return Uncreate(obj)
        except:
            return 1
    
    def clearAll(self):
        self.play(*[self.clearSceneFunc(obj) for obj in self.mobjects if self.clearSceneFunc(obj)!=1])

class CurAnimation(Scene):
    def construct(self):
        learnPigLatinText = MarkupText('<gradient from="GREEN" to="BLUE"> subscribe to learn how to speak pig latin</gradient>', font="Courier New", font_size=30)
        self.play(Write(learnPigLatinText))

        self.wait()
        
        learnPigLatinText2 = MarkupText(
            f'<span fgcolor="{LIGHT_BROWN}">s</span><span fgcolor="{BLUE_B}">ubscribe </span>'
            f'<span fgcolor="{LIGHT_BROWN}">t</span><span fgcolor="{BLUE_B}">o </span>'
            f'<span fgcolor="{LIGHT_BROWN}">l</span><span fgcolor="{BLUE_B}">earn </span>'
            f'<span fgcolor="{LIGHT_BROWN}">h</span><span fgcolor="{BLUE_B}">ow </span>'
            f'<span fgcolor="{LIGHT_BROWN}">t</span><span fgcolor="{BLUE_B}">o </span>'
            f'<span fgcolor="{LIGHT_BROWN}">sp</span><span fgcolor="{BLUE_B}">eak </span>'
            f'<span fgcolor="{LIGHT_BROWN}">p</span><span fgcolor="{BLUE_B}">ig </span>'
            f'<span fgcolor="{LIGHT_BROWN}">l</span><span fgcolor="{BLUE_B}">atin</span>'
            , font="Courier New", font_size=30)
        self.play(ReplacementTransform(learnPigLatinText, learnPigLatinText2))

        self.wait()

        learnPigLatinText3Top =    MarkupText(' ubscribe  o  earn  ow  o   eak  ig  atin'
                                     , color=BLUE_B, font="Courier New", font_size=30)
        learnPigLatinText3Bottom = MarkupText('s         t  l     h   t  sp    p   l    '
                                     , color=LIGHT_BROWN, font="Courier New", font_size=30).next_to(learnPigLatinText3Top, DOWN).shift(.6*LEFT)
        self.play(ReplacementTransform(learnPigLatinText2.copy(), learnPigLatinText3Top), ReplacementTransform(learnPigLatinText2, learnPigLatinText3Bottom))

        self.wait()
        learnPigLatinText4Bottom = MarkupText('         s  t     l   h  t     sp  p     l'
                                     , color=LIGHT_BROWN, font="Courier New", font_size=30,).next_to(
                                         learnPigLatinText3Top, DOWN).shift(1.1*RIGHT)
        self.play(ReplacementTransform(learnPigLatinText3Bottom, learnPigLatinText4Bottom))

        self.wait()

        learnPigLatinText5Bottom = learnPigLatinText4Bottom.copy().shift(.55*UP)
        self.play(ReplacementTransform(learnPigLatinText4Bottom, learnPigLatinText5Bottom))

        self.wait()

        learnPigLatinTextFinal = MarkupText(
            f'<span fgcolor="{BLUE_B}">ubscribe </span><span fgcolor="{LIGHT_BROWN}">s</span><span fgcolor="{PURPLE}">ay</span>'
            f'<span fgcolor="{BLUE_B}">o </span><span fgcolor="{LIGHT_BROWN}">t</span>'
            f'<span fgcolor="{BLUE_B}">earn </span><span fgcolor="{LIGHT_BROWN}">l</span>'
            f'<span fgcolor="{BLUE_B}">ow </span><span fgcolor="{LIGHT_BROWN}">h</span>'
            f'<span fgcolor="{BLUE_B}">o </span><span fgcolor="{LIGHT_BROWN}">t</span>'
            f'<span fgcolor="{BLUE_B}">eak </span><span fgcolor="{LIGHT_BROWN}">sp</span>'
            f'<span fgcolor="{BLUE_B}">ig </span><span fgcolor="{LIGHT_BROWN}">p</span>'
            f'<span fgcolor="{BLUE_B}">atin</span><span fgcolor="{LIGHT_BROWN}">l</span>'
            , font="Courier New", font_size=30)
        self.play(ReplacementTransform(VGroup(learnPigLatinText3Top, learnPigLatinText5Bottom), learnPigLatinTextFinal))

        self.wait()


#returns the mobject made of a Vgroup that is the speech bubble
#kwargs
#text=text to be in the speech bubble
#multiLineText: to implement if needed
global speechBubble
def speechBubble(**kwargs):
    #default is blank
    words = kwargs.get("text", "")
    text = Text(words, width=3, height=1.5)
    totalHeight = 1.5
    multiLineWords = kwargs.get("multiLineText",[])
    multiLineTexts = []
    if(len(multiLineWords) > 0):
        lineHeight = totalHeight / len(multiLineWords)
        for i, line in enumerate(multiLineWords):
            heightDiff = ((len(multiLineTexts)/2.0) - i)*totalHeight/2
            multiLineTexts.append(Text(line, width=3, height=lineHeight).shift(heightDiff*UP))

    rect1 = RoundedRectangle(corner_radius=1, height=2, width=4)
    rect2 = rect1.copy()
    rect1.pointwise_become_partial(rect1, 0, .56)
    rect2.pointwise_become_partial(rect2, .5962, 1)
    line1 = Line([-2.5,-1.5,0],[-1.8,-.6,0])
    line2 = Line([-2.5,-1.5,0],[-1.48,-.88,0])

    #this is uneeded now, it could have covered stuff in the background
    points = Group(
        Point([-1.8,-.65,0], color = RED),
        Point([-1.75,-.55,0], color = RED),
        Point([-1.48,-.83,0], color = RED),
        Point([-1.53,-.88,0], color = RED)
    )
    cover = Polygon([-1.8,-.67,0], [-1.75,-.57,0], 
                    [-1.47,-.83,0], [-1.565,-.88,0],  color=BLACK, fill_opacity = 1)

    #group = Group(line1,rect,line2, cover, points)
    group = VGroup(line1, rect1, rect2, line2, text, *[line for line in multiLineTexts])
    return group

global makePerson
#args:
#color:color of person, default blue
#mood: happy,sad,thinking,evil,teaching,default
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

