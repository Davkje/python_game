# Lektioner

Uppgifterna är märkta `TODO(du): Lektion N` i koden. Sök med **Cmd+Shift+F**.
Spelet kraschar inte på en ofärdig del. Det skriver `🛠 Inte klart än: Lektion N ...` och fortsätter.

Kör spelet efter varje lektion: `uv run python -m game`

---

## Lektion 1: Klasser och metoder (`characters.py`)
**Läs:** klassen `Character`. Jämför med JS:
```js
class Character {
  constructor(name, maxHp, attack) { this.name = name; this.hp = maxHp; ... }
  get isAlive() { return this.hp > 0; }
}
```
**Uppgift:** `take_damage`.
**Klart när:** du kan gå norr (`g norr`) och `attackera` råttan tills den dör.

**Testa i REPL:en** (`uv run python`):
```python
>>> from game.characters import Character
>>> c = Character("Testgubbe", max_hp=10, attack=3)
>>> c.take_damage(4); print(c)
>>> c.take_damage(100); print(c, c.is_alive)
```

---

## Lektion 2: Arv och super() (`characters.py`)
**Läs:** `Player` och `Monster`. Båda ärver från `Character` och anropar `super().__init__(...)`.
**Uppgifter:**
1. `Player.roll_damage`: lägg till vapnets bonus. Det här är en *override* av förälderns metod.
2. `Player.heal`

**Klart när:** testa i REPL:en:
```python
>>> from game.characters import Player
>>> p = Player("Du"); p.take_damage(5)
>>> p.heal(3), p.hp      # (3, 28)
>>> p.heal(100), p.hp    # (2, 30): aldrig över max
```

---

## Lektion 3: Polymorfism (`items.py`)
**Läs:** `Item`, `Weapon` och `Potion`. Alla har `use()`, men den gör olika saker.
**Uppgift:** `Potion.use`.
**Klart när:** du kan testa den i Lektion 5, eller redan nu i REPL:en:
```python
>>> from game.characters import Player
>>> from game.items import Potion
>>> p = Player("Du"); p.take_damage(10)
>>> dryck = Potion("Läkedryck", "", heal_amount=8); p.inventory.append(dryck)
>>> dryck.use(p)
>>> p.inventory          # ska vara tom
```

---

## Lektion 4: Världen – dataclasses och dicts (`world.py`)
**Läs:** `Room` och `build_world()`.
**Uppgift:** bygg minst ett eget rum och koppla ihop det med kartan.
**Klart när:** du kan gå till ditt rum i spelet och tillbaka igen.

---

## Lektion 5: Spelloopen och kommandon (`engine.py`)
**Läs:** `run()` (while-loopen), `handle()` (match-satsen) och `take()`.
**Uppgifter:** `show_inventory` och `use`.
**Klart när:** `ta svärd` → `i` → `använd svärd` → `attackera` gör mer skada, och läkedrycken fungerar.

---

## Lektion 6: Strid och slump (`combat.py`)
**Uppgift:** `monster_turn`, så att monstren slår tillbaka.
**Klart när:** spelet går att förlora. Prova att slåss mot golemen utan svärd! 💀

---

## Extrauppgifter (välj fritt)
- **Fly:** ett kommando `fly` som tar dig tillbaka till förra rummet, men monstret får ett gratis slag.
- **Fler monstertyper:** `class Boss(Monster)` med en specialattack (override `roll_damage`).
- **Nycklar och låsta dörrar:** en utgång som bara går att använda om en `Key` finns i ryggsäcken.
- **XP och nivåer:** spelaren får XP av monster och blir starkare.
- **Spara spelet:** `spara`/`ladda` till `savegame.json` (som i budget-projektet).
- **Färger:** `uv add rich` och färglägg texten.

---

## Fusklapp: klasser i JS → Python

| JavaScript | Python |
|---|---|
| `class A { }` | `class A:` |
| `class B extends A` | `class B(A):` |
| `constructor(x) { this.x = x }` | `def __init__(self, x): self.x = x` |
| `this.x` | `self.x` |
| `super(x)` | `super().__init__(x)` |
| `super.method()` | `super().method()` |
| `get prop() { }` | `@property` + `def prop(self):` |
| `static create() { }` | `@classmethod` + `def create(cls):` |
| `toString()` | `__str__(self)` |
| `new A(1)` | `A(1)` (inget `new`) |
| `obj instanceof A` | `isinstance(obj, A)` |
| `switch (x) { case "a": ... }` | `match x: case "a": ...` |
| `while (cond) { }` | `while cond:` |
| `prompt("?")` | `input("?")` |
| `Math.max(a, b)` / `Math.min` | `max(a, b)` / `min(a, b)` |
| `arr.find(...)` | `next((x for x in lst if ...), None)` |
| `arr.every(...)` | `all(... for x in lst)` |
| `Object.values(obj)` | `d.values()` |
