import os
import time

print(time.ctime(os.path.getctime("FileCheck.py")))
print(time.ctime(os.path.getmtime("FileCheck.py")))
