from manim import *
from manim_slides import Slide
import numpy as np

from .config import GonioStyle as gs

def do_poloprimky(usecka, ratio=100):
    delta = usecka.end - usecka.start
    usecka.put_start_and_end_on(usecka.start, usecka.end + ratio * delta)
    return usecka

def norm(vel_uhlu):
    return vel_uhlu % (2*PI)

class Jednotkova_kruznice():

    def misto_na_kruznici(self, vel_uhlu):
        x = np.cos(vel_uhlu)
        y = np.sin(vel_uhlu)
        return self.osy.c2p(x, y)
    
    def udelej_kruznicovy_oblouk(self, vel_uhlu_start, vel_uhlu_end):
        if (vel_uhlu_start < vel_uhlu_end):
            return self.osy.plot_parametric_curve(
                lambda t: np.array([np.cos(t),np.sin(t),0]),
                t_range=[vel_uhlu_start, vel_uhlu_end],
                color=gs.KRUHOVY_OBLOUK_BARVA,
            )
        else:
            return self.osy.plot_parametric_curve(
                lambda t: np.array([np.cos(t),np.sin(t),0]),
                t_range=[vel_uhlu_end, vel_uhlu_start],     # obracene
                color=gs.KRUHOVY_OBLOUK_ZAPORNE_BARVA,
            )
    
    def misto_pro_text_vysec(self):
        return self.misto_na_kruznici(self.velikost_uhlu.get_value() / 2) * 0.7
    
    def misto_znak_u_kruznice(self, vel_uhlu, vpravo=False):
        posun = -10*DEGREES if vpravo else 10*DEGREES
        return self.misto_na_kruznici(vel_uhlu + posun) * 1.15
    
    def misto_pod_uhlem(self, vel_uhlu):
        return self.misto_na_kruznici(vel_uhlu) * 0.45

    def misto_u_uhel_symbol(self):
        vel_uhlu = norm(self.velikost_uhlu.get_value())
        if vel_uhlu < 30 * DEGREES:
            return self.misto_pod_uhlem(vel_uhlu + 10*DEGREES)
        return self.misto_pod_uhlem(vel_uhlu / 3)
    
    def bod_na_kruznici(self, vel_uhlu):
        return Dot(self.misto_na_kruznici(vel_uhlu),color=gs.BODY_BARVA2)

    def get_stupne(self):
        return round(self.velikost_uhlu.get_value() / DEGREES)
    
    def get_stupne_norm(self):
        vel_uhlu = round(self.velikost_uhlu.get_value() / DEGREES)
        if vel_uhlu == 360:
            return 360
        return vel_uhlu % 360
    
    def get_text_radiany(self, text_tex, rad=False):
        if rad==True: text_tex += r" rad"
        return MathTex(text_tex).scale(0.7).move_to(self.misto_u_uhel_symbol() * 0.8)
    
    def animuj_pohyb_po_kruznici(self, slides, vel_uhlu_start, vel_uhlu_cil, run_time=3):
        vt = ValueTracker(vel_uhlu_start)
        
        self.bod_pohybpokruznici = always_redraw(
            lambda: Dot(
                self.misto_na_kruznici(vt.get_value()),
                color=gs.KRUHOVY_OBLOUK_BARVA if vel_uhlu_cil > vel_uhlu_start else gs.KRUHOVY_OBLOUK_ZAPORNE_BARVA)
        )
        self.oblouk_pohybpokruznici = always_redraw(
            lambda: self.udelej_kruznicovy_oblouk(vel_uhlu_start, vt.get_value())
        )
        slides.add(self.bod_pohybpokruznici, self.oblouk_pohybpokruznici)
        slides.play(vt.animate.set_value(vel_uhlu_cil), run_time=run_time, rate_func=smooth)
    
    def odstran_pohyb_po_kruznici(self, slides):
        slides.play(FadeOut(self.bod_pohybpokruznici), FadeOut(self.oblouk_pohybpokruznici))
        del self.bod_pohybpokruznici
        del self.oblouk_pohybpokruznici

    def udelej_delka_text(self, vel_uhlu, text_tex):
        return MathTex(text_tex, color=gs.KRUHOVY_OBLOUK_BARVA).scale(0.8).move_to(self.misto_znak_u_kruznice(vel_uhlu, vpravo=True))
        
    def get_bod_x_souradnice(self, vel_uhlu):
        x = np.cos(vel_uhlu)
        return self.osy.c2p(x, 0)
    
    def get_bod_y_souradnice(self, vel_uhlu):
        y = np.sin(vel_uhlu)
        return self.osy.c2p(0, y)


    def __init__(self, poc_vel_uhlu=90*DEGREES, osy_config = gs.OSY_CONFIG, posun = None, rotace = 0):

        # Definovani os x a y
        self.osy = Axes(**osy_config).rotate(rotace)

        # pro specialni pripad posunu celeho objektu nekam
        if (posun is not None):
            self.osy.to_edge(posun, buff=1)

        # Definovani kruznice
        self.kruznice = self.osy.plot_parametric_curve(
            lambda t: np.array([np.cos(t),np.sin(t),0]),
            t_range=[0, 2 * PI],
            color=gs.KRUZNICE_BARVA,
        )

        self.velikost_uhlu = ValueTracker(poc_vel_uhlu)

        self.bodA = Dot(self.misto_na_kruznici(0), color=gs.BODY_BARVA)
        self.bodV = Dot(self.osy.c2p(0,0), color=gs.BODY_BARVA)
        self.bodB = always_redraw(lambda: Dot(
            self.misto_na_kruznici(self.velikost_uhlu.get_value()),
            color=gs.BODY_BARVA)
        )  # ten pohyblivy, souradnice se budou menit
        
        self.znakA = MathTex("A").next_to(self.bodA, UR)
        self.znakV = MathTex("V").next_to(self.bodV, DR * 0.5)
        self.znakB = MathTex("B").add_updater(lambda m:m.move_to(self.misto_znak_u_kruznice(self.velikost_uhlu.get_value())))
        
        self.useckaVA = Line(self.bodV, self.bodA)
        self.poloprVA = do_poloprimky(Line(self.bodV, self.bodA))

        self.useckaVB = always_redraw(lambda: Line(self.bodV.get_center(), self.bodB))
        self.poloprVB = always_redraw(lambda: do_poloprimky(Line(self.bodV.get_center(), self.bodB)))

        self.uhel_symbol = always_redraw(lambda: Angle(self.poloprVA, self.poloprVB, radius=0.5, color=gs.UHEL_BARVA))

        self.text_stupne = always_redraw(lambda: Integer(self.get_stupne_norm(), unit=r"^{\circ}").move_to(self.misto_u_uhel_symbol()))   

        self.vysec = always_redraw(lambda: Sector(
            arc_center=self.bodV.get_center(),
            radius=self.osy.get_x_unit_size(),
            angle=self.velikost_uhlu.get_value(),
            color=gs.VYSEC_BARVA,
            fill_opacity=0.2,
        ))

        self.AVBgrupa = VGroup(
            self.bodA, self.bodV, self.bodB,
            self.poloprVA, self.poloprVB,
            self.znakA, self.znakB, self.znakV,
            self.uhel_symbol)
        
        self.kruznicovy_oblouk_AB = always_redraw(lambda:
            self.udelej_kruznicovy_oblouk(0, self.velikost_uhlu.get_value())
        )

        self.misto_pro_pocitani = self.osy.c2p(1.5, 1.2)

        ### pro zavedeni funkci sinus a kosinus

        self.usecka_na_ose_x = always_redraw(lambda: Line(
            self.bodV.get_center(),
            self.get_bod_x_souradnice(self.velikost_uhlu.get_value()),
            color = gs.COS_BARVA,
            stroke_width = 8
        ))

        self.usecka_na_ose_y = always_redraw(lambda: Line(
            self.bodV.get_center(),
            self.get_bod_y_souradnice(self.velikost_uhlu.get_value()),
            color = gs.SIN_BARVA,
            stroke_width = 8
        ))

        self.kolmice_k_ose_x = always_redraw(lambda: DashedLine(
            self.misto_na_kruznici(self.velikost_uhlu.get_value()),
            self.get_bod_x_souradnice(self.velikost_uhlu.get_value())
        ))

        self.kolmice_k_ose_y = always_redraw(lambda: DashedLine(
            self.misto_na_kruznici(self.velikost_uhlu.get_value()),
            self.get_bod_y_souradnice(self.velikost_uhlu.get_value())
        ))

        self.souradnice_grupa = VGroup(
            self.usecka_na_ose_x,
            self.usecka_na_ose_y,
            self.kolmice_k_ose_x,
            self.kolmice_k_ose_y
        )


        self.sin_stupne = always_redraw(lambda:
            MathTex(
                f"\\sin({self.get_stupne()}^\\circ)",
                font_size = gs.GONIO_FONT_VELIKOST,
                color = gs.SIN_BARVA,
            ).next_to(self.usecka_na_ose_y.get_center(), LEFT + 0.2*UP)
        )

        relative_down = rotate_vector(DOWN, rotace)
        self.cos_stupne = always_redraw(lambda:
            MathTex(
                f"\\cos({self.get_stupne()}^\\circ)",
                font_size = gs.GONIO_FONT_VELIKOST,
                color = gs.COS_BARVA,
            ).rotate(rotace).next_to(self.usecka_na_ose_x.get_center(), relative_down)
        )