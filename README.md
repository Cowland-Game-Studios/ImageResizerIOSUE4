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

