from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *

class Jednotkove_delky_na_kruznici(Slide):

    def construct(self):
        
        k = Jednotkova_kruznice(0)
        delka_text = k.udelej_delka_text(1, "1")
        polomer = Line(k.osy.c2p(1,0),k.osy.c2p(0,0), color=RED)
        znakR = MathTex("1").move_to(k.osy.c2p(0.5, -0.1))

        self.add(
            k.bodA, k.bodV, k.kruznice, k.znakA
        )
        self.play(Create(polomer), Create(znakR))
        self.next_slide()

        body = []
        oblouky = []
        for i in range(0,6+1):
            body.append(k.bod_na_kruznici(i))
            oblouky.append(k.udelej_kruznicovy_oblouk(i,i+1))

        self.next_slide()
        self.play(TransformFromCopy(polomer, oblouky[0]),run_time=2)
        self.play(Create(body[1]), Create(delka_text))
        self.next_slide()

        for i in range(1,5+1):
            self.play(TransformFromCopy(oblouky[i-1], oblouky[i], run_time=1.5))
            self.play(Create(body[i+1]))
            self.play(Transform(delka_text, k.udelej_delka_text(i+1, str(i+1))))
            self.next_slide()

        self.wait(1)
        self.play(*[Unwrite(mob) for mob in body[:6]], *[Unwrite(mob) for mob in oblouky])
        k.animuj_pohyb_po_kruznici(self, 0, 2*PI, run_time=4)
        self.play(Write(k.udelej_delka_text(2*PI, r"2 \pi")))
        self.wait(1)
