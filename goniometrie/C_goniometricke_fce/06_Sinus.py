from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *

class Sinus(Slide):

    def construct(self):
        
        k = Jednotkova_kruznice(0.1 * DEGREES, osy_config = gs.OSY_CONFIG_MENSI, posun=LEFT)

        self.add(k.kruznice, k.osy, k.bodB, k.useckaVB, k.sin_stupne, k.usecka_na_ose_y)
        
        osy_grafu = Axes(
            x_range = [0, 2*PI, PI/4],
            y_range = [-1.3, 1.3, 0.2],
            x_length = 7,
            y_length = 5,
            axis_config = {"include_tip": False}
        ).to_edge(RIGHT, buff=1)
        labels = osy_grafu.get_axis_labels(x_label="x", y_label="\\sin(x)")

        hodnoty_na_ose_x = {
            PI/2: MathTex(r"\frac{\pi}{2}"),
            PI: MathTex(r"\pi"),
            3*PI/2: MathTex(r"\frac{3}{2}\pi"),
            2*PI: MathTex(r"2\pi"),
        }
        #
        ## Přidání popisků na x-ovou osu
        osy_grafu.x_axis.add_labels(hodnoty_na_ose_x)

        
        bod_na_grafu = always_redraw(lambda: Dot(
            color=YELLOW
        ).move_to(osy_grafu.c2p(k.velikost_uhlu.get_value(), np.sin(k.velikost_uhlu.get_value())))
        )

        pomocna_usecka = always_redraw(lambda: DashedLine(
            start = k.bodB,
            end = bod_na_grafu,
            color=YELLOW
        ))

        cesta_na_grafu = TracedPath(bod_na_grafu.get_center, stroke_color=YELLOW, stroke_width=4)
        
        self.add(osy_grafu, labels, bod_na_grafu, pomocna_usecka, cesta_na_grafu)

        self.play(k.velikost_uhlu.animate.set_value(2*PI), run_time=5, rate_func=linear)
        self.wait(1)


class Cosinus(Slide):

    def construct(self):
        
        k = Jednotkova_kruznice(0.1 * DEGREES, osy_config = gs.OSY_CONFIG_MENSI, posun=LEFT, rotace=PI/2)
        popisky_kruz = k.osy.get_axis_labels(x_label="x", y_label="y")

        self.add(k.kruznice, k.osy, k.bodB, k.useckaVB, k.cos_stupne, k.usecka_na_ose_x)
        
        osy_grafu = Axes(
            x_range = [0, 2*PI, PI/4],
            y_range = [-1.3, 1.3, 0.2],
            x_length = 7,
            y_length = 5,
            axis_config = {"include_tip": False}
        ).to_edge(RIGHT, buff=1)
        popisky_graf = osy_grafu.get_axis_labels(x_label="x", y_label="\\cos(x)")

        hodnoty_na_ose_x = {
            PI/2: MathTex(r"\frac{\pi}{2}"),
            PI: MathTex(r"\pi"),
            3*PI/2: MathTex(r"\frac{3}{2}\pi"),
            2*PI: MathTex(r"2\pi"),
        }
        #
        ## Přidání popisků na x-ovou osu
        osy_grafu.x_axis.add_labels(hodnoty_na_ose_x)

        
        bod_na_grafu = always_redraw(lambda: Dot(
            color=YELLOW
        ).move_to(osy_grafu.c2p(k.velikost_uhlu.get_value(), np.cos(k.velikost_uhlu.get_value())))
        )

        pomocna_usecka = always_redraw(lambda: DashedLine(
            start = k.bodB,
            end = bod_na_grafu,
            color=YELLOW
        ))

        cesta_na_grafu = TracedPath(bod_na_grafu.get_center, stroke_color=YELLOW, stroke_width=4)
        
        self.add(osy_grafu, popisky_kruz, popisky_graf, bod_na_grafu, pomocna_usecka, cesta_na_grafu)

        self.play(k.velikost_uhlu.animate.set_value(2*PI), run_time=5, rate_func=linear)
        self.wait(1)