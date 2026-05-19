"""Cette chaîne de streaming s'utilise comme du Java : is_live() et
describe(). On veut du Python.

Refactor :
1. Remplace is_live() par __bool__ : une chaîne est "vraie" si viewers > 0.
2. Remplace describe() par __repr__ :
     - live    -> Channel(name='News', viewers=42)
     - offline -> Channel(name='News', offline)
3. Supprime is_live() et describe(). `name` et `viewers` restent accessibles.
"""


class Channel:
    def __init__(self, name, viewers):
        self.name = name
        self.viewers = viewers

    def is_live(self):
        if self.viewers > 0:
            return True
        else:
            return False

    def describe(self):
        if self.is_live():
            return "Channel " + self.name + " (" + str(self.viewers) + ")"
        return "Channel " + self.name + " offline"
