"""
To All Travelers, This Program is Great For Decluttering Your Desktop, HOWEVER
it deletes stuff. Make sure to finetune it to your needs before you let a random script you found
delete all your personal information. 

Thank You!
"""


import os
import shutil

files = os.listdir()

#Files to Delete
toDelete = {"svg", "stl", "jar", "msi", "zip", "iso"}

#Files to Move to a Media Folder
moveToMedia = {"png", "jpg", "mp4", "mp3", "m4a", "jpeg", "webm", "ogg", "wav", "webp"}

#Files to Move to a Scripts Folder
moveToScripts = {"py", "ahk"}

#Files to Move to a Shortcuts Folder
moveToShortcuts = {"lnk", "Lnk"}

#Files to Move to an Apps Folder
moveToApps = {"exe"}

if not os.path.exists("scripts"):
    os.mkdir("scripts")
if not os.path.exists("media"):
    os.mkdir("media")
if not os.path.exists("folders"):
    os.mkdir("folders")
if not os.path.exists("shortcuts"):
    os.mkdir("shortcuts")
if not os.path.exists("apps"):
    os.mkdir("apps")

print(files)
for file in files:
    if file == "debloat_desktop.py" or file == "scripts" or file == "media" or file == "folders" or file == "shortcuts":
        continue

    try:
        os.rmdir(file)
        continue
    except Exception as e:
        e

    if os.path.isdir(os.path.join(os.path.abspath("."), file)):
        try:
            shutil.move(file, "folders")
            continue
        except Exception as e:
            e

    if file.split(".")[-1].lower() in toDelete:
        try:
            os.remove(file)
            continue
        except Exception as e:
            e

    if file.split(".")[-1].lower() in moveToMedia:
        try:
            shutil.move(file, "media")
            continue
        except Exception as e:
            e

    if file.split(".")[-1].lower() in moveToScripts:
        try:
            shutil.move(file, "scripts")
            continue
        except Exception as e:
            e
            
    if file.split(".")[-1].lower() in moveToShortcuts:
        try:
            shutil.move(file, "shortcuts")
            continue
        except Exception as e:
            print(e)
            
    if file.split(".")[-1].lower() in moveToApps:
        try:
            shutil.move(file, "apps")
            continue
        except Exception as e:
            print(e)
                    
