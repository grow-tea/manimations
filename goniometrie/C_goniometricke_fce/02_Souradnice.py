from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *


  
class Souradnice(Slide):

    def construct(self):
        
        k = Jednotkova_kruznice(0.1 * DEGREES, osy_config = gs.OSY_CONFIG_CARKY)
        vsehogrupa = VGroup(k.useckaVA, k.useckaVB, k.souradnice_grupa, k.sin_stupne, k.cos_stupne) 
        self.add(k.kruznice, k.osy, k.bodB, vsehogrupa)
        
        # rozsah 0-360
        self.play(k.velikost_uhlu.animate.set_value(2 *PI), run_time=7, rate_func=linear)
        self.wait(1)
        self.next_slide()

        # rozsah 360-720
        self.play(k.velikost_uhlu.animate.set_value(4*PI), run_time=7, rate_func=linear)
        self.wait(1)
        self.next_slide()

        self.play(FadeOut(vsehogrupa))
        k.velikost_uhlu.set_value(30*DEGREES)
        self.wait(1)
        self.play(FadeIn(vsehogrupa.update()))
        self.wait(2)
        self.next_slide()
        self.play(k.velikost_uhlu.animate.set_value(-2*PI), run_time=7, rate_func=linear)

        self.wait(1)


