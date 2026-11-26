"""Spelvärlden: rum, utgångar, föremål och monster.

Lektion 4: dataclasses, dicts och hur världen hänger ihop.
"""

from dataclasses import dataclass, field

from game.characters import Monster
from game.items import Item, Potion, Weapon


# @dataclass skapar __init__ automatiskt utifrån fälten nedan, så att vi kan skriva
# Room("Namn", "Beskrivning", exits={...}) utan att skriva en constructor själva.
@dataclass
class Room:
    name: str
    description: str
    # exits: riktning → id för rummet åt det hållet, t.ex. {"norr": "gang"}
    # field(default_factory=dict) ger varje rum en EGEN tom dict. (Skriv aldrig `= {}` här.)
    exits: dict[str, str] = field(default_factory=dict)
    items: list[Item] = field(default_factory=list)
    monster: Monster | None = None

    def describe(self) -> str:
        """Texten som visas när man går in i rummet eller skriver 'titta'."""
        lines = [f"== {self.name} ==", self.description]

        if self.monster is not None:
            lines.append(f"⚔️  Här finns {self.monster}!")
        if self.items:  # en tom lista är falsy
            # ", ".join(...) ≈ arr.join(", "), och generatorn ≈ .map()
            lines.append("På marken: " + ", ".join(str(item) for item in self.items))
        if self.exits:
            lines.append("Utgångar: " + ", ".join(self.exits))  # att loopa en dict ger nycklarna

        # "\n".join(lines) sätter ihop raderna med radbrytning
        return "\n".join(lines)


START_ROOM = "grotta"


def build_world() -> dict[str, Room]:
    """Bygg alla rum. Returnerar en dict: rum-id → Room."""
    rooms = {
        "grotta": Room(
            name="Grottöppningen",
            description="Dagsljuset bakom dig blir svagare. Det droppar från taket.",
            exits={"norr": "gang"},
            items=[Weapon("Rostigt svärd", "Har sett bättre dagar.", bonus=2)],
        ),
        "gang": Room(
            name="Den smala gången",
            description="Väggarna är fuktiga och något prasslar i mörkret.",
            exits={"söder": "grotta", "öster": "sal"},
            items=[Potion("Läkedryck", "Luktar mynta.", heal_amount=8)],
            monster=Monster("Grottråtta", max_hp=8, attack=3),
        ),
        "sal": Room(
            name="Kristallsalen",
            description="Kristaller i taket lyser blått. Marken skakar när något stort rör sig.",
            exits={"väster": "gang"},
            monster=Monster(
                "Stengolem",
                max_hp=20,
                attack=5,
                loot=Potion("Stor läkedryck", "Glittrar.", heal_amount=15),
            ),
        ),
    }

    # TODO(du): Lektion 4 – bygg ut världen!
    #   1. Lägg till minst ett eget rum i dicten ovan, gärna med ett föremål och/eller ett monster.
    #   2. Koppla ihop det med ett befintligt rum ÅT BÅDA HÅLLEN. Om ditt rum ligger norr om
    #      salen behöver salen {"norr": "ditt_id"} och ditt rum {"söder": "sal"}.
    #   3. Bonus: skapa ett nytt vapen med högre bonus som man hittar längre in.
    #   Tips: ändra en befintlig dict i efterhand med  rooms["sal"].exits["norr"] = "ditt_id"

    return rooms
