from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *

from Gonio_kvadranty import *  

class Gonio_kvadranty_cos(GonioKvadranty):
 
    # pro vyreseni bugu, ze se neda video vyrenderovat
    max_duration_before_split_reverse = None
    
    def construct(self):
        
        ### inicializace promennych pro kosinus
        cos_texts = []
        cos_texts_alt = [True, False, False, True, True]
        for i in range(0,4+1):
            cos_texts.append( MathTex(
                r"\cos("+ self.ctverice_uhlu_text[i] + ")", **gs.COS_TEXT,
                ).next_to(self.k.usecka_na_ose_x.get_center(), DOWN))
        
            cos_texts_alt[i] = MathTex(
                ("" if cos_texts_alt[i] else "-") +
                r"\cos("+ self.ctverice_uhlu_text[0] + ")", **gs.COS_TEXT,
                )

        self.pridej_obdelnik()
        self.next_slide()
        self.play(Write(cos_texts[0]), Create(self.k.cos_grupa))
        self.wait(1)
        self.next_slide()

        for i in range(0,3+1):
            self.play_posun(i)
            self.play(TransformMatchingShapes(cos_texts[i], cos_texts_alt[i+1].next_to(self.k.usecka_na_ose_x.get_center(), DOWN)))
            self.wait(1)
            self.play(TransformMatchingShapes(cos_texts_alt[i+1], cos_texts[i+1].next_to(self.k.usecka_na_ose_x.get_center(), DOWN)))
            self.wait(1)
            self.next_slide()
