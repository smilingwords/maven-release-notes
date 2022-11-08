# Maven release notes script

Release notes script for maven projects which is working based on pom.xml file in current folder.
Uses pom.xml file to generate structured release notes (RELEASE.md) file

## Release notes workflow

* Release notes are generated automatically by script
* As result script generates two files: RELEASE.md and release_supp.data
* RELEASE.md file and release_supp.data file are added to be commited automatically by script
* RELEASE.md file and release_supp.data file are commited and pushed automatically by script

## How to run?

* Copy release-notes.py file to the folder where pom.xml exists
* Configure pom.xml file to commit and push generated files automatically by script:
  * add and configure profile with id 'release' into profiles
  * example of pom.xml configuration:

      <profile>
          <id>production</id>
          <properties>
              <release-notes-message>chore: release</release-notes-message>
              <use-release-notes-ticket>true</use-release-notes-ticket>
              ...
          </properties>
      </profile>

* Run ```python3 release-notes.py```
* Run through based on instructions
* On the end, the script will generate two files:
  * First, 'release_supp.data' for data of which release was already added to RELEASE.md
  * Second, 'RELEASE.md' for release notes itself
