from manim import *

class mainRailFence(Scene):
    def construct(self):
        #rf = RailFence("hello", 5)
        #self.play(rf, run_time=3)
        msg = "secretsericgerbers"
        pt1 = MarkupText(f'<gradient from="GREEN" to="BLUE"> pt: {msg} </gradient>', font="Courier New")
        tx = customText(msg).align_on_border(LEFT).align_on_border(UP)
        self.play(ReplacementTransform(pt1, tx))

        self.playRailAnimation(tx, 3, colors=[RED,GREEN,BLUE])
        
        self.wait()

        self.playRailAnimation(tx, 6, downSize = 0.5)
        self.wait()
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
            
        self.add(tx)
        for i in range(len(tx.textList)):
            #downMod = i%rails for scytale (01234)(01234)...

            #for 5 rails (01234321)(01234321)(01234321)(01...
            #tempNum     (01234567)(01234567)
            #subtractTerm(00000123)(00000123)
            tempNum = i%(2*(rails-1))
            downMod = tempNum - np.floor(tempNum/rails)*(tempNum+1-rails)
            txTemp = tx.copy()
            try:
                txTemp.textList[i].shift((i%rails)*DOWN*downSize).set_color(kwargs["colors"][i%rails])
            except:
                txTemp.textList[i].shift((i%rails)*DOWN*downSize)
            self.play(Transform(tx, txTemp,  run_time=.2/speed))
        
        for i in range(0, rails):
            if(i>0):
                txTemp = tx.copy()
                for idx in reversed(range(len(txTemp.textList))):
                    if(idx%rails == i-1):
                        break
                txTemp.textList[i].next_to(txTemp.textList[idx], buff=.05).align_to(txTemp.textList[idx], DOWN)
                self.play(Transform(tx, txTemp), run_time=.2/speed)
            for j in range(rails, len(tx.textList)):
                if(j%rails==i):
                    txTemp = tx.copy()
                    txTemp.textList[j].next_to(txTemp.textList[j-rails], buff=.05).align_to(txTemp.textList[j-rails], DOWN)
                    self.play(Transform(tx, txTemp), run_time=.2/speed)
        
        textListTemp=[]
        for railNum in range(rails):
            for j in range(0, len(tx.textList)):
                if(j%rails==railNum):
                    textListTemp.append(tx.textList[j])
        tx.textList=textListTemp




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
    