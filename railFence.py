from manim import *

class mainRailFence(Scene):
    def construct(self):
        #rf = RailFence("hello", 5)
        #self.play(rf, run_time=3)
        msg = "secretsgerbsblahblanndblankddd"
        pt1 = MarkupText(f'<gradient from="GREEN" to="BLUE"> pt: {msg} </gradient>', font="Courier New")
        tx = customText(msg).align_on_border(LEFT).align_on_border(UP)
        self.play(ReplacementTransform(pt1, tx))

        self.playRailAnimation(tx, 5, downSize = .25, colors=[RED,ORANGE, YELLOW,GREEN,BLUE, PURPLE])
        
        self.wait()

        #self.playRailAnimation(tx, 6, downSize = 0.5)
        #self.wait()
        # ct1 = MarkupText('<gradient from="RED" to="ORANGE">CT: STKOOESIDWCMNYSRIOKEKBN</gradient>', font="Courier New")
        # self.play(ReplacementTransform(tx, ct1)) 
        # self.wait()
        # self.remove(ct1)
        # self.wait()

        # msg = "stkooesidwcmnysriokekbn"
        # tx = customText(msg).align_on_border(LEFT).align_on_border(UP)
        # self.playRailAnimation(tx, 5, 3)
        # self.remove(tx)

        # msg = "secretsmikkinobodyknowsXX"
        # tx = customText(msg).align_on_border(LEFT).align_on_border(UP)
        # self.playRailAnimation(tx, 5, 3)
        # self.wait()
    
    def playRailAnimation(self, tx, rails, **kwargs):
        #tx = customText(msg).align_on_border(LEFT).align_on_border(UP)
        
        try:
            speed = kwargs["speed"]
        except:
            speed = 1
        
        try:
            downSize = kwargs["downSize"]
        except:
            downSize = 1


        encryptedList=[[]]
        for i in range(len(tx.textList)):
            #for 5 rails (01234321)(01234321)(01234321)(01...
            #tempNum     (01234567)(01234567)
            #subtractTerm(00000123)(00000123)
            tempNum = i%(2*(rails-1))
            downMod = tempNum + 2*np.floor(tempNum/(rails-1))*(rails-1-tempNum)
            txTemp = tx.copy()
            txTemp.textList[i].shift((downMod)*DOWN*downSize)

            self.play(Transform(tx, txTemp,  run_time=.2/speed))

            #adding the letters to the encrypted list
            try:
                encryptedList[int(downMod)].append(tx.textList[i])
            except:
                encryptedList.append([tx.textList[i]])

                self.add(tx)
        try:
            colors = kwargs["colors"]
            for i in range(len(encryptedList)):
                for j in range(len(encryptedList[i])):
                    uncoloredLett = encryptedList[i][j]
                    coloredLett = uncoloredLett.copy().set_color(colors[i])
                    self.play(Transform(uncoloredLett, coloredLett,  run_time=.1/speed))
        except:
            1
        
        collapsedEncryptedList = []
        for line in encryptedList:
            for lett in line:
                collapsedEncryptedList.append(lett)
        
        for i in range(1, len(collapsedEncryptedList)):
            prevLet = collapsedEncryptedList[i-1]
            oldLet = collapsedEncryptedList[i]
            newLet = oldLet.copy().next_to(prevLet, buff = .1).align_to(prevLet, DOWN)
            self.play(Transform(oldLet, newLet), run_time=.2/speed)




class customText(VGroup):
    def __init__(self, str, **kwargs):
        self.str = str
        super().__init__(**kwargs)
        charList = list(str)
        self.textList = []
        for i in range(len(charList)):
            if(i>0):
                self.textList.append(Text(charList[i], font="Courier New").next_to(self.textList[i-1], RIGHT, buff=0.05).align_to(self.textList[i-i], DOWN))
            else:
                self.textList.append(Text(charList[i], font="Courier New"))
        
        for i in self.textList:
            self.add(i)

class RailFence(Animation):
    def __init__(self, message, numRails, **kwargs) -> None:
        self.message = list(message)
        self.numRauls = numRails
        super().__init__(customText(message), **kwargs)
        
    def interpolate_mobject(self, alpha:float) -> None:
        self.mobject.add(Circle())
        for i in range(int(alpha*len(self.mobject.textList))):
            1
            #self.mobject.add(self.mobject.textList[i])
            #self.mobject.set_color(GREEN)
    