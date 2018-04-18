'''
	Purpose: Spec file for building jupyter notebook exe

	Author: Matthew Mitchell, Biometix Pty Ltd
	
	Credit: This spec file is based off the file uploaded by Andrew Leech
		https://github.com/andrewleech
		https://github.com/ipython/ipython/issues/4779
		
	Instructions: pyinstaller notebook_folder.spec
'''

import os
import glob

pathex=["<Path to zmq package>"]

a = Analysis(['jupyter_notebook.py'],
             pathex=pathex,
             hiddenimports=['IPython','zmq.backend.cffi','jupyter','notebook',
              'zmq.backend.cython.constants', 'zmq.backend.cython.error',
             'zmq.backend.cython.socket','zmq.backend.cython.utils','zmq.backend.cython._poll','zmq.backend.cython._version','zmq.backend.cython._device',
             'zmq.backend.cython','zmq.backend','zmq.sugar.attrsettr','zmq.sugar.poll','zmq.sugar.socket','zmq.sugar.context','zmq.sugar.frame',
             'zmq.sugar.tracker','zmq.sugar.version','zmq.sugar.stopwatch','zmq.sugar','zmq.backend.cython.error','zmq','send2trash', 'html.parser','entrypoints','defusedxml',
             'mistune','pygments','pygments.lexers','pygments.formatters','pygments.util','pandocfilters','nbformat','nbconvert',
             'ipykernel.datapub','backcall'],
             hookspath=None,
             runtime_hooks=None)

# Find all modules and add them (brute force)
import pkgutil
imps = []
for each in pkgutil.iter_modules():
  mod = each[1]
  if not mod.startswith('_'):
    imps.append(mod)

a.hiddenimports.extend(imps)

# Add ipython extensions folder
from IPython import extensions as IPython_extensions
IPython_extensions_path = os.path.split(IPython_extensions.__file__)[0]

files = glob.glob(os.path.join(IPython_extensions_path, "/*.py"))
extra_datas = []
for f in files:
    extra_datas.append(("IPython/extensions/" + os.path.basename(f), f, 'DATA'))
a.datas += extra_datas

# Add nbconvert templates
files = glob.glob(os.path.join(os.path.realpath('templates'), "*.tpl"))
extra_datas = []
for f in files:
    extra_datas.append(("IPython/nbconvert/templates/" + os.path.basename(f), f, 'DATA'))
a.datas += extra_datas

pyz = PYZ(a.pure)
exe = EXE(pyz,
          #a.scripts + [('v', '', 'OPTION')],
          a.scripts,
          exclude_binaries=True,
          name='notebook.exe',
          debug=False,
          strip=None,
          upx=False,
          console=True,
          icon='app.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=False,
               name='notebook')