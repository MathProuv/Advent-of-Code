import sys
import inputAoC

path = ""

if len(sys.argv) == 2:
    path = "2020/" + sys.argv[1]
elif len(sys.argv) == 3:
    path = "y" + sys.argv[2] + ".y" + sys.argv[2] + "_day" + sys.argv[1]

print(path)
__import__(path)
#from y2015 import y2015_day1