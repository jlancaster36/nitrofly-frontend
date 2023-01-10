from internetarchive import download
import os

def getFileCount():
    # folder path
    dir_path = r'D:\ROMS\PS2\ps2usaredump1'
    count = 0
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    print('File count:', count)
    return count

while(getFileCount() <= 706):
    try: 
        download("ps2usaredump1", files="/usa",
            verbose = True, 
            destdir="D:\ROMS\PS2",
            formats="7z"
            )  
    except:
        print("ERROR: Script Crashed Restarting")
    