import sys
import subprocess
import random

try:
    import pyfiglet
except ImportError:
    print("pyfiglet not found. Installing...")
    subprocess.check_call([
        sys.executable,
        "-m",
        "pip",
        "install",
        "pyfiglet",
        "--break-system-packages"
    ])
    import pyfiglet

from game_rules import NpcAndPlayerRules
from game_rules import saveRules
from game_rules import itemRules
from game_rules.gameUI import AdventureUI

import game_rules.randomEccointers as randomEccointers
from game_rules.intors import show_layer_intro
from game_rules.intors import show_boss_intro
from game_rules.intors import show_post_boss_lore

# =========================
# INFERNO MAP
# =========================
INFERNO_MAP = (
    r"            \ /  1. Limbo" + "\n"
    r"            / \ " + "\n"
    r"           /   \ 2. Lust" + "\n"
    r"          /_____\ " + "\n"
    r"         /       \ 3. Gluttony" + "\n"
    r"        /_________\ " + "\n"
    r"       /           \ 4. Greed" + "\n"
    r"      /_____________\ " + "\n"
    r"     /               \ 5. Anger" + "\n"
    r"    /_________________\ " + "\n"
    r"   /                   \ 6. Heresy" + "\n"
    r"  /_____________________\ " + "\n"
    r" /                       \ 7. Violence" + "\n"
    r"/_________________________\ " + "\n"
    r"|                          \ 8. Fraud" + "\n"
    r"|___________________________\ " + "\n"
    r"|                            \ 9. Treachery" + "\n"
    r" \___________________________/ " + "\n"
    r"               || " + "\n"
    r"            LUCIFER"
)


# =========================
# LAYER DATA
# =========================
LAYER_NAMES = {
    1: "Limbo",
    2: "Lust",
    3: "Gluttony",
    4: "Greed",
    5: "Wrath",
    6: "Heresy",
    7: "Violence",
    8: "Fraud",
    9: "Treachery",
}

LEVEL_HP = {
    2: 54,
    3: 86,
    4: 129,
    5: 194,
    6: 237,
    7: 302,
    8: 377,
    9: 538
}

def puzzle(ui, player):

    ui.show_message("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
THE FINAL SEAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The frozen cavern narrows into a dead end.

At first it looks natural.

Then you notice the symmetry.

The ice walls are smooth.
Too smooth.

Massive chains disappear upward into darkness.

Something was built here.
""")

    ui.show_message("""
At the center of the chamber stands a colossal vault.

Bone-white.

Half buried beneath black ice.

Its surface is covered in thousands of carved horn symbols.

Most are cracked.
Broken.
Removed violently.
""")

    ui.show_message("""
Then something inside your inventory begins vibrating.
""")

    has_horn = False

    for item in player.inventory:
        if getattr(item, "name", "") == "Horn fragment":
            has_horn = True
            horn = item
            break

    if has_horn:

        ui.show_message(f"""
The {horn.name} grows warm in your pocket.

Not heat.

Recognition.
""")

    else:

        ui.show_message("""
Your inventory remains silent.

But the vault does not.

A deep grinding noise echoes through the cavern.

Like something behind the door noticed your arrival.
""")

        ui.show_message("""
Words slowly carve themselves into the ice:

"CONTINUATION INCOMPLETE."
""")

        ui.show_message("""
Without the missing fragment,
the seal cannot react.

And something behind it continues waiting.
""")

        return False

    solved = False

    while solved is False:

        choice = ui.show(
"""
The center of the vault contains a hollow space.

Exactly the shape of the Horn Fragment.

Around it are deep claw marks.

Something tried very hard to keep this sealed.
""",
[
"Place the Horn Fragment into the seal",
"Keep holding it",
"Throw it away"
]
        )

        # =========================
        # CORRECT CHOICE
        # =========================
        if choice == 1:

            ui.show_message(f"""
You press the {horn.name} into the center seal.
""")

            ui.show_message("""
The fragment sinks into the vault instantly.

Like bone reconnecting to a skeleton.
""")

            ui.show_message("""
Deep beneath the ice—

something massive suddenly stops moving.
""")

            ui.show_message("""
Then the entire chamber begins shaking violently.
""")

            ui.show_message("""
The horn symbols across the vault begin glowing one by one.

Thousands of them.

Not symbols.

Fingerprints.

Evidence.

Every crawl that reached this place left one behind.
""")

            ui.show_message("""
Images begin flashing across the frozen walls.

Old crawl teams.

Different uniforms.
Different centuries.
Different equipment.

But always the same chamber.

Always the same choice.
""")

            ui.show_message("""
Some teams turned back.

The vault stayed sealed.

Others inserted their fragments willingly.

The vault opened every single time.
""")

            ui.show_message("""
The realization settles slowly.

The Horn Fragment was never a key.

It was proof.

Proof that someone had already reached the seal before you.
""")

            ui.show_message("""
The fragment wasn't guiding you downward.

It was marking you as the next continuation.
""")

            ui.show_message("""
A final message tears across the ice:

"CONTAINMENT CYCLE TERMINATED."
""")

            ui.show_message("""
The chains above begin retracting violently.

Not unlocking.

Failing.
""")

            ui.show_message("""
The vault doors slowly split apart.

Beyond them is not fire.

Not darkness.

An abyss of frozen black air.
""")

            ui.show_message("""
Something enormous unfolds its wings deep below.
""")

            ui.show_message("""
Then, for the first time since entering Hell—

you hear Lucifer laugh.
""")

            solved = True

        # =========================
        # REFUSE
        # =========================
        elif choice == 2:

            ui.show_message("""
You keep hold of the Horn Fragment.

Immediately the pressure in the chamber increases.

The vault does not open.

But something behind it shifts slowly.

Patiently.
""")

            ui.show_message("""
Words appear across the ice:

"CONTINUATION REJECTED."
""")

            ui.show_message("""
The Horn Fragment becomes hotter in your hand.

Like the layer itself is waiting for you to stop hesitating.
""")

        # =========================
        # THROW IT
        # =========================
        elif choice == 3:

            ui.show_message("""
You throw the Horn Fragment across the chamber.

It skids across the ice.

For a moment—

nothing happens.
""")

            ui.show_message("""
Then the fragment begins dragging itself back toward you.
""")

            ui.show_message("""
Tiny cracks spread beneath it as it slowly pulls itself across the frozen floor.

Not pulled.

Crawling.
""")

            ui.show_message("""
It stops directly at your feet.
""")

            ui.show_message("""
The message on the vault changes:

"DESCENT CANNOT BE ABANDONED."
""")

    return True

# =========================
# SHOW MAP
# =========================
def show_map(ui: AdventureUI, player):

    choice = ui.show_message(
        f"INFERNO MAP\n\n"
        f"{INFERNO_MAP}\n\n"
        f"You are currently in Layer {player.layer}: "
        f"{LAYER_NAMES[player.layer]}",
    )
    

def deathCheck(ui, player):
    if player.current_health <= 0:

        ui.show_message(
            "You have died in the Inferno.",
            "[ Press any key ]"
        )

        saveRules.delete_save()

        return True

    return False


# =========================
# RUN A SINGLE LAYER
# =========================
def run_layer(ui: AdventureUI, player):

    current_layer = player.layer
    layer_name = LAYER_NAMES[current_layer]

    if current_layer not in player.completed_layers:

        hp_gain = LEVEL_HP.get(current_layer, 0)

        if hp_gain > 0:
            player.level_up(hp_gain)

        player.completed_layers.append(current_layer)

    # =========================
    # Show map
    # =========================
    show_map(ui, player)
    show_layer_intro(ui, player.layer)

    # =========================
    # Encounters
    # =========================
    encounters = random.randint(10, 20)
    player.shop_number = random.randint(1, encounters)



    for i in range(encounters):
        player.encountNumbr = i
        randomEccointers.randomEncounter(ui, player)

        # =========================
        # Death Check
        # =========================
        if deathCheck(ui, player):
            return False

    # =========================
    # Boss Fight
    # =========================
    # Boss Fight
    boss_factory = NpcAndPlayerRules.BOSSES.get(player.layer)
    boss = boss_factory() if boss_factory else None
    if player.layer != 9:
        if boss is None:
            ui.show_message(f"[ERROR] No boss defined for layer {player.layer}. Skipping.")
        else:
            show_boss_intro(ui, player.layer)
            
            randomEccointers.run_theCombat(ui, player, boss)
    else:
        if not puzzle(ui, player):
            return False
        if boss is None:
            ui.show_message(f"[ERROR] No boss defined for layer {player.layer}. Skipping.")
        else:
            show_boss_intro(ui, player.layer)
            randomEccointers.run_theCombat(ui, player, boss)

    # =========================
    # Death Check After Boss
    # =========================
    if deathCheck(ui, player):
        return False

    show_post_boss_lore(ui, player.layer)

    # =========================
    # Final Layer Complete
    # =========================
    if current_layer >= 9:

        ui.show_message(
            "You defeated Lucifer.\n\n"
            "The Final Crawl is Complete.",
            "[ Press any key ]"
        )

        saveRules.delete_save()

        return False

    # =========================
    # Descend Option
    # =========================
    choice = ui.show(
        f"You survived Layer {current_layer}: {layer_name}",
        ["Descend Deeper", "Save and Exit"]
    )

    player.layer = current_layer + 1

    if choice == 2:
        saveRules.save_game(player)
        raise SystemExit(0)

    return True


# =========================
# MAIN GAME LOOP
# =========================
def game_loop(ui: AdventureUI, player):

    running = True

    while running:

        running = run_layer(ui, player)

        # Reset rests between layers
        if running:
            player.rests_remaining = 3
    if not player.current_health <= 0:
        ui.show_message(
            "The Final Crawl is Complete.",
            "[ Press any key ]"
        )

def show_game_intro(ui):

    ui.show_message(
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
THE FINAL CRAWL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

YEAR 2089

Hell was discovered decades ago.

Not spiritually.

Physically.

Beneath the Earth's crust,
massive artificial shafts descend into impossible depths.
""")

    ui.show_message(
"""
The first crawls were government experiments.

Then corporations got involved.

Soon entire economies depended on it.

Hell produces energy.

Not oil.
Not nuclear power.

Suffering.

The deeper a crawl descends,
the more energy can be extracted.
""")

    ui.show_message(
"""
Every nation on Earth now operates Infernal Wells.

Most crawlers never return.

But the pay is life changing.

You signed the contract anyway.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NEXUS EXTRACTION GROUP
INFERNAL RECOVERY DIVISION

TEAM 48 DESCENT LOG
""")

    ui.show_message(
"""
Your squad descended three days ago.

12 crawlers.
4 security personnel.
2 researchers.

Your objective:

Reach Layer 5.

Recover a lost extraction drill.

Return alive.

Simple.

At least that was the lie.
""")

    ui.show_message(
"""
The elevator stopped suddenly.

Then the lights went out.

People started screaming in the dark.

Something massive moved beneath the platform.

You remember the sound first.

Chains dragging across stone.

Then wings.

Huge wings.
""")

    ui.show_message(
"""
The security team opened fire blindly.

It did nothing.

The researchers vanished first.

Then the screaming started.

One by one,
your team disappeared into the darkness.

You never even saw what killed them.

Only eyes.

Ancient.
Frozen.
Watching.
""")

    ui.show_message(
"""
Then silence.

When the emergency lights returned,
you were alone.

Bodies covered the elevator floor.

Steel walls were torn open like paper.

Across the far wall,
written in blood:

"TURN BACK."
""")

    ui.show_message(
"""
But the elevator was still descending.

And somehow...

Whatever killed your team...

Left you alive.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You have entered Hell.
""")


# =========================
# NEW GAME
# =========================
def gamestart(ui: AdventureUI):

    name = ui.input_str(
        "Welcome to The Final Crawl.\n\n"
        "Enter your character name.",
        prompt="Name: "
    )

    if not name:
        name = "Dante"

    player = NpcAndPlayerRules.Player(name, 35)

    # =========================
    # Starter Items
    # =========================
    player.inventory.append(itemRules.ALL_ITEMS[0])  # Weapon
    player.inventory.append(itemRules.ALL_ITEMS[3])  # Armor
    player.inventory.append(itemRules.ALL_ITEMS[6])  # Healing item

    player.equip_weapon(player.inventory[0])
    player.equip_armor(player.inventory[1])

    # Track level-up progress
    player.completed_layers = []

    ui.show_message(
        f"Welcome, {player.name}.",
        "[ Press any key ]"
    )

    # Delete old save on new game
    saveRules.delete_save()

    show_game_intro(ui)

    game_loop(ui, player)


# =========================
# LOAD GAME
# =========================
def loadgame(ui: AdventureUI):

    player = saveRules.load_game()

    if player is None:

        ui.show_message(
            "No save file found.",
            "[ Press any key ]"
        )

        return

    # Prevent crashes on old saves
    if not hasattr(player, "completed_layers"):
        player.completed_layers = []

    weapon_name = (
        player.equipped_weapon.name
        if player.equipped_weapon else "None"
    )

    armor_name = (
        player.equipped_armor.name
        if player.equipped_armor else "None"
    )

    ui.show_message(
        f"Save Loaded.\n\n"
        f"Name: {player.name}\n"
        f"Layer: {player.layer} — {LAYER_NAMES[player.layer]}\n"
        f"HP: {player.current_health}/{player.max_health}\n"
        f"Gold: {player.gold}\n"
        f"Weapon: {weapon_name}\n"
        f"Armor: {armor_name}",
        "[ Press any key ]"
    )

    game_loop(ui, player)


# =========================
# START SCREEN
# =========================
def start_screen():

    with AdventureUI(title="[ The Final Crawl ]") as ui:

        while True:

            logo = pyfiglet.figlet_format("The Final Crawl")

            save_label = (
                "Load Game"
                if saveRules.save_exists()
                else "Load Game (No Save)"
            )

            choice = ui.show(
                logo,
                ["New Game", save_label, "Quit"]
            )

            # =========================
            # NEW GAME
            # =========================
            if choice == 1:
                gamestart(ui)

            # =========================
            # LOAD GAME
            # =========================
            elif choice == 2:

                if saveRules.save_exists():
                    loadgame(ui)

                else:
                    ui.show_message(
                        "No save file exists.",
                        "[ Press any key ]"
                    )

            # =========================
            # QUIT
            # =========================
            elif choice == 3:

                ui.show_message(
                    "Thanks for playing The Final Crawl.",
                    "[ Press any key ]"
                )

                break


# =========================
# ENTRY POINT
# =========================
if __name__ == "__main__":
    start_screen()