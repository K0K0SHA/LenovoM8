import os
import platform

if (platform.System=='Windows'):
    os.execute("windows_config.bat")
elif (platform.os=='Linux'):
    os.execute("linux_setup.sh")
