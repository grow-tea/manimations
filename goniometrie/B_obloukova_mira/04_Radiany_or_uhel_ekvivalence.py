from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *


class Radiany_or_uhel_ekvivalence(Slide):
     
    # pro vyreseni bugu, ze se neda video vyrenderovat
    max_duration_before_split_reverse = None

    def construct(self):    
        
        cil_rad = - PI/4
        minus_cil_rad = -cil_rad
        minus_cil_rad_tex = r"\frac{\pi}{4}"
        radiany = [7/4*PI, -1/4*PI]
        radiany_tex = [r"\frac{7 \pi}{4}", r"\frac{- \pi}{4}"]
        radiany_tex_rozeps = [
            r"\frac{7 \pi}{4}",
            r"\frac{- \pi}{4}",
        ]

        k = Jednotkova_kruznice(0)
        self.add(
            k.kruznice, k.osy,
            k.bodA, k.bodB, k.bodV,
            k.kruznicovy_oblouk_AB,
        )

        self.play(k.velikost_uhlu.animate.set_value(minus_cil_rad), run_time=3, rate_func=smooth)
        text =k.udelej_delka_text(minus_cil_rad, minus_cil_rad_tex)
        self.next_slide()
        self.play(Write(text))
        self.wait(1)
        self.next_slide()
        usecka = DashedLine(k.misto_na_kruznici(minus_cil_rad), k.misto_na_kruznici(cil_rad))
        self.play(Create(usecka))
        self.play(Unwrite(text))
        self.play(k.velikost_uhlu.animate.set_value(cil_rad), run_time=3)
        self.wait(1)
        self.play(Flash(k.bodB))
        self.play(Uncreate(usecka), Uncreate(k.kruznicovy_oblouk_AB))
        self.wait(1)
        self.next_slide()
        


        for i in range(len(radiany)):
            k.animuj_pohyb_po_kruznici(self, 0, radiany[i], run_time=3)
            delka_text = k.udelej_delka_text(radiany[i], radiany_tex_rozeps[i])
            self.play(Write(delka_text))
            self.wait(1)
            self.next_slide()
            self.play(Transform(delka_text, k.udelej_delka_text(radiany[i], radiany_tex[i])))
            self.play(delka_text.copy().animate.move_to(k.osy.c2p(-1.9 + i*0.5, -1.2)))
            k.odstran_pohyb_po_kruznici(self)
            self.play(FadeOut(delka_text))
            self.wait(1)
            self.next_slide()