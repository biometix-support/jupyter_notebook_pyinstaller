#!/bin/bash
pyinstaller jupyter_notebook.spec --clean -strip --onefile --icon=app.ico
