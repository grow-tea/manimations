from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *


class Radiany_or_uhel_ekvivalence(Slide):
    def construct(self):
        
        k = Jednotkova_kruznice(cil_rad)
        self.add(
            k.kruznice, k.osy,
            k.bodA, k.bodB, k.bodV,
            k.kruznicovy_oblouk_AB,
            k.get_text_radiany(cil_rad_tex)
        )
        
        cil_rad = 7/6*PI
        cil_rad_tex = r"\frac{7 \pi}{6}"
        radiany = [7/6*PI, 7/6*PI + 2*PI, 7/6*PI - 2*PI, 7/6*PI + 4*PI]
        radiany_tex = [r"\frac{7 \pi}{6}", r"\frac{19 \pi}{6}", r"-\frac{5 \pi}{6}", r"\frac{31 \pi}{6}"]
        radiany_tex_rozeps = [
            r"\frac{7 \pi}{6}",
            r"\frac{7 \pi}{6} + 2 \pi",
            r"\frac{7 \pi}{6} - 2 \pi",
            r"\frac{7 \pi}{6} + 4 \pi"
        ]

        for i in range(len(radiany)):
            k.animuj_pohyb_po_kruznici(self, 0, radiany[i], run_time=3)
            delka_text = k.udelej_delka_text(radiany[i], radiany_tex_rozeps[i])
            self.play(Write(delka_text))
            self.wait(1)
            self.next_slide()
            self.play(Transform(delka_text, k.udelej_delka_text(radiany[i], radiany_tex[i])))
            self.play(delka_text.copy().animate.move_to(k.osy.c2p(0.3 + i*0.5, -1.2)))
            k.odstran_pohyb_po_kruznici(self)
            self.play(FadeOut(delka_text))
            self.wait(1)
            self.next_slide()