from manim import *
from manim_slides import Slide

# add project root to PYTHONPATH so "goniometrie" package can be imported
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from goniometrie.jednotkova_kruznice import *

from Stupne_or_uhel import *


class Stupne_or_uhel_plus(Stupne_or_uhel):
    zastavky = [420, 780, 1500]


