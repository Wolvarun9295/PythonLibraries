# Imported os and glob modules.
import os
import glob

# Getting all the files in files variable.
files = glob.glob("*")
# Sorting the files with key value of modified date.
files.sort(key=os.path.getmtime)
# Printing the list of files sorted by date.
print("\n".join(files))
