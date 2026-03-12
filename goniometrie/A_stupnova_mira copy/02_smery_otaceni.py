from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *
from goniometrie.config import GonioStyle as gs

class Smery_otaceni(Slide):

    def construct(self):
        
        stare_s = 45
        k = Jednotkova_kruznice(stare_s*DEGREES)
        self.add(
            k.kruznice, k.osy,
            k.AVBgrupa,
            k.text_stupne.update()
        )
        self.next_slide()

        
        for s in [225, 135, 315]:
            bod_hadej = k.bod_na_kruznici(s*DEGREES)
            self.add(bod_hadej)
            self.play(Flash(bod_hadej))
            self.next_slide()
            
            barva = gs.KLADNE_OTOCENI_BARVA if s - stare_s > 0 else gs.ZAPORNE_OTOCENI_BARVA
            pomocna_tecna = TangentLine(k.kruznice, alpha=stare_s*DEGREES/2/PI)
            vektor_tecny = pomocna_tecna.get_unit_vector() * np.sign(s - stare_s)
            koncovy_bod = k.bodB.get_center() + vektor_tecny
            sipka = Arrow(
                start=k.bodB.get_center(),
                end=koncovy_bod,
                buff=0,
                color=barva
            )
            self.play(Write(sipka))
            popisek = Integer(s - stare_s, unit=r"^{\circ}", include_sign=True, color=barva).move_to(koncovy_bod * 0.5)
            self.play(Write(popisek))
            self.wait(1)
            self.next_slide()
            
            self.play(Unwrite(popisek), Unwrite(sipka))
            self.play(k.velikost_uhlu.animate.set_value(s * DEGREES),run_time=3, rate_func=smooth)
            self.play(FadeOut(bod_hadej))
            self.wait(1)

            # pro dalsi iteraci
            stare_s = s