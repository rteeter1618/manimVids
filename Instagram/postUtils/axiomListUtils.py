from manim import *

def MakeAxiomList(scene, list, letter, **kwargs):
        try:
              color1 = kwargs['color1']
        except:
              color1 = BLUE
        
        try:
              color2 = kwargs['color2']
        except:
              color2 = GREEN

        try:
              leftShift = kwargs['leftShift']
        except:
              leftShift = 4

        total = len(list)
        colors = color_gradient([color1, color2], total)
        for i in range(len(list)):
            shift = ((total/2) - i) * UP*4/total
            shift+= DOWN*1.5

            num = Tex(letter, f'{i + 1}: ').scale(.75).shift(shift, leftShift*LEFT)

            list[i].shift(shift).scale(.75).next_to(num, RIGHT)
            
            num.set_color(colors[i])
            list[i].set_color(colors[i])

            scene.add(list[i], num)
