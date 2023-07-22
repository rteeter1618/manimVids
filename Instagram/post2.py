from manim import *

class subspaceCriterion(Scene):
    def construct(self):
        self.add(Square(side_length=8))
        spacing = .15
        title = MarkupText('<gradient from="BLUE" to="GREEN">Subspace Criterion</gradient>').scale(1.5).to_edge(UP)
        description = Tex(
           'A subset ','W ','of a vector space ','V ','(','W',r'$\subseteq$','V',') is a subspace of ','V ',' if and only if:'
            ).scale(.5).next_to(title, DOWN, buff=.75).align_to(title, LEFT).shift(1.75*LEFT)
        description2 = Tex('W',' has the following three properties:').scale(.5).next_to(description, buff=0.1)

        description.set_color_by_tex("V", BLUE)
        description.set_color_by_tex("W", GREEN)
        description2.set_color_by_tex("W", GREEN)
        self.add(title, description, description2)


        list = []
        list.append(Tex('W ', 'Contains the zero vector of ', 'V', r'$: \vec{0} \in$', 'W'))
        list.append(Tex('W is closed under additon: ', r'$\forall \vec{w_{1}}, \vec{w_{2}} \in W,  \vec{w_{1}} + \vec{w_{2}} \in W$'))
        list.append(Tex('W is closed under scalar multiplication: ', r'$\forall \alpha \in F, \alpha \cdot \vec{w} \in W$'))

        #self.add(list[2])
        self.makeOList(list)

    def makeOList(self, list):
        total = len(list)
        colors = color_gradient([BLUE, GREEN], total)
        for i in range(len(list)):
            shift = ((total/2) - i) * UP*4/total
            shift+= DOWN*1.5

            num = Tex(f'S{i + 1}: ').scale(.75).shift(shift, 5*LEFT)

            list[i].shift(shift).scale(.75).next_to(num, RIGHT)
            
            num.set_color(colors[i])
            list[i].set_color(colors[i])

            self.add(list[i], num)
