# Translator



For the documentation of the library check [here](https://github.com/Disk-MTH/Translator/blob/master/diskmth/README.md).


## Overview

This library allows you to manage a translation system in an extremely simple way.   
It supports compilation with Pyinstaller (you just need to include the translation files when compiling and setup correctly the library).

## Installation

Installation with [pip](https://pypi.org/project/pip/):
```bash
pip install translator
```
Installation with [files](https://github.com/Disk-MTH/Translator/releases):

Build or [download](https://github.com/Disk-MTH/Translator/releases) the library and in the folder where the .whl file is, open a command promt and execute:
```bash
pip install your_file_name.whl
```

## How to edit ?

This project is completely self-contained: you don't need to have python installed, or anything else!

****/!\ WARNING :****

If during one of the following steps a SmartScreen window opens saying "SmartScreen to protect your computer", this is normal: the .exe files (which I made entirely myself) do not have a digital signature therefore windows defender is in panic. (If ever you do not trust my scripts do not go further because you will necessarily need them! Moreover you can see their "contents" in the "[uncompiled scripts](https://github.com/Disk-MTH/Translator/tree/master/scripts/uncompiled%20scripts)" folder).

Once the environment is setup (see below), it will take VERY long to move the folder, so choose a "permanent" location!

1.  Download :

To start, above the frame containing the code, there is a green button titled "Code", click on it, then on "Download ZIP" (or use  [this link](https://github.com/Disk-MTH/Translator/archive/refs/heads/master.zip)). This will download you a .zip folder which you will need to extract (I recommend extracting to a "permanet" location).

2.  Setup :

(Warning : This step can be very long (depends on your computer))

Then in the unzipped folder find the "[scripts](https://github.com/Disk-MTH/Translator/tree/master/scripts)" folder and run the "setup.exe" file. This will open a window of the control terminal in which you will be able to follow the decompilation of the integrated python interpreter. (If you go back to the root folder of the project you can find a "python" folder that has been created).

/!\ : In case of update, if you resetup the python environment, it will overwrite the old one

3. Edit the code.


4.  Build :

To compile the program, nothing could be easier: all you have to do is run the "build.exe" file and a control terminal window will open. Wait for the end of the execution (when the terminal displays "press a key to continue ...") and you will see in the [diskmth](https://github.com/Disk-MTH/Translator/tree/master/diskmth) folder a "dist" folder in which 1 .tar.gz file and 1 .whl file will be present. The .whl is the compiled version of the library.

/!\ : If you ever rebuild the program after making changes, the program will overwrite the old build files.

## License

All the files in this repository are completely free of rights (see the  [license](https://github.com/Disk-MTH/Translator/blob/master/license.txt)) so you can grab the code and do whatever you want with them (just respect the  [license](https://github.com/Disk-MTH/Translator/blob/master/license.txt)).

Thanks for reading and good development!

Disk_MTH