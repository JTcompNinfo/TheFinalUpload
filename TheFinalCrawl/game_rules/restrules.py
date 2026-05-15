import random
def rest(player, ui):

    # -------------------------
    # CHECK REST LIMIT
    # -------------------------
    if player.rests_remaining <= 0:
        ui.show_message(
            "You are too exhausted to rest again here."
        )
        return

    if player.current_health >= player.max_health:
        ui.show_message(
            "You are already at full strength."
        )
        return


    # consume a rest
    player.rests_remaining -= 1


    # -------------------------
    # REST HEALING
    # -------------------------
    heal_amount = round(player.max_health * 0.30)
    heal_amount += random.randint(-8, 8)
    heal_amount = max(12, heal_amount)

    old_hp = player.current_health
    player.current_health = min(
        player.max_health,
        player.current_health + heal_amount
    )
    healed = player.current_health - old_hp


    # -------------------------
    # AMBIENT TEXT PER LAYER
    # -------------------------
    messages = {

        1: "You sit in front of flickering screens. Silence surrounds you.",
        2: "Neon light hums softly while distant music fades in and out.",
        3: "The smell of decay and sugar hangs in the air as you rest.",
        4: "You hide behind financial ruins while distant systems collapse.",
        5: "Sirens echo endlessly as you catch your breath.",
        6: "Static-filled broadcasts whisper nonsense while you recover.",
        7: "Gunfire echoes far away as you patch your wounds.",
        8: "Glitching reality flickers while corrupted data flows around you.",
        9: "Even silence feels frozen here… something moves beneath the ice."
    }


    ui.show_message(messages.get(player.layer, "You take a moment to rest."))


    # -------------------------
    # AMBUSH CHANCE
    # -------------------------
    if random.randint(1, 100) <= 18:

        damage = max(5, round(player.max_health * 0.12))
        player.take_damage(damage)

        ui.show_message(f"""
Something finds you while you're resting.

You barely escape, but take {damage} damage.

HP: {player.current_health}/{player.max_health}
""")
        return


    # -------------------------
    # SUCCESS REST
    # -------------------------
    ui.show_message(f"""
You recover for a moment.

Rested: +{healed} HP
Remaining rests: {player.rests_remaining}

HP: {player.current_health}/{player.max_health}
""")