from manim import *
from manim_slides import Slide
import numpy as np


class MovingCameraSlide(Slide, MovingCameraScene):
    pass

class Pythagoras(MovingCameraSlide):
    def construct(self):
        modra = "#3DA6E2"
        cervena = "#D81E1E"
        a = 3
        b = 2
        obsah = a*b/2
        c = np.sqrt(a**2 + b**2)
        vyska = 2*obsah / c

        self.camera.frame.save_state()

        def vzdyNavrch(mob):
            self.bring_to_front(mob)
        
        # objeveni trojuhelniku
        trojuhelnik = Polygon([0, 0, 0], [b, 0, 0], [0, a, 0])
        trojuhelnik.set_stroke(GREEN)
        self.camera.frame.move_to(trojuhelnik)
        self.play(Write(trojuhelnik))
        trojuhelnik.add_updater(vzdyNavrch)

        # objeveni praveho uhlu
        stranaA = Line([0,0,0], [0,a,0])
        stranaB = Line([0,0,0], [b,0,0])
        stranaC = Line([b,0,0], [0,a,0])
        uhel1 = RightAngle(stranaA, stranaB) 
        self.play(Write(trojuhelnik), Write(uhel1))
        uhel2 = uhel1.copy().shift([-a,-b,0])


        # popisky
        oznA = MathTex("a").next_to(trojuhelnik, LEFT, buff=0.1)
        oznA_orig = oznA.copy()
        oznB = MathTex("b").next_to(trojuhelnik, DOWN, buff=0.1)
        oznB_orig = oznB.copy()
        oznC = MathTex("c").move_to(stranaC).shift(0.2,0,0)
        for x in [oznA, oznB, oznC]:
            self.play(Write(x))

        self.next_slide() ######################################
        # vizualizace ctvercu a^2, b^2

        ctverecA = Polygon((0,0,0), (a,0,0), (a,a,0), (0,a,0)).set_fill(modra,opacity=0.5).set_stroke(modra)
        ctverecB = Polygon((0,0,0), (b,0,0), (b,b,0), (0,b,0)).set_fill(cervena,opacity=0.5).set_stroke(cervena)
        ctverecA.shift(a*LEFT)
        ctverecB.shift(b*DOWN)
        oznA2 = MathTex("a^2").move_to(ctverecA)
        oznB2 = MathTex("b^2").move_to(ctverecB)
        
        # pro recap na konci 
        ctverecA_orig = ctverecA.copy() 
        ctverecB_orig = ctverecB.copy()
        oznA2_orig = oznA2.copy()
        oznB2_orig = oznB2.copy()

        self.play(Write(ctverecA))
        self.play(Write(oznA2))
        self.play(Write(ctverecB))
        self.play(Write(oznB2))

        self.next_slide() #######################################
        # rovnobezky, priprava pro koseni 

        nahore = UP * self.camera.frame_height
        dole = DOWN * self.camera.frame_height
        nalevo = LEFT * self.camera.frame_width
        napravo = RIGHT * self.camera.frame_width

        svisla1 = Line(nahore, dole).set_color(GRAY)
        svisla2 = svisla1.copy().shift(a*LEFT)
        sipkaSvisle = DoubleArrow((a+0.5)*UP + a*LEFT, (a+0.5)*UP,buff=0, color=GRAY)
        oznA_sipka = oznA.copy().move_to(sipkaSvisle).shift(0.2 * UP)

        vodorovna1 = Line(nalevo, napravo).set_color(GRAY)
        vodorovna2 = vodorovna1.copy().shift(b*DOWN)
        sipkaVodorovne = DoubleArrow((b+0.5)*RIGHT, (b+0.5)*RIGHT + b*DOWN,buff=0, color=GRAY)
        oznB_sipka = oznB.copy().move_to(sipkaVodorovne).shift(0.2 * RIGHT)

        self.play(Write(svisla1), Write(svisla2))
        self.play(Write(sipkaSvisle), Write(oznA_sipka))
        self.play(Write(vodorovna1),Write(vodorovna2))
        self.play(Write(sipkaVodorovne), Write(oznB_sipka))

        self.play(Indicate(uhel1))      # upozorneni na pravy uhel
        self.play(Write(uhel2))
        
        self.next_slide() ##########################################
        # zkoseni ctverce a^2 a b^2

        rovnobeznikA = Polygon([-a,-b,0],[0,0,0], [0,a,0], [-a,-b+a,0]).set_fill(ctverecA.color, opacity=0.5).set_stroke(modra)
        self.play(oznA.animate.shift(a*LEFT))
        self.play(ReplacementTransform(ctverecA, rovnobeznikA), oznA2.animate.move_to(rovnobeznikA), oznA.animate.shift(b*DOWN))

        rovnobeznikB = Polygon([-a,-b,0], [-a+b,-b,0], [b,0,0], [0,0,0]).set_fill(ctverecB.color, opacity=0.5).set_stroke(cervena)     
        self.play(oznB.animate.shift(b*DOWN))
        self.play(ReplacementTransform(ctverecB, rovnobeznikB), oznB2.animate.move_to(rovnobeznikB), oznB.animate.shift(a*LEFT))

        self.next_slide() ##########################################
        # ukazani, ze delka stran je c

        # prvni shodny trojuhelnik
        self.play(FadeOut(uhel2, oznA2, oznB2))

        shodny1 = trojuhelnik.copy().rotate(- np.pi/2,about_point=[0,0,0]).shift([-a,0,0]).remove_updater(vzdyNavrch)
        uhel3 = RightAngle(
            Line(shodny1.get_vertices()[0], shodny1.get_vertices()[2]),
            Line(shodny1.get_vertices()[0], shodny1.get_vertices()[1])).set_color(GREEN)


        self.play(Write(shodny1), Write(uhel3))
        self.play(oznA_sipka.animate.shift((a+0.5)*DOWN), sipkaSvisle.animate.shift((a+0.5)*DOWN))
        self.play(FadeOut(sipkaSvisle), oznA_sipka.animate.set_color(GREEN))
        self.play(oznB_sipka.animate.shift((a+b+0.5)*LEFT), sipkaVodorovne.animate.shift((a+b+0.5)*LEFT))
        self.play(FadeOut(sipkaVodorovne), oznB_sipka.animate.set_color(GREEN))
        stranaC = Line([-a,-b,0], [0,0,0])
        oznC_2 = oznC.copy().move_to(stranaC).shift(0.4 * UP).set_color(GREEN)
        self.play(Write(oznC_2))
        oznC_3 = oznC_2.copy()
        oznC_4 = oznC_2.copy()
        self.play(oznC_3.animate.shift(a * UP).set_color(WHITE))
        self.play(oznC_4.animate.shift((b + 0.6)* RIGHT + (0.4 * DOWN)).set_color(WHITE))

        self.next_slide() ###########################################
        # posun rovnobezniku do jednoho ctverce

        self.play(Unwrite(shodny1), Unwrite(oznA_sipka), Unwrite(oznB_sipka), Unwrite(uhel3), Unwrite(oznC_2))
        self.play(FadeOut(svisla1), FadeOut(svisla2))
        self.play(FadeOut(vodorovna1), FadeOut(vodorovna2))

        # druhy shodny trojuhelnik
        shodny2 = trojuhelnik.copy().shift([-a,-b,0]).remove_updater(vzdyNavrch)
        uhel4 = RightAngle(Line([-a,-b,0], [-a,-b+a,0]), Line([-a,-b,0], [-a+b,-b,0])).set_color(GREEN)
        self.play(Write(shodny2), Write(uhel4))
        self.play(Unwrite(shodny2), Unwrite(oznA), Unwrite(oznB), Unwrite(uhel4))
        self.play(FadeIn(oznA2, oznB2))

        smer = [a / c * vyska, b / c * vyska, 0]
        obdelnikA = Polygon(rovnobeznikA.get_vertices()[0] + smer, rovnobeznikA.get_vertices()[1] + smer, rovnobeznikA.get_vertices()[2], rovnobeznikA.get_vertices()[3]).set_fill(rovnobeznikA.color, opacity=0.5)
        self.play(ReplacementTransform(rovnobeznikA, obdelnikA), oznA2.animate.move_to(obdelnikA))
        obdelnikB = Polygon(rovnobeznikB.get_vertices()[0] + smer, rovnobeznikB.get_vertices()[1], rovnobeznikB.get_vertices()[2], rovnobeznikB.get_vertices()[3] + smer).set_fill(rovnobeznikB.color, opacity=0.5)
        self.play(ReplacementTransform(rovnobeznikB, obdelnikB), oznB2.animate.move_to(obdelnikB))

        self.next_slide() ############################################
        # vizualizace ctverce c

        ctverecC = Polygon(obdelnikB.get_vertices()[1], obdelnikB.get_vertices()[2] ,obdelnikA.get_vertices()[2],obdelnikA.get_vertices()[3],).set_fill(GREEN, opacity=0.5)
        oznC2 = MathTex("c^2").move_to(ctverecC)
        self.play(FadeOut(obdelnikA, obdelnikB, oznA2, oznB2, oznC_3, oznC_4), FadeIn(ctverecC, oznC2))
        self.play(ctverecC.animate.shift([a, b, 0]), oznC2.animate.shift([a, b, 0]))

        self.next_slide()

        self.play(Write(oznA_orig), Write(oznB_orig))
        self.play(Write(ctverecA_orig), Write(ctverecB_orig))
        self.play(Write(oznA2_orig), Write(oznB2_orig))

        self.next_slide()


class BasicExample(Slide):

    def construct(self):
        circle = Circle(radius=3, color=BLUE)

        dot = Dot()


        self.play(GrowFromCenter(circle))


        self.next_slide(loop=True)

        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)

        self.next_slide()


        self.play(dot.animate.move_to(ORIGIN))
