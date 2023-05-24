# SHCR(UI) [SH extension command repository] From article to practicle
> ## What is pyinstaller?
 * #### `pip install pyinstaller` Complete Pyinstaller installation.
 * #### `pip install --upgrade pyinstaller` Upgrade Pyinstaller to the existing latest version.
 * #### `pyinstaller fileName.py` The executable file creation.

> ## What is .sh extension file?  
* #### `fileName.sh` This is a script language type, and executed by Unix Shell. [Can be used to control linux system]
> ## What is Unix Shell? 
* #### Unix Shell : which is a interpreter for running the command line as an interface for client to use, and performed by the computer operating system to manipulate the instruction that script within the file.
* #### User also introduce a method that directly visit the Secure Shell, here's an example:
	##### `ls -l | grep key | less`
	###### The concept of pipeline(Unix) is like to split each word apart and concurrently executed and input for next instruction or send back exception sentences, perform input and output syntax analyze. 
> ## What is Secure Shell? 

* #### Secure Shell (Protocol, also called SSH): Is to substitute unsecured protocol like Unix shell protocol, which means the unix-like system will regard this protocol seriously and Unix shell insecure side (but just because it facilitates in a cross server usage, it is useful in specific situations to use). For an example:
	##### `ssh -1 user@host` Forces to use SSH-1 proctocol version(version is crucially and influencial) 

> ## What is Remote Shell? 
* #### editing
> ### How to connect python with c?(calling from python)
* #### Here is an interesting topic, I remember the discrepancy between `communication` and `calling` words, so here is the difference introducing a different method that can be `scam` or `extraordinarily useful function`.
* ##### C program called test.c
```
#include <stdio.h>
int plus(int i){
return i+1;
}
```
* ##### We can use this command to creat a .so extension file, used to compile and build a shared library.
```
cc -fPIC -shared -o test.so test.c 
```
* ##### python code called python.py
```
from ctypes import *
extension_so = "directory/of/test.so"
method =  CDLL(extension_so)
print(type(method))
print(method.plus(1))
```
* ##### compile
```
python3 python.py
```
* #### output : 2
c
> ### How to write a C program as python's library?(Python calling method from C library(Python/C API))

* ##### There are two general purpose to use the python/c API, one of which is to write an extension module for another program to use, and the other one is to be embedded into another larger program to use. 
* The following macro definitions are mandatory and must be included before any other standard library.(Rcommended == mandatory)
* ##### Create a file called library.c.
```
#define PY_SSIZE_T_CLEAN
#include <Python.h>
//Function Declaration
```
* ##### Create a file called setup.py.
```
from setuptools import setup, Extension
setup(
    name='library',
    version='1.0',
    author='Your Name',
    description='A simple C library for Python',
    ext_modules=[Extension('library', sources=['library.c'])]
)
```
