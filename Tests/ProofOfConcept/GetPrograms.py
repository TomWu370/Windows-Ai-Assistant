import os
import subprocess

from win32comext.shell import shell, shellcon

print(shell.SHGetSpecialFolderPath(0,shellcon.CSIDL_COMMON_STARTMENU  ))
print(shell.SHGetSpecialFolderPath(0,shellcon.CSIDL_STARTMENU ))

# os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad.lnk")
with open(r"C:\Users\tomwu\Downloads\aa.txt", "rb") as f:
    f.write("hi")