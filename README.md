# Maven release notes script
Release notes script for maven projects which is working based on pom.xml file in current folder.
Uses pom.xml file to generate structured release notes (RELEASE.md) file

## How to run?
* Copy release-notes.py file to the folder where pom.xml exists
* Run ```python3 release-notes.py```
* Run through based on instructions
* On the end, the script will generate two files:
    * First, 'release_supp.data' for data of which release was already added to RELEASE.md
    * Second, 'RELEASE.md' for release notes itself
