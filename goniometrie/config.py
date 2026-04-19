from manim import *
import os

class GonioStyle:

    # Zjistíme, zda chceme světlý režim (výchozí je False)
    DM = not os.getenv("LIGHT_MODE", "false").lower() == "true"
    config.background_color = BLACK if DM else WHITE
    DEFAULT = WHITE if DM else BLACK # neni třeba

    # sablona
    KRUZNICE = {"color": GREY, "z_index": -3}
    TLOUSTKA_KRUZNICE = 2
    POMOCNA_CARA = {"color": WHITE if DM else BLACK, "z_index": -1}
    HLAVNI_CARA = {"color": WHITE if DM else BLACK, "z_index": 0}
    TEXT = {"color": WHITE if DM else BLACK}

    # zakladni nastroje (poloprimky maji defaultni bilou barvu)
    BOD_POHYB= {"color": RED, "z_index": 2}
    BOD_STATIC = {"color": RED_A if DM else RED_E, "z_index":1}
    POLOMER_TEXT = {"color": RED}
    POLOMER_USECKA = {"color": RED, "stroke_width": 4}
    
    # pro stupnovou miru
    UHEL_BARVA = YELLOW if DM else GOLD
    UHEL_SYMBOL = {"radius": 0.5, "color": UHEL_BARVA, "z_index": -1}
    UHEL_LABEL = {"color": YELLOW, "z_index": 1}
    UHEL_SVISLICE = {"color": YELLOW, "stroke_opacity": 0.5, "z_index": -2}

    # zlomky
    VYSEC_BARVA = YELLOW_E
    VYSEC = { "color": VYSEC_BARVA, "fill_opacity": 0.3, "z_index": -2 }
    VYSEC_TEXT = {"color": YELLOW_A if DM else BLACK}
    
    # pro obrazy, cile, veci k hadani
    BOD_HADEJ = {"color": BLUE, "z_index": 1}
    OBRAZ = {"color": BLUE_E if DM else BLUE_B, "z_index": -1}
    OBRAZ_TEXT = {"color": BLUE, "z_index": -1}
    UHEL_SYMBOL_OBRAZ = {"radius": 0.5, "color": BLUE_E if DM else BLUE_B, "z_index": -1}
    

    # pro obloukovou miru
    KLADNE_OTOCENI_BARVA = GREEN
    ZAPORNE_OTOCENI_BARVA = GOLD
    KRUZ_OBLOUK = {"color": GREEN_D if DM else GREEN_B, "stroke_width": 8}
    KRUZ_OBLOUK_ZAPORNE = {"color": GOLD_D if DM else GOLD_B, "stroke_width": 8}
    KRUZ_OBLOUK_BOD = {"color": GREEN_A if DM else GREEN_E, "z_index": 2}
    KRUZ_OBLOUK_BOD_ZAP = {"color": GOLD_A if DM else GOLD_E, "z_index": 2}
    KRUZ_OBLOUK_TEXT = {"color": GREEN_A if DM else GREEN_E, "font_size": 40}
    KRUZ_OBLOUK_TEXT_ZAP = {"color": GOLD_A if DM else GOLD_E, "font_size": 40}




    # sinus, kosinus
    SIN_TEXT = {"color": TEAL if DM else TEAL_E, "font_size": 40, "z_index": 3}
    SIN_BOD = {"color": TEAL_A if DM else TEAL_E, "z_index": 1}
    SIN_USECKA = {"color": TEAL_D if DM else TEAL_B, "stroke_width": 8, "z_index": 0}
    SINUSOIDA = {"stroke_color": TEAL_D if DM else TEAL_B, "stroke_width": 6}
    
    COS_TEXT = {"color": PURPLE_A if DM else PURPLE_E, "font_size": 40, "z_index": 3}
    COS_BOD = {"color": PURPLE_A if DM else PURPLE_E, "z_index": 1}
    COS_USECKA = {"color": PURPLE_B if DM else PURPLE_D, "stroke_width": 8, "z_index": 0}
    COSINUSOIDA = {"stroke_color": PURPLE_B if DM else PURPLE_D, "stroke_width": 6}

    # trojuhelnik zavedeni sin cos
    TROJUHELNIK = {"fill_color": WHITE if DM else BLACK, "stroke_color": WHITE if DM else BLACK, "fill_opacity": 0.3, "z_index": 0}

    # polarni souradnice
    POLARNI_BACKGROUND_LINE = {
        "stroke_color": BLUE_D if DM else BLUE_B,
        "stroke_width": 2,
        "stroke_opacity": 0.5
    }
    POLARNI_KRUZNICE = {"color": BLUE_E if DM else BLUE_A, "stroke_width": 6}

    BACKGROUND_RECTANGLE = {
        "color": BLACK if DM else WHITE,
        "opacity": 0.75,
        "buff": 0.2
    }


    OSY_CONFIG = {
        "x_range": (-1.3, 1.3, 0.1),
        "y_range": (-1.3, 1.3, 0.1),
        "x_length": 7,
        "y_length": 7,
        "axis_config": {
            "include_numbers": False, 
            "include_tip": False, 
            "include_ticks": False,
            "color": GREY,
        },
        "z_index": -4
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
            "include_ticks": True,
            "color": GREY,
        },
        #"color": GREY,
        "z_index": -4
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
            "include_ticks": True,
            "color": GREY
        },
        "z_index": -4
    }