from PIL import Image  
import datetime
import os

DictionairyOfSizes = {
    20 : 3,
    29 : 3,
    40 : 3,
    50 : 2,
    57 : 2,
    60 : 3,
    72 : 2,
    76 : 2,
    167 : 1,
    1024 : 1
}

CurrentDir = os.path.dirname(os.path.realpath(__file__))

TargetImage = Image.open(rf"{CurrentDir}/Source/Target.png")

FolderTimestamp = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')

Directory = rf"{CurrentDir}/Result/{FolderTimestamp}"

os.mkdir(Directory.replace("\\", "/"))

for key in list(DictionairyOfSizes.keys()):

    for i in range(1, int(DictionairyOfSizes[key]) + 1):

        if key == 60 and i == 1:
            continue

        NewImage = TargetImage.resize((int(key) * i,int(key) * i))

        if key != 167:
            if i != 1:
                ResolutionString = f"{str(key)}@{i}x"
            else:
                ResolutionString = str(key)
        else:
            ResolutionString = "83.5@2x"

        NewImage.save(f"{Directory}/Icon{ResolutionString}.png")

print("Successfully converted image")