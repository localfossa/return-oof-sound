from os import environ, getcwd, remove
from os.path import exists
from winreg import HKEY_CURRENT_USER, OpenKeyEx, QueryValueEx
from shutil import copy

filename = "ouch.ogg"

path = r"Software\ROBLOX Corporation\Environments\roblox-player\Versions"

key = OpenKeyEx(HKEY_CURRENT_USER, path)
value = QueryValueEx(key, "version0")[0]

destination = environ["USERPROFILE"]+"\AppData\Local\Roblox\Versions"+'\\'+value+"\content\sounds"+'\\'+filename
source = getcwd()+"\\"+filename

if exists(destination):
    remove(destination)
copy(source, destination)
