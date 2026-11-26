"""Spelmotorn: spelloopen och kommandona.

Lektion 5: while-loopar, input(), match-satser och att leta i listor.
"""

from game.characters import Player
from game.combat import fight_round
from game.items import Item
from game.world import START_ROOM, Room, build_world

HELP = """Kommandon:
  gå <riktning>    (g)   gå åt ett håll, t.ex. 'gå norr'
  titta            (t)   beskriv rummet igen
  ta <sak>               plocka upp något
  attackera        (a)   slåss mot monstret i rummet
  inventarie       (i)   visa vad du bär på
  använd <sak>     (u)   använd något i ryggsäcken
  hjälp            (h)   visa den här texten
  avsluta          (q)   avsluta spelet"""


def find_item(items: list[Item], name: str) -> Item | None:
    """Hitta första föremålet vars namn börjar med `name`, utan hänsyn till versaler.

    'ta rost' hittar alltså "Rostigt svärd". Returnerar None om inget hittas.
    """
    name = name.lower()
    # next(generator, None) ≈ items.find(item => ...) ?? null
    return next((item for item in items if item.name.lower().startswith(name)), None)


class Game:
    def __init__(self) -> None:
        self.rooms: dict[str, Room] = build_world()
        self.current: Room = self.rooms[START_ROOM]
        self.player = Player("Äventyraren")
        self.running = True

    # ------------------------------------------------------------------
    # Spelloopen
    # ------------------------------------------------------------------

    def run(self) -> None:
        print("🗡️  Välkommen till Grottan! Besegra alla monster för att vinna.")
        name = input("Vad heter du? ").strip()
        if name:  # tom sträng är falsy
            self.player.name = name
        print(f"\nLycka till, {self.player.name}! Skriv 'hjälp' för kommandon.\n")
        print(self.current.describe())

        # Spelloopen: fortsätt så länge spelet körs OCH spelaren lever.
        while self.running and self.player.is_alive:
            try:
                command = input("\n> ")
            except (EOFError, KeyboardInterrupt):  # Ctrl+D / Ctrl+C
                print("\nHej då!")
                return

            try:
                self.handle(command)
            except NotImplementedError as e:
                # Fångar alla TODO-stubbar så att spelet fortsätter.
                print(f"🛠  Inte klart än: {e}")

            if self.all_monsters_defeated():
                print(f"\n🎉 Alla monster är besegrade. Du vann, {self.player.name}!")
                return

        if not self.player.is_alive:
            print("\n💀 Du har fallit i grottans mörker. Game over.")

    def handle(self, command: str) -> None:
        """Tolka ett kommando och anropa rätt metod."""
        # "gå norr" → ["gå", "norr"].  maxsplit=1 gör att "ta stor läkedryck" → ["ta", "stor läkedryck"]
        words = command.strip().lower().split(maxsplit=1)
        if not words:
            return
        verb = words[0]
        arg = words[1] if len(words) > 1 else ""  # ≈ ternary: cond ? a : b

        # match ≈ switch i JS, men kraftfullare. `|` betyder "eller". Ingen break behövs.
        match verb:
            case "gå" | "g":
                self.go(arg)
            case "titta" | "t":
                print(self.current.describe())
            case "ta":
                self.take(arg)
            case "attackera" | "a":
                self.attack()
            case "inventarie" | "i":
                self.show_inventory()
            case "använd" | "u":
                self.use(arg)
            case "hjälp" | "h" | "?":
                print(HELP)
            case "avsluta" | "q":
                self.running = False
                print("Hej då!")
            case _:  # ≈ default
                print("Det förstod jag inte. Skriv 'hjälp'.")

    # ------------------------------------------------------------------
    # Kommandon (färdiga exempel)
    # ------------------------------------------------------------------

    def go(self, direction: str) -> None:
        if not direction:
            print("Gå vart?")
            return
        # `in` på en dict kollar om nyckeln finns ≈ direction in obj / obj.hasOwnProperty(...)
        if direction not in self.current.exits:
            print("Du kan inte gå åt det hållet.")
            return
        room_id = self.current.exits[direction]
        self.current = self.rooms[room_id]
        print(self.current.describe())

    def take(self, name: str) -> None:
        if not name:
            print("Ta vad?")
            return
        item = find_item(self.current.items, name)
        if item is None:
            print("Det finns inget sådant här.")
            return
        self.current.items.remove(item)
        self.player.inventory.append(item)
        print(f"Du plockar upp {item.name}.")

    def attack(self) -> None:
        monster = self.current.monster
        if monster is None:
            print("Det finns inget att slåss mot här.")
            return

        fight_round(self.player, monster)

        if not monster.is_alive:
            if monster.loot is not None:
                self.current.items.append(monster.loot)
                print(f"{monster.name} tappade {monster.loot.name}.")
            self.current.monster = None

    def all_monsters_defeated(self) -> bool:
        # all() ≈ .every(). .values() ger alla värden i dicten, ≈ Object.values()
        return all(room.monster is None for room in self.rooms.values())

    # ------------------------------------------------------------------
    # Lektion 5: din tur
    # ------------------------------------------------------------------

    def show_inventory(self) -> None:
        # TODO(du): Lektion 5 – visa ryggsäcken.
        #   - Är den tom (self.player.inventory)? Skriv "Ryggsäcken är tom."
        #   - Annars: skriv ut varje föremål på en egen rad, t.ex. "  - Rostigt svärd (+2 skada)"
        #     (print(item) använder föremålets __str__)
        #   - Bonus: visa spelarens HP (print(self.player)) och vilket vapen som är i handen.
        #   - Bonus: numrera raderna med  for i, item in enumerate(lista, start=1):
        raise NotImplementedError("Lektion 5: show_inventory i engine.py")

    def use(self, name: str) -> None:
        # TODO(du): Lektion 5 – använd ett föremål.
        #   Titta på take() ovan. Det här är nästan samma sak:
        #   1. Inget namn angivet? Skriv "Använd vad?" och avbryt med return.
        #   2. Leta i self.player.inventory med find_item(...).
        #   3. Hittades inget? Skriv ett meddelande och return.
        #   4. Anropa item.use(self.player) och skriv ut texten den returnerar.
        #      Här ser du polymorfism i praktiken: samma anrop gör olika saker för
        #      Weapon och Potion.
        raise NotImplementedError("Lektion 5: use i engine.py")
