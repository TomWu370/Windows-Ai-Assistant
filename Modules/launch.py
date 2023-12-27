# import the exe dictionary
# similar to CommandMapper
# there would be mapper to from different exe names to exe locations, as well as another map to aliases
import getpass
import os
import struct
import subprocess
import locale
from datetime import time

from win32comext.shell import shell, shellcon

exes = {'notepad': 'notepad.exe', 'note pad': 'notepad.exe'}
print("hi")


def launch(executable):
    match executable:
        case "notepad" | 'note pad':
            os.startfile(exes[executable])
            print("opening")


def mapExecutables():
    exes = {}

    return exes.keys()


import locale
import struct

def readLink(path):
    # http://stackoverflow.com/a/28952464/1119602
    print(path)
    with open(path, 'rb') as stream:
        content = stream.read()
        # skip first 20 bytes (HeaderSize and LinkCLSID)
        # read the LinkFlags structure (4 bytes)
        lflags = struct.unpack('I', content[0x14:0x18])[0]
        position = 0x18
        # if the HasLinkTargetIDList bit is set then skip the stored IDList
        # structure and header
        if (lflags & 0x01) == 1:
            position = struct.unpack('H', content[0x4C:0x4E])[0] + 0x4E
        last_pos = position
        position += 0x04
        # get how long the file information is (LinkInfoSize)
        length = struct.unpack('I', content[last_pos:position])[0]
        # skip 12 bytes (LinkInfoHeaderSize, LinkInfoFlags and VolumeIDOffset)
        position += 0x0C
        # go to the LocalBasePath position
        lbpos = struct.unpack('I', content[position:position+0x04])[0]
        position = last_pos + lbpos
        # read the string at the given position of the determined length
        size = (length + last_pos) - position - 0x02
        content = content[position:position+size].split(b'\x00', 1)
        return content[-1].decode('utf-16' if len(content) > 1
                                  else locale.getdefaultlocale()[1])


def get_exe_path():
    username = getpass.getuser()
    print(username)
    print(shell.SHGetSpecialFolderPath(0, shellcon.CSIDL_COMMON_STARTMENU))
    print(shell.SHGetSpecialFolderPath(0, shellcon.CSIDL_STARTMENU))
    start_menu = f'C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs'

    for subdir, dirs, files in os.walk(start_menu):
        for file in files:
            if file.endswith('.lnk'):
                link = readLink(f'{subdir}\{file}')
                print(link)
                # improveme
                if file in exes:
                    pass
                else:
                    # remove .lnk
                    exes[file[:-4]] = link

get_exe_path()
print(exes)