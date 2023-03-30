from manim import *

class Logo(Scene):

    def construct(self):

        self.r2 = ValueTracker(.4)
        
        bigCircle = Circle(fill_opacity = 1).scale(2.08)
        bigCircle.set_color('#3333FF')
        bigCircle.stroke_color = '#3333CC'
        bigCircle.stroke_width = 12
        self.play(GrowFromPoint(bigCircle, bigCircle.get_center()))
        startLittleCircle = Circle(fill_opacity = 1).shift(1.4*RIGHT).scale(.2)
        startLittleCircle.set_color('#FF6600')
        startLittleCircle.stroke_color = '#CC5200'
        startLittleCircle.stroke_width = 6
        self.play(GrowFromPoint(startLittleCircle, startLittleCircle.get_center()))
        #self.play(ReplacementTransform(startLittleCircle, startLittleCircle.copy().rotate_about_origin(TAU/12), run_time=2/12, rate_func=linear))
        tracker = ValueTracker(0.0)
        circles = VGroup()
        self.add(circles)
        self.remove(startLittleCircle)
        for i in range(0,6):
            circleTemp = always_redraw(self.circleFuncFactory(i, tracker))
            circles.add(circleTemp)
        self.play(tracker.animate.set_value(1), run_time = 1.5)

        '''
        #making the circles and 
        bigCircle = Circle(fill_opacity = 1).scale(2.08)
        #bigCircle.set_color('#4900DB')
        bigCircle.set_color('#3333FF')
        bigCircle.stroke_color = '#3333CC'
        bigCircle.stroke_width = 12
        self.add(bigCircle)
        startLittleCircle = Circle(fill_opacity = 1).shift(0*UP).shift(1.4*RIGHT).scale(.2)
        startLittleCircle.set_color('#FF6600')
        startLittleCircle.stroke_color = '#CC5200'
        startLittleCircle.stroke_width = 6
        self.play(GrowFromPoint(startLittleCircle, startLittleCircle.get_center()))
        circlesGroup = VGroup()
        circlesGroup.add(startLittleCircle)
        circles = []
        startLittleCircle.rotate_about_origin(-TAU/(12*5))
        for i in range(0,6):
            newCircleGroup = VGroup()
            newCircleGroup.add(startLittleCircle.copy().rotate_about_origin(TAU/(12*5)))
            for j in range(0,i):
                newCircleGroup.add(circles[j].copy().rotate_about_origin(TAU/6))
            self.play(Transform(circlesGroup, newCircleGroup), run_time = .2, rate_func = linear)
            theta=i*TAU/(12*5)
            x=np.cos(theta)*1.4
            y=np.sin(theta)*1.4
            circleTemp = Circle(fill_opacity = 1).shift(y*UP).shift(x*RIGHT).scale(.2)
            circleTemp.set_color('#FF6600')
            circleTemp.stroke_color = '#CC5200'
            circleTemp.stroke_width = 6
            circles.append(circleTemp)
            circlesGroup.add(circleTemp)
        '''

        
        #self.wait()
        e = ValueTracker(0.01)
        
        graph1 = always_redraw(lambda : ParametricFunction(self.func, t_range = np.array([0, e.get_value()]), fill_opacity=0).set_color('#6BFF81'))
        dot1 = always_redraw(lambda : Dot(fill_color = WHITE).scale(.5).move_to(graph1.get_end()))
        self.add(graph1, dot1)
        mathSpirals = MarkupText('<gradient from="BLUE" to="RED">Math Spirals</gradient>').shift(3.2*DOWN)
        self.play(e.animate.set_value(2*PI), 
                  Write(mathSpirals),
                  run_time=2.5)
        self.remove(dot1)

        #e2 = ValueTracker(.4)
        graph2 = always_redraw(lambda : ParametricFunction(self.func, t_range = np.array([0, 2*PI]), fill_opacity=0).set_color('#6BFF81'))

        self.add(graph2)
        self.play(self.r2.animate.set_value(5),
                  ReplacementTransform(bigCircle, Circle().scale(10).set_opacity(0)),
                  ReplacementTransform(circles, Circle().scale(10).set_opacity(0)),
                  ReplacementTransform(mathSpirals, Circle().scale(5).shift(9.5*DOWN).set_opacity(0)),
                   run_time=4)

        # d1 = Dot()
        # func2 = VMobject()
        #func2.add_updater(lambda x: x.become(ParametricFunction(self.func, t_range = np.array([0, 2*PI]), fill_opacity=0)))
        #self.play(MoveAlongPath(d1, func1), run_time=3)

        #just the logo
        '''
        bigCircle = Circle(fill_opacity = 1).scale(2.08)
        #bigCircle.set_color('#4900DB')
        bigCircle.set_color('#3333FF')
        bigCircle.stroke_color = '#3333CC'
        bigCircle.stroke_width = 12
        circles = VGroup()
        for i in range(0,6):
            theta=TAU/6*i+TAU/12
            x=np.cos(theta)*1.4
            y=np.sin(theta)*1.4
            circleTemp = Circle(fill_opacity = 1).shift(y*UP).shift(x*RIGHT).scale(.2)
            #circleTemp.set_color('#FF844B')
            circleTemp.set_color('#FF6600')
            circleTemp.stroke_color = '#CC5200'
            circleTemp.stroke_width = 6
            circles.add(circleTemp)
        staticLogoGraph = ParametricFunction(self.func, t_range = np.array([0, 2*PI]), fill_opacity = 0)
        staticLogoGraph.stroke_width = 5
        staticLogoGraph.set_color('#6BFF81')

        self.add(bigCircle, circles)
        self.add(staticLogoGraph)
        '''
    
    def circleFuncFactory(self, i, tracker):
        def f():
            circ = Circle(fill_opacity = 1).shift(np.sin(tracker.get_value()*(i*(TAU/6)+TAU/(12)))*1.4*UP,
                                                  np.cos(tracker.get_value()*(i*(TAU/6)+TAU/(12)))*1.4*RIGHT).scale(.2)
            circ.set_color('#FF6600')
            circ.stroke_color = '#CC5200'
            circ.stroke_width = 6
            return circ
        
        return f

    def weirdFunc(self, t):
        return ParametricFunction(self.func, t_range = np.array([0, 2*PI]), fill_opacity=0).set_color('#6BFF81')

    def func(self, t):
        r2 = self.r2.get_value()
        r1 = 1
        w1 = 1
        w2 = 7
        p = 3.2
        k = 7.6
        x = r1*np.cos(w1*t)+r2*np.cos(w2*t)
        y = r1*np.sin(w1*t)+r2*np.sin(w2*t)
        dist = np.sqrt(x**2+y**2)
        modifier = (dist**8 + 50)/30
        # modifier = 1.8
        return np.array((modifier*x, modifier*y, 0))