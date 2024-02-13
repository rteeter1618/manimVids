from postUtils.axiomListUtils import *
from manim import *

class QuadraticVecSpace(Scene):
    def construct(self):
        #self.add(Square(side_length=8))
        spacing = .15
        title = MarkupText('<gradient from="BLUE" to="GREEN">Quadratic Equations, Another Vector Space</gradient>').scale(1).to_edge(UP)
        headingSize = 35
        description = Tex('The space of Quadratic Equations can be considered a ','vector space, ', 'in order to', font_size = headingSize).next_to(title, DOWN, buff=.2).align_to(title, LEFT)#.shift(1.75*LEFT)
        description2 = Tex('prove it is a ','vector space, ','we must first define the two ', 'vector operations', font_size = headingSize).next_to(description, DOWN, buff=0.1).align_to(description, LEFT)


        description.set_color_by_tex("vector space", GREEN)
        description2.set_color_by_tex("vector space", GREEN)
        description2.set_color_by_tex("vector operations", BLUE)

        self.add(title, description, description2)

        midSize = 40
        format = Tex('0: ', 'These vectors have the form ', r'$\langle a, b, c\rangle$', ', representing the quadratic', font_size = midSize).next_to(description2, DOWN, buff=1).align_to(description, LEFT)
        format2 = Tex('equation: ', r'$a+bx+cx^2$', font_size = midSize).next_to(format, DOWN, buff=0).align_to(description, LEFT)
        addition = Tex('1: ', r'scalar multiplication with scalar $\alpha$ is defined as follows:', font_size = midSize).next_to(format2, DOWN, buff=.5).align_to(description, LEFT)
        addition2 = Tex(r'$\alpha \cdot \langle a, b, x\rangle = \langle \alpha a, \alpha b, \alpha c \rangle$, or $\alpha(a+bx+cx^2) = \alpha a + \alpha bx + \alpha cx^2$', font_size = midSize).next_to(addition, DOWN, buff=0).align_to(description, LEFT)
        multiplication = Tex('2: ', r'and addition $\langle a_1, b_1, c_1 \rangle + \langle x_2, y_2 \rangle = \langle x_1 + x_2, y_1 + y_2 \rangle$, or', font_size = midSize).next_to(addition2, DOWN, buff=.5).align_to(description, LEFT)
        multiplication2 = Tex(r'$a_1+b_1x+c_1x^2 + a_2+b_2x+c_2x^2 = (a_1+a_2) + (b_1+b_2)x + (c_1+c_2)x^2$', font_size = midSize).next_to(multiplication, DOWN, buff=0).align_to(description, LEFT)

        # format.set_color_by_tex("0", BLUE)
        # addition.set_color_by_tex("1", TEAL)
        # multiplication.set_color_by_tex("2", GREEN)

        
        format.set_color(BLUE)
        format2.set_color(BLUE)
        addition.set_color(TEAL)
        addition2.set_color(TEAL)
        multiplication.set_color(GREEN)
        multiplication2.set_color(GREEN)

        
        # format[2].set_color(TEAL)
        # format2[1].set_color(TEAL)
        # addition.set_color_by_tex("alpha", PURPLE)
        self.add(format, format2, addition, addition2, multiplication, multiplication2)