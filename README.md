# Advent-of-Code

Mes codes pour les Avents of code.  
Je vais commencer par 2015 et suivre 2020 en direct.

---

Pour utiliser mon code, il faut que vous modifiez le fichier `private_default.py` avec votre cookie.  
**Attention à ne pas le push !** Il faut ensuite le renommer en `private.py`.

Il faudrait aussi un dossier inputs dans lequel seront enregistrés les fichiers `.txt` de l'input de chaque jour.

---

Pour une meilleure hiérarchisation de mes codes, j'ai préféré les séparer dans des sous-packages. Ainsi, il y a maintenant une petite manipulation à faire pour pouvoir utiliser `inputAoC`. Il va donc falloir utiliser exactement la même hiérarchie et respecter précisément le nom des fichiers.

En particulier, pour runner le code du jour `J` de l'année `AAAA` (avec `J` entre 1 et 25 et `AAAA` entre 2015 et 2025), le code doit être dans le dossier `yAAAA` et le fichier doit s'appeler `AAAA-dayJ.py` (sans zero inutile). Il faudra ensuite exécuter le fichier `__main__.py` d'une des façons suivantes :

    python ../Advent-of-Code J AAAA
    python __main__.py J AAAA
