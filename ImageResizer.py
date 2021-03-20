from PIL import Image  
from datetime import datetime
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

TargetImage = Image.open("./Source/Target.png")

FolderTimestamp = datetime.now()

Directory = f"./Result/{FolderTimestamp.strftime('''%d-%m-%Y-%H-%M-%S''')}"

os.mkdir(Directory)

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