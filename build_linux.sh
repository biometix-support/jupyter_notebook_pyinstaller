pyinstaller notebook_folder.spec
cp -r .venv/lib/python3.6/site-packages/notebook dist/server/notebook
cp -r .venv/lib/python3.6/site-packages/nbconvert dist/server/nbconvert
cp -r .venv/lib/python3.6/site-packages/nbformat dist/server/nbformat
cp -r .venv/lib/python3.6/site-packages/jupyter_core dist/server/jupyter_core
cp -r .venv/lib/python3.6/site-packages/jedi dist/server/jedi
pyinstaller nb.py --onefile --icon=app.ico
cp -r dist/server nb/server
cp dist/nb nb/nb
