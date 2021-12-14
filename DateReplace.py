import sys
import os
import time
print(sys.argv[:])
print("stefo")
print(os.path.getmtime(" ".join(sys.argv[1:])))
with open("test.txt", 'w') as f:
    f.write(str(sys.argv[1:]))
print(sys.argv)
time.sleep(5)
import win32api, sys
# win32api.MessageBox(0, 'You clicked on ' + " ".join(sys.argv[1:]), 'Context Menu')


from ctypes import windll, wintypes, byref

# Arbitrary example of a file and a date
filepath = " ".join(sys.argv[1:])
epoch = os.path.getmtime(" ".join(sys.argv[1:]))

# Convert Unix timestamp to Windows FileTime using some magic numbers
# See documentation: https://support.microsoft.com/en-us/help/167296
timestamp = int((epoch * 10000000) + 116444736000000000)
ctime = wintypes.FILETIME(timestamp & 0xFFFFFFFF, timestamp >> 32)

# Call Win32 API to modify the file creation date
handle = windll.kernel32.CreateFileW(filepath, 256, 0, None, 3, 128, None)
windll.kernel32.SetFileTime(handle, byref(ctime), None, None)
windll.kernel32.CloseHandle(handle)



