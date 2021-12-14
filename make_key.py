import os
import sys
import winreg as reg

# Send to dir
# C:\Users\<user>\AppData\Roaming\Microsoft\Windows\SendTo
# Get path of current working directory and python.exe
cwd = os.getcwd()
python_exe = "C:\\Users\\stefa\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe"
fl = "D:\\1. Programiranje\\1. Klijenti\\ContextMenuScript\\DateReplace.py"
# optional hide python terminal in windows
# hidden_terminal = '\\'.join(python_exe.split('\\')[:-1])+"\\pythonw.exe"


# Set the path of the context menu (right-click menu)
key_path = r'*\\shell\\Date Replace (PY)' 
# FOR WORKING ON FOLDERS USE HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Directory\shell 

# Create outer key
key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
reg.SetValue(key, '', reg.REG_SZ, '&Date Replace (Py)2')  # Change 'Organise folder' to the function of your script

# create inner key
key1 = reg.CreateKey(key, r"command")
reg.SetValue(key1, '', reg.REG_SZ, f'{python_exe} {fl} "%~f1"') # change 'file_organiser.py' to the name of your script
#reg.SetValue(key1, '', reg.REG_SZ, hidden_terminal + f' "{cwd}\\file_organiser.py"')  # use to to hide terminal


# REG EDIT COMMANDS:

# Windows Registry Editor Version 5.00

# [HKEY_CLASSES_ROOT\*\shell\Run script]
# @="Run &script"

# [HKEY_CLASSES_ROOT\*\shell\Run script\command]
# @="\"C:\\Users\\<user>\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe\" \"C:\\Users\\<user>\\AppData\\Roaming\\Microsoft\\Windows\\SendTo\\test.py\" \"%1\""

# In a regular Send to action - use "%~f1"