"""Föremål: basklassen Item och subklasserna Weapon och Potion.

Det här är kärnan i Lektion 3: *polymorfism*. Alla föremål har en metod use(),
men varje subklass gör något eget med den. Spelet anropar bara `item.use(player)`
och behöver inte veta vilken sorts föremål det är.
"""

# Den här importen gör att vi kan skriva typen "Player" utan att importera characters.py
# när koden körs. (characters.py importerar redan items.py, och åt andra hållet hade
# det blivit en cirkulär import.)
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.characters import Player


class Item:
    """Basklass för alla föremål.

    JS:
        class Item {
          constructor(name, description) { this.name = name; ... }
        }
    """

    # __init__ ≈ constructor. `self` ≈ `this`, men skrivs ut som första parameter.
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def use(self, player: "Player") -> str:
        """Använd föremålet. Returnerar en text som spelet skriver ut.

        Subklasser *överskuggar* (override) den här metoden.
        """
        return f"Du vet inte hur man använder {self.name}."

    def __str__(self) -> str:
        return self.name


# `class Weapon(Item)` ≈ `class Weapon extends Item`
class Weapon(Item):
    """Ett vapen ger extra skada när spelaren håller det."""

    def __init__(self, name: str, description: str, bonus: int) -> None:
        # super().__init__(...) ≈ super(...) i JS. Den anropar förälderns constructor.
        super().__init__(name, description)
        self.bonus = bonus

    # Färdigt exempel på override: samma metodnamn som i Item, men annat beteende.
    def use(self, player: "Player") -> str:
        player.weapon = self
        return f"Du håller nu {self.name} (+{self.bonus} skada)."

    def __str__(self) -> str:
        return f"{self.name} (+{self.bonus} skada)"


class Potion(Item):
    """En dryck som återställer HP. Försvinner när den används."""

    def __init__(self, name: str, description: str, heal_amount: int) -> None:
        super().__init__(name, description)
        self.heal_amount = heal_amount

    def use(self, player: "Player") -> str:
        # TODO(du): Lektion 3 – låt drycken hela spelaren.
        #   1. Anropa player.heal(self.heal_amount). Den returnerar hur mycket som faktiskt
        #      helades (Lektion 2).
        #   2. Ta bort drycken från player.inventory. Den är ju uppdrucken.
        #      (Tips: listor har .remove(x), och här är `self` själva drycken.)
        #   3. Returnera en text, t.ex. "Du dricker Läkedryck och får tillbaka 8 HP."
        #   Titta på Weapon.use ovan för hur det ser ut.
        raise NotImplementedError("Lektion 3: Potion.use i items.py")

    def __str__(self) -> str:
        return f"{self.name} (+{self.heal_amount} HP)"
