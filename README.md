# 0x00. AirBnB clone - The console

We are aspiring to be Web developers and Software Engineers. At **ALX SE Programme**, one of the requirements that makes you standout and become a formidable Software Engineer, is to create an _AirBnB Clone_. You do not just roll out these solutions but rather, approach it one at a time. Our first step to developing this web application is to create a Command Line Interpreter  (CLI) to help us manage our projects' objects. This step is very important because we will be building and including static and dynamic contents: HTML/CSS/JS templates, DB storage, File Storage, API (Application Proramming Interface) and Front-End Integration.

## What is a CLI (Command Line Interpreter)?

A `CLI` is a text-based User-Interface (`UI`) that runs commands and programes. It manages  computer files and interact with the computer. Do you remember the `Shell`? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Learning Objectives

During and after the cause of this project, we will be able to do the following:

- Know how to create a Python package
- Know how to create a CLI in Python using the `cmd module`
- Know what is `Unit testing` and how to implement it in a large project
- Know how to `serialize` and `deserialize` a Class
- Know how to write and read a `JSON` file
- Know how to manage `datetime`
- Know what is an `UUID`
- Know what is `*args` and how to use it
- Know what is `**kwargs` and how to use it
- Know how to handle named arguments in a function

## Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3 (version 3.8.5)`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle (version 2.8.*)`
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests

- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `./tests`
- You have to use the `unittest` module
- All your test files should be python files `(extension: .py)`
- All your test files and folders should start by `test_`
- Your file organization in the tests folder should be the same as your project
- > e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
- > e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`