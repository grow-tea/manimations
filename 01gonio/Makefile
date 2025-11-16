PYTHON_FILE := 01-uhly.py
SCENES := Sablona_jednotkova_kruznice Stupne_hadanka Stupne_symetrie Stupne_or_uhel_plus Stupne_or_uhel_minus Stupne_or_uhel_ekvivalence Radiany_zavedeni Delky_na_kruznici

#.PHONY: all $(SCENES) ahoj

all: $(SCENES)
	@echo ""

$(SCENES):
	manim -ql $(PYTHON_FILE) $@
	manim-slides convert $@ slides-publish/$@.html