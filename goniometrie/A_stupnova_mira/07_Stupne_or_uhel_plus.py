from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *


class Stupne_or_uhel(Slide):

    # pro vyreseni bugu, ze se neda video vyrenderovat
    max_duration_before_split_reverse = None
    
    zastavky = []

    def construct(self):

        k = Jednotkova_kruznice(60*DEGREES)
        k.misto_pro_pocitani += LEFT * 0.7
        or_uhel_popis = always_redraw(lambda: Integer(k.get_stupne(), unit=r"^{\circ}", group_with_commas=False).move_to(k.misto_pro_pocitani))
        pocet_tristasedesatek = MathTex("")

        self.add(
            k.kruznice, k.osy,
            k.AVBgrupa,
            k.text_stupne,
            or_uhel_popis.update()
        )

        self.play(Write(k.uhel_symbol), Write(k.text_stupne))
        self.next_slide()

        for s in self.zastavky:
            self.play(k.velikost_uhlu.animate.set_value(s * DEGREES), run_time=4, rate_func=smooth)
            self.wait(1)
            self.next_slide()
            pocet_tristasedesatek = MathTex("= " + str(s//360) + " \cdot 360^{\circ} + 60^{\circ}").next_to(k.misto_pro_pocitani, DOWN, aligned_edge=LEFT)
            self.play(Write(pocet_tristasedesatek))
            self.next_slide()
            self.play(FadeOut(pocet_tristasedesatek))

class Stupne_or_uhel_plus(Stupne_or_uhel):
    zastavky = [420, 780, 1500]

class Stupne_or_uhel_minus(Stupne_or_uhel):
    zastavky = [-300, -660, -1380]


