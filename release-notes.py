from datetime import datetime
from xml.dom import minidom

POMXML_PATH = "pom.xml"
RELEASE_SUPPFILE_PATH = "release_supp.data"
RELEASE_NOTES_PATH = "RELEASE.md"

pomxml = minidom.parse(POMXML_PATH)

xml_version = pomxml.getElementsByTagName('version')
xml_name = pomxml.getElementsByTagName('name')

app_ver = xml_version[0].firstChild.data
app_name = xml_name[0].firstChild.data

app_ver_num, app_ver_suffix = app_ver.split('-')

release_suppfile = open(RELEASE_SUPPFILE_PATH, "a+")
release_suppfile.seek(0)

already_done = release_suppfile.readlines()

release_suppfile.close()

print("RELEASE NOTE GENERATOR")
print("Generating release notes for app '" +
      app_name+"' with version '"+app_ver_num+"'")

app_ver_full = app_ver_num+"\n"

if app_ver_full in already_done:
    print("Release note already added! Quitting")
    quit()

print("Please write release notes and press Enter (End with Ctrl-D):")
release_notes_raw = []
while True:
    try:
        line = input()
    except EOFError:
        break
    release_notes_raw.append(line)

release_notes = ""

for note in release_notes_raw:
    release_notes += "* "+note+"\n"

# Datetime
now = datetime.now()
dt_string = now.strftime("Datetime: %d-%m-%Y %H:%M:%S")

append_text = "# Release version '"+app_ver_num+"'\n"+dt_string+"\n"+release_notes

releasemd = open(RELEASE_NOTES_PATH, "a")

try:
    releasemd.write(append_text+"\n\n")
except IOError:
    print("Error writing to RELEASE.md!")
else:
    print("Writing to RELEASE.md OK!")
    release_suppfile = open("release_supp.data", "a")
    try:
        release_suppfile.write(app_ver_num+"\n") == 0
    except IOError:
        print("Error writing to support file!")
    else:
        print("Writing to support file OK!")
    release_suppfile.close()

releasemd.close()
