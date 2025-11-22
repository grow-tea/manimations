#PYTHON_FILE := 01-uhly.py
SCENES := Jednotkove_delky_na_kruznici Radiany_na_stupne Zlomky_na_radiany

#.PHONY: all $(SCENES) ahoj

all: $(SCENES)
	@echo ""

$(SCENES):
#	manim -ql $(PYTHON_FILE) $@
	manim-slides convert $@ slides-publish/$@.html