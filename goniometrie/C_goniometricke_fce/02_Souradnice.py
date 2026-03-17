from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *


  
class Souradnice(Slide):

    # pro vyreseni bugu, ze se neda video vyrenderovat
    max_duration_before_split_reverse = None

    def construct(self):
        
        k = Jednotkova_kruznice(PI/3, osy_config = gs.OSY_CONFIG_CARKY)
        uhel_symbol = always_redraw(lambda: Angle(k.useckaVA, k.useckaVB, **gs.UHEL_SYMBOL))    # puvodni definovany pro poloprimky
        vsehogrupa = VGroup(k.useckaVA, k.useckaVB, k.sin_grupa, k.cos_grupa, k.sin_stupne, k.cos_stupne, uhel_symbol)
        self.add(k.kruznice, k.osy, k.bodA, k.bodV, k.bodB, vsehogrupa)
        self.play(k.velikost_uhlu.animate.set_value(0.1*DEGREES), run_time=2)
        self.wait(1)
        self.next_slide()

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


