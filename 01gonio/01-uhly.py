from manim import *
from manim_slides import Slide
import numpy as np


RUDA = RED
STUPNE_BARVA = BLUE

class Sdilene(Slide):
    
    def do_poloprimky(usecka, ratio=100):
        delta = usecka.end - usecka.start
        usecka.put_start_and_end_on(usecka.start, usecka.end + ratio * delta)
        return usecka

    def pozice_na_kruznici(self, vel_uhlu):
        x = np.cos(vel_uhlu)
        y = np.sin(vel_uhlu)
        return self.osy.c2p(x, y)
    
    def bod_na_kruznici(osy, vel_uhlu):
        return Dot(Sdilene.pozice_na_kruznici(osy,vel_uhlu),color=BLUE)

    def udelej_vysec(osy, uhel1, uhel2):
        nova_vysec = osy.plot_parametric_curve(
            lambda t: np.array([np.cos(t),np.sin(t),0]),
            t_range=[uhel1, uhel2],
            color=RED
        )
        return nova_vysec

    def misto_pod_uhlem(osy, uhel):
        return osy.c2p(np.cos(uhel) * 0.45, np.sin(uhel) * 0.45)


    def udelej_popis(osy, uhel, hodnota):
        uhel -= 10*DEGREES
        pozice = osy.c2p(np.cos(uhel) * 1.15, np.sin(uhel) * 1.25)
        return MathTex(hodnota).move_to(pozice)

    def udelej_vysec_vypln(osy, uhel):
        return Sector(radius=1, angle=uhel).move_to(osy.c2p(0,0))

    def __init__(self, **kwarks):
        super().__init__(**kwarks)
        
        def update_bodB(mobject):
            uhel = self.velikost_uhlu.get_value()
            novy_bod = self.osy.c2p(np.cos(uhel), np.sin(uhel))
            mobject.move_to(novy_bod)

        def update_poloprVB(mobject):
            new_usecka = Line(self.osy.c2p(0,0), self.bodB)
            mobject.become(new_usecka) if self.chci_useckuVB else mobject.become(Sdilene.do_poloprimky(new_usecka))

        def update_znakB(mobject):
            uhel = (self.velikost_uhlu.get_value() - 10 * DEGREES)
            novy_bod = self.osy.c2p(np.cos(uhel) * 1.15, np.sin(uhel) * 1.15)
            mobject.move_to(novy_bod)

        def update_text_stupne(mobject):
            norm_velikost = (self.velikost_uhlu.get_value() / DEGREES) % 360
            mobject.set_value(norm_velikost)
            mobject.move_to(Sdilene.misto_pod_uhlem(self.osy, norm_velikost * DEGREES / 2))

        def update_text_radianu(mobject):
            polouhel = self.velikost_uhlu.get_value() / 2
            polobod = self.osy.c2p(np.cos(polouhel) * 0.5, np.sin(polouhel) * 0.5)
            mobject.move_to(polobod)
            
        def update_vysec(mobject):
            uhel = self.velikost_uhlu.get_value()
            mobject.become(Sdilene.udelej_vysec(self.osy, 0, uhel))

        self.osy = Axes( 
            x_range=(-1.3, 1.3, 0.1),
            y_range=(-1.3, 1.3, 0.1),
            x_length=7,
            y_length=7,
            axis_config={"include_numbers": False, "include_tip": False, "include_ticks": False},
            color=GREY,
        )

        self.kruznice = self.osy.plot_parametric_curve(
            lambda t: np.array([np.cos(t),np.sin(t),0]),
            t_range=[0, 2 * PI],
            color=GREY,
        )

        self.velikost_uhlu = ValueTracker(90 * DEGREES)
        self.bodA = Dot(self.osy.c2p(1,0), color=RED)
        self.bodB = Dot(self.osy.c2p(0,1), color=RED)  # ten pohyblivy, souradnice se budou menit
        self.bodV = Dot(self.osy.c2p(0,0), color=RED)

        self.znakA = MathTex("A").next_to(self.bodA, UR)
        self.znakB = MathTex("B").next_to(self.bodB) 
        self.znakV = MathTex("V").next_to(self.bodV, DR * 0.5)

        self.poloprVA = Sdilene.do_poloprimky(Line(self.bodV, self.bodA))
        self.poloprVB = Sdilene.do_poloprimky(Line(self.bodV, self.bodB))
        self.chci_useckuVB = False
        
        self.uhel_symbol = Angle(self.poloprVA, self.poloprVB, radius=0.5, color=YELLOW)
        self.text_stupne = Integer(self.velikost_uhlu.get_value(), unit=r"^{\circ}").scale(1.0)
        self.text_radianu = MathTex("rad")
        
        # orientovany uhel popis pro stupne vpravo nahore
        self.or_uhel_popis = Integer(0, unit=r"^{\circ}", group_with_commas=False).scale(1.2).move_to(self.osy.c2p(1.5,1.2))
        
        self.vysec = self.osy.plot_parametric_curve(
            lambda t: np.array([np.cos(t),np.sin(t),0]),
            t_range=[0, PI],
            color=RED,
        )

        self.bodB.add_updater(update_bodB)
        self.poloprVB.add_updater(update_poloprVB)
        self.znakB.add_updater(update_znakB)
        self.vysec.add_updater(update_vysec)
        self.uhel_symbol.add_updater(lambda m: m.become(Angle(self.poloprVA, self.poloprVB, radius=0.5, color=YELLOW)))
        self.text_stupne.add_updater(update_text_stupne)
        self.text_radianu.add_updater(update_text_radianu)
        self.or_uhel_popis.add_updater(lambda m:m.set_value(self.velikost_uhlu.get_value() / DEGREES))


    def show(self):
        self.wait(2)


class Sablona_jednotkova_kruznice(Sdilene):
    
    def construct(self):
        self.camera.background_color = WHITE
        self.kruznice.color = BLACK
        self.osy.color = BLACK
        self.add(self.kruznice,self.osy)
        self.wait(1)

class Stupne_hadanka(Sdilene):

    def construct(self):

        self.velikost_uhlu.set_value(90 * DEGREES)
        self.znakB.update()
        self.bodB.update()
        self.poloprVB.update()
        self.text_stupne.update()

        self.osy.color = GREY

        self.add(
            self.kruznice,
            self.bodA, self.bodV, self.bodB,
            self.poloprVA, self.poloprVB,
            self.uhel_symbol,
            self.text_stupne,
            self.znakA, self.znakB, self.znakV,
            self.osy
        )

        for s in [180, 45]:
            bod_hadej = Dot(Sdilene.pozice_na_kruznici(self.osy, s * DEGREES),color=BLUE)
            self.add(bod_hadej)
            self.play(Flash(bod_hadej))
            self.next_slide()
            self.play(self.velikost_uhlu.animate.set_value(s * DEGREES),run_time=3, rate_func=smooth)
            self.play(FadeOut(bod_hadej))

        stare_s = s
        stary_bod = bod_hadej
        
        for s in [225, 135, 315, 270, 359.9]:
            bod_hadej = Dot(Sdilene.pozice_na_kruznici(self.osy, s * DEGREES),color=BLUE)
            self.add(bod_hadej)
            self.play(Flash(bod_hadej))
            self.next_slide()
            
            pomocna_tecna = TangentLine(self.kruznice, alpha=stare_s*DEGREES/2/PI, color=RED)
            vektor_tecny = pomocna_tecna.get_unit_vector() * np.sign(s - stare_s)
            koncovy_bod = stary_bod.get_center() + vektor_tecny
            sipka = Arrow(
                start=stary_bod.get_center(),
                end=koncovy_bod,
                buff=0
            )
            self.play(Write(sipka))
            popisek = Integer(s - stare_s, unit=r"^{\circ}", include_sign=True).move_to(koncovy_bod * 0.5)
            self.play(Write(popisek))
            self.next_slide()
            
            self.play(Unwrite(popisek), Unwrite(sipka))
            self.play(self.velikost_uhlu.animate.set_value(s * DEGREES),run_time=3, rate_func=smooth)
            self.play(FadeOut(bod_hadej))

            # pro dalsi iteraci
            stary_bod = bod_hadej
            stare_s = s




        self.next_slide()
        nula_stupnu = Integer(0, unit=r"^{\circ}").move_to(self.osy.c2p(0.2,0.2))
        text_rovnase = MathTex("A = B").move_to(self.osy.c2p(1.3,0.2))
        self.play(Unwrite(self.uhel_symbol), FadeOut(self.text_stupne), Write(nula_stupnu), Create(text_rovnase), FadeOut(self.znakB), FadeOut(self.znakA))
        self.wait(3)


    
class Stupne_symetrie(Sdilene):
    def construct(self):
        self.velikost_uhlu.set_value(33 * DEGREES)

        self.add(
            self.kruznice,
            self.bodA, self.bodV, self.bodB.update(),
            self.poloprVA, self.poloprVB.update(),
            self.uhel_symbol.update(),
            self.text_stupne.update(),
            self.osy
        )

        obraz_barva = XKCD.AVOCADO
        b = self.pozice_na_kruznici(33*DEGREES)
        b1 = self.pozice_na_kruznici((180-33)*DEGREES)
        b2 = self.pozice_na_kruznici((180+33)*DEGREES)
        b3 = self.pozice_na_kruznici((360-33)*DEGREES)
        vodorovna = DashedLine(b, b1) 
        db1 = Dot(b1, color=BLUE)
        db2 = Dot(b2, color=BLUE)
        db3 = Dot(b3, color=BLUE)
        svisla = DashedLine(b, b3)
        stredova = DashedLine(b, b2)

        self.next_slide()
        self.play(Write(vodorovna), Create(db1), run_time=1)
        self.play(Flash(db1))
        self.play(Write(stredova), Create(db2), rum_time=1)
        self.play(Flash(db2))
        self.play(Write(svisla), Create(db3), run_time=1)
        self.play(Flash(db3))
        self.next_slide()
        self.play(FadeOut(svisla), FadeOut(stredova))

        # vodorovny obraz
        poloprVB_obraz = Sdilene.do_poloprimky(Line(self.bodV, b1, color=obraz_barva))
        poloprVA_obraz = Sdilene.do_poloprimky(Line(self.bodV, self.osy.c2p(-1,0), color=obraz_barva))
        uhel_symbol_obraz = Angle(poloprVB_obraz, poloprVA_obraz, radius=0.5, color=obraz_barva)
        uhel_text_obraz = Integer(33, unit=r"^{\circ}").move_to(Sdilene.misto_pod_uhlem(self.osy, PI - 33*DEGREES/2))
        vyraz1 = MathTex("180^{\circ} = 33^{\circ} + 147^{\circ}").move_to(self.osy.c2p(1.5,1.2))
        vyraz2 = MathTex("180^{\circ} - 33^{\circ} = 147^{\circ}").next_to(vyraz1, DOWN)

        obrazy = VGroup(poloprVB_obraz, poloprVA_obraz, uhel_symbol_obraz, uhel_text_obraz)
        self.play(Create(obrazy))
        self.next_slide()
        
        self.play(self.velikost_uhlu.animate.set_value((180-33)*DEGREES), run_time=2, rate_func=smooth)
        self.play(Write(vyraz1))
        self.next_slide()
        self.play(TransformFromCopy(vyraz1, vyraz2))
        self.next_slide()
        self.play(Unwrite(vyraz1), Unwrite(vyraz2), FadeOut(obrazy), FadeOut(vodorovna), self.velikost_uhlu.animate.set_value(33*DEGREES), run_time=2, rate_func=smooth)

        # stredovy obraz
        poloprVB_obraz = Sdilene.do_poloprimky(Line(self.bodV, b2, color=obraz_barva))
        uhel_symbol_obraz = Angle(poloprVA_obraz, poloprVB_obraz, radius=0.5, color=obraz_barva)
        uhel_text_obraz.move_to(Sdilene.misto_pod_uhlem(self.osy, PI + 33*DEGREES/2))
        vyraz1 = MathTex("180^{\circ} + 33^{\circ} = 213^{\circ}").move_to(self.osy.c2p(1.5,1.2))
        obrazy = VGroup(poloprVB_obraz, poloprVA_obraz, uhel_symbol_obraz, uhel_text_obraz)
        self.play(FadeIn(obrazy), FadeIn(stredova))

        self.next_slide()        
        self.play(self.velikost_uhlu.animate.set_value((180)*DEGREES), run_time=2, rate_func=smooth)
        self.play(self.velikost_uhlu.animate.set_value((180+33)*DEGREES), run_time=1, rate_func=smooth)
        self.play(Write(vyraz1))
        self.next_slide()
        self.play(Unwrite(vyraz1), Uncreate(obrazy), Uncreate(stredova),self.velikost_uhlu.animate.set_value(33*DEGREES), run_time=2, rate_func=smooth)

        # svisly obraz
        poloprVB_obraz = Sdilene.do_poloprimky(Line(self.bodV, b3, color=obraz_barva))
        uhel_symbol_obraz = Angle(poloprVB_obraz, self.poloprVA, radius=0.5, color=obraz_barva)
        uhel_text_obraz = Integer(33, unit=r"^{\circ}").move_to(Sdilene.misto_pod_uhlem(self.osy, 2*PI - 33*DEGREES/2))
        vyraz1 = MathTex("360^{\circ} = 33^{\circ} + 327^{\circ}").move_to(self.osy.c2p(1.5,1.2))
        vyraz2 = MathTex("360^{\circ} - 33^{\circ} = 327^{\circ}").next_to(vyraz1, DOWN)
        obrazy = VGroup(poloprVB_obraz, uhel_symbol_obraz, uhel_text_obraz)
        self.play(FadeIn(obrazy), FadeIn(svisla))
        self.next_slide()
        
        self.play(self.velikost_uhlu.animate.set_value((327)*DEGREES), run_time=2, rate_func=smooth)
        self.play(Write(vyraz1))
        self.next_slide()
        self.play(TransformFromCopy(vyraz1, vyraz2))
        self.next_slide()
        self.play(Unwrite(vyraz1), FadeOut(obrazy), FadeOut(svisla), Unwrite(vyraz2))
        self.play(self.velikost_uhlu.animate.set_value((33)*DEGREES), run_time=3, rate_func=smooth)
        self.wait(1)



        
class Stupne_or_uhel_plus(Sdilene):
    def construct(self):

        pocet_tristasedesatek = MathTex("360^{\circ} + 60^{\circ}").move_to(self.osy.c2p(1.5,0.8))

        self.velikost_uhlu.set_value(60*DEGREES)

        self.add(
            self.kruznice,
            self.bodA, self.bodV, self.bodB.update(),
            self.znakA, self.znakV, self.znakB.update(),
            self.poloprVA, self.poloprVB.update(),
            self.uhel_symbol.update(),
            self.text_stupne.update(),
            self.osy,
            self.or_uhel_popis.update()
        )

        self.play(Write(self.uhel_symbol), Write(self.text_stupne))
        self.next_slide()

        self.play(self.velikost_uhlu.animate.set_value((360+60)*DEGREES), run_time=4, rate_func=smooth)
        self.play(Create(pocet_tristasedesatek))
        self.next_slide()
        self.play(self.velikost_uhlu.animate.set_value((2*360+60)*DEGREES), run_time=4, rate_func=smooth)
        self.play(Transform(pocet_tristasedesatek, MathTex("2 \cdot 360^{\circ} + 60^{\circ}").move_to(pocet_tristasedesatek)))
        self.next_slide()
        self.play(self.velikost_uhlu.animate.set_value((4*360+60)*DEGREES), run_time=4, rate_func=smooth)
        self.play(Transform(pocet_tristasedesatek, MathTex("4 \cdot 360^{\circ} + 60^{\circ}").move_to(pocet_tristasedesatek)))


class Stupne_or_uhel_minus(Sdilene):
    def construct(self):

        pocet_tristasedesatek = MathTex("-360^{\circ} + 60^{\circ}").move_to(self.osy.c2p(1.5,0.8))

        self.velikost_uhlu.set_value(60*DEGREES)

        self.add(
            self.kruznice,
            self.bodA, self.bodV, self.bodB.update(),
            self.znakA, self.znakV, self.znakB.update(),
            self.poloprVA, self.poloprVB.update(),
            self.uhel_symbol.update(),
            self.text_stupne.update(),
            self.osy,
            self.or_uhel_popis.update()
        )
        self.play(Write(self.uhel_symbol), Write(self.text_stupne))        
        self.next_slide()
        self.play(self.velikost_uhlu.animate.set_value((-360+60)*DEGREES), run_time=4, rate_func=smooth)
        self.play(Create(pocet_tristasedesatek))
        self.next_slide()
        self.play(self.velikost_uhlu.animate.set_value((-2*360+60)*DEGREES), run_time=4, rate_func=smooth)
        self.play(Transform(pocet_tristasedesatek, MathTex("-2 \cdot 360^{\circ} + 60^{\circ}").move_to(pocet_tristasedesatek)))
        self.next_slide()
        self.play(self.velikost_uhlu.animate.set_value((-4*360+60)*DEGREES), run_time=4, rate_func=smooth)
        self.play(Transform(pocet_tristasedesatek, MathTex("-4 \cdot 360^{\circ} + 60^{\circ}").move_to(pocet_tristasedesatek)))



class Stupne_or_uhel_ekvivalence(Sdilene):
    def construct(self):

        cil_pozice = Sdilene.pozice_na_kruznici(self.osy,210*DEGREES)
        cil_bod = Sdilene.bod_na_kruznici(self.osy, 210*DEGREES)
        cil_polopr = Sdilene.do_poloprimky(Line(self.osy.c2p(0,0), cil_pozice))
        cil_polopr.color = GREEN
        cil_uhel = Angle(self.poloprVA, cil_polopr, radius=0.5, color=GREEN)
        cil_uhel_text = Integer(210, unit="^{\circ}", color=GREEN).move_to(Sdilene.misto_pod_uhlem(self.osy, 195*DEGREES))

        self.add(
            self.kruznice,
            self.bodA, self.bodV, self.znakA, self.znakV, self.poloprVA,
            self.osy,
        )
        self.play(Write(cil_bod), Write(cil_polopr), Write(cil_uhel), Write(cil_uhel_text))
        self.next_slide()

        self.velikost_uhlu.set_value(0)
        self.add(
            self.or_uhel_popis.update(),
            self.bodB.update(), self.poloprVB.update(),
        )

        grupa = VGroup(self.bodB, self.poloprVB)

        # prvni velikost orientovaneho uhlu: 210 stupnu
        self.play(self.velikost_uhlu.animate.set_value((210)*DEGREES), run_time=3, rate_func=smooth)
        self.play(FadeOut(grupa))
        self.play(TransformFromCopy(self.or_uhel_popis, Integer(210, unit="^{\circ}").move_to(self.osy.c2p(0.2, -1.2))))
        self.next_slide()

        self.velikost_uhlu.set_value(0*DEGREES)
        grupa.update()
        self.or_uhel_popis.update()

        # druha velikost orientovaneho uhlu: -150 stupnu
        self.add(grupa)
        self.play(self.velikost_uhlu.animate.set_value((-360+210)*DEGREES), run_time=3, rate_func=smooth)
        self.play(FadeOut(grupa))
        self.play(TransformFromCopy(self.or_uhel_popis, Integer(-150, unit="^{\circ}").move_to(self.osy.c2p(0.7, -1.2))))
        self.next_slide()

        self.velikost_uhlu.set_value(0*DEGREES)
        grupa.update()
        self.or_uhel_popis.update()

        # treti velikost orientovaneho uhlu: 570 stupnu
        self.add(grupa)
        self.play(self.velikost_uhlu.animate.set_value((+360+210)*DEGREES), run_time=4, rate_func=smooth)
        self.play(FadeOut(grupa))
        self.play(TransformFromCopy(self.or_uhel_popis, Integer(570, unit="^{\circ}").move_to(self.osy.c2p(1.2, -1.2))))
        self.next_slide()

        self.velikost_uhlu.set_value(0*DEGREES)
        grupa.update()
        self.or_uhel_popis.update()

        # ctvrta velikost orientovaneho uhlu: - 870 stupnu
        self.add(grupa)
        self.play(self.velikost_uhlu.animate.set_value((-3*360+210)*DEGREES), run_time=5, rate_func=smooth)
        self.play(FadeOut(grupa))
        self.play(TransformFromCopy(self.or_uhel_popis, Integer(-870, unit="^{\circ}").move_to(self.osy.c2p(1.7, -1.2))))
        self.next_slide()

class Stupne_jako_cast_celku(Sdilene):
    def construct(self):
        self.wait()


class Delky_na_kruznici(Sdilene):

    def construct(self):
        
        polomer = Line(self.osy.c2p(1,0),self.osy.c2p(0,0), color=RED)
        znakR = MathTex("1").move_to(self.osy.c2p(0.5, -0.1))

        self.add(
            self.bodA, self.bodV, self.kruznice, self.znakA
        )
        self.play(Create(polomer), Create(znakR))
        self.next_slide()

        znakA_rovnase = MathTex("0").move_to(self.znakA, LEFT)
        self.play(Transform(self.znakA, znakA_rovnase))

        body = []
        texty = []
        vysece = []
        for i in range(1,7+1):
            body.append(Sdilene.bod_na_kruznici(self.osy,i))
            texty.append(Sdilene.udelej_popis(self.osy,i,str(i)))
            vysece.append(Sdilene.udelej_vysec(self.osy,i-1,i))

        self.next_slide()
        self.play(TransformFromCopy(polomer, vysece[0]),run_time=2)
        self.play(Create(body[0]), Create(texty[0]))
        self.next_slide()

        self.play(TransformFromCopy(polomer, vysece[1], run_time=1.5))
        self.play(Create(body[1]), Create(texty[1]))
        self.play(TransformFromCopy(polomer, vysece[2], run_time=1.5))
        self.play(Create(body[2]), Create(texty[2]))
        self.next_slide()

        text_stupne_des = DecimalNumber(0.0, 3, unit=r"^{\circ}", font_size=40).move_to(self.osy.c2p(0.4,0.2)) #desetinny
        text_stupne_des.add_updater(lambda m: m.set_value(self.velikost_uhlu.get_value() / DEGREES))

        self.chci_useckuVB = True
        self.poloprVB.update()
        self.velikost_uhlu.set_value(1)
        grupa = VGroup(self.bodB, self.uhel_symbol, self.poloprVB, text_stupne_des)
        grupa.update()
        self.play(FadeIn(grupa))
        self.wait(1)

        #self.next_slide()
        #self.play(self.velikost_uhlu.animate.set_value(3), run_time=3, rate_func=smooth)
        #self.wait(1)
        #self.next_slide()
        #self.play(FadeIn(self.osy), FadeOut(grupa))

        #bodPi = Sdilene.bod_na_kruznici(self.osy, PI)
        #textPi = Sdilene.udelej_popis(self.osy, 187 * DEGREES, r"P(\pi r)")

        #bodPi_pul = Sdilene.bod_na_kruznici(self.osy, PI/2)
        #textPi_pul = Sdilene.udelej_popis(self.osy, 83 * DEGREES, r"P(\tfrac{\pi}{2} r)")

        #bodPi_tripoloviny = Sdilene.bod_na_kruznici(self.osy, 3*PI/2)
        #textPi_tripoloviny = Sdilene.udelej_popis(self.osy, 263 * DEGREES, r"P(\tfrac{3 \pi}{2} r)")

        #self.velikost_uhlu.set_value(0.1)
        #self.add(self.bodB.update(), self.vysec.update())

        #self.play(self.velikost_uhlu.animate.set_value(PI), run_time=3, rate_func=smooth)
        #self.play(Create(bodPi))
        #self.play(Flash(bodPi), Write(textPi))
        #self.next_slide()
        #self.play(self.velikost_uhlu.animate.set_value(2*PI), run_time=3, rate_func=smooth)

        #znakA_rovnase = MathTex("A = P(0) = P(2 \pi r)").move_to(self.znakA, LEFT).shift(0.3 * LEFT)
        #self.play(Flash(self.bodA))
        #self.play(Transform(self.znakA, znakA_rovnase))

        #self.next_slide()

        #self.play(Create(bodPi_pul))
        #self.play(Flash(bodPi_pul), Write(textPi_pul))
        #self.play(Create(bodPi_tripoloviny))
        #self.play(Flash(bodPi_tripoloviny), Write(textPi_tripoloviny))
        #self.wait(1)

class Predstaveni_pi(Sdilene):
    def construct(self):
        self.wait(1)


class Radiany_zavedeni(Sdilene):

    def construct(self):
        # pridam zavedeni obloukove miry
        self.velikost_uhlu.set_value(1)

        #grupa - self.text_stupne
        #grupa + self.text_radianu.become(MathTex("1 rad"))
        #self.add(grupa.update())
        #self.next_slide()
        #self.play(self.velikost_uhlu.animate.set_value(2), self.text_radianu.animate.become(MathTex("2 rad")), run_time=1, rate_func=smooth)
        #self.next_slide()
        #self.play(self.velikost_uhlu.animate.set_value(PI/2), self.text_radianu.animate.become(MathTex(r"\tfrac{\pi}{2} rad")), run_time=1, rate_func=smooth)
        #self.next_slide()
        #self.play(self.velikost_uhlu.animate.set_value(3), self.text_radianu.animate.become(MathTex(r"3 rad")), run_time=1, rate_func=smooth)
        #self.next_slide()

