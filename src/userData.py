from PyQt5.QtWidgets import QWidget, QFileDialog
import os
import json

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
def storeRomData(dir: list[str], path):
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
            rom_data[file[:-4]] = {
                "system": extension_table[extension],
                "path": path + "/" + file,
                "has_video": True,
                "box2d": True,
                "box3d": True,
                "support": True,
                "alias": "None"
                }
        
        # TODO: Locate and store metadata locally
        # Set boolean to false if metadata not found

        # TODO: Re-initialize the gallery to inlcude newly added roms
    
    with open("userData/roms.json", "w") as f:
        json.dump(rom_data, f, indent = 4)