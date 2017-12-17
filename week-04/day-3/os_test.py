import os
from sys import platform

if platform == "linux" or platform == "linux2":
    print('Linux')
elif platform == "darwin":
    print('OS X')
elif platform == "win32":
    print('Windows')

print(platform)
