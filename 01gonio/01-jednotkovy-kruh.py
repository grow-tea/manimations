from manim import *
from manim_slides import Slide
import numpy as np

class Uvod_do_stupnu(Slide):

    def construct(self):
        
        ##### POMOCNE FUNKCE

        def do_poloprimky(usecka, ratio=100):
            delta = usecka.end - usecka.start
            usecka.put_start_and_end_on(usecka.start, usecka.end + ratio * delta)
            return usecka

        def update_bodB(mobject):
            uhel = velikost_uhlu.get_value() * np.pi / 180.
            novy_bod = osy.c2p(np.cos(uhel), np.sin(uhel))
            mobject.move_to(novy_bod)            

        def update_poloprVB(mobject):
            new_polopr = Line(osy.c2p(0,0), bodB)
            mobject.become(do_poloprimky(new_polopr))

        def update_uhel_popisek(mobject):
            polouhel = velikost_uhlu.get_value() * DEGREES / 2
            polobod = osy.c2p(np.cos(polouhel) * 0.5, np.sin(polouhel) * 0.5)
            mobject.set_value(velikost_uhlu.get_value())
            mobject.move_to(polobod)

        def update_znakB(mobject):
            uhel = (velikost_uhlu.get_value() - 10) * DEGREES  
            novy_bod = osy.c2p(np.cos(uhel) * 1.15, np.sin(uhel) * 1.15)
            mobject.move_to(novy_bod)

        ##### Zavedeni mobject promennych

        osy = Axes( 
            x_range=(-1.3, 1.3, 0.1),
            y_range=(-1.3, 1.3, 0.1),
            x_length=7,
            y_length=7,
            axis_config={"include_numbers": False},
        )
        kruznice = osy.plot_implicit_curve(lambda x, y: x*x + y*y - 1, color=BLUE)
        velikost_uhlu = ValueTracker(90)
        bodA = Dot(osy.c2p(1,0), color=RED)
        bodB = Dot(osy.c2p(0,1), color=RED)
        bodV = Dot(osy.c2p(0,0), color=RED)
        poloprVA = do_poloprimky(Line(bodV, bodA))
        poloprVB = do_poloprimky(Line(bodV, bodB))
        uhel_symbol = Angle(poloprVA, poloprVB, radius=0.5, color=YELLOW)
        uhel_popisek = Integer(uhel_symbol.get_value(degrees=True), unit=r"^{\circ}")
        uhel_popisek.next_to(uhel_symbol, UR)
        znakA = Tex("A").next_to(bodA, UR)
        znakB = Tex("B").next_to(bodB)
        

        bodB.add_updater(update_bodB)
        poloprVB.add_updater(update_poloprVB)
        uhel_symbol.add_updater(lambda m: m.become(Angle(poloprVA, poloprVB, radius=0.5, color=YELLOW)))
        uhel_popisek.add_updater(update_uhel_popisek)
        znakB.add_updater(update_znakB)

        self.add(kruznice, bodA, bodV, bodB, poloprVA, poloprVB, uhel_symbol, uhel_popisek, znakA, znakB)
        
        
        # prvni animace
        self.next_slide()
        self.play(velikost_uhlu.animate.set_value(60),run_time=4,rate_func=smooth)
        self.next_slide(1)
        self.play(velikost_uhlu.animate.set_value(260),run_time=4,rate_func=smooth)
        self.next_slide(1)
        self.play(velikost_uhlu.animate.set_value(30),run_time=4,rate_func=smooth)






































class Uvod_do_radianu(Slide):

    def construct(self):
        
        ##### POMOCNE FUNKCE

        def do_poloprimky(usecka, ratio=100):
            delta = usecka.end - usecka.start
            usecka.put_start_and_end_on(usecka.start, usecka.end + ratio * delta)
            return usecka

        def update_bodB(mobject):
            uhel = velikost_uhlu.get_value() * np.pi / 180.
            novy_bod = osy.c2p(np.cos(uhel), np.sin(uhel))
            mobject.move_to(novy_bod)            

        def update_poloprVB(mobject):
            new_polopr = Line(osy.c2p(0,0), bodB)
            mobject.become(do_poloprimky(new_polopr))

        def update_uhel_popisek(mobject):
            polouhel = velikost_uhlu.get_value() * DEGREES / 2
            polobod = osy.c2p(np.cos(polouhel) * 0.5, np.sin(polouhel) * 0.5)
            mobject.set_value(velikost_uhlu.get_value())
            mobject.move_to(polobod)

        def update_znakB(mobject):
            uhel = (velikost_uhlu.get_value() - 10) * DEGREES
            novy_bod = osy.c2p(np.cos(uhel) * 1.15, np.sin(uhel) * 1.15)
            mobject.move_to(novy_bod)

        def update_vysec(mobject):
            uhel = velikost_uhlu.get_value()
            nova_vysec = osy.plot_parametric_curve(
                lambda t: np.array([np.cos(t),np.sin(t),0]),
                t_range=[0, uhel * DEGREES],
                color=RED
            )
            mobject.become(nova_vysec)

        ##### Zavedeni mobject promennych

        osy = Axes( 
            x_range=(-1.3, 1.3, 0.1),
            y_range=(-1.3, 1.3, 0.1),
            x_length=7,
            y_length=7,
            axis_config={"include_numbers": False},
        )
        kruznice = osy.plot_parametric_curve(
            lambda t: np.array([np.cos(t),np.sin(t),0]),
            t_range=[0, 2 * PI],
            color="#0FF1CE",
        )
        vysec = osy.plot_parametric_curve(
            lambda t: np.array([np.cos(t),np.sin(t),0]),
            t_range=[0, PI],
            color=RED,
        )
        velikost_uhlu = ValueTracker(1 / DEGREES)
        bodA = Dot(osy.c2p(1,0), color=RED)
        bodB = Dot(osy.c2p(0,1), color=RED)
        bodV = Dot(osy.c2p(0,0), color=RED)
        poloprVA = do_poloprimky(Line(bodV, bodA))
        poloprVB = do_poloprimky(Line(bodV, bodB))
        uhel_symbol = Angle(poloprVA, poloprVB, radius=2.5, color=YELLOW)
        uhel_popisek = Integer(uhel_symbol.get_value(degrees=True), unit=r"^{\circ}")
        uhel_popisek.next_to(uhel_symbol, UR)
        znakA = Tex("A").next_to(bodA, UR)
        znakB = Tex("B").next_to(bodB)
        znakR = Tex("r").move_to(osy.c2p(0.5, -0.1))
        polomer = Line(osy.c2p(1,0),osy.c2p(0,0), color=RED)      

        bodB.add_updater(update_bodB)
        poloprVB.add_updater(update_poloprVB)
        uhel_symbol.add_updater(lambda m: m.become(Angle(poloprVA, poloprVB, radius=0.5, color=YELLOW)))
        uhel_popisek.add_updater(update_uhel_popisek)
        znakB.add_updater(update_znakB)
        vysec.add_updater(update_vysec)

        bodB.update()
        poloprVB.update()
        uhel_symbol.update()
        uhel_popisek.update()
        znakB.update()
        vysec.update()

        self.add(bodA, bodV, bodB, poloprVA, poloprVB, uhel_symbol, uhel_popisek, znakA, znakB, znakR, polomer)
        
        self.wait(4)
        self.play(ReplacementTransform(polomer, vysec),run_time=2)
        self.play(velikost_uhlu.animate.set_value(260),run_time=4,rate_func=smooth)



        self.play(velikost_uhlu.animate.set_value(60),run_time=4,rate_func=smooth)