from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PURPLE, .25)

        square = Square()
        square.set_fill(GREEN, .25)
        square.next_to(circle, RIGHT, buff=1)
        square.rotate_about_origin(PI/2)

        squareL = Square()
        squareL.next_to(circle, LEFT, buff=1)
        squareL.set_fill(RED, .75)

        squareU = Square()
        squareU.next_to(circle, UP, buff=.25)
        squareU.rotate(PI/4)
        squareU.set_fill(ORANGE, .5)

        self.play(Create(circle), Create(square))
        self.play(Transform(square, squareL))
        self.play(circle.animate.set_fill(ORANGE), 
                  ReplacementTransform(squareL, squareU))
        self.add(square)
        self.wait(2)
        self.remove(square)
        self.wait(2)