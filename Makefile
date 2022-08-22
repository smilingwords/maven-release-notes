# THIS IS JUST EXAMPLE ON HOW TO USE WITH MAKEFILE and Maven

release: build rel_notes

build:

maven-release-notes:
	git clone git@github.com:smilingwords/maven-release-notes.git

rel_notes_clone: maven-release-notes

rel_notes_update: rel_notes_clone
	git -C maven-release-notes pull
	cp -a ./maven-release-notes/release-notes.py .

rel_notes: rel_notes_update
	python3 release-notes.py
