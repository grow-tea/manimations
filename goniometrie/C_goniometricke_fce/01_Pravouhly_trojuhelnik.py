from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *


class Pravouhly_trojuhelnik(Slide):

    # pro vyreseni bugu, ze se neda video vyrenderovat
    max_duration_before_split_reverse = None
    
    def construct(self):
        k = Jednotkova_kruznice(90*DEGREES, posun=UL, zmena_velikosti=1.5)
        bodC = always_redraw(lambda: Dot(
            k.osy.c2p(np.cos(k.velikost_uhlu.get_value()), 0)
        ))

        uhly = [60,30,45]
        muj_uhel_symbol = always_redraw (lambda: Angle(
            k.useckaVA, k.useckaVB,
            **gs.UHEL_SYMBOL
        ))
        
        muj_text_stupne = always_redraw(lambda: Integer(
            k.get_stupne_norm(), unit=r"^{\circ}")
            .next_to(muj_uhel_symbol)) 

        self.add(k.kruznice, k.osy, k.useckaVA, k.useckaVB)

        self.play(FadeIn(k.bodB), FadeIn(k.bodV), FadeIn(bodC), Write(muj_uhel_symbol))

        for i in range(len(uhly)):
            self.play(k.velikost_uhlu.animate.set_value(uhly[i]*DEGREES))
            self.wait(1)
            trojuhelnik = Polygon(
                k.bodB.update().get_center(), k.bodV.get_center(), bodC.update().get_center(),
                stroke_color = WHITE,
                fill_color = WHITE,
                fill_opacity = 0.3
            )

            self.wait(1)
            self.play(Create(trojuhelnik), Write(muj_text_stupne.update()))
            self.wait(2)
            self.play(FadeOut(trojuhelnik), Unwrite(muj_text_stupne))

  