DIRS := A_stupnova_mira B_obloukova_mira C_goniometricke_fce
GLOBAL_DEPS := config.py jednotkova_kruznice.py
SRCS := $(foreach dir,$(DIRS),$(wildcard $(dir)/[0-9][0-9]_*.py))
HTML_TARGETS := $(foreach src,$(SRCS),$(dir $(src))slides_publish/$(notdir $(src:.py=.html)))
MANIM_FLAGS := -ql

all: $(HTML_TARGETS)

define render_rule
$(dir $(1))slides_publish/$(notdir $(1:.py=.html)): $(1) $(GLOBAL_DEPS)
	mkdir -p $$(dir $$@)
	$$(eval CLASS_NAME := $$(shell echo $$(notdir $$(basename $(1))) | cut -c 4-))
	manim $(MANIM_FLAGS) $(1) $$(CLASS_NAME)
	manim-slides convert $$(CLASS_NAME) $$@
endef

$(foreach src,$(SRCS),$(eval $(call render_rule,$(src))))

clean:
	rm -rf ./media ./slides $(foreach dir,$(DIRS),$(dir)slides_publish)       