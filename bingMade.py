from manim import *
from random import randint
import numpy as np

class Transformations(Scene):
    def construct(self):
        square = Square().set_color(RED)
        circle = Circle().set_color(BLUE).shift(RIGHT * 2)
        triangle = Triangle().set_color(GREEN).shift(LEFT * 2)
        ellipse = Ellipse().set_color(YELLOW).shift(UP * 2)
        rectangle = Rectangle().set_color(PURPLE).shift(DOWN * 2)

        shapes = [square, circle, triangle, ellipse, rectangle]
        colors = [RED, BLUE, GREEN, YELLOW, PURPLE]

        for shape in shapes:
            self.play(Transform(shape.copy(), shape.set_color(colors[randint(0,len(colors)-1)])))
            self.play(ApplyMethod(shape.shift,[randint(-5,5) for _ in range(3)]))


class SunToMoon(Scene):
    def construct(self):
        # Create a sun with triangles around the edge
        sun = Ellipse(width=2, height=2, color=YELLOW)
        triangles = VGroup()
        for i in range(8):
            triangle = Triangle(color=YELLOW).scale(0.2)
            triangle.rotate(-PI/2 + i * PI/4)
            triangle.move_to(sun.get_center() + RIGHT * 1.1 * (np.cos(i*PI/4))
                             + sun.get_center() + UP * 1.1 * np.sin(i*PI/4))
            #triangle.next_to(sun.get_edge_center(i * PI / 4), OUT)
            triangles.add(triangle)
        sun.add(triangles)
        sun.move_to(LEFT)
        sun2 = sun.copy()

        # Create a moon with darker circles for craters
        moon = Circle(color=WHITE)
        craters = VGroup()
        for i in range(8):
            crater = Circle(color=DARK_GRAY).scale(0.1)
            crater.move_to(moon.get_center() + 0.5 * RIGHT * np.cos(i * PI / 8)
                           + moon.get_center() + 0.5 * UP * np.sin(i * PI / 8))
            craters.add(crater)
        moon.add(craters)
        moon.move_to(RIGHT)

        self.play(Create(sun))
        self.wait(1)
        self.play(Transform(sun, moon), run_time=3)
        self.wait(1)
        
        self.remove(moon)
        self.remove(sun)
        # Create a bigger circle as the path
        path1 = Circle(radius=1.5)
        path2 = Circle(radius=3)
        self.play(MoveAlongPath(sun2, path1), MoveAlongPath(moon, path2), run_time=4, rate_func = linear)

class RotatingCircles(Scene):
    def construct(self):
        # Create two circles
        circle1 = Circle(radius=0.5, color=BLUE)
        circle2 = Circle(radius=0.5, color=GREEN)
        square1 = Square(side_length = 2)

        # Create a bigger circle as the path
        path = Circle(radius=2)

        # Animate the circles rotating around their centers
        self.play(Rotate(square1, angle=TAU), Rotate(circle2, angle=-TAU), run_time=4)

        # Animate the circles moving along the path
        self.play(MoveAlongPath(circle1, path), MoveAlongPath(circle2, path), run_time=4)

class RateFunctionsExample(Scene):
    def construct(self):
        # Create three lines with different colors
        line1 = Line(3*LEFT, 3*RIGHT).shift(UP).set_color(RED)
        line2 = Line(3*LEFT, 3*RIGHT).set_color(GREEN)
        line3 = Line(3*LEFT, 3*RIGHT).shift(DOWN).set_color(BLUE)

        # Create three dots at the left end of each line
        dot1 = Dot().move_to(line1.get_left())
        dot2 = Dot().move_to(line2.get_left())
        dot3 = Dot().move_to(line3.get_left())

        # Add lines and dots to scene
        self.add(line1, line2, line3)
        self.add(dot1, dot2, dot3)

        # Animate dots moving along lines with different rate functions
        self.play(
            MoveAlongPath(dot1, line1), # default rate function is smooth
            MoveAlongPath(dot2, line2), # linear rate function
            MoveAlongPath(dot3, line3), # rush into rate function
            run_time=4,
            rate_func=linear
        )
from manim import *

class LoadingScreen(Scene):
    def construct(self):
        # Create a circle with a dashed stroke
        circle = Circle(stroke_width=6, stroke_color=WHITE)
        #circle.set_style(stroke_pattern=[0.1, 0.1])

        # Create an arc that starts from the top of the circle
        arc = Arc(radius=circle.radius, start_angle=PI/2)
        arc.move_to(circle.get_center())

        # Add the circle and the arc to the scene
        self.add(circle, arc)

        # Animate the arc rotating around the circle
        self.play(Rotating(arc, radians=TAU, about_point=circle.get_center(), run_time=5))

class HappyBirthday(Scene):
    def construct(self):
        # Create a text mobject with "Happy Birthday" and set its color and font
        text = Text("Happy Birthday", color=YELLOW).set_font("Comic Sans MS")

        # Add the text to the scene
        self.add(text)

        # Animate the text with different effects
        self.play(Write(text)) # write the text on screen
        self.wait()
        self.play(FadeIn(text[0])) # fade in the first letter
        self.play(ScaleInPlace(text[1], 2)) # scale up the second letter
        self.play(Rotate(text[2], PI/4)) # rotate the third letter
        #self.play(WiggleOutThenIn(text[3])) # wiggle the fourth letter
        self.wait()

class BouncingCircle(Scene):
    def construct(self):
        # Create a circle with radius 0.5 and color yellow
        circle = Circle(radius=0.5, color=YELLOW)

        # Create a line with length 6 and color white
        line = Line(start=LEFT * 3, end=RIGHT * 3, color=WHITE)

        # Add the circle and the line to the scene
        self.add(circle, line)

        # Create a path for the circle to follow
        path = VMobject()
        path.set_points_as_corners([circle.get_center(), RIGHT * 2 + DOWN * 2])

        # Animate the circle moving along the path
        self.play(MoveAlongPath(circle, path))

        # Animate the circle bouncing on the line
        #self.play(Bounce(circle, line))

        # Add some gravity effect to the circle
        #self.play(ApplyForce(circle.velocity * DOWN))

from manim import *

class SquareWave(FunctionGraph):
    def __init__(self):
        super().__init__(lambda x: 1 if x % (2 * PI) < PI else -1,
                         #x_min=-PI,
                         #x_max=PI,
                         color=BLUE)

class SineWave(FunctionGraph):
    def __init__(self, n):
        self.n = n
        super().__init__(lambda x: (4 / (n * PI)) * np.sin(n * x),
                         #x_min=-PI,
                         #x_max=PI,
                         color=YELLOW)

class Fourier(VGroup):
    def __init__(self):
        self.waves = [SineWave(2 * n + 1) for n in range(10)]
        super().__init__(*self.waves)

    def get_sum(self):
        return sum([wave.get_function() for wave in self.waves], start=self.waves[0].get_function())

class FourierScene(Scene):
    def construct(self):
        signal = SquareWave()
        fourier = Fourier()
        fourier_sum = FunctionGraph(fourier.get_sum(), color=GREEN)
        
        self.add(signal)
        self.play(Create(fourier))
        
        for wave in fourier:
            self.play(Transform(wave,fourier_sum), run_time=0.5)
            self.wait(0.5)
        
        self.wait(1)


class Alphabet(Scene):
    def construct(self):
        self.play(Write(Text("ABC")))


class Alphabet1(Scene):
    def construct(self):
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        vigSquare = []
        groupVigSquare = VGroup()
        for i in range(0,26):
            str = ""
            l1 = alphabet[i:26]
            l2 = (alphabet[0:i])
            for j in range(len(l1)):
                str+=l1[j]
            for j in range(len(l2)):
                str+=l2[j]
            strObj = Text(str).scale(.2)
            try:
                vigSquare.append(strObj.next_to(vigSquare[i-1], DOWN, buff=0))
            except:
                vigSquare.append(strObj.shift(3*UP))
            #print(str)
            groupVigSquare.add(vigSquare[i])
            #self.wait()
        self.play(Write(groupVigSquare))
        self.wait()

class Integral(Scene):
    def construct(self):
        integral = MathTex(r"\int_a^b f(x) dx")
        self.play(Write(integral))
        self.wait(2)