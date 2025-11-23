from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *

class Zlomky_na_stupne(Slide):

    def construct(self):
        k = Jednotkova_kruznice(90*DEGREES)
        self.add(
            k.kruznice, k.osy,
            k.AVBgrupa,
        )

        stupne_a_zlomky = {
            90: r"\frac{1}{4}",
            270: r"\frac{3}{4}",
            60: r"\frac{1}{6}"
        }

        for s in stupne_a_zlomky.keys():
            self.play(k.velikost_uhlu.animate.set_value(s * DEGREES), run_time=3, rate_func=smooth)
            self.wait(1)
            self.next_slide()
            zlomek = MathTex(stupne_a_zlomky[s], color=VYSEC_BARVA).move_to(k.misto_pro_text_vysec())
            self.play(FadeIn(k.vysec.update(), run_time=1))
            self.next_slide()
            self.play(Write(zlomek))
            self.next_slide()
            vypocet = MathTex(r"360^{\circ} \cdot " + stupne_a_zlomky[s] + "=" + str(s) + r"^{\circ}").move_to(k.misto_pro_pocitani)
            self.play(Write(vypocet))
            self.next_slide()
            self.play(Write(k.text_stupne.update()))
            self.wait(1)
            self.next_slide()

            self.play(FadeOut(k.vysec), Unwrite(zlomek), Unwrite(vypocet), Unwrite(k.text_stupne))
            self.wait(1)


class Stupne_na_zlomky(Slide):

    def construct(self):
        k = Jednotkova_kruznice(90*DEGREES)
        self.add(
            k.kruznice, k.osy,
            k.AVBgrupa,
            k.text_stupne.update()
        )

        stupne_a_zlomky = {
            45: r"\frac{1}{8}",
            120: r"\frac{1}{3}",
            300: r"\frac{5}{6}",
        }

        for s in stupne_a_zlomky.keys():
            self.play(k.velikost_uhlu.animate.set_value(s * DEGREES), run_time=3, rate_func=smooth)
            self.wait(1)
            zlomek = MathTex(stupne_a_zlomky[s], color=VYSEC_BARVA).move_to(k.misto_pro_text_vysec())
            self.play(FadeIn(k.vysec.update()))
            self.wait(1)
            self.next_slide()
            vypocet = MathTex(r"\frac{" + str(s) + "^{\circ}}{360^{\circ}} = " + stupne_a_zlomky[s]).move_to(k.misto_pro_pocitani)
            self.play(Write(vypocet))
            self.play(Write(zlomek))
            self.wait(1)
            self.next_slide()

            self.play(FadeOut(k.vysec), Unwrite(zlomek), Unwrite(vypocet))
            self.wait(1)
