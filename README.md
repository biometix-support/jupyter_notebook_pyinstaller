# Project: Jupyter Notebook Pyinstaller

Contains the spec file and python script to generate an executable for Jupyter notebook.


Follow the instructions at: 
https://medium.com/@m.mitchell_35295/jupyter-notebook-pyinstaller-4cb3482609aa


Please contact m.mitchell@biometix.com or support@biometix.com with any questions relating to this project.

# Requirements

* Python 3.6 or greater
* pipenv is require, can be installed with pip install pipenv
* virtualenv == 16.2.0

# Instructions

Based on your operating system, please run either of the following:

# Windows
```
set PIPENV_VENV_IN_PROJECT=1
pipenv install
pipenv shell
build_win_exe.bat
```

# Ubuntu
```
export PIPENV_VENV_IN_PROJECT=1
pipenv install
pipenv shell
build_lin_exe.sh
```

You will now have an executable in nb to run jupyter notebook.