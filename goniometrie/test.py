from manim import *
from manim_slides import Slide
from goniometrie.jednotkova_kruznice import Jednotkova_kruznice

class Testik(Slide):
    def construct(self):
        k = Jednotkova_kruznice()
        self.play(FadeIn(k.kruznice), Create(k.bodB))
        self.play(k.velikost_uhlu.animate.set_value(30 * DEGREES))

        self.play(Create(k.bod_na_kruznici(90 * DEGREES)))
        

