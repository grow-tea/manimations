from manim import *

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7)
        right_square = Square(color=GREEN, fill_opacity=0.7).next_to(left_square)
        self.play(
            left_square.animate.rotate(PI),
            Rotate(right_square, angle=PI),
            run_time = 2
        )

class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(a))
    

    def construct(self):
        self.transform()
        self.wait(0.5)