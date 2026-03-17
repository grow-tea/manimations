from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *

class Stupne_or_uhel_ekvivalence(Slide):
 
    # pro vyreseni bugu, ze se neda video vyrenderovat
    max_duration_before_split_reverse = None

    def construct(self):

        k = Jednotkova_kruznice(0.1*DEGREES)
        cil_stupen = 210
        or_uhel_popis = always_redraw(lambda: Integer(k.get_stupne(), unit=r"^{\circ}", group_with_commas=False).move_to(k.misto_pro_pocitani))

        cil_pozice = k.misto_na_kruznici(cil_stupen*DEGREES)
        cil_bod = k.bod_na_kruznici(cil_stupen*DEGREES)
        cil_polopr = do_poloprimky(Line(k.osy.c2p(0,0), cil_pozice)).set(**gs.OBRAZ)
        cil_uhel = Angle(k.poloprVA, cil_polopr, **gs.UHEL_SYMBOL_OBRAZ)
        cil_uhel_text = Integer(cil_stupen, unit="^{\circ}", **gs.OBRAZ_TEXT).move_to(k.misto_pod_uhlem((cil_stupen-15)*DEGREES))

        self.add(
            k.kruznice, k.osy,
            k.AVBgrupa.update(),
        )
        self.remove(k.znakB)

        self.play(Write(cil_bod), Write(cil_polopr), Write(cil_uhel), Write(cil_uhel_text))
        self.next_slide()

        k.velikost_uhlu.set_value(0.1*DEGREES)
        self.add(
            or_uhel_popis.update(),
            k.bodB.update(), k.poloprVB.update(),
        )

        grupa = VGroup(k.bodB, k.poloprVB)

        i = 0
        for s in [cil_stupen, cil_stupen - 360, cil_stupen + 360, cil_stupen - 2*360]:
            self.add(grupa)
            self.play(k.velikost_uhlu.animate.set_value((s)*DEGREES), run_time=4, rate_func=smooth)
            self.play(FadeOut(grupa))
            self.play(TransformFromCopy(or_uhel_popis, Integer(s, unit="^{\circ}").move_to(k.osy.c2p(0.3 + i * 0.5, -1.2))))
            self.next_slide()

            k.velikost_uhlu.set_value(0.1*DEGREES)
            grupa.update()
            or_uhel_popis.update()

            i += 1

