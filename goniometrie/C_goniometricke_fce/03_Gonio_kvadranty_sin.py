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
            self.body.append(Dot(self.k.misto_na_kruznici(self.ctverice_uhlu[i])))

        self.add(self.k.kruznice, self.k.osy, self.k.kruznicovy_oblouk_AB, self.k.souradnice_grupa)
        self.add(self.body[0]) 
        self.add(self.k.usecka_na_ose_x, self.k.usecka_na_ose_y)

        self.delka_text = self.k.udelej_delka_text(self.ctverice_uhlu[0], self.ctverice_uhlu_text[0])

    # nepouzito
    def vytyc_body(self):
        for i in range(1,4):
            draha = DashedLine(self.body[0], self.body[i])
            self.play(Write(draha))
            self.wait(1)
            self.play(FadeIn(self.body[i]))
            self.play(Flash(self.body[i]))
            self.play(Uncreate(draha))
    
    # nepouzito
    def vytyc_pomocne_usecky(self):
        for i in range(0,4):
            self.play(Write(Line(
                self.body[i], self.body[(i+1)%4],
                color=GRAY
            )))

    def pridej_obdelnik(self): 

        self.play(Write(self.delka_text))
        self.wait(1)

        for i in range(0,4):
            self.play(Write(self.body[i]))

            self.play(Write(Line(
                self.body[i], self.body[(i+1)%4],
                color=GRAY
            )))
            
    def play_posun(self, i):
        self.play(
            self.k.velikost_uhlu.animate.set_value(self.ctverice_uhlu[i+1]),
            CounterclockwiseTransform(self.delka_text,self.k.udelej_delka_text(self.ctverice_uhlu[i+1], self.ctverice_uhlu_text[i+1])),
            run_time=2)
        self.wait(1)
        self.next_slide()

class Gonio_kvadranty_sin(GonioKvadranty):
    def construct(self):
        
        ### inicializace promennych pro sinus
        sin_texts = []
        sin_texts_alt = [True, True, False, False, True]
        for i in range(0,4+1):
            sin_texts.append( MathTex(
                r"\sin("+ self.ctverice_uhlu_text[i] + ")", **gs.SIN_TEXT,
                ).next_to(self.k.usecka_na_ose_y.get_center(), LEFT - 0.2*UP))
            
            sin_texts_alt[i] = MathTex(
                ("" if sin_texts_alt[i] else "-") +
                r"\sin("+ self.ctverice_uhlu_text[0] + ")", **gs.SIN_TEXT,
                )
            
        self.pridej_obdelnik()

        self.play(Write(sin_texts[0]))
        self.wait(1)
        self.next_slide()

        for i in range(0,3+1):
            self.play_posun(i)
            self.play(TransformMatchingShapes(sin_texts[i], sin_texts_alt[i+1].next_to(self.k.usecka_na_ose_y.get_center(), LEFT - 0.2*UP)))
            self.wait(1)
            self.play(TransformMatchingShapes(sin_texts_alt[i+1], sin_texts[i+1].next_to(self.k.usecka_na_ose_y.get_center(), LEFT - 0.2*UP)))
            self.wait(1)
            self.next_slide()


