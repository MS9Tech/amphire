Amphire Lang
=======
Amphire is a Python-like programming language interpreter. In this project by MS9 you can find a more functional lang.

The project contains:

- Regular expression based lexer
- Top-down recursive descent parser
- AST-walking interpreter
- REPL of the code

Amphire doesn't require any third-party libraries.

What the language looks like:



    func map(arr, fn):
        r = []
        for val in arr:
            r = r + [fn(val)]
        r

    func factorial(n):
        if n <= 1:
            1
        else:
            n * factorial(n - 1)

    print(map(1...10, factorial))


You can find more examples in ``tests`` directory.

## Amphire - Run through AmpCLI - ComingSoon
Find AmpCLI at this github profile.
```
# To run a .abr amphire file:
# WARNING: make sure to read about setup.abr files below.
$ amp run setup
```
## Setup - Setup.abr files - ComingSoon
Setup.abr files tell AmpCLI on which files to run. For now you can run 1 file at a time with diffrent options:
  ```
  setup.abr
  --------
1 projevt.define = projectName, version
2 filename.abr # file to run
  ```
## AmpSecure Package - ComingSoon
To password protect your .abr files, first have these:
```
- AmpCLI
- A abr file in Folder
```
To password protect, do as follows:
```
  $ amp pkg get secure
$ amp -secure setup.py # will use the filename inside
>> Enter Password: EnterYourPassword
```
## AmpPython Module - amppy - ComingSoon

AmpPython is an extension that is not part of this language. Instead it is a module of Python3 that extends functions. Many of the greatest python3 functions will be baked into one library.
#### Install - ComingSoon
```
$ pip3 install amppy
# find documentation in this github profile
```
## AmpPyMath Module - ampmath - ComingSoon
Ampmath is a next-gen library that combines intense math functions all into one simple library. It makes it easy to do many advanced math calculations. Documentation in github profile.
#### Install - ComingSoon
```
$ pip install ampmath
```

## AmpPythonRun - aPyRun - ComingSoon
aPyRun allows you to run premade scripts in AmpCLI. It includes many functions that are listed in the documentation in this github profile.
#### Install - ComingSoon
```
$ amp pkg get apyrun
```
#### Example Run - ComingSoon
```
$ amp -apy tetris -py
```
