# ImageResizerIOSUE4
Resize images for ue4 iOS
Demo:

![image](https://user-images.githubusercontent.com/50122069/111879850-91cdcb80-897e-11eb-92c6-fc48f407d9f1.png)

Above in the folder is generated, below is the unreal folder

# Dependencies

- Datetime
- Os
- Pillow (You will have to pip3 install this)

# How to run

1. Clone this repository

2. After cloning, you will see two folders and the script

![image](https://user-images.githubusercontent.com/50122069/111879902-d22d4980-897e-11eb-9ad9-6b326b9cfbd5.png)

3. Go into the `./Source/` folder and put in your image, rename it to Target.png

![image](https://user-images.githubusercontent.com/50122069/111879914-deb1a200-897e-11eb-842c-6ab9284a893e.png)

Image stats:
- Resolution 5000x5000 recommended
- No alpha channel

4. Run the program with `python3 ImageResizer.py`, make sure you have the dependencies installed, and also make sure you are in the root directory, so it can detect your image.

You should recieve a "Successfully converted image" message, else something may have went wrong

![image](https://user-images.githubusercontent.com/50122069/111880030-6ac3c980-897f-11eb-826e-ac08c6dfa59e.png)

5. Go to the `./Result/` folder, and you should have a timestamped folder

![image](https://user-images.githubusercontent.com/50122069/111880050-829b4d80-897f-11eb-81b9-7e827466f8ec.png)

6. Go into the most recent folder, you should have the generated images here

![image](https://user-images.githubusercontent.com/50122069/111880064-9050d300-897f-11eb-8f66-63f1921442d1.png)


7. Drag and drop the images into the `YourUnrealProject/Build/IOS/Resources/Graphics` folder

![image](https://user-images.githubusercontent.com/50122069/111880188-4caa9900-8980-11eb-95b3-a0b83e5d9650.png)

8. It should update in the game engine after a restart

![image](https://user-images.githubusercontent.com/50122069/111880170-2b49ad00-8980-11eb-91cc-05b22095483f.png)

