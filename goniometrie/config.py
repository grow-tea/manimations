from manim import *
    
class GonioStyle:
    
    KRUZNICE_BARVA = GREY
    BODY_BARVA = RED
    BODY_BARVA2 = BLUE
    UHEL_BARVA = YELLOW
    VYSEC_BARVA = PURPLE
    KLADNE_OTOCENI_BARVA = GREEN
    ZAPORNE_OTOCENI_BARVA = ORANGE
    OBRAZ_BARVA = MAROON
    KRUHOVY_OBLOUK_BARVA = TEAL
    KRUHOVY_OBLOUK_ZAPORNE_BARVA = ORANGE

    SIN_BARVA = BLUE
    COS_BARVA = RED
    GONIO_FONT_VELIKOST = 40

    TLOUSTKA_KRUZNICE = 2

    OSY_CONFIG = {
        "x_range": (-1.3, 1.3, 0.1),
        "y_range": (-1.3, 1.3, 0.1),
        "x_length": 7,
        "y_length": 7,
        "axis_config": {
            "include_numbers": False, 
            "include_tip": False, 
            "include_ticks": False
        },
        "color": GREY,
    }

    # pro zavedeni gonio fci
    OSY_CONFIG_CARKY = {
        "x_range": (-1.3, 1.3, 0.1),
        "y_range": (-1.3, 1.3, 0.1),
        "x_length": 7,
        "y_length": 7,
        "axis_config": {
            "include_numbers": False,
            "include_tip": False, 
            "include_ticks": True
        },
        "color": GREY,
    }

    # pro gonio nacrtnuti grafu
    OSY_CONFIG_MENSI = {
        "x_range": (-1.3, 1.3, 0.2),
        "y_range": (-1.3, 1.3, 0.2),
        "x_length": 5,
        "y_length": 5,
        "axis_config": {
            "include_numbers": False,
            "include_tip": True, 
            "include_ticks": True
        },
        "color": GREY,
    }

    UHEL_SYMBOL = {
        "radius": 0.5,
        "color": UHEL_BARVA
    }

    SIN_TEXT = {
        "color": SIN_BARVA,
        "font_size": 40
    }

    COS_TEXT = {
        "color": COS_BARVA,
        "font_size": 40
    }

    VYSEC = {
        "color": VYSEC_BARVA,
        "fill_opacity": 0.4,
        "z_index": -1,  # pod ostatnimi
    }