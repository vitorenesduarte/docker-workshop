OS := $(shell uname)
ifeq ($(OS), Linux)
    VIEWER=evince
else ifeq ($(OS), Darwin)
    VIEWER=open -a Skim
endif

pdfs:
	bin/to_pdf.sh 1/README.md
	$(VIEWER) 1/README.pdf
