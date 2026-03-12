from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *


class Polarni_souradnice(Slide):
    def construct(self):

        k = Jednotkova_kruznice(0.1*DEGREES)
        grupa = VGroup(k.bodA, k.bodB, k.bodV, k.poloprVA, k.poloprVB, k.uhel_symbol, k.text_stupne)

        i = 6
        mrizka = PolarPlane(
            radius_max=i,
            size= i * k.osy.x_axis.get_unit_size(),
            azimuth_step = 12,
            radius_step = 0.5,
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 2,
                "stroke_opacity": 0.5
            }
        ).move_to(k.osy.get_center())
        
        delka_jedna = k.osy.x_axis.get_unit_size()
        polomer_kruznice = ValueTracker(delka_jedna)
        zluta_kruznice = always_redraw( lambda: Circle(
            radius = polomer_kruznice.get_value(),
            color = YELLOW,
            stroke_width = 4
        ).move_to(k.osy.get_center()))

        uhly = [5*PI/4, 5*PI/6, 11/6*PI]
        polomery = [1, 1.5, 0.75]
        pol_str = ["1", "1,5", "0,75"]

        self.add(k.kruznice, zluta_kruznice)
        self.add(grupa)
        self.next_slide()
        self.play(Write(mrizka))
        self.wait(2)

        for i in range(len(uhly)):
            k.velikost_uhlu.set_value(0.1*DEGREES)
            bod = Dot(k.osy.c2p(polomery[i] * np.cos(uhly[i]), polomery[i] * np.sin(uhly[i])))
            usecka = Line(bod.get_center(), k.bodV.get_center(), color=GREEN, stroke_width = 4)
            polomer = MathTex(str(polomery[i]), color=GREEN).next_to(usecka.get_center(), buff = 0.25)
            self.add(grupa)
            self.play(Write(bod))
            self.play(k.velikost_uhlu.animate.set_value(uhly[i]), run_time=3, rate_func=smooth)
            self.play(polomer_kruznice.animate.set_value(delka_jedna * polomery[i]))
            kolmiceX = DashedLine(bod, Dot(k.osy.c2p(polomery[i] * np.cos(uhly[i]), 0)))
            kolmiceY = DashedLine(bod, Dot(k.osy.c2p(0, polomery[i] * np.sin(uhly[i]))))
            self.play(Write(kolmiceX), Write(kolmiceY))
            self.play(Create(usecka))
            self.play(Write(polomer))
            self.wait(2)
            souradnice = MathTex(r"[" + pol_str[i] + " \cdot \cos(" + str(k.get_stupne()) + "^{\circ}), "+pol_str[i]+"\cdot \sin("+str(k.get_stupne())+"^{\circ})]")
            self.play(Write(souradnice.move_to(k.misto_pro_pocitani).scale(0.8)))
            self.play(FadeOut(bod), FadeOut(grupa), Unwrite(usecka), Unwrite(polomer), Unwrite(souradnice), Unwrite(kolmiceX), Unwrite(kolmiceY))
            self.wait(1)
            

