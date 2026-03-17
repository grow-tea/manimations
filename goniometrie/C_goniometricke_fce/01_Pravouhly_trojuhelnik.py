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
            k.osy.c2p(np.cos(k.velikost_uhlu.get_value()), 0),
            **gs.BOD_STATIC
        ))

        uhly = [60,30,45]
        zapisy_sin = []
        zapisy_cos = []
        for u in uhly:
            zapisy_sin.append(r"\sin(" + str(u) + "^{\circ})")
            zapisy_cos.append(r"\cos(" + str(u) + "^{\circ})")
        hodnoty_sin = [r"\frac{\sqrt{3}}{2}", r"\frac{1}{2}", r"\frac{\sqrt{2}}{2}"]
        hodnoty_cos = [r"\frac{1}{2}", r"\frac{\sqrt{3}}{2}", r"\frac{\sqrt{2}}{2}"]


        # je treba vytvorit nove uhel_symbol a text_stupne, aby fungovalo pro tuto scenu
        muj_uhel_symbol = always_redraw (lambda: Angle(
            k.useckaVA, k.useckaVB,
            **gs.UHEL_SYMBOL
        ))
        muj_text_stupne = always_redraw(lambda: Integer(
            k.get_stupne_norm(), unit=r"^{\circ}")
            .move_to(k.osy.c2p(0,0) * 0.7 + k.misto_na_kruznici(k.velikost_uhlu.get_value()*1/2) * 0.3)
        ) 
        jedna = always_redraw(lambda: Integer(1).next_to(k.useckaVB.get_center(), UL, buff=0.2))
        
        self.add(k.kruznice, k.osy, k.useckaVA, k.useckaVB, k.bodA, k.bodB, k.bodV,
                 muj_text_stupne, muj_uhel_symbol, jedna)
        self.wait(1)

        for i in range(len(uhly)):
            self.play(k.velikost_uhlu.animate.set_value(uhly[i]*DEGREES))
            self.wait(1)
            self.next_slide()


            trojuhelnik = Polygon(
                k.bodB.update().get_center(), k.bodV.get_center(), bodC.update().get_center(),
                **gs.TROJUHELNIK
            )
            pravy_uhel = RightAngle(Line(bodC, k.bodV), Line(bodC, k.bodB))
            trojuhelnik_grupa = VGroup(trojuhelnik, bodC) #pravy_uhel)
            self.play(FadeIn(trojuhelnik_grupa))
            self.wait(1)
            self.next_slide()


            sour_y = Line(bodC.get_center(), k.bodB.get_center(), **gs.SIN_USECKA)
            sour_x = Line(bodC, k.bodV, **gs.COS_USECKA)
            sin_text = MathTex("a", **gs.SIN_TEXT).next_to(sour_y)
            cos_text = MathTex("b", **gs.COS_TEXT).next_to(sour_x,DOWN)

            self.play(Create(sour_y), Create(sin_text))
            self.play(Create(sour_x), Create(cos_text))
            self.wait(1)
            self.next_slide()

            self.play(Transform(sin_text, MathTex(zapisy_sin[i], **gs.SIN_TEXT).move_to(sin_text, LEFT)))
            self.play(Transform(cos_text, MathTex(zapisy_cos[i], **gs.COS_TEXT).move_to(cos_text)))
            self.wait(1)
            self.next_slide()

            self.play(Transform(sin_text, MathTex(hodnoty_sin[i], **gs.SIN_TEXT).move_to(sin_text, LEFT)))
            self.play(Transform(cos_text, MathTex(hodnoty_cos[i], **gs.COS_TEXT).move_to(cos_text, UP)))
            self.wait(1)
            self.next_slide()

            souradnice = MathTex(r"\left[" + hodnoty_cos[i] + ";" + hodnoty_sin[i]  + r"\right]")
            self.play(Write(souradnice.next_to(k.bodB, UR)))
            self.wait(1)
            self.next_slide()

            self.play(FadeOut(trojuhelnik_grupa), FadeOut(sin_text), FadeOut(cos_text),
                      FadeOut(sour_y), FadeOut(sour_x), FadeOut(souradnice))

  