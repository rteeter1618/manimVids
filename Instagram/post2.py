from manim import *

class subspaceCriterion(Scene):
    def construct(self):
        spacing = .15
        title = MarkupText('<gradient from="BLUE" to="GREEN">Subspace Criterion</gradient>').scale(1.5).to_edge(UP)
        description = Tex(
            'A subset ','W ' 'of a vector space ','V ','is a subspace of ','V ',' if and only if ','W ',' has the following three properties:'
            ).scale(.5).next_to(title, DOWN).align_to(title, LEFT).shift(.75*LEFT)

        description.set_color_by_tex("V", BLUE)
        description.set_color_by_tex("W", GREEN)
        self.add(title, description)


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
