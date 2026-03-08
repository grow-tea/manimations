#PYTHON_FILE := 01-uhly.py
SCENES := Souradnice Sinus Cosinus

#.PHONY: all $(SCENES) ahoj

all: $(SCENES)
	@echo ""

$(SCENES):
#	manim -ql $(PYTHON_FILE) $@
	manim-slides convert $@ slides-publish/$@.html