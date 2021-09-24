import xml.etree.ElementTree as ET 
import os
import glob

strSourcePath = "/home/jason/Desktop/arcade/"
strDestPath = "/home/jason/Desktop/arcade/"

arrayGamelist = []
arrayGameFileList = []

intISClone = 2
intGameName = 0
intLongName = 1

#Load and process XML File storing required info Name, Discription/Long name, Clone of the another game
# MAME0.78.xml is MAME 0.78.dat renamed
# Location of MAME 0.78.dat https://raw.githubusercontent.com/HerbFargus/retropie-dat/master/lr-mame2003/MAME%200.78.dat
filePath = os.path.abspath('MAME0.78.xml')
tree = ET.parse(filePath)
root = tree.getroot()

for xmlgame in root.findall("game"):
    strGameName = xmlgame.get('name')
    strGameDesc = xmlgame.find('description').text
    #check to see clone    
    if xmlgame.get('cloneof')  is None:
        arrayGamelist.append([strGameName,strGameDesc,"False"])
    else:
        arrayGamelist.append([strGameName,strGameDesc,"True"])




index = 0
#get zipped roms from path
for strFilePath in glob.iglob(strSourcePath + "*.zip",recursive=False):
    #get rom name with full path
    strFileGameNameFull = os.path.basename(strFilePath)
    #Take the .zip off the file name
    strFileGameName = strFileGameNameFull[:-4]
    #Loops thur all the games in the Game list Loaded from XML File
    for game in arrayGamelist:
        # if game in the path  is on the list then procede with Clone check and rename
        if game[0] == strFileGameName:
             if game[intISClone] == "False":
                strNewFileName = game[intLongName].replace("/","-") + ".zip"
             else:
                strNewFileName = game[intLongName].replace("/","-") + " Clone.zip"

             print(str(index) + ". Game Name: " + game[intLongName] + "   File Name: " + strNewFileName)
             os.rename( strSourcePath + strFileGameNameFull,strDestPath + strNewFileName)
    index = index + 1

#for game in arrayGamelist:
#    print(game)


