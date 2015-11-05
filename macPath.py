#! python3
# Change network path format from Mac to Windows
# Example: src = smb://server/folder/folder/folder/file dest = \\server\folder\folder\folder\file
import pyperclip, os, re

macPath = pyperclip.paste()
macPath = os.path.normpath(macPath)

def combinePublic():
    global macPath
    i = macPath.index(m1.group())
    macPath = macPath[i:]
    macPath = ('\\\\Server\\Folder\\' + macPath)
    pyperclip.copy(macPath)
    print(macPath)

def combineArtwork():
    global macPath
    i = macPath.index(m2.group())
    macPath = macPath[i:]
    macPath = ('\\\\Server\\' + macPath)
    pyperclip.copy(macPath)
    print(macPath)

m1 = re.search('public', macPath, flags=re.IGNORECASE)
m2 = re.search('artwork', macPath, flags=re.IGNORECASE)

if m1:
    combinePublic()
elif m2:
    combineArtwork()
else:
    print('Copy a \"Mac\" network path to receive a \"Windows\" path format')
