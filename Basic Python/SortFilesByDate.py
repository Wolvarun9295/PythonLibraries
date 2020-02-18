import os
import glob

files = glob.glob("*")
files.sort(key=os.path.getmtime)
print("\n".join(files))
