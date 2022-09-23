from datetime import datetime
from xml.dom import minidom
import subprocess

POMXML_PATH = "pom.xml"
RELEASE_SUPPFILE_PATH = "release_supp.data"
RELEASE_NOTES_PATH = "RELEASE.md"

pomxml = minidom.parse(POMXML_PATH)

xml_version = pomxml.getElementsByTagName('version')
xml_name = pomxml.getElementsByTagName('name')
xml_message = pomxml.getElementsByTagName('message')
xml_use_ticket = pomxml.getElementsByTagName('use-ticket')

app_version = xml_version[0].firstChild.data
app_name = xml_name[0].firstChild.data
app_message = ""
app_use_ticket = ""

if xml_message:
    app_message = xml_message[0].firstChild.data
if xml_use_ticket:
    app_use_ticket = xml_use_ticket[0].firstChild.data

app_version_number, app_version_suffix = app_version.split('-')

release_suppfile = open(RELEASE_SUPPFILE_PATH, "a+")
release_suppfile.seek(0)

already_done = release_suppfile.readlines()

release_suppfile.close()

print("RELEASE NOTE GENERATOR")
print("Generating release notes for app '" +
      app_name+"' with version '"+app_version_number+"'")

app_version_full = app_version_number+"\n"

if app_version_full in already_done:
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

append_text = "# Release version '"+app_version_number+"'\n"+dt_string+"\n"+release_notes

releasemd = open(RELEASE_NOTES_PATH, "a")

try:
    releasemd.write(append_text+"\n\n")
except IOError:
    print("Error writing to RELEASE.md!")
else:
    print("Writing to RELEASE.md OK!")
    release_suppfile = open("release_supp.data", "a")
    try:
        release_suppfile.write(app_version_numbr+"\n") == 0
    except IOError:
        print("Error writing to support file!")
    else:
        print("Writing to support file OK!")
    release_suppfile.close()

releasemd.close()

# default value
message_text = app_message+app_version_number

if xml_message:
    if app_use_tckt == "true":
        print("Please write ticket and press Enter")
        ticket_txt = input()
        message_text = app_message+app_version_number+", "+ticket_txt

    subprocess.run(["git", "add", "RELEASE.md", "release_supp.data"])
    subprocess.run(["git", "commit", "-m", message_text])
    subprocess.run(["git", "push"])

else:
    print("No message template defined in pom.xml file!")
    print("To configure pom.xml follow steps in part How to run? in README file)")
    print("Now perform commit of release notes manually!")
    quit()