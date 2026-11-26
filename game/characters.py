"""Varelser i spelet: basklassen Character och subklasserna Player och Monster.

Lektion 1: klasser, __init__, metoder och @property
Lektion 2: arv, super() och override
"""

import random  # Pythons inbyggda modul med slumpfunktioner

from game.items import Item, Weapon  # ≈ import { Item, Weapon } from "./game/items"


class Character:
    """Allt som har HP och kan slåss."""

    # __init__ ≈ constructor, self ≈ this, `: str` ≈ TS-typ, `-> None` ≈ void
    def __init__(self, name: str, max_hp: int, attack: int) -> None:
        self.name = name  # ≈ this.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack

    @property  # ≈ getter: läses som character.is_alive, utan ()
    def is_alive(self) -> bool:
        return self.hp > 0

    def roll_damage(self) -> int:
        """Slå fram skada: ett slumptal mellan 1 och attack (båda inräknade)."""
        return random.randint(1, self.attack)  # slumpat heltal, båda ändar inräknade

    def take_damage(self, amount: int) -> None:
        """Minska HP med amount, men aldrig under 0."""
        self.hp = max(self.hp - amount, 0)
        # self.hp = self.hp - amount
        # if self.hp < 0:
        #     self.hp = 0

    def __str__(self) -> str:  # ≈ toString(), används av print()
        return f"{self.name} ({self.hp}/{self.max_hp} HP)"  # f-sträng ≈ `${...}`


class Player(Character):  # ≈ class Player extends Character
    """Spelaren. Har en ryggsäck (inventory) och kan hålla ett vapen."""

    def __init__(self, name: str) -> None:
        super().__init__(name, max_hp=30, attack=4)  # kör Character.__init__
        self.inventory: list[Item] = []  # ≈ TS: Item[]
        self.weapon: Weapon | None = None  # None ≈ null

    def roll_damage(self) -> int:  # override av Character.roll_damage
        """Spelarens skada = vanlig skada + vapnets bonus."""
        damage = super().roll_damage()  # förälderns version
        # TODO(du): Lektion 2 – om spelaren håller ett vapen (self.weapon är inte None),
        #   lägg till self.weapon.bonus på damage. Just nu hjälper vapnet inte alls!
        if self.weapon is not None:
            damage += self.weapon.bonus
        return damage

    def heal(self, amount: int) -> int:
        """Öka HP med amount, men aldrig över max_hp.

        Returnerar hur mycket som faktiskt helades. Om du har 28/30 HP och
        dricker en dryck på 8 helas bara 2.
        """
        # TODO(du): Lektion 2
        #   1. Spara gamla HP i en variabel.
        #   2. Öka self.hp, men inte över self.max_hp (tips: min(), motsatsen till max()).
        #   3. Returnera skillnaden.
        old_hp = self.hp
        self.hp = min(self.hp + amount, self.max_hp)
        return self.hp - old_hp


class Monster(Character):
    """Ett monster. Kan släppa ett föremål (loot) när det besegras."""

    # loot är valfri: = None ≈ JS default-parameter
    def __init__(self, name: str, max_hp: int, attack: int, loot: Item | None = None) -> None:
        super().__init__(name, max_hp, attack)
        self.loot = loot
