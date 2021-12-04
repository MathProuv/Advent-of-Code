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

```tree
📦hierarchie
 ┣ 📂inputs
 ┃ ┣ 📜2015_1.txt
 ┃ ┣ 📜2015_2.txt
 ┃ ┗ 📜2015_3.txt
 ┣ 📂y2015
 ┃ ┣ 📜2015-day01.py
 ┃ ┣ 📜2015-day02.py
 ┃ ┣ 📜2015-day03.py
 ┃ ┗ 📜__init__.py
 ┣ 📂y2021
 ┃ ┗ 📜__init__.py
 ┣ 📜.gitignore
 ┣ 📜inputAoC.py
 ┣ 📜my_utils.py
 ┣ 📜private.py
 ┣ 📜README.md
 ┣ 📜__init__.py
 ┗ 📜__main__.py
```

Remarque : initialement le dossier `inputs` est vide, les fichiers `inputs/AAAA-J.txt` sont créés et remplis par la méthode `get_input_file` du module `inputAoC`.

---

En particulier, pour runner le code du jour `JJ` de l'année `AAAA` (avec `JJ` entre 1 et 25 et `AAAA` entre 2015 et 2035), le code doit être dans le dossier `yAAAA` et le fichier doit s'appeler `AAAA-dayJJ.py` (`JJ` en 2 chiffres **obligatoirement ici**). Il faudra ensuite exécuter le fichier `__main__.py` d'une des façons suivantes (`JJ` en 1 ou 2 chiffres) :

```bash
python ../Advent-of-Code JJ AAAA
python __main__.py JJ AAAA
```

Indication : le code pourrait commencer comme suit :

```python
import inputAoC as aoc
data = aoc.get_input_file(JJ,AAAA).splitlines()   # si les données sont sur des lignes séparées
data = [int(i) for i in data]  # si les données sont des nombres
#data = list(map(int,data))
```
