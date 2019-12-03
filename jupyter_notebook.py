#!//usr/bin/env python3
from logging import getLogger
logger = getLogger(__name__)  # you can use other name

# Takes string
# Returns list of successfully deleted jobid's as strings

def jupyter_notebook(arglist):
    logger.info("epmt_notebook: %s",str(arglist))

    mode = None
    cmd_args = []
    all_args = arglist
    for index, arg in enumerate(all_args):
        if arg == "kernel":
            mode = "kernel"
            pass
        else:
            cmd_args.append(arg)

    if mode == "kernel":  # run iPython kernel with passed ops
        args = ["kernel"]
        args.extend(cmd_args)
        # This does not want argv[0]
        logger.info("ipython kernel argv: %s",str(args))
        from IPython import start_ipython, start_kernel
        rv = start_ipython(argv=args)
    else:                 # Run IPython Notebook with passed ops
        import sys
        from os.path import realpath
        from os import getcwd
        me = realpath(sys.argv[0])
        logger.debug("Using %s as binary" ,me)
        args = []
        args.extend(["--notebook-dir="+getcwd(),
                     # If this is being run as a subcommand, be sure to insert it here, below example is for subcommand notebook
                     # and also using argparse, note the -- to terminate argument parsing
                     # "--KernelManager.kernel_cmd=['"+me+"', 'notebook', 'kernel', '--', '-f', '{connection_file}']"])
                     "--KernelManager.kernel_cmd=['"+me+"', 'kernel', '-f', '{connection_file}']"])
        args.extend(all_args)
        logger.info("notebook argv: %s",str(args))
        from notebook import notebookapp
        rv = notebookapp.launch_new_instance(argv=args)
    return True

if __name__== "__main__":
  import sys
  from logging import basicConfig, DEBUG
  basicConfig(level=DEBUG)
  jupyter_notebook(sys.argv)
  
