# Imported os.
import os

# NOTE: The path should be given of folder where only files exits and not folders, or the output will be blank.
print(
    [f for f in os.listdir('/home/bridgelabz/Desktop/Sample/Functional Programs/') if
     os.path.isfile(os.path.join('/home/bridgelabz/Desktop/Sample/Functional Programs', f))])
