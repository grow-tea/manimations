from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *


class Grafy():
   
    def __init__(self, mod="SIN"):

        self.k = Jednotkova_kruznice(0.1 * DEGREES, osy_config = gs.OSY_CONFIG_MENSI, posun=LEFT, rotace = PI/2 if (mod=="COS") else 0)
        self.uhel_symbol = always_redraw(lambda: Angle(self.k.useckaVA, self.k.useckaVB, **gs.UHEL_SYMBOL))
        self.popisky_kruz = self.k.osy.get_axis_labels(x_label="x", y_label="y")

        self.kruznice_grupa = VGroup(self.k.kruznice, self.k.osy,
                                     self.k.bodB, self.k.useckaVB, self.k.useckaVA,
                                     self.k.bodV, self.k.bodA, self.uhel_symbol)
        
        self.osy_grafu = Axes(
            x_range = [0, 2*PI, PI/4],
            y_range = [-1.3, 1.3, 0.2],
            x_length = 7,
            y_length = 5,
            axis_config = {"include_tip": False, "color": gs.GRAF_OSY_BARVA},
        ).to_edge(RIGHT, buff=1)
        
        self.labels = self.osy_grafu.get_axis_labels(x_label="x", y_label="\\sin(x)" if mod=="SIN" else "\\cos(x)")

        hodnoty_na_ose_x = {
            PI/2: MathTex(r"\frac{\pi}{2}", **gs.UHEL_LABEL),
            PI: MathTex(r"\pi", **gs.UHEL_LABEL),
            3*PI/2: MathTex(r"\frac{3}{2}\pi", **gs.UHEL_LABEL),
            2*PI: MathTex(r"2\pi", **gs.UHEL_LABEL),
        }
        #
        ## Přidání popisků na x-ovou osu
        self.osy_grafu.x_axis.add_labels(hodnoty_na_ose_x)

        self.graf_grupa = VGroup(self.osy_grafu, self.labels)
 
        self.bod_sinusoida = always_redraw(lambda: Dot(**gs.SIN_BOD)
            .move_to(self.osy_grafu.c2p(self.k.velikost_uhlu.get_value(), np.sin(self.k.velikost_uhlu.get_value()))))
        self.bod_kosinusoida = always_redraw(lambda: Dot(**gs.COS_BOD)
            .move_to(self.osy_grafu.c2p(self.k.velikost_uhlu.get_value(), np.cos(self.k.velikost_uhlu.get_value()))))

        self.pomocna_usecka = always_redraw(lambda: DashedLine(
            start = self.k.bodB,
            end = self.bod_sinusoida if mod=="SIN" else self.bod_kosinusoida,
            **gs.POMOCNA_CARA
        ))

        self.svislice = always_redraw(lambda: Line(
            start = self.osy_grafu.c2p(self.k.velikost_uhlu.get_value(), -2),
            end = self.osy_grafu.c2p(self.k.velikost_uhlu.get_value(), 2),
            **gs.UHEL_SVISLICE
        ))

        self.sinusoida_krivka = TracedPath(self.bod_sinusoida.get_center, **gs.SINUSOIDA)
        self.kosinusoida_krivka = TracedPath(self.bod_kosinusoida.get_center, **gs.COSINUSOIDA)
        
