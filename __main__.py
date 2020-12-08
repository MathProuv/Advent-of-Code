import sys
import inputAoC

path = ""

if len(sys.argv) == 3:
    path = "y" + sys.argv[2] + "." + sys.argv[2] + "-day" + sys.argv[1]

print(path)
__import__(path)
#from y2015 import y2015_day1