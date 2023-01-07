from internetarchive import download
import os

def getFileCount():
    # folder path
    dir_path = r'D:\ROMS\GCN\rr-nintendo-gamecube-2\usa'
    count = 0
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    print('File count:', count)
    return count

while(getFileCount() <= 894):
    try: 
        download("rr-nintendo-gamecube-2", files="/usa",
            verbose = True, 
            destdir="D:\ROMS\GCN",
            formats="7z"
            )
        pass
    except:
        print("ERROR: Script Crashed Restarting")
    