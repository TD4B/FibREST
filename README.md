# FibREST [![Build Status](https://travis-ci.org/TD4B/FibREST.svg?branch=master)](https://travis-ci.org/TD4B/FibREST)
A Beautiful Fibonacci Calculator Web App with a REST API Interface.



This Program uses C++ extension modules for the Calculation, this interface can be viewed at:
https://github.com/TD4B/FibExtensionModule

The extension modules come with pre-compiled binaries for both Windows and Linux operating systems.
# Installation Instructions.
Dependencies:
* Python 3.5
* virtualenv

VirtualEnv Depenencies:
* flask

Obtaining the Project Source Files:
```
git clone https://github.com/TD4B/FibREST.git
```

### Linux Guide

1) After Cloning the repositroy and navigating to the root of the project directory we create our virtual environment.
```
admin> virtualenv project --python=python3.5
admin> cd project
admin> source bin/activate
(project)admin>
```
2) Now install the depencency requirements.
```
(project)admin> pip install -r requires.txt
```
3) Run the Web Server!
```
(project)admin> python fib_web.py
```
4) Navigate to "http://127.0.0.1:5000"

<img src="https://i.imgur.com/E4tY8zw.gif" width="700" height="1000">

### Windows Guide (slightly different setup with virtualenv)

1) After Cloning the repositroy and navigating to the root of the project directory we create our virtual environment.
```
admin> virtualenv project --python=C:\Python36\python36.exe
admin> cd project/Scripts
admin> activate
(project)admin>
```
2) Now install the depencency requirements.
```
(project)admin> pip install -r requires.txt
```
3) Run the Web Server!
```
(project)admin> python fib_web.py
```
4) Navigate to "http://127.0.0.1:5000"
