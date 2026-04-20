from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *
from goniometrie.config import GonioStyle as gs

from Stupne_symetrie import *


class Stredova_soumernost(Stupne_symetrie):
    def operace(self, stupen):
        return stupen + 180

    A_to_B = True # jako obraz se zobrazi uhel AVB, ne BVA

    poc_uhel = 33
    koncovy_uhel = 180 + poc_uhel

    vyraz = MathTex("180^{\circ} + "+ str(poc_uhel) +"^{\circ} = " + str(koncovy_uhel) + "^{\circ}", **gs.TEXT)