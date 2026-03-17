from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *

from Grafy import *

class Cosinus(Slide):
    
    # pro vyreseni bugu, ze se neda video vyrenderovat
    max_duration_before_split_reverse = None

    def construct(self):
        
        g = Grafy("COS")
        zachytne = [ 0.1*DEGREES, PI/2, PI, PI*3/2, 2*PI, PI/4]
        zachytne_fast = [PI/6, PI/3, 3*PI/4, 5*PI/4, 7*PI/4]

        self.add(g.kruznice_grupa, g.k.cos_grupa, g.graf_grupa)

        for uhel in zachytne:
            self.play(g.k.velikost_uhlu.animate.set_value(uhel), run_time=3)
            self.play(FadeIn(g.svislice.update()))
            self.wait(1)
            self.next_slide()
            self.play(FadeIn(g.bod_kosinusoida.update()))
            self.play(Write(g.pomocna_usecka.update()))
            self.add(g.bod_kosinusoida.copy())
            self.wait(1)
            self.next_slide()
            self.play(Unwrite(g.bod_kosinusoida), Unwrite(g.pomocna_usecka), FadeOut(g.svislice))
            self.wait(1)

        self.next_slide()
        for uhel in zachytne_fast:
            self.play(FadeIn(Dot(g.osy_grafu.c2p(uhel, np.cos(uhel)), **gs.COS_BOD)))        
        self.wait(1)
        self.next_slide()
        
        
        self.play(g.k.velikost_uhlu.animate.set_value(0.1*DEGREES), run_time=3)
        self.add(g.bod_kosinusoida.update(), g.pomocna_usecka.update(), g.kosinusoida_krivka)
        self.play(g.k.velikost_uhlu.animate.set_value(2*PI), run_time=5, rate_func=linear)
        self.wait(1)
