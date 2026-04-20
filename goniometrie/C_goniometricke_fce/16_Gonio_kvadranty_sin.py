from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *

from Gonio_kvadranty import *
  
class Gonio_kvadranty_sin(GonioKvadranty):

    # pro vyreseni bugu, ze se neda video vyrenderovat
    max_duration_before_split_reverse = None

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
        self.next_slide()
        self.play(Write(sin_texts[0]), Create(self.k.sin_grupa))
        self.wait(1)
        self.next_slide()

        for i in range(0,3+1):
            self.play_posun(i)
            self.play(TransformMatchingShapes(sin_texts[i], sin_texts_alt[i+1].next_to(self.k.usecka_na_ose_y.get_center(), LEFT - 0.2*UP)))
            self.wait(1)
            self.play(TransformMatchingShapes(sin_texts_alt[i+1], sin_texts[i+1].next_to(self.k.usecka_na_ose_y.get_center(), LEFT - 0.2*UP)))
            self.wait(1)
            self.next_slide()


