# A script to generate ghost files from lists of roms
# 

import os
import csv
import re


path="C:\\Projects\\Nitrofly\\nitrofly-frontend\\scripts\\gameLists"
dstPath = 'C:\\Projects\\Nitrofly\\nitrofly-frontend\\scripts\\ghostFiles'
dir = os.listdir(path)

for file in dir:
    with open(path + f"\{file}", "r") as f:
        reader = csv.DictReader(f, delimiter=";")
        games = [game['Game Name'] for game in list (reader)]
        print (games)
    f.close()

    #Create directory with name of source csv file
    newDir = dstPath + '\\' + file[:-4]
    try:
        os.mkdir(newDir)
    except:
        print('Folder already exists')
        pass
    # Create a ghost txt file for every game in each file
    for game in games:
        rawGame = re.sub('[!?<>:/*\"]', "", game)
        rawGame = re.sub('( +)\Z', " ", rawGame)
        rawGame = re.sub('  ', " ", rawGame)
        if rawGame[-1] == ' ':
            rawGame = rawGame[:-1]


        with open(newDir + "\\{}.txt".format(rawGame), "w") as out:
            out.write('0')
        out.close()
    
        



