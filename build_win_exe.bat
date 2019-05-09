pyinstaller notebook_folder.spec
ROBOCOPY .venv/Lib/site-packages/notebook dist/server/notebook /E
ROBOCOPY .venv/Lib/site-packages/nbconvert dist/server/nbconvert /E
ROBOCOPY .venv/Lib/site-packages/nbformat dist/server/nbformat /E
ROBOCOPY .venv/Lib/site-packages/jupyter_core dist/server/jupyter_core /E
ROBOCOPY .venv/Lib/site-packages/jedi dist/server/jedi /E
pyinstaller nb.py --onefile --icon=app.ico
ROBOCOPY dist/server nb/server /E
ROBOCOPY dist nb nb.exe