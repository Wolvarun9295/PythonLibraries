# Imported path and time modules.
from os import path
import time

fileName = __file__
print(f'File: {fileName}')
print(f'Last access time: {time.ctime(path.getatime(fileName))}')
print(f'Last modified time: {time.ctime(path.getmtime(fileName))}')
print(f'Last changed time: {time.ctime(path.getctime(fileName))}')
print(f'Size: {path.getsize(fileName)} bytes')
