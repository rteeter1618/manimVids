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

        bubble = speechBubble()
        #self.add(bubble)
        self.play(Create(bubble))

        self.wait()


    def clearSceneFunc(self, obj):
        try:
            return Uncreate(obj)
        except:
            return 1


global speechBubble
def speechBubble():
    rect = RoundedRectangle(corner_radius=1, height=2, width=4)
    line1 = Line([-2.5,-1.5,0],[-1.8,-.6,0])
    line2 = Line([-2.5,-1.5,0],[-1.48,-.88,0])

    points = Group(
        Point([-1.8,-.65,0], color = RED),
        Point([-1.75,-.55,0], color = RED),
        Point([-1.48,-.83,0], color = RED),
        Point([-1.53,-.88,0], color = RED)
    )

    cover = Polygon([-1.8,-.67,0], [-1.75,-.57,0], 
                    [-1.47,-.83,0], [-1.565,-.88,0],  color=BLACK, fill_opacity = 1)

    #group = Group(line1,rect,line2, cover, points)
    group = VGroup(line1,rect,line2, cover,)
    return group

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

