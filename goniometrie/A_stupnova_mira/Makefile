#PYTHON_FILE := 01-uhly.py
SCENES := Zlomky_na_stupne Stupne_na_zlomky Smery_otaceni Vodorovna_symetrie Svisla_symetrie Stredova_soumernost Stupne_or_uhel_plus Stupne_or_uhel_minus Stupne_or_uhel_ekvivalence  

#.PHONY: all $(SCENES) ahoj

all: $(SCENES)
	@echo ""

$(SCENES):
#	manim -ql $(PYTHON_FILE) $@
	manim-slides convert $@ slides-publish/$@.html