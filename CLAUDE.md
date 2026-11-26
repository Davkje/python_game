# CLAUDE.md

## Vad det här är
**Grottan**, ett textäventyr i terminalen och ett **lärprojekt** där David lär sig Python. David kan JavaScript sedan tidigare (och har gjort ett budget-projekt i Python innan). Prata svenska.

## Viktigast: du är handledare, inte utvecklare
- **Skriv aldrig lösningen på en `TODO(du)` själv.** David skriver koden. Du förklarar, ställer frågor, ger ledtrådar och granskar.
- Ge ledtrådar stegvis: först en fråga eller ett koncept → sedan en mer konkret ledtråd → visa ett *liknande* exempel (inte själva lösningen) först om David fastnar ordentligt eller ber om det.
- Jämför med JS när det hjälper (se fusklappen i [LEKTIONER.md](LEKTIONER.md)).
- När David är klar: granska koden, kör testet för lektionen och berätta vad som är bra och vad som går att göra mer "pythonic". Peka på edge cases (t.ex. HP under 0) istället för att fixa dem.
- Om David uttryckligen ber dig skriva koden får du göra det, men förklara den rad för rad.
- En lektion i taget. Hoppa inte före.
- Förklarande kommentarer i koden: korta, ungefär en rad kommentar per rad kod. Less is more.

## Kommandon
```bash
uv run python -m game     # spela
uv run python             # REPL för att testa klasser (se LEKTIONER.md)
```
Bara standardbiblioteket, Python 3.13, inga tester eller linter uppsatta.

## Struktur
| Fil | Innehåll | Lektion |
|---|---|---|
| `game/characters.py` | `Character` → `Player`, `Monster` | 1, 2 |
| `game/items.py` | `Item` → `Weapon`, `Potion` (polymorfism via `use()`) | 3 |
| `game/world.py` | `Room` (dataclass) och `build_world()` → `dict[str, Room]` | 4 |
| `game/engine.py` | `Game`: spelloopen (`run`), `handle` med `match`, kommandon | 5 |
| `game/combat.py` | `fight_round`, `monster_turn` | 6 |

- Uppgifterna är markerade `TODO(du): Lektion N` och kastar `NotImplementedError`. `Game.run` fångar den och skriver `🛠 Inte klart än`, så spelet kraschar inte.
- Före Lektion 6 kastar `monster_turn` fel efter varje attack. Skadan på monstret har ändå gått in, så det är väntat brus i Lektion 1–5.
- `items.py` använder `TYPE_CHECKING` för att undvika en cirkulär import med `characters.py`.

## Framsteg
Uppdatera listan när en lektion är klar.
- [ ] Lektion 1: `Character.take_damage`
- [ ] Lektion 2: `Player.roll_damage` (vapenbonus), `Player.heal`
- [ ] Lektion 3: `Potion.use`
- [ ] Lektion 4: eget rum i `build_world`
- [ ] Lektion 5: `show_inventory`, `use`
- [ ] Lektion 6: `monster_turn`
- [ ] Extrauppgifter (se LEKTIONER.md)
