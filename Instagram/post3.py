from postUtils.axiomListUtils import *
from manim import *

class R3VecSpace(Scene):
    def construct(self):
        #self.add(Square(side_length=8))
        spacing = .15
        title = Tex('$\mathbb{R}^2$ ').scale(2).to_edge(UP).shift(5*LEFT)
        title.set_color(BLUE)
        title2 = MarkupText('<gradient from="BLUE" to="GREEN">The Model Vector Space</gradient>').scale(1.5).to_edge(UP).next_to(title, RIGHT, buff=0.1)
        headingSize = 28
        description = Tex('$\mathbb{R}^2$', ', the 2d plane is one of the most common ','vector spaces ', 'studied, in order to', font_size = headingSize).next_to(title, DOWN, buff=.5).align_to(title, LEFT)#.shift(1.75*LEFT)
        description2 = Tex('prove it is a ','vector space, ','we must prove it follows all the vec','tor space ','axioms', font_size = headingSize).next_to(description, DOWN, buff=0.1).align_to(description, LEFT)
        description3 = Tex(r'Vectors in $\mathbb{R}^2$ have the form $\langle x, y\rangle$, scalar multiplication with scalar $\alpha$ is:', font_size = headingSize).next_to(description2, DOWN, buff=0.1).align_to(description, LEFT)
        description4 = Tex(r'$\alpha \cdot \langle x, y\rangle = \langle \alpha x, \alpha y \rangle$, and addition $\langle x_1, y_1 \rangle + \langle x_2, y_2 \rangle = \langle x_1 + x_2, y_1 + y_2 \rangle$', font_size = headingSize).next_to(description3, DOWN, buff=0.1).align_to(description, LEFT)
        
        #self.add(index_labels(title))

        #this would make all the text blocks with V's blue
        description.set_color_by_tex("3", BLUE)
        description.set_color_by_tex("vector space", GREEN)
        description2.set_color_by_tex("vector space", GREEN)
        description2.set_color_by_tex("axiom", BLUE)

        
        self.add(title, title2, description, description2, description3, description4)


        textList = []
        textList.append([Tex(r'Addition is commutative: $\langle x_1, y_1 \rangle + \langle x_2, y_2 \rangle = \langle x_1 + x_2, y_1 + y_2 \rangle$'),
                          Tex(r'$ = \langle x_2, y_2 \rangle + \langle x_1, y_1 \rangle $')])
        textList.append([Tex(r'Addition is assosciative: $(\langle x_1, y_1 \rangle + \langle x_2, y_2 \rangle) + \langle x_3, y_3 \rangle$'),
                          Tex(r'$= \langle x_1 + x_2 + x_3, y_1 + y_2 + y_3 \rangle = \langle x_1, y_1 \rangle + (\langle x_2, y_2 \rangle + \langle x_3, y_3 \rangle)$')])
        textList.append([Tex(r'The zero vector is $\langle 0,0 \rangle, and \langle x, y \rangle + \langle 0,0 \rangle = \langle x, y \rangle$')])
        textList.append([Tex(r'The inverse of $\langle x, y \rangle$ is $\langle -x, -y \rangle$, since $\langle x, y \rangle + \langle -x, -y \rangle = \langle 0,0 \rangle$')])
        textList.append([Tex(r'Scalar multiplication works like normal: '),
                         Tex(r'$\alpha \cdot (\beta \cdot \langle x, y \rangle = \beta \cdot \langle \alpha x, \alpha y \rangle)$'),
                         Tex(r'$= \langle \beta \alpha x, \beta \alpha y \rangle = (\alpha \beta) \cdot \langle x, y \rangle$')])
        textList.append([Tex(r'Addition of scalars distributes: $(\alpha + \beta) \cdot \langle x, y \rangle = \langle (\alpha + \beta)x, (\alpha + \beta)y \rangle$'),
                         Tex(r'$= \langle \alpha x + \beta x, \alpha y + \beta y \rangle = \langle \alpha x, \alpha y \rangle + \langle \beta x, \beta y \rangle = \alpha \langle x, y \rangle + \beta \langle x, y \rangle $')])
        textList.append([Tex(r'Addition of vectors distributes: $\alpha \cdot (\langle x_1, y_1 \rangle + \langle x_2, y_2 \rangle)$'),
                         Tex(r'$= \alpha \cdot \langle x_1 + x_2, y_1 + y_2 \rangle = \langle \alpha x_1 + \alpha x_2, \alpha y_1 + \alpha y_2 \rangle = \alpha \langle x_1, y_1 \rangle + \alpha \langle x_2, y_2 \rangle$')])
        textList.append([Tex(r'The scalar 1 acts like the identity: $1 \cdot \langle x, y \rangle = \langle 1 \cdot x, 1 \cdot y \rangle = \langle x, y \rangle$')])

        MakeAxiomList(self, textList, "V", color1 = GREEN, color2 = BLUE, leftShift = 5.5, size = 20)