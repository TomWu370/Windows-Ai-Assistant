# import the exe dictionary
# similar to CommandMapper
# there would be mapper to from different exe names to exe locations, as well as another map to aliases
import subprocess
from datetime import time

exes = {'notepad': 'notepad.exe', 'note pad': 'notepad.exe'}
print("hi")
def open(executable):
    match executable:
        case "notepad" | 'note pad':
            subprocess.Popen(exes[executable])
            print("opening")

def findExes():
    return exes.keys()
