# Advent-of-Code

Mes codes pour les Avents of code.

J'ai commencé par suivre 2020 en direct et 2015 en retard.  
Bonne nouvelle : je continue en 2021 !!

---

Pour utiliser mon code, il faut que vous modifiez le fichier `private_default.py` avec votre cookie.  
**Attention à ne pas le push !** Il faut ensuite le renommer en `private.py`.  
Comment trouver votre cookie ?

* Il faut d'abord vous connecter sur le site d'[Advent of Code](https://adventofcode.com) dans votre fureteur favori
* Menu inspecter (Ctrl+Maj+I) &rarr; Application &rarr; Cookies &rarr; adventofcode

---

Il va falloir utiliser exactement la même hiérarchie et respecter précisément le nom des fichiers :

```markdown
```

Pour une meilleure hiérarchisation de mes codes, j'ai préféré les séparer dans des sous-packages. Ainsi, il y a maintenant une petite manipulation à faire pour pouvoir utiliser `inputAoC` dans les packages.

En particulier, pour runner le code du jour `JJ` de l'année `AAAA` (avec `JJ` entre 1 et 25 et `AAAA` entre 2015 et 2035), le code doit être dans le dossier `yAAAA` et le fichier doit s'appeler `AAAA-dayJJ.py` (`JJ` en 2 chiffres **obligatoirement ici**). Il faudra ensuite exécuter le fichier `__main__.py` d'une des façons suivantes (`JJ` en 1 ou 2 chiffres) :

```bash
python ../Advent-of-Code JJ AAAA
python __main__.py JJ AAAA
```

Indication : le code pourrait commencer comme suit :

```python
import inputAoC as aoc
data = aoc.get_input_file(JJ,AAAA).splitlines()
#data = [int(i) for i in data]  ### si les données sont des nombres
```
