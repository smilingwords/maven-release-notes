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

app_ver = xml_version[0].firstChild.data
app_name = xml_name[0].firstChild.data
app_msg = ""
app_use_tckt = ""

if xml_message:
    app_msg = xml_message[0].firstChild.data
if xml_use_ticket:
    app_use_tckt = xml_use_ticket[0].firstChild.data

app_ver_numbr, app_ver_suffix = app_ver.split('-')

release_suppfile = open(RELEASE_SUPPFILE_PATH, "a+")
release_suppfile.seek(0)

already_done = release_suppfile.readlines()

release_suppfile.close()

print("RELEASE NOTE GENERATOR")
print("Generating release notes for app '" +
      app_name+"' with version '"+app_ver_numbr+"'")

app_ver_full = app_ver_numbr+"\n"

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

append_text = "# Release version '"+app_ver_numbr+"'\n"+dt_string+"\n"+release_notes

releasemd = open(RELEASE_NOTES_PATH, "a")

try:
    releasemd.write(append_text+"\n\n")
except IOError:
    print("Error writing to RELEASE.md!")
else:
    print("Writing to RELEASE.md OK!")
    release_suppfile = open("release_supp.data", "a")
    try:
        release_suppfile.write(app_ver_numbr+"\n") == 0
    except IOError:
        print("Error writing to support file!")
    else:
        print("Writing to support file OK!")
    release_suppfile.close()

releasemd.close()

message_text = ""
if xml_message:
    if app_use_tckt == "true":
        print("Please write ticket and press Enter")
        ticket_txt = input()
        message_text = app_msg+app_ver_numbr+", "+ticket_txt
    elif app_use_tckt == "false":
        message_text = app_msg+app_ver_numbr

    subprocess.run(["git", "add", "--all"])
    subprocess.run(["git", "commit", "-m", message_text])
    subprocess.run(["git", "push"])

else:
    print("No message template defined in pom.xml file!")
    print("Perform commit of release manually!")
    quit()
