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
      
        try:
              fontSize = kwargs['size']
        except:
              fontSize = 30

        total = len(list)
        colors = color_gradient([color1, color2], total)
        for i in range(len(list)):
            shift = ((total/2) - i) * UP*4/total
            shift+= DOWN*1.5

            num = Tex(letter, f'{i + 1}: ', font_size = fontSize).shift(shift, leftShift*LEFT)
            num.set_color(colors[i])
            scene.add(num)

            try:
                  list[i].shift(shift).set_font_size(fontSize).next_to(num, RIGHT)
                  list[i].set_color(colors[i])
                  scene.add(list[i], num)
            except:
                  prevElem = num
                  for innerElem in list[i]:
                        innerElem.shift(shift).set_font_size(fontSize).next_to(prevElem, buff = 0.1)
                        innerElem.set_color(colors[i])
                        prevElem = innerElem
                        scene.add(innerElem)

