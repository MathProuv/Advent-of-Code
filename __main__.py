import sys
import inputAoC

try:
    JJ, AAAA = sys.argv[1], sys.argv[2]
    jj, aaaa = int(JJ), int(AAAA)
    JJ, AAAA = ('0'+str(jj))[-2:], str(aaaa) #JJ et AAAA sont au bon format
    if not (1 <= jj <= 25 and 2015 <= aaaa <= 2035):
        raise Exception
except:
    print("""
    Il y a un problème avec les arguments :
        respectez le format JJ AAAA avec 1 <= JJ <= 25 et 2015 <= AAAA <= 2035
    """)

else:
    path = "y" + AAAA + "." + AAAA + "-day" + JJ
    try:
        __import__(path)
    except ModuleNotFoundError:
        print("    Le problème du jour " + AAAA + "/" + JJ + " n'a pas encore été résolu")
    except ImportError:
        print("    Il y a un problème à l'importation des inputs")
    except Exception:
        print("    Il y a un problème à l'éxecution")
