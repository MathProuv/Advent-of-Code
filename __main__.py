import sys
import inputAoC

try:
    JJ, AAAA = sys.argv[1], sys.argv[2]
    jj, aaaa = int(JJ), int(AAAA)
    JJ, AAAA = ('0'+str(jj))[-2:], str(aaaa) #J et AAAA sont au bon format
    if not (1 <= jj <= 25 and 2015 <= aaaa <= 2025):
        raise Exception
except:
    print("""
    Il y a un problème avec les arguments :
        respectez le format J AAAA avec 1 <= J <= 25 et 2015 <= AAAA <= 2025
    """)

else:
    path = "y" + AAAA + "." + AAAA + "-day" + JJ
    try:
        __import__(path)
    except ModuleNotFoundError:
        print("\n    Le problème du jour " + AAAA + "/" + JJ + " n'a pas encore été résolu")
    # except:
    #     print("\n    Il y a un problème à l'éxecution")
