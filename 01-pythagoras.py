from manim import *
import numpy as np

class Pythagoras(MovingCameraScene):
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



        # objeveni ctvercu pro a, b
        ctverecA = Polygon((0,0,0), (a,0,0), (a,a,0), (0,a,0)).set_fill(modra,opacity=0.5)
        ctverecB = Polygon((0,0,0), (b,0,0), (b,b,0), (0,b,0)).set_fill(cervena,opacity=0.5)
        ctverecA.shift(a*LEFT)
        ctverecB.shift(b*DOWN)        
        
        ctverecA_orig = ctverecA.copy() # pro recap na konci
        ctverecB_orig = ctverecB.copy()

        self.play(Write(ctverecA), run_time=2)
        self.play(Write(ctverecB), run_time=2)

        # popisky ke ctvercum
        oznA2 = MathTex("a^2").move_to(ctverecA)
        oznA2_orig = oznA2.copy()
        oznB2 = MathTex("b^2").move_to(ctverecB)
        oznB2_orig = oznB2.copy()
        self.play(Write(oznA2),Write(oznB2))

        # priprava pro rovnobezky
        nahore = UP * self.camera.frame_height
        dole = DOWN * self.camera.frame_height
        nalevo = LEFT * self.camera.frame_width
        napravo = RIGHT * self.camera.frame_width

        svisla1 = Line(nahore, dole)
        svisla2 = svisla1.copy().shift(a*LEFT)
        vodorovna1 = Line(nalevo, napravo)
        vodorovna2 = vodorovna1.copy().shift(b*DOWN)

        # zkoseni ctvercu
        self.play(Write(svisla1), Write(svisla2))
        rovnobeznikA = Polygon(ctverecA.get_vertices()[0] + b*DOWN, ctverecA.get_vertices()[1], ctverecA.get_vertices()[2], ctverecA.get_vertices()[3] + b*DOWN).set_fill(ctverecA.color, opacity=0.5)
        self.play(ReplacementTransform(ctverecA, rovnobeznikA), oznA2.animate.move_to(rovnobeznikA))
        oznA_1 = oznA.copy().shift([-a,-b,0])
        self.play(ReplacementTransform(oznA, oznA_1))

        self.play(Write(vodorovna1),Write(vodorovna2))
        self.play(Indicate(uhel1))
        self.play(Write(uhel2))

        rovnobeznikB = Polygon(ctverecB.get_vertices()[0] + a*LEFT, ctverecB.get_vertices()[1] + a*LEFT, ctverecB.get_vertices()[2], ctverecB.get_vertices()[3]).set_fill(ctverecB.color, opacity=0.5)        
        self.play(ReplacementTransform(ctverecB, rovnobeznikB), oznB2.animate.move_to(rovnobeznikB))
        oznB_1 = oznB.copy().shift([-a,-b,0])
        self.play(ReplacementTransform(oznB, oznB_1))

        # prvni shodny trojuhelnik
        self.play(FadeOut(uhel2))
        for x in [svisla1, svisla2, vodorovna1, vodorovna2, oznA2, oznB2]:
            x.set_color(GREY)

        shodny1 = trojuhelnik.copy().rotate(- np.pi/2,about_point=[0,0,0]).shift([-a,0,0]).remove_updater(vzdyNavrch)
        oznA_2 = oznA.copy().move_to(Line(shodny1.get_vertices()[0], shodny1.get_vertices()[2])).shift(0.2 * DOWN).set_color(GREEN)
        oznB_2 = oznB.copy().move_to(Line(shodny1.get_vertices()[0], shodny1.get_vertices()[1])).shift(0.2*RIGHT).set_color(GREEN)
        self.play(Write(shodny1), Write(oznA_2), Write(oznB_2))
        stranaC = Line([-a,-b,0], [0,0,0])
        oznC_2 = oznC.copy().move_to(stranaC).shift(0.4 * UP)
        self.play(Write(oznC_2))
        oznC_3 = oznC_2.copy()
        oznC_4 = oznC_2.copy().shift((b + 0.6)* RIGHT + (0.4 * DOWN))
        self.play(oznC_3.animate.shift(a * UP))
        self.play(TransformMatchingShapes(oznC_2, oznC_4))
        self.play(Unwrite(shodny1), Unwrite(oznA_2), Unwrite(oznB_2))

        self.play(FadeOut(svisla1), FadeOut(svisla2))
        self.play(FadeOut(vodorovna1), FadeOut(vodorovna2))

        shodny2 = trojuhelnik.copy().shift([-a,-b,0]).remove_updater(vzdyNavrch)
        self.play(Write(shodny2))
        self.play(Unwrite(shodny2), Unwrite(oznA_1), Unwrite(oznB_1))

        smer = [a / c * vyska, b / c * vyska, 0]
        obdelnikA = Polygon(rovnobeznikA.get_vertices()[0] + smer, rovnobeznikA.get_vertices()[1] + smer, rovnobeznikA.get_vertices()[2], rovnobeznikA.get_vertices()[3]).set_fill(rovnobeznikA.color, opacity=0.5)
        self.play(ReplacementTransform(rovnobeznikA, obdelnikA), oznA2.animate.move_to(obdelnikA))
        obdelnikB = Polygon(rovnobeznikB.get_vertices()[0] + smer, rovnobeznikB.get_vertices()[1], rovnobeznikB.get_vertices()[2], rovnobeznikB.get_vertices()[3] + smer).set_fill(rovnobeznikB.color, opacity=0.5)
        self.play(ReplacementTransform(rovnobeznikB, obdelnikB), oznB2.animate.move_to(obdelnikB))

        ctverecC = Polygon(obdelnikB.get_vertices()[1], obdelnikB.get_vertices()[2] ,obdelnikA.get_vertices()[2],obdelnikA.get_vertices()[3],).set_fill(GREEN, opacity=0.5)
        oznC2 = MathTex("c^2").move_to(ctverecC)
        self.play(FadeOut(obdelnikA, obdelnikB, oznA2, oznB2, oznC_3, oznC_4), FadeIn(ctverecC, oznC2))
        self.play(ctverecC.animate.shift([a, b, 0]), oznC2.animate.shift([a, b, 0]))
        self.play(Write(oznA_orig), Write(oznB_orig))
        self.play(Write(ctverecA_orig), Write(ctverecB_orig))
        self.play(Write(oznA2_orig), Write(oznB2_orig))

        self.wait(2)