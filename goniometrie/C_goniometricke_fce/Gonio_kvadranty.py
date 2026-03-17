from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *


  
class GonioKvadranty(Slide):
    def setup(self):
        self.ctverice_uhlu = [PI/5, 4*PI/5, 6/5*PI, 9/5*PI, 11/5*PI]
        self.ctverice_uhlu_text = [r"\tfrac{\pi}{5}", r"\tfrac{4}{5}\pi", r"\tfrac{7}{5}\pi", r"\tfrac{9}{5}\pi", r"\tfrac{11}{5}\pi"]
        
        self.k = Jednotkova_kruznice(self.ctverice_uhlu[0])
        self.body = []
        for i in range(0,4):
            self.body.append(Dot(self.k.misto_na_kruznici(self.ctverice_uhlu[i]), **gs.BOD_HADEJ))

        self.add(self.k.kruznice, self.k.osy, self.k.kruznicovy_oblouk_AB, self.k.bodV, self.k.bodA, self.k.bodB)
        self.add(self.body[0]) 

        self.delka_text = self.k.udelej_delka_text(self.ctverice_uhlu[0], self.ctverice_uhlu_text[0])
    
    def pridej_obdelnik(self): 

        self.play(Write(self.delka_text))
        self.wait(1)

        for i in range(0,4):
            self.play(Write(self.body[i]))

            self.play(Write(Line(
                self.body[i], self.body[(i+1)%4],
                **gs.OBRAZ
            )))
            
    def play_posun(self, i):
        self.play(
            self.k.velikost_uhlu.animate.set_value(self.ctverice_uhlu[i+1]),
            CounterclockwiseTransform(self.delka_text,self.k.udelej_delka_text(self.ctverice_uhlu[i+1], self.ctverice_uhlu_text[i+1])),
            run_time=2)
        self.wait(1)
        self.next_slide()