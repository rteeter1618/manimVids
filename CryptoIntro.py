from manim import *

class CryptoIntro(Scene):
    def construct(self):
        register_font("roboto_mono")
        #Cryptography, Cryptanalysis, 
        definitionsText = Text("Definitions").to_edge(UP, buff=1)
        smallSize = .65

        cryptography = MarkupText('<gradient from="GREEN" to="BLUE"> Cryptography = code making </gradient>')
        cryptography.scale(smallSize)
        cryptography.move_to(Point([-3,1,0]))

        cryptanalysis = MarkupText('<gradient from="RED" to="ORANGE"> Cryptanalysis = code breaking </gradient>').scale(smallSize)
        cryptanalysis.next_to(cryptography, RIGHT)

        cryptology = Text("Cryptology = both!")

        #pt and CT example
        medSize = .6
        pt = Text("pt: ", font="Courier New")
        plaintextDef = MarkupText('<gradient from="GREEN" to="BLUE">this is a secret message nobody should read</gradient>', font="Courier New")
        plaintextDef.next_to(pt, RIGHT)
        plaintext = Group(pt, plaintextDef)
        plaintext.scale(medSize).to_edge(LEFT)
        
        ct = Text("CT: ", font="Courier New")
        ciphertextDef = MarkupText('<gradient from="RED" to="ORANGE">TI SASCE ESG OOYSOL EDHSI  ERTMSAENBD HUDRA</gradient>', font="Courier New")
        ciphertextDef.next_to(ct, RIGHT)
        ciphertext = Group(ct, ciphertextDef).scale(medSize).next_to(plaintext, DOWN)

        #without spaces
        plaintextDefNoSpace = MarkupText('<gradient from="GREEN" to="BLUE">thisisasecretmessagenobodyshouldread</gradient>', font="Courier New")
        plaintextDefNoSpace.scale(medSize).next_to(pt, RIGHT)
        ciphertextDefNoSpace = MarkupText('<gradient from="RED" to="ORANGE">TISASCEESGOOYSOLEDHSIERTMSAENBDHUDRA</gradient>', font="Courier New")
        ciphertextDefNoSpace.scale(medSize).next_to(ct, RIGHT)

        self.wait()
        self.play(Write(definitionsText, run_time=1))
        self.wait()
        self.play(Write(cryptography, run_time=1))
        self.play(Write(cryptanalysis, run_time=1))
        self.play(Write(cryptology, run_time=1))
        self.wait()
        self.play(Unwrite(cryptology), run_time=1)
        self.wait()
        self.play(ReplacementTransform(Group(cryptography), plaintext),
                  ReplacementTransform(Group(cryptanalysis), ciphertext))
        self.wait()
        self.play(ReplacementTransform(plaintextDef, plaintextDefNoSpace),
                  ReplacementTransform(ciphertextDef, ciphertextDefNoSpace))
        self.wait()



        titleText = Text("Caeser Cipher").align_on_border(UP)
        alphabetList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
