from manim import*

class logo(Scene):
    def construct(self):
        
        self.r2 = .4
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

        self.add(bigCircle.shift(.8*UP), circles.shift(.8*UP))
        self.add(staticLogoGraph.shift(.8*UP))
        self.add(MarkupText('<gradient from="BLUE" to="RED">Math Spirals</gradient>').shift(3.2*DOWN))
    
    def func(self, t):
        r2 = self.r2
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