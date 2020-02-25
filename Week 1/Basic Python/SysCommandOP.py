# Imported subprocess module.
import subprocess

# Storing the command in returnThis variable.
returnThis = subprocess.check_output("ls", shell=True, universal_newlines=True)
print(returnThis)
