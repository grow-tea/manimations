from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *
from goniometrie.config import GonioStyle as gs

from Stupne_symetrie import *

class Svisla_symetrie(Stupne_symetrie):
    def operace(self, stupen):
        return 360 - stupen

    poc_uhel = 33
    koncovy_uhel = 360 - poc_uhel
    A_to_B = False

    vyraz = MathTex("360^{\circ} - "+ str(poc_uhel) +"^{\circ} = " + str(koncovy_uhel) + "^{\circ}", **gs.TEXT)
