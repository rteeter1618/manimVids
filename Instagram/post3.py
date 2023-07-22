from postUtils.axiomListUtils import *
from manim import *

class R3VecSpace(Scene):
    def construct(self):
        self.add(Square(side_length=8))
        spacing = .15
        title = Tex('$\mathbb{R}^2$ The Model Vector Space').scale(1.5).to_edge(UP)
        title.set_color(BLUE)
        description = Tex('$\mathbb{R}^3$', ', the 2d plane is one of the most common ','vector spaces ','studied, in order to prove').scale(.65).next_to(title, DOWN, buff=.75).align_to(title, LEFT)#.shift(1.75*LEFT)
        description2 = Tex('it is a ','vector space, ','we must prove it follows all the vec','tor space ','axioms').scale(.65).next_to(description, DOWN, buff=0.1).align_to(description, LEFT)
        description3 = Tex(r'vectors in $\mathbb{R}^2 have the form \langle x, y\rangle$').scale(.65).next_to(description2, DOWN, buff=0.1).align_to(description, LEFT)
        #self.add(index_labels(title))

        #this would make all the text blocks with V's blue
        description.set_color_by_tex("3", BLUE)
        description.set_color_by_tex("vector space", GREEN)
        description2.set_color_by_tex("vector space", GREEN)
        description2.set_color_by_tex("axiom", BLUE)

        
        self.add(title, description, description2, description3)


        textList = []
        textList.append(Tex('point1'))
        textList.append(Tex('point2'))
        #etc...

        MakeAxiomList(self, textList, "V", color1 = ORANGE)