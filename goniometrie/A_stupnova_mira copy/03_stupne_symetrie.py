from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *
from goniometrie.config import GonioStyle as gs

class Stupne_symetrie(Slide):

    poc_uhel = 33
    vyraz = None

    def operace(self, stupen):
        return stupen
    
    def construct(self):

        k = Jednotkova_kruznice(self.poc_uhel * DEGREES)
        A_to_B = False

        self.add(
            k.kruznice, k.osy,
            k.bodA, k.bodV, k.bodB,     # bez oznaceni
            k.poloprVA, k.poloprVB,
            k.uhel_symbol,
            k.text_stupne,
        )

        cilova_pozice = k.misto_na_kruznici((self.operace(self.poc_uhel)) * DEGREES)
        cilovy_bod = Dot(cilova_pozice, color=gs.BODY_BARVA2)
        usecka = DashedLine(k.bodB.get_center(), cilova_pozice)

        self.next_slide()
        self.play(Create(usecka), Create(cilovy_bod))
        self.play(Flash(cilovy_bod))
        self.next_slide()

        poloprVB_obraz = do_poloprimky(Line(k.osy.c2p(0,0), cilova_pozice, color=gs.OBRAZ_BARVA))
        poloprVA_obraz = do_poloprimky(Line(k.osy.c2p(0,0), k.misto_na_kruznici(self.operace(0)*DEGREES), color=gs.OBRAZ_BARVA))
        uhel_symbol_obraz = Angle(poloprVB_obraz, poloprVA_obraz, radius=0.5, color=gs.OBRAZ_BARVA) if not self.A_to_B \
            else Angle(poloprVA_obraz, poloprVB_obraz, radius=0.5, color=gs.OBRAZ_BARVA)
        uhel_text_obraz = Integer(self.poc_uhel, unit=r"^{\circ}").move_to(k.misto_pod_uhlem(self.operace(self.poc_uhel/2)*DEGREES))

        self.vyraz.move_to(k.misto_pro_pocitani)

        obrazy = VGroup(poloprVB_obraz, poloprVA_obraz, uhel_symbol_obraz, uhel_text_obraz)
        self.play(Create(obrazy))
        self.wait(1)
        self.next_slide()
        
        self.play(k.velikost_uhlu.animate.set_value(self.operace(0)*DEGREES), run_time=2, rate_func=smooth)
        self.wait(1)
        self.next_slide()
        self.play(Write(self.vyraz))
        self.wait(1)
        self.next_slide()
        
        self.play(k.velikost_uhlu.animate.set_value(self.operace(self.poc_uhel)*DEGREES), run_time=2, rate_func=smooth)
        self.next_slide()
        self.play(Unwrite(self.vyraz), FadeOut(obrazy), FadeOut(usecka))
        self.play(k.velikost_uhlu.animate.set_value(self.poc_uhel*DEGREES), run_time=2, rate_func=smooth)
        self.wait(1)


class Vodorovna_symetrie(Stupne_symetrie):

    def operace(self, stupen):
        return 180 - stupen

    poc_uhel = 33
    koncovy_uhel = 180 - poc_uhel
    A_to_B = False

    vyraz = MathTex("180^{\circ} - "+ str(poc_uhel) +"^{\circ} = " + str(koncovy_uhel) + "^{\circ}")


class Svisla_symetrie(Stupne_symetrie):
    def operace(self, stupen):
        return 360 - stupen

    poc_uhel = 33
    koncovy_uhel = 360 - poc_uhel
    A_to_B = False

    vyraz = MathTex("360^{\circ} - "+ str(poc_uhel) +"^{\circ} = " + str(koncovy_uhel) + "^{\circ}")

class Stredova_soumernost(Stupne_symetrie):
    def operace(self, stupen):
        return stupen + 180

    A_to_B = True # jako obraz se zobrazi uhel AVB, ne BVA

    poc_uhel = 33
    koncovy_uhel = 180 + poc_uhel

    vyraz = MathTex("180^{\circ} + "+ str(poc_uhel) +"^{\circ} = " + str(koncovy_uhel) + "^{\circ}")