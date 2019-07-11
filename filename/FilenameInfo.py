import re
filename = "EP103_SQ001_SH0170_LGT_v004.ma"

def FilenameInfo(filename):
    # Inicializate the dictionary
    fileDict = {}
    # Remove the file extension
    filenameNoExt    = filename.split('.') [0]
    filenameSplit    = filenameNoExt.split('_')
    filenameIndex    = len(filenameSplit) - 1;

    # Format alphanumeric fields
    for i in range(filenameIndex):
        if (len(filenameSplit[i]) > 3):
            filenameSplit[i] = re.sub("[^0-9]", "", filenameSplit[i]).strip("0")

    # Once formatted, assign the values to each section
    episode         = filenameSplit[0]
    sequence        = filenameSplit[1]
    shot            = filenameSplit[2]
    departament     = filenameSplit[3]
    version         = filenameSplit[4]

    # Add the formatted values to the dictionary
    fileDict["Episode"]     = episode
    fileDict["Sequence"]    = sequence
    fileDict["Shot"]        = shot
    fileDict["Department"]  = departament
    fileDict["Version"]     = version

    print("File info is ", fileDict)
    return fileDict;

FilenameInfo(filename)
