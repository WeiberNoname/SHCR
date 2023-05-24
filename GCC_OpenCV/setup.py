from distutils.core import setup, Extension

module = Extension('image_display', sources=['image_display.cpp'], libraries=['opencv_core', 'opencv_imgcodecs', 'opencv_highgui'])

setup(name='image_display',
      version='1.0',
      description='OpenCV Image Display',
      ext_modules=[module])
