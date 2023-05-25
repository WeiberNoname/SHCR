# SHCR(UI) [SH extension command repository] From article to practicle

> ## How can I write a python/c API to make a C++ opencv shared library to display an image in python?(using setup.py)  
* #### 1. Create a new file called `displayImage.cpp` and add C++ code within it.
* #### 2. Create a new file called `setup.py` in python.
```
from distutils.core import setup, Extension

module = Extension('displayImage', sources=['displayImage.cpp'], libraries=['opencv_core', 'opencv_imgcodecs', 'opencv_highgui'])

setup(name='displayImage',
      version='1.0',
      description='OpenCV Image Display',
      ext_modules=[module])
```
* #### 3. BUILD and INSTALL.
```
//python3 may vary on different OS.
python3 setup.py build
python3 setup.py install
```
### Exception:  fatal error: opencv2/opencv.hpp: No such file or directory
* #### Two potential solutions:
```
//First: Check environment variables for detail: 
printenv
```
* ##### This will be required when the python build and install command starts operating. 
```
export CPLUS_INCLUDE_PATH=/usr/include/opencv4
```
* ##### It can be used to set a specific path which the operating system should look forward to a shared library.
```
//A: Directory that contains libraries.
export LD_LIBRARY_PATH=/file/to/library_directory

//B: Specify two libraries:
export LD_LIBRARY_PATH=/path/to/library1:/path/to/library2
```
* #### 4. Create a new file called `example.py` in python.
```
import image_display
image_display.display_image('path/to/your/image.jpg')
```
* #### 5. Executing the program.
```
python3 example.py
```
![Screenshot 2023-05-24 215559](https://github.com/WeiberNoname/SHCR/assets/129390032/7b719512-3556-4226-a651-b9b3ec0474b1)

