from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *
from goniometrie.config import GonioStyle as gs

class Zlomky_na_radiany(Slide):

    # pro vyreseni bugu, ze se neda video vyrenderovat
    max_duration_before_split_reverse = None
    
    def construct(self):
        k = Jednotkova_kruznice(PI/2)
        znakR = MathTex("1").move_to(k.osy.c2p(0.5, -0.1))
        self.add(
            k.kruznice, k.osy,
            k.AVBgrupa, znakR,
        )

        radiany = [PI/2, 3*PI/2, PI/3]
        radiany_tex = [r"\frac{\pi}{2}", r"\frac{3 \pi}{2}", r"\frac{\pi}{3}"]
        zlomky = [r"\frac{1}{4}", r"\frac{3}{4}", r"\frac{1}{6}"]

        for i in range(len(radiany)):
            self.play(k.velikost_uhlu.animate.set_value(radiany[i]), run_time=3, rate_func=smooth)
            self.wait(1)
            self.next_slide() 
            zlomek = MathTex(zlomky[i], color=gs.VYSEC_BARVA).move_to(k.misto_pro_text_vysec())
            self.play(FadeIn(k.vysec.update(), run_time=1))
            self.play(Write(zlomek))
            self.wait(1)
            self.next_slide()
            vypocet = MathTex(r"2 \pi \cdot " + zlomky[i] + "=" + radiany_tex[i]).move_to(k.misto_pro_pocitani)
            self.play(Write(vypocet))
            self.wait(1)
            self.next_slide()
            k.animuj_pohyb_po_kruznici(self, 0, radiany[i], run_time=2)
            delka_text = k.udelej_delka_text(radiany[i], radiany_tex[i])
            self.play(Write(delka_text))
            self.wait(1)
            self.next_slide()

            self.play(FadeOut(k.vysec), Unwrite(zlomek), Unwrite(vypocet), Unwrite(delka_text))
            k.odstran_pohyb_po_kruznici(self)
            self.wait(1)

