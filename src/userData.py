from PyQt5.QtWidgets import QWidget, QFileDialog
import os
import json
import js2py

# NOTE: Firebase has a shitty dependency list that cant find the Crypto module... because it doesnt exist
# QUICK FIX: Change the package name in your package manager from crypto to Crypto.
# This is incredibly stupid and I dont know how Firebase got this past production
from firebase import Firebase

# TODO: Add MAME, SNES, and other exentsions
extension_table = {
    "gba": "GBA",
    "z64": "N64",
    "cia": "3DS",
    "3ds": "3DS",
    "nds": "NDS",
    "pbp": "PS1",
}

# Opens dialogue to select a rom path and store the data
def selectDirectory(parent: QWidget):
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.Directory)
    path = dialog.getExistingDirectory(parent)

    if path == "":
        return

    print(path)

    files = os.listdir(path)
    storeRomData(files, path)

# Catalogue data in roms.json for future
def storeRomData(dir: list[str], path: str):
    system = None
    if dir == []:
        print("No rom files detected")
        return
    with open("userData/roms.json") as f:
        rom_data = json.load(f)

    for file in dir:
        extension = file.split(".")[-1]
        if extension == "iso":
            #TODO: generate iso dialogue
            print(f"Found iso {file}, select corrosponding system")
            # Retreive user input for system
            pass

        if extension in extension_table.keys():
            system = extension_table[extension]
            romName = file[:-4]

            # TODO: Implement search engine to look for standardized name given file name
            # and add that name to the file's alias
            accessFirebase(romName, system)
            # TODO: Set boolean to false in json if metadata not found

            rom_data[file[:-4]] = {
                "system": extension_table[extension],
                "path": path + "/" + file,
                "has_video": True,
                "box2d": True,
                "box3d": False,
                "support": True,
                "alias": "None"
                }
    
    with open("userData/roms.json", "w") as f:
        json.dump(rom_data, f, indent = 4)

# name: Normalized rom name without file extension
def accessFirebase(name: str, system: str):
    config = {
        "apiKey": "AIzaSyBDbgHUYImNeapL2bFBW2CEwNaeIBaaZIk",
        "authDomain": "nitrofly-2f5d0.firebaseapp.com",
        "projectId": "nitrofly-2f5d0",
        "storageBucket": "nitrofly-2f5d0.appspot.com",
        "messagingSenderId": "958552361171",
        "appId": "1:958552361171:web:e633bc03086c8fd7a4ac26",
        "measurementId": "G-Z3NQH7KNGR",
        "databaseURL": "",
    }

    firebase = Firebase(config)
    storage = firebase.storage()

    coverRef = "Metadata/" + system + "/box2dfront/" + name + ".png"
    videoRef = "Metadata/" + system + "/video/" + name + ".mp4"
    supportRef = "Metadata/" + system + "/support/" + name + ".png"
    # romRef = "Roms/" + system + "/" + name + ".gba";

    #TODO: Create folders for metadata if they do not already exist
    folders = os.listdir("./metadata")
    if system not in folders:
        os.mkdir(f"./metadata/{system}")
        os.mkdir(f"./metadata/{system}/box2dfront")
        os.mkdir(f"./metadata/{system}/videos")
        os.mkdir(f"./metadata/{system}/support")
    #Plan: Initialize {system}/box2d./videos./support on new system
    storage.child(coverRef).download(f"metadata/{system}/box2dfront/" + name + ".png")
    storage.child(videoRef).download(f"metadata/{system}/videos/" + name + ".mp4")
    storage.child(supportRef).download(f"metadata/{system}/support/" + name + ".png")


def debug():
    accessFirebase("Pokemon - Emerald Version (U)", "GBA")

# debug()