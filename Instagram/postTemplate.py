from postUtils.axiomListUtils import *
from manim import *

class NAME(Scene):
    def construct(self):
        spacing = .15
        title = MarkupText('<gradient from="BLUE" to="GREEN">TITLE</gradient>').scale(1.5).to_edge(UP)
        headingSize = .5
        description = Tex('EXAMPLE', 'Vblah', font_size = headingSize).next_to(title, DOWN, buff=.75).align_to(title, LEFT).shift(1.75*LEFT)
        description2 = Tex('LINE2').scale(.5).next_to(description, buff=0.1)

        #this would make all the text blocks with V's blue
        description.set_color_by_tex("V", BLUE)
        outline = square(3)

        self.add(title, description, description2, outline)


        textList = []
        textList.append(Tex('point1'))
        textList.append(Tex('point2'))
        #etc...

        MakeAxiomList(self, textList, "V")