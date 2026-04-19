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
                **gs.KRUZ_OBLOUK,
            )
        else:
            return self.osy.plot_parametric_curve(
                lambda t: np.array([np.cos(t),np.sin(t),0]),
                t_range=[vel_uhlu_end, vel_uhlu_start],     # obracene
                **gs.KRUZ_OBLOUK_ZAPORNE,
            )
    
    def misto_pro_text_vysec(self):
        return self.misto_na_kruznici(self.velikost_uhlu.get_value() / 2) * 0.7
    
    def misto_znak_u_kruznice(self, vel_uhlu, vpravo=False):
        posun = -10*DEGREES if vpravo else 10*DEGREES
        return self.misto_na_kruznici(vel_uhlu + posun) * 1.15
    
    def misto_pod_uhlem(self, vel_uhlu):
        return self.osy.c2p(0,0) * 0.55 + self.misto_na_kruznici(vel_uhlu) * 0.45

    def misto_u_uhel_symbol(self):
        vel_uhlu = norm(self.velikost_uhlu.get_value())
        if vel_uhlu < 30 * DEGREES:
            return self.misto_pod_uhlem(vel_uhlu + 10*DEGREES)
        return self.misto_pod_uhlem(vel_uhlu / 3)

    def bod_na_kruznici(self, vel_uhlu):
        return Dot(self.misto_na_kruznici(vel_uhlu), **gs.BOD_HADEJ)

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
                **gs.KRUZ_OBLOUK_BOD if vel_uhlu_cil > vel_uhlu_start else gs.KRUZ_OBLOUK_BOD_ZAP)
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
        return MathTex(
            text_tex,
            **gs.KRUZ_OBLOUK_TEXT if vel_uhlu > 0 else gs.KRUZ_OBLOUK_TEXT_ZAP,
            ).move_to(self.misto_znak_u_kruznice(vel_uhlu, vpravo=True))
        
    def get_bod_x_souradnice(self, vel_uhlu, polomer = 1):
        x = np.cos(vel_uhlu) * polomer
        return self.osy.c2p(x, 0)
    
    def get_bod_y_souradnice(self, vel_uhlu, polomer = 1):
        y = np.sin(vel_uhlu) * polomer
        return self.osy.c2p(0, y)


    def __init__(self, poc_vel_uhlu=90*DEGREES, osy_config = gs.OSY_CONFIG, posun = None, rotace = 0, zmena_velikosti = 1):
        
        # Definovani os x a y
        self.osy = Axes(**osy_config).rotate(rotace).scale(zmena_velikosti)

        # pro specialni pripad posunu celeho objektu nekam
        if (posun is not None):
            self.osy.to_edge(posun, buff=1)

        # Definovani kruznice
        self.kruznice = self.osy.plot_parametric_curve(
            lambda t: np.array([np.cos(t),np.sin(t),0]),
            t_range=[0, 2 * PI],
            **gs.KRUZNICE
        )

        self.velikost_uhlu = ValueTracker(poc_vel_uhlu)

        self.bodA = Dot(self.misto_na_kruznici(0), **gs.BOD_STATIC)
        self.bodV = Dot(self.osy.c2p(0,0), **gs.BOD_STATIC)
        self.bodB = always_redraw(lambda: Dot(
            self.misto_na_kruznici(self.velikost_uhlu.get_value()),
            **gs.BOD_POHYB)
        )  # ten pohyblivy, souradnice se budou menit
        
        self.znakA = MathTex("A", **gs.TEXT).next_to(self.bodA, UR)
        self.znakV = MathTex("V", **gs.TEXT).next_to(self.bodV, DR * 0.5)
        self.znakB = MathTex("B", **gs.TEXT).add_updater(lambda m:m.move_to(self.misto_znak_u_kruznice(self.velikost_uhlu.get_value())))
        
        self.useckaVA = Line(self.bodV, self.bodA, **gs.HLAVNI_CARA)
        self.poloprVA = do_poloprimky(Line(self.bodV, self.bodA, **gs.HLAVNI_CARA))

        self.useckaVB = always_redraw(lambda: Line(self.bodV.get_center(), self.bodB, **gs.HLAVNI_CARA))
        self.poloprVB = always_redraw(lambda: do_poloprimky(Line(self.bodV.get_center(), self.bodB, **gs.HLAVNI_CARA)))

        self.uhel_symbol = always_redraw(lambda: Angle(self.poloprVA, self.poloprVB, **gs.UHEL_SYMBOL))

        self.text_stupne = always_redraw(lambda: Integer(
            self.get_stupne_norm(),
            unit=r"^{\circ}")
            .set(**gs.TEXT)
            .move_to(self.misto_u_uhel_symbol())
            #.add_background_rectangle(**gs.BACKGROUND_RECTANGLE)
        )

        self.vysec = always_redraw(lambda: Sector(
            arc_center=self.bodV.get_center(),
            radius=self.osy.get_x_unit_size(),
            angle=self.velikost_uhlu.get_value(),
            **gs.VYSEC,
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

        self.x = always_redraw(lambda: Dot(
            self.get_bod_x_souradnice(self.velikost_uhlu.get_value()),
            **gs.COS_BOD
        ))
        self.usecka_na_ose_x = always_redraw(lambda: Line(
            self.bodV.get_center(),
            self.x,
            **gs.COS_USECKA,
        ))

        self.y = always_redraw(lambda: Dot(
            self.get_bod_y_souradnice(self.velikost_uhlu.get_value()),
            **gs.SIN_BOD
        ))
        self.usecka_na_ose_y = always_redraw(lambda: Line(
            self.bodV.get_center(),
            self.y,
            **gs.SIN_USECKA,
        ))

        self.kolmice_k_ose_x = always_redraw(lambda: DashedLine(
            self.misto_na_kruznici(self.velikost_uhlu.get_value()),
            self.get_bod_x_souradnice(self.velikost_uhlu.get_value()),
            **gs.POMOCNA_CARA,
        ))

        self.kolmice_k_ose_y = always_redraw(lambda: DashedLine(
            self.misto_na_kruznici(self.velikost_uhlu.get_value()),
            self.get_bod_y_souradnice(self.velikost_uhlu.get_value()),
            **gs.POMOCNA_CARA,
        ))

        self.sin_grupa = VGroup(self.y, self.usecka_na_ose_y, self.kolmice_k_ose_y)
        self.cos_grupa = VGroup(self.x, self.usecka_na_ose_x, self.kolmice_k_ose_x)

        sin_label = MathTex(r"\sin(", **gs.SIN_TEXT)
        sin_zavorka = MathTex(r")", **gs.SIN_TEXT)
        self.sin_stupne = always_redraw(lambda :VGroup(
            sin_label, Integer(self.get_stupne(), unit=r"^{\circ}", **gs.SIN_TEXT), sin_zavorka)
            .arrange(RIGHT, buff=0.1)
            .next_to(self.usecka_na_ose_y.get_center(), LEFT + 0.2*UP)
            .add_background_rectangle(**gs.BACKGROUND_RECTANGLE)
        )


        cos_label = MathTex(r"\cos(", **gs.COS_TEXT).rotate(rotace)
        cos_zavorka = MathTex(r")", **gs.COS_TEXT).rotate(rotace)

        # navic pro moznost otocit jedn. kruznici o 90 stupnu a ukazat promitnuti kosinu do grafu
        relative_down = DOWN if rotace == 0 else RIGHT
        relative_right = RIGHT if rotace == 0 else UP
        
        self.cos_stupne = always_redraw(lambda: VGroup(
            cos_label, Integer(self.get_stupne(), unit=r"^{\circ}", **gs.COS_TEXT).rotate(rotace), cos_zavorka)
            .arrange(relative_right, buff=0.1)
            .next_to(self.usecka_na_ose_x.get_center(), relative_down)
            .add_background_rectangle(**gs.BACKGROUND_RECTANGLE)
        )