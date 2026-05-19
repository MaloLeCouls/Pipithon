"""Ce menu expose get(i) et nb(). Pour itérer, le code appelant doit faire
une boucle d'indices à la main. Non pythonique.

Refactor :
1. Remplace get(i) par __getitem__ (délègue à la liste interne).
2. Remplace nb() par __len__.
3. Après ça, `for dish in menu` et `menu[-1]` doivent marcher sans rien
   d'autre. Supprime get() et nb().
"""


class Menu:
    def __init__(self, dishes):
        self.dishes = list(dishes)

    def get(self, i):
        return self.dishes[i]

    def nb(self):
        return len(self.dishes)
