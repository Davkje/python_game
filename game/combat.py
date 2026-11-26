"""Strid: en runda = spelaren slår, sedan slår monstret tillbaka.

Lektion 6: slumptal, villkor och att låta objekt prata med varandra.
"""

from game.characters import Monster, Player


def fight_round(player: Player, monster: Monster) -> None:
    """Kör en stridsrunda och skriv ut vad som händer."""
    # --- Spelarens tur (färdig) ---
    damage = player.roll_damage()
    monster.take_damage(damage)  # Lektion 1
    print(f"Du träffar {monster.name} för {damage} skada. {monster}")

    if not monster.is_alive:
        print(f"🏆 {monster.name} är besegrad!")
        return  # monstret är dött, så det slår inte tillbaka

    # --- Monstrets tur ---
    monster_turn(player, monster)


def monster_turn(player: Player, monster: Monster) -> None:
    """Monstret slår tillbaka."""
    # TODO(du): Lektion 6
    #   1. Slå fram monstrets skada (monster har samma roll_damage som alla Characters).
    #   2. Låt spelaren ta skadan.
    #   3. Skriv ut t.ex. "Grottråtta biter dig för 2 skada. Du har 28/30 HP."
    #   Bonus (lägg till `import random` högst upp i filen först):
    #   - Missar: med 20 % chans missar monstret. random.random() ger ett tal mellan 0 och 1,
    #     så `if random.random() < 0.2:` är sant ungefär var femte gång.
    #   - Kritiska träffar: med 10 % chans gör monstret dubbel skada.
    #   (Gör samma sak för spelaren i fight_round om du vill.)
    raise NotImplementedError("Lektion 6: monster_turn i combat.py (monstren slår inte tillbaka än!)")
