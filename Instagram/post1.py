from manim import *

class vectorAxioms(Scene):
    def construct(self):
        spacing = .15
        title = MarkupText('<gradient from="BLUE" to="GREEN">Vector space axioms </gradient>').scale(1.5).to_edge(UP)
        intro = Tex('A vector space is a triple (','V',', ','$\cdot$',', ','+',') over a field ','F',':').scale(.5).next_to(title, DOWN).align_to(title, LEFT).shift(.75*LEFT)
        intro2 = Tex('Where ','V',' is a set of ements called vectors, ','$\cdot$',' and ','+',' are binary operators').scale(.5).next_to(intro, DOWN, buff=spacing).align_to(intro, LEFT)
        intro3 = Tex(r'Such that for any vectors ',r'$\vec{u}, \vec{v}, \vec{w}$',r' $\in$ ','V',r' and scalars ',r'$\alpha , \beta$',r' $\in$ ','F').scale(.5).next_to(intro2, DOWN, buff=spacing).align_to(intro, LEFT)
        intro4 = Tex(', the following axioms hold').scale(.5).next_to(intro3, RIGHT, buff=0)

        # colors = color_gradient([RED, ORANGE], 3)
        # intro.set_color(colors[0])
        # intro2.set_color(colors[1])
        # intro3.set_color(colors[2])
        # intro4.set_color(colors[2])

        #intro.set_color_by_gradient([RED, ORANGE])

        #self.add(index_labels(intro).shift(.1*UP))
        colors = color_gradient([BLUE, GREEN], 3)
        vectColor = colors[0]
        opsColor = colors[1]
        scalarColor = colors[2]

        intro[1].set_color(vectColor)
        intro.set_color_by_tex("cdot", opsColor)
        intro.set_color_by_tex("+", opsColor)
        intro.set_color_by_tex("F", scalarColor)

        intro2.set_color_by_tex("V", vectColor)
        intro2.set_color_by_tex("cdot", opsColor)
        intro2.set_color_by_tex("+", opsColor)

        #colors the whole group
        intro3.set_color_by_tex("V", vectColor)
        intro3.set_color_by_tex("vec{u}", vectColor)
        #intro3[1].set_color(vectColor)
        intro3.set_color_by_tex("alpha", scalarColor)
        intro3.set_color_by_tex("F", scalarColor)

        self.add(title, intro, intro2, intro3, intro4)

        list = []
        list.append(Tex(r'Vector addition is commutative: '
                            +r'\(\vec{v} + \vec{w} = \)'
                            +r'\(\vec{w} + \vec{v}\)'))
        
        list.append(Tex(r'Vector addition is assosciative: '
                            +r'\( (\vec{u} + \vec{v}) + \vec{w}='
                            +r'\vec{u} + (\vec{w} + \vec{v}) \)'))
        
        list.append(Tex(r'There exists a zero vector \(\vec{0}\), with '
                            +r'\(\vec{v} + \vec{0} = \vec{v}\) and '
                            +r'\(\vec{0} + \vec{v} = \vec{v}\)'))
        
        list.append(Tex(r'Every vector \( \vec{v} \) has an inverse vector \( -\vec{v} \)'
                        +r', with \( \vec{v} + (-\vec{v}) = \vec{0} ='
                        +r' (-\vec{v}) + \vec{v} \)'))
        
        list.append(Tex(r'Scalar multiplication works like normal multiplication: '
                        +r'$ \alpha\cdot(\beta \cdot \vec{v}) = ( \alpha\beta) \cdot \vec{v} $'))
        
        list.append(Tex(r'Addition of scalars distributes: '
                        +r'$ (\alpha + \beta) \cdot \vec{v} = '
                        +r'\alpha \cdot \vec{v} + \beta \cdot \vec{v}$'))
        
        list.append(Tex(r'addition of vectors distributes: '
                        +r'$\alpha \cdot ( \vec{v} + \vec{w}) = '
                        +r'\alpha \cdot \vec{v} + \alpha \cdot \vec{w}$'))
        
        list.append(Tex(r'The scalar 1 acts like the identity on vectors: '
                        +r'$ 1 \cdot \vec{v} = \vec{v}$'))

        #self.add(list[2])
        self.makeOList(list)

    def makeOList(self, list):
        total = len(list)
        colors = color_gradient([BLUE, GREEN], total)
        for i in range(len(list)):
            shift = ((total/2) - i) * UP*4/total
            shift+= DOWN*1.5

            num = Tex(f'V{i + 1}: ').scale(.5).shift(shift, 5*LEFT)

            list[i].shift(shift).scale(.5).next_to(num, RIGHT)
            
            num.set_color(colors[i])
            list[i].set_color(colors[i])

            self.add(list[i], num)
