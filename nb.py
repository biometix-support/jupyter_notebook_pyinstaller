import os
import sys

cwd = os.getcwd()
server_loc = os.path.join(cwd, 'server')
server_exe_loc = os.path.join(server_loc, 'server.exe')
conn_file = '{connection_file}'

kernel_cmd = [server_exe_loc, "kernel", "-f", conn_file]

custom_args = ""
for arg in sys.argv[1:]:
    custom_args += f"{arg} "

cmd = f'{server_exe_loc} --KernelManager.kernel_cmd="{kernel_cmd}" {custom_args}'

os.system(cmd)