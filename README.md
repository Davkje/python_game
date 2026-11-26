# Grottan 🗡️

Ett textäventyr i terminalen och ett lärprojekt i Python med fokus på klasser, arv och spellogik.

## Spela

```bash
uv run python -m game
```

Mål: besegra alla monster i grottan. Skriv `hjälp` i spelet för att se kommandona.

## Struktur

| Fil | Innehåll |
|---|---|
| `game/__main__.py` | Startpunkt |
| `game/items.py` | `Item` → `Weapon`, `Potion` |
| `game/characters.py` | `Character` → `Player`, `Monster` |
| `game/world.py` | `Room` och kartan |
| `game/combat.py` | Stridsrundor |
| `game/engine.py` | Spelloopen och kommandona |

```
           Item                  Character
          /    \                /         \
     Weapon    Potion       Player       Monster
```

**Börja med [LEKTIONER.md](LEKTIONER.md).**
