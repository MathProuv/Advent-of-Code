import sys
import inputAoC

try:
    J, AAAA = sys.argv[1], sys.argv[2]
    j, aaaa = int(J), int(AAAA)
    J, AAAA = str(j), str(aaaa) #J et AAAA n'ont pas de leading zeroes et sont au bon format
    if not (1 <= j <= 25 and 2015 <= aaaa <= 2025):
        raise Exception
except:
    print("""
    Il y a un problème avec les arguments :
        respectez le format J AAAA avec 1 <= J <= 25 et 2015 <= AAAA <= 2025
    """)

else:
    path = "y" + AAAA + "." + AAAA + "-day" + J
    try:
        __import__(path)
    except ModuleNotFoundError:
        print("\n    Le problème du jour " + AAAA + "/" + J + " n'a pas encore été résolu")
    except :
        print("\n    Il y a un problème à l'éxecution")