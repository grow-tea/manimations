from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *

from goniometrie.config import *

class Polarni_souradnice(Slide):
    
    # pro vyreseni bugu, ze se neda video vyrenderovat
    max_duration_before_split_reverse = None
    
    def construct(self):

        k = Jednotkova_kruznice(0.1*DEGREES)
        grupa = VGroup(k.bodA, k.bodB, k.bodV, k.poloprVA, k.poloprVB.update(), k.uhel_symbol.update(), k.text_stupne)

        i = 6
        mrizka = PolarPlane(
            radius_max=i,
            size= i * k.osy.x_axis.get_unit_size(),
            azimuth_step = 12,
            radius_step = 0.5,
            background_line_style=gs.POLARNI_BACKGROUND_LINE
        ).move_to(k.osy.get_center())
        
        delka_jedna = k.osy.x_axis.get_unit_size()
        polomer_kruznice = ValueTracker(delka_jedna)
        polarni_kruznice = always_redraw( lambda: Circle(
            radius = polomer_kruznice.get_value(),
            **gs.POLARNI_KRUZNICE
        ).move_to(k.osy.get_center()))

        uhly = [5*PI/4, 5*PI/6, 11/6*PI]
        polomery = [1, 1.5, 0.75]
        pol_str = ["1", "1,5", r"\tfrac{3}{4}"]

        self.add(k.kruznice, k.osy)
        self.play(FadeIn(grupa))
        self.play(k.velikost_uhlu.animate.set_value(45*DEGREES), run_time=3)
        self.wait(1)
        self.next_slide()
        self.play(Write(mrizka), Write(polarni_kruznice), run_time=3)
        self.wait(1)
        self.next_slide()

        for i in range(len(uhly)):
            
            bod = Dot(k.osy.c2p(polomery[i] * np.cos(uhly[i]), polomery[i] * np.sin(uhly[i])), **gs.BOD_HADEJ)
            usecka = Line(bod.get_center(), k.bodV.get_center(), **gs.POLOMER_USECKA)
            polomer = MathTex(str(pol_str[i]), **gs.POLOMER_TEXT).next_to(usecka.get_center(), buff = 0.25)
            
            self.play(Write(bod))
            self.play(Flash(bod))
            self.wait(1)
            self.next_slide()

            self.play(k.velikost_uhlu.animate.set_value(uhly[i]), run_time=3, rate_func=smooth)
            self.wait(1)
            self.next_slide()

            self.play(polomer_kruznice.animate.set_value(delka_jedna * polomery[i]))
            self.wait(1)
            self.next_slide()

            kolmiceX = DashedLine(bod, Dot(k.osy.c2p(polomery[i] * np.cos(uhly[i]), 0)))
            kolmiceY = DashedLine(bod, Dot(k.osy.c2p(0, polomery[i] * np.sin(uhly[i]))))
            self.play(Write(kolmiceX), Write(kolmiceY), run_time=1)
            self.wait(1)
            self.next_slide()

            self.play(Create(usecka))
            self.play(Write(polomer.add_background_rectangle(**gs.BACKGROUND_RECTANGLE)))
            self.wait(1)
            self.next_slide()

            souradnice = MathTex(
                r"[" + pol_str[i] + " \cdot \cos(" + str(k.get_stupne()) + "^{\circ}), "
                + pol_str[i] + "\cdot \sin("+str(k.get_stupne())+"^{\circ})]"
                ).set(**gs.TEXT)
            self.play(Write(souradnice.move_to(k.misto_pro_pocitani).scale(0.9).add_background_rectangle(**gs.BACKGROUND_RECTANGLE)))
            self.wait(1)
            self.next_slide()

            self.play(FadeOut(bod), Unwrite(usecka), Unwrite(polomer), Unwrite(souradnice), Unwrite(kolmiceX), Unwrite(kolmiceY))
            self.play(
                k.velikost_uhlu.animate.set_value(45*DEGREES),
                polomer_kruznice.animate.set_value(delka_jedna),    
                run_time=2)
            self.wait(1)
            self.next_slide()
            

