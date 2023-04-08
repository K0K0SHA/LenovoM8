# critical imports
import os
import platform
import subprocess

def inquire(prompt):
    user_input = input(prompt + "\ntype Y to confirm)
    bool_input = (input.lower() == 'y')
    return bool_input

# try downloading miscX with user permission
try:
    import miscX
except ImportError:
    if inquire("Cannot import helper Python module miscX, attempt git clone from github at...\nhttps://github.com/K0K0SHA/miscX \n...? (Y/N)"):
        cmd = ("git clone --force https://github.com/K0K0SHA/miscX")
        os.execute(cmd)
    if ! os.path.exists("miscX.py"):
        if inquire("Cannot import helper Python module miscX; git clone failed. Would you like to attempt download with wget?"):
            cmd = ("wget https://github.com/K0K0SHA/miscX")
            os.execute(cmd)
    

if (platform.System=='Windows'):
    os.execute(".\windows_config.bat")
elif (platform.os=='Linux'):
    os.execute("./linux_setup.sh")
