from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *

class Zlomky_na_radiany(Slide):

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
            zlomek = MathTex(zlomky[i], color=VYSEC_BARVA).move_to(k.misto_pro_text_vysec())
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


class Radiany_na_stupne(Slide):

    def construct(self):
        k = Jednotkova_kruznice(0)
        self.add(
            k.kruznice, k.osy,
            k.bodA, k.bodB, k.bodV,
            k.kruznicovy_oblouk_AB
        )
        grupa_ke_stupnum = VGroup(k.poloprVA, k.poloprVB, k.znakA, k.znakV, k.znakB, k.uhel_symbol)
        radiany = [3*PI/4, 2*PI/3, 5*PI/3]
        radiany_tex = [r"\frac{3 \pi}{4}", r"\frac{2 \pi}{3}", r"\frac{5 \pi}{3}"]
        zlomky = [r"\frac{3}{8}", r"\frac{1}{3}", r"\frac{5}{6}"]

        for i in range(len(radiany)):
            self.play(k.velikost_uhlu.animate.set_value(radiany[i]), run_time=3, rate_func=smooth)
            self.wait(1)
            self.next_slide()
            delka_text = k.udelej_delka_text(radiany[i], radiany_tex[i])
            self.play(Write(delka_text))
            self.wait(1)
            self.next_slide()
            grupa_ke_stupnum.update()
            self.play(FadeIn(grupa_ke_stupnum))
            self.play(FadeIn(k.vysec.update()))
            self.wait(1)
            self.next_slide()
            vypocet = MathTex(r"\frac{" + radiany_tex[i] + "}{2 \pi} = " + zlomky[i]).move_to(k.misto_pro_pocitani)
            zlomek = MathTex(zlomky[i], color=VYSEC_BARVA).move_to(k.misto_pro_text_vysec())
            self.play(Write(vypocet))
            self.play(Write(zlomek))
            self.wait(1)
            self.next_slide()

            vypocet2 = MathTex(zlomky[i] + r"\cdot 360^{\circ} =" + str(k.get_stupne()) + r"^{\circ}").next_to(vypocet, DOWN, aligned_edge=LEFT)
            self.play(Write(vypocet2))
            self.wait(1)
            self.play(Write(k.text_stupne.update()))

            self.next_slide()

            self.play(FadeOut(k.vysec), Unwrite(zlomek), Unwrite(vypocet), Unwrite(vypocet2), Unwrite(delka_text), FadeOut(grupa_ke_stupnum), Unwrite(k.text_stupne))
            self.wait(1)
