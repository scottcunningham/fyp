default: build spell
	cp thesis.pdf /home/scott/Dropbox/FYP/draft.pdf

spell:
	for x in `ls ch*tex`; \
		do aspell -c $$x; \
	done && \
	echo "Spell-check pass"

build:
	pdflatex thesis && bibtex thesis && pdflatex thesis && pdflatex thesis
