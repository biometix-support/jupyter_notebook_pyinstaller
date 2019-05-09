#from notebook import notebookapp as app
#app.launch_new_instance()

###############################################################
#   @file
#   @brief  Main bootstrap file for running ipython notebook.
#           Place this in the same folder as notebook_*.spec and run
#           #> pyinstaller -y notebook_single_exe.spec
#           or
#           #> pyinstaller -y notebook_folder.spec
#
#           Resulting .exe can be run directly to start ipython notebook,
#           or with argument including kernel to run ipython notebook kernel.
#           or with argument including nbconvert to convert notebook into html etc.

import sys
import IPython

# Parse command line to check for kernel mode and clean up extraneous commands
mode = None
cmd_args = []
all_args = sys.argv
for index, arg in enumerate(all_args):
    if index == 0:  # remove exe name
        pass
    elif arg == "notebook":
        mode = "notebook"
        pass
    elif arg == "nbconvert":
        mode = "nbconvert"
        pass
    elif arg == "kernel":
        mode = "kernel"
        pass
    elif arg == "-c":  # when spawned by main notebook.exe to run kernel, this will be present but not needed for our use
        if "kernel" in all_args[index + 1]:
            mode = "kernel"
        del all_args[index + 1]  # the following argument will be undesirable for our use
        pass
    elif arg == "notebook.py":  # remove this if it's run locally (not in exe)
        pass
    else:
        cmd_args.append(arg)

if mode == "kernel":
    # run kernel with passed commands
    args = ["kernel"]
    args.extend(cmd_args)
    IPython.start_ipython(args)
elif mode == "nbconvert":
    # run nbconvert with passed commands
    args = ["nbconvert"]
    args.extend(cmd_args)
else:
    # Run IPython Notebook
    args = None
    from notebook import notebookapp as app
    app.launch_new_instance()
