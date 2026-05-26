import random
from game_rules import NpcAndPlayerRules
from game_rules import combatRules
from game_rules.combatRules import paged_item_picker
from game_rules import shopRules
from game_rules.restrules import rest
import os
import platform
import subprocess
from game_rules.itemRules import ALL_ITEMS, key

# ── Inventory / equip menu (accessible from the explore screen) ───────────────

def show_inventory_menu(ui, player):
    """
    Let the player view their inventory and manually change equipped gear.
    Items are shown 6 per page so large inventories don't break the UI.
    Loops until the player chooses to go back.
    """
    while True:
        weapon_name = player.equipped_weapon.name if player.equipped_weapon else "None"
        armor_name  = player.equipped_armor.name  if player.equipped_armor  else "None"

        # ── Summary header shown above the action menu ──
        header = "\n".join([
            "=== INVENTORY ===",
            f"HP: {player.current_health} / {player.max_health}",
            f"Gold: {player.gold}",
            f"ATK: {player.get_attack_power()}  |  DEF: {player.get_defense()}",
            "",
            f"Equipped Weapon : {weapon_name}",
            f"Equipped Armor  : {armor_name}",
            "",
            f"Items in bag: {len(player.inventory)}",
        ])

        # ── Top-level action choice ──
        action = ui.show(header, ["Use / Equip item", "Back"])

        if action == 2:
            break

        # ── Pick an item from the paged list ──
        if not player.inventory:
            ui.show_message("Your inventory is empty.")
            continue

        # Build display labels that show equipped tags
        class LabelledItem:
            def __init__(self, item, label):
                self.item  = item
                self._label = label
            def __str__(self):
                return self._label

        labelled = []
        for item in player.inventory:
            tag = ""
            if item is player.equipped_weapon:
                tag = " [W]"
            elif item is player.equipped_armor:
                tag = " [A]"
            labelled.append(LabelledItem(item, f"{item}{tag}"))

        picked = paged_item_picker(ui, labelled, title="Select an item")
        if picked is None:
            continue

        item = picked.item

        # ── Act on the chosen item ──
        if hasattr(item, "heal_amount"):
            old_hp = player.current_health
            player.heal(item)
            healed = player.current_health - old_hp
            ui.show_message(
                f"Used {item.name}.\n"
                f"Healed {healed} HP.\n"
                f"HP: {player.current_health}/{player.max_health}"
            )

        elif hasattr(item, "attack_bonus"):
            player.equipped_weapon = item
            ui.show_message(f"Equipped {item.name} (+{item.attack_bonus} ATK).")

        elif hasattr(item, "defense_bonus"):
            player.equipped_armor = item
            ui.show_message(f"Equipped {item.name} (+{item.defense_bonus} DEF).")

        else:
            ui.show_message(
                f"{item.name} cannot be used right now."
            )


# ── Standard encounters ───────────────────────────────────────────────────────
def spawn_enemy(layer):
    factory = random.choice(NpcAndPlayerRules.ENEMY_POOLS[layer])
    return factory()

def run_theCombat(ui, player, enemies):
    return combatRules.combat(player, enemies, ui)

def random_combat_encounter(ui, player):
    count = random.choices([1, 2], weights=[80, 20], k=1)[0]
    enemies = [spawn_enemy(player.layer) for _ in range(count)]
    names = ", and ".join(e.name for e in enemies)
    ui.show_message(f"{names} emerge!")
    return run_theCombat(ui, player, enemies)

def baller(ui, player):
    choice = ui.show(
        "You see a red ball rest on the ground",
        ["Grab", "Walk away"]    
    )

    if choice == 1:
        ui.show_message("You walk up and grab the ball.")
        image_path = 'baller.jpeg'
        try:

            if platform.system() == 'Windows':
                # Windows uses os.startfile
                os.startfile(image_path)
            elif platform.system() == 'Darwin':
                # macOS uses the 'open' command
                subprocess.run(['open', image_path])
            else:
                # Linux typically uses 'xdg-open'
                subprocess.run(['xdg-open', image_path])
        except:
            pass
        ui.show_message("Your mind fills with infromtion of someone called Baller and the ball is now gone.")
        player.base_attack += 1
    
    elif choice == 2:
        ui.show_message("You walk away from the ball")


def timid_soul(ui, player):

    def justdoit(ui, player):
        combatRules.combat(player, NpcAndPlayerRules.Luke(), ui)
    
    choice = ui.show(
        "Between two burning cars, a timied soul drifts toward you.\n"
        "It moves wrong — too slow, too quiet — like it forgot how to be angry.\n"
        "Everyone else on this block is screaming.\n"
        "This one just watches them.",
        ["Talk", "Ignore"]
    )
    if choice == 1:
        choice = ui.show(
            'The soul looks at you the way someone looks at a door\n'
            'they have never been allowed to open.\n\n'
            '"You\'re talking to me."\n'
            'Not a question. Just a fact it hasn\'t figured out yet.\n'
            '"Nobody really... okay. Okay.\n'
            'Will you hear my story?"',
            ["Listen", "Tell it to leave", "Reach out and touch it"]
        )

        if choice == 2:
            ui.show_message(
                "It nods once. Slow.\n"
                "\"Right. Yeah. Of course.\"\n\n"
                "It doesn't get angry right away.\n"
                "That's almost worse — watching it decide,\n"
                "watching a lifetime of swallowed anger finally find a direction.\n\n"
                "It finds you."
            )
            justdoit(ui, player)

        elif choice == 3:
            ui.show_message(
                "Your hand passes through it.\n"
                "The cold of it — the specific cold of someone who was never touched\n"
                "with anything kind — sets something off deep inside it.\n"
                "Don't."
            )
            justdoit(ui, player)

        elif choice == 1:
            ui.show_message(
                'It takes a second before it starts. Like it\'s checking\n'
                'whether you\'re going to leave mid-sentence.\n\n'
                '"I was seventeen when I died. Car accident.\n'
                'Nobody came to identify me for four days."\n\n'
                "A siren wails down the burning street. The soul doesn't react.\n\n"
                '"I\'d been on my own since I was about twelve.\n'
                'Parents weren\'t — they weren\'t around. So it was just me.\n'
                'I figured it out. I always figured it out.\n'
                'That\'s what you do when there\'s nobody else to do it."\n\n'
                "It says this the way someone says it\n"
                "who has said it to themselves every single day."
            )

            choice = ui.show(
                '"I wasn\'t a bad kid. I just never had anywhere to put it, you know?\n'
                'The anger. It just kind of... sat there.\n'
                'All of it. My whole life.\n'
                'I kept thinking one day I\'d figure out what to do with it."',
                ["Ask if it was always angry", "Tell it everyone has problems", "Say nothing and look away"]
            )

            if choice == 2:
                ui.show_message(
                    "It stares at you.\n"
                    '"Everyone has problems."\n\n'
                    "The words come out of you and just hang there in the hot air.\n\n"
                    "The soul's expression doesn't change.\n"
                    "But the wrath layer answers — it always answers\n"
                    "when someone says exactly the wrong thing."
                )
                justdoit(ui, player)

            elif choice == 3:
                ui.show_message(
                    "You look away.\n"
                    "It notices immediately.\n"
                    "Of course it does. It spent its whole life watching\n"
                    "for exactly that — the moment someone decides\n"
                    "you aren't worth the effort.\n\n"
                    "The anger it held its entire life picks now to finally move."
                )
                justdoit(ui, player)

            elif choice == 1:  # Correct
                ui.show_message(
                    'It thinks about that for a moment.\n\n'
                    '"Yeah. I think so. Even when I was little.\n'
                    'But you can\'t be angry when you\'re the only one holding\n'
                    'everything together. You just can\'t afford it.\n'
                    'So I just... kept it. All of it.\n'
                    'Every time someone didn\'t show up. Every time I had to\n'
                    'figure something out alone that kids aren\'t supposed to\n'
                    'figure out alone.\n\n'
                    'I kept it all and I never told anyone\n'
                    'because there was nobody to tell."\n\n'
                    "Down the block, two souls are screaming at each other\n"
                    "over something that stopped mattering decades ago.\n"
                    "This one just watches them quietly."
                )

                choice = ui.show(
                    'It turns back to you.\n\n'
                    '"That\'s why I\'m here, I think.\n'
                    'Not because I was mean. I wasn\'t mean.\n'
                    'I just never let it out and then I died\n'
                    'and it was still in me\n'
                    'and I guess it had to go somewhere."',
                    ["Ask what it needed back then", "Tell it it should have asked for help", "Ask why it never let it out"]
                )

                if choice == 2:
                    ui.show_message(
                        '"Should have asked for help."\n\n'
                        "It repeats it quietly.\n\n"
                        '"Who."\n\n'
                        "Not a question.\n\n"
                        "The single word sits between you.\n"
                        "And then the layer of Wrath does what it does —\n"
                        "it takes the thing that was never allowed out\n"
                        "and it lets it out now."
                    )
                    justdoit(ui, player)

                elif choice == 3:
                    ui.show_message(
                        '"Because if I started I wasn\'t sure I\'d stop.\n'
                        'And I couldn\'t stop. I didn\'t have that option.\n'
                        'I had rent. I had—"\n\n'
                        "It cuts itself off.\n"
                        "You can see it — the wall going back up,\n"
                        "the old reflex, the one that kept it functioning\n"
                        "and kept it alone and brought it here.\n\n"
                        "The wall comes up and the anger comes with it."
                    )
                    justdoit(ui, player)

                elif choice == 1:  # Correct
                    ui.show_message(
                        "It goes very still.\n\n"
                        "The sirens keep wailing. The broken speaker down the road\n"
                        "keeps broadcasting someone insisting they are a genius.\n"
                        "The burning cars keep burning.\n\n"
                        '"Someone to just... check in.\n'
                        'Not fix it. Not even fix anything.\n'
                        'Just — ask how I was doing and actually want to know.\n'
                        'That\'s it. That\'s the whole thing.\n\n'
                        'Stupid, right?"\n\n'
                        "You tell it that it isn't stupid.\n\n"
                        "It looks at you for a long time.\n\n"
                        '"I found this on the street the day before I died.\n'
                        'Was gonna pawn it but I never got around to it.\n'
                        'Kept it in my pocket.\n'
                        'Don\'t really know why I still have it down here."\n\n'
                        "It holds out a lighter. Old, steel, dented on one side.\n"
                        "Still works. You can tell by the way it holds it —\n"
                        "like something that got it through cold nights\n"
                        "it never talked about.\n\n"
                        '"Take it. You look like you\'ve got somewhere to be."\n\n'
                        "It drifts back toward the burning street.\n"
                        "Doesn't dissolve dramatically. Doesn't say anything else.\n"
                        "Just goes.\n"
                        "The quietest thing in Wrath."
                    )
                    player.inventory.add(ALL_ITEMS[44])

    # ── Ignore branch ──────────────────────────────────────────────────────────
    elif choice == 1:
        weights = [95, 5]
        options = [1, 2]
        bosspossible = random.choices(options, weights=weights, k=1)[0]

        if bosspossible == 1:
            ui.show_message(
                "The soul begins to rage as you try to ignore it and walk away.\n"
                "You watch it swell and bubble with something it spent a lifetime compressing."
            )
            justdoit(ui, player)

        elif bosspossible == 2:
            ui.show_message(
                "You move away from the soul with the feeling like you just barely missed something big."
            )

def encounter_cursed_chest(ui, player):
    choice = ui.show(
"""
A supply crate sits wedged against a wall.

Stenciled on the side:

"CRAWL 31 — EQUIPMENT CACHE — DO NOT ABANDON"

Someone abandoned it anyway.

The seal is still intact.
""",
        ["Break the seal", "Leave it"]
    )
    if choice == 1:
        if random.random() < 0.5:
            player.gold += 15
            ui.show_message(
"""
Inside: emergency rations, a half-spent flare, and a roll of currency from a government
that apparently funds these descents.

The crawl number on the bills is different from the crate.

Someone restocked this before they left.

They didn't make it back either.
"""
            )
        elif key not in player.inventory:
            player.inventory.append(key)
            ui.show_message(
f"""
Most of the supplies have rotted or burned out.

But taped to the inside lid is a {key.name}.

A handwritten label reads: "If you got this far — you'll need it more than we did."

You take the {key.name}.
"""
            )
        else:
            player.take_damage(5)
            ui.show_message(
"""
The crate reacts the moment you touch it.

Not a mechanical trap.

Something inside the layer itself — like it recognized the breach.

A pulse of heat tears through your hand.

The crate collapses into ash.

Nothing inside.

Whatever was here was already claimed.
"""
            )
    else:
        ui.show_message(
"""
You leave it.

CRAWL 31 left it here for a reason.

You're not sure that reason was good.
"""
        )


def encounter_healing_fountain(ui, player):
    choice = ui.show(
"""
A pipe juts from the wall at a broken angle.

Liquid drips from it steadily.

Not water.

Too still. Too slow. Faintly luminescent.

A crawl-team field note is taped beside it, hand-written:

"TESTED. STABLE. PROBABLY."
""",
        ["Drink from it", "Ignore it"]
    )
    if choice == 1:
        if random.random() < 0.5:
            player.current_health = min(player.max_health, player.current_health + 10)
            ui.show_message(
"""
It tastes like nothing.

Then your body processes it.

Whatever the crawl teams pumped through these pipes to survive down here —
it works.

You feel the damage in your muscles close slightly.

Probably fine.
"""
            )
        else:
            player.current_health -= 10
            ui.show_message(
"""
It goes down wrong.

Not poison exactly.

More like your body trying to process something that was never meant for living tissue.

The layer shifts around you for a moment.

Then settles.

The note lied, or was written by someone with a much higher tolerance than you.
"""
            )
    else:
        ui.show_message(
"""
You leave it dripping.

Somewhere in a corporate building on the surface,
an energy meter ticks up by a fraction.

That's all this place is to them.
"""
        )


def shopNormal(ui, player):
    ui.show_message("You see what looks to be a shop in the distance as you walk.")
    shopRules.shop(ui, player)

def guideguy(ui, player):

    layer_info = {

        1: """
Guyde adjusts his cracked glasses.

"Limbo drains people slowly."

He gestures toward the endless apartment halls.

"Nobody here fights to survive anymore."
"They just exist."

"People spend eternity staring into glowing screens,
pretending they still have purpose."

"Be careful."
"The deeper you go,
the harder it becomes to care."
""",

        2: """
Guyde lights a cigarette with shaking hands.

"Lust isn't about love."

"It's obsession."
"Control."
"Need."

Music pulses faintly through distant alleyways.

"People here will say whatever you want to hear."
"That doesn't mean they mean it."

"Trust gets people killed in this layer."
""",

        3: """
Guyde wrinkles his nose.

"Gluttony consumes everything."

Grease drips from nearby walls.

"People here eat constantly."
"Food. Entertainment. Distractions."

"They're terrified of silence."

A loud laugh echoes somewhere far away.

"If something here seems excessive..."
"Run."
""",

        4: """
Guyde stares upward at distant skyscrapers.

"Greed turned suffering into infrastructure."

Stock tickers crawl endlessly across broken screens.

"The people above live like gods."
"The people below die unnoticed."

He pauses.

"This layer worships ambition."
"No matter the cost."
""",

        5: """
Guyde flinches at distant sirens.

"Wrath spreads fast."

"Nobody here knows how to stop being angry."

Burned cars line the streets.

"Arguments become riots."
"Riots become massacres."

"Doesn't matter who started it anymore."
""",

        6: """
Guyde lowers his voice.

"Heresy destroys truth itself."

Televisions nearby broadcast conflicting information.

"The people here don't know what's real anymore."

"They argue constantly."
"About history."
"About science."
"About reality."

He looks exhausted.

"Eventually people stop caring about truth entirely."
""",

        7: """
Guyde looks away from a nearby bloodstain.

"Violence became normal here."

Factories thunder in the distance.

"The people stopped seeing each other as human."

He kicks an abandoned glove aside.

"Mercy doesn't survive long in this layer."
""",

        8: """
Guyde checks the shadows nervously.

"Fraud lies about everything."

Digital billboards flicker overhead.

"Names change."
"Faces change."
"Promises change."

He sighs.

"Nobody here believes in truth anymore."
"They only believe in profit."
""",

        9: """
Guyde goes silent for several seconds.

The air itself feels frozen.

"Treachery is different."

"No screaming."
"No riots."

"Just betrayal."

Massive cracks spread beneath the black ice.

"Something ancient waits below."

"And I don't think it ever forgave humanity."
"""
    }
    choice = ui.show(
"""
A man leans against the wall ahead of you.

Not a soul.

Equipment. Crawl gear, older model. Cracked glasses.

He sees you coming and doesn't move.

Like he's been waiting, but not for anything specific.

Just waiting.
""",
        ["Talk", "Punch"]
    )
    if choice == 1:
        ui.show_message(
            f"Hello {player.name}.\n"
            f"I am Guyde.\n\n"
            f"{layer_info.get(player.layer, 'I know nothing about this place.')}"
        )
    elif choice == 2:
        ui.show_message(
            "You punch him in the face.\n\n"
            "He doesn't stumble. Doesn't react with pain.\n\n"
            "His expression moves through surprise and lands somewhere that looks like relief."
        )
        ui.show_message(
            '"I\'ve been waiting for someone to break my seal. To make the first hit."\n\n'
            "He rolls his neck slowly.\n\n"
            '"The layers don\'t let me fight until someone starts it."\n\n'
            '"Thanks for that."'
        )
        ui.show_message(
            '"Now prepare for the end."'
        )
        combatRules.combat(player, NpcAndPlayerRules.Guyde, ui)


def encounter_wandering_soul(ui, player):
    choice = ui.show(
"""
A soul drifts toward you.

It moves differently from the ones native to this layer.

Purposeful. Searching.

It stops when it sees your equipment.

It recognizes it.
""",
        ["Let it approach", "Back away"]
    )

    options = [1, 2]
    weights = [60, 40]
    battleChance = random.choices(options, weights=weights, k=1)[0]

    if choice == 1 and battleChance == 1:
        ui.show_message(
"""
It gets close enough that you can see the crawl-team insignia burned into what was once its jacket.

A different number than yours.

"You're still solid," it says.

Not a compliment. Just an observation from something that no longer is.

"Listen. Before I lose the thread completely."
"""
        )

        options = [1, 2, 3]
        weights = [80, 10, 10]
        bonus = random.choices(options, weights=weights, k=1)[0]

        if bonus == 1:
            player.rests_remaining += 1
            ui.show_message(
f"""
"The teams that made it past layer 5 — the ones who actually came back —
they rationed everything. Energy. Movement. Rest."

"Don't burn yourself out chasing the bottom."

It presses something intangible against your chest.
A kind of warmth that doesn't belong to any layer.

"They sent me down here to find the last team's data."

"I didn't find it."

"But I found enough."

It drifts back into the dark.

You feel steadier. Restored in some way the layer can't account for.

You now have {player.rests_remaining} rests this layer.
"""
            )

        elif bonus == 2:
            player.base_defense += 1
            ui.show_message(
f"""
"The early crawls — they didn't account for what the layers do to the body."

"By layer 4, soldiers were cracking. Not breaking. Cracking. Like the pressure
was getting into them at a structural level."

"The teams that survived long enough to come back made modifications."

It reaches out. Its hand passes through your arm — but leaves something behind.

A dull solidity. Like the surface tension of your body increased by a fraction.

"They learned. Slowly. Too slowly for most of them."

"You have a head start now."

You now have {player.base_defense} base defense.
"""
            )

        elif bonus == 3:
            player.base_attack += 1
            ui.show_message(
f"""
"The layers push back. That's not metaphor."

"The deeper you go, the more the structure resists you."

"The only crawlers who got through were the ones who pushed harder."

It stares at you for a long moment. Like it's deciding something.

"The data we were sent to recover — it doesn't matter."

"What matters is that you get further than we did."

Something fierce transfers between you. 
Not emotion. Capacity.

"Survive this layer. That's all."

You now have {player.base_attack} base attack.
"""
            )

    elif choice == 1 and battleChance == 2:
        ui.show_message(
"""
As you hold still, it gets close enough that you can see its expression.

Wrong.

Not searching. Not purposeful.

Hollow.

Whatever this soul was before the layer processed it — it's gone.

What's left reacts the way the layer made it react.

It attacks.
"""
        )
        random_combat_encounter(ui, player)

    else:
        ui.show_message(
"""
You back away.

It watches you go.

Doesn't follow.

You don't know if that was the right call.

You keep walking.
"""
        )

# lore based

def encounter_static_broadcast(ui, player):

    choice = ui.show(
"""
A broken television hangs from the ceiling.

It is not plugged in.

Still, it plays static.
""",
[
"Ignore it",
"Listen closely",
"Touch the screen"
]
    )

    if choice == 2:
        ui.show_message("""
The static resolves for half a second.

A map appears.

Not of Earth.

Of something layered.

You only recognize one word before it disappears:

"DESCENT LOG: PRIOR ATTEMPTS"
""")

    elif choice == 3:
        ui.show_message("""
Your hand passes through the screen.

For a moment, you feel something on the other side.

Cold stone.

And breathing.

Then it snaps back to static.
""")

    elif choice == 1:
        ui.show_message("The television continues to play nothing that makes sense.")

def encounter_missing_team(ui, player):

    choice = ui.show(
"""
You find a body slumped against a wall.

Crawl-team gear.

Not current issue. Older.

Their face is frozen mid-expression —
not fear, not pain.

Something closer to realization.

A worn patch on their shoulder reads a team number.

Not yours.

Close, but not yours.
""",
        ["Search the body", "Check the team patch", "Leave it"]
    )

    if choice == 1:
        ui.show_message(
"""
Their pockets contain dozens of identical maps.

All labeled with different crawl numbers.

All ending at the same place.

Someone on this team was collecting them.

Tracking the pattern.

None of them got further than this layer.

A folded note reads, in cramped handwriting:

"EVERY CRAWL ENDS HERE. COINCIDENCE THRESHOLD EXCEEDED."

"IT IS NOT ROUTING US RANDOMLY."
"""
        )

    elif choice == 2:
        ui.show_message(
"""
The patch is heat-damaged but readable.

"TEAM DESIGNATION: 48"

Your team number.

You check the gear more carefully.

Wrong manufacture date. Wrong kit generation.

This is not your team.

This is a prior crawl that was assigned the same designation.

The same number, again, for a reason no one briefed you on.
"""
        )

    elif choice == 3:
        ui.show_message(
"""
You walk away.

The silence settles back in around them.

Whatever they found — whatever stopped them here —
is still somewhere ahead of you.
"""
        )

def encounter_memory_wall(ui, player):

    choice = ui.show(
"""
A wall pulses faintly when you approach it.

Like it's reacting to your presence.
""",
[
"Touch the wall",
"Press your ear to it",
"Walk past"
]
    )

    if choice == 1:
        ui.show_message("""
The stone reacts instantly.

Images flash under your hand:

Elevators.

Crawlers.

Failures.

Then your own face.

From an angle you do not recognize.
""")

    elif choice == 2:
        ui.show_message("""
You hear voices inside the wall.

Not speaking.

Repeating.

The same phrase over and over:

"DO NOT REACH THE FINAL LAYER"
""")

    elif choice == 3:
        ui.show_message("The wall continues to pulse faintly as you leave.")

def encounter_recorder(ui, player):

    choice = ui.show(
"""
A cracked recording device lies half-buried in ash.

Its light is still blinking.

Not steadily.

Like it’s responding to something nearby.
""",
[
"Play recording",
"Download data",
"Open file system",
"Destroy it"
]
    )

    if choice == 1:
        ui.show_message("""
A voice plays through heavy distortion:

"...this is crawl 17... we lost two teams before layer 3..."

"...the structure isn't consistent anymore..."

"...it changes depending on who is observing it..."
""")

        ui.show_message("""
A long pause.

Then:

"...we're not descending anymore..."

"...we're being routed..."
""")

        ui.show_message("""
The recording glitches violently.

A second voice overlaps.

Not part of the file.

Too close to the microphone.
""")

        ui.show_message("""
"...stop recording that..."
""")

        ui.show_message("""
Silence.
""")

        ui.show_message("""
The device returns to static.
""")

    elif choice == 2:
        ui.show_message("""
Data transfer begins.

Progress: 12%
Progress: 38%
Progress: 61%

Then it stops.
""")

        ui.show_message("""
A single directory appears:

"CORE_ARCHIVE / ACCESS LIMITED"
""")

        deeper = ui.show(
"""
The device is requesting confirmation.

Something inside is still active.
""",
[
"Force access",
"Back out",
"Corrupt the transfer"
]
        )

        if deeper == 1:

            ui.show_message("""
Access attempt initiated...
""")

            success_chance = 0.65

            if random.random() < success_chance:

                ui.show_message("""
Access forced.

The directory opens unwillingly.
""")

                ui.show_message("""
Files unzip themselves without permission.
""")

                ui.show_message("""
Crawl logs appear.

Not sequential.

Overlapping.
""")

                ui.show_message("""
Crawl 3: no recorded exit  
Crawl 8: no recorded exit  
Crawl 12: no recorded exit  
Crawl 17: partial return, subject unstable  
Crawl 24: no recorded exit  
Crawl 31: no recorded exit  
""")

                ui.show_message("""
Then a final entry appears:

"ALL DESCENTS ARE CONTINUATIONS OF PREVIOUS DESCENTS"
""")

            else:

                ui.show_message("""
The device rejects the request.

Not with an error.

With resistance.
""")

                ui.show_message("""
The screen briefly shows:

"UNAUTHORIZED CONTINUATION ATTEMPT DETECTED"
""")

                ui.show_message("""
The folder collapses into itself.

Lines of text delete themselves as you watch.
""")

                ui.show_message("""
Then one final message appears:

"YOU ARE NOT LISTED IN THIS DESCENT."
""")

                ui.show_message("""
The device goes warm.

Too warm to hold for long.

Then it resets to the main menu.
""")

        elif deeper == 2:
            ui.show_message("""
You stop the transfer.

The device cools slightly in your hand.

Like it stopped listening.
""")

        elif deeper == 3:
            ui.show_message("""
Corruption injected.

The device emits a single tone.

Like something acknowledging interference.
""")

            ui.show_message("""
A brief message appears:

"GOOD."
""")

    elif choice == 3:
        ui.show_message("""
The device cracks under pressure.

The light dies instantly.

For a moment, everything feels quieter.

Then your surroundings feel less certain.
""")

        ui.show_message("""
Like something that was being recorded is now aware it is no longer being observed.
""")

    elif choice == 3:
        ui.show_message("""
You leave it alone.

The blinking continues.

Slower now.

Like it’s waiting.
""")
        
def encounter_watcher(ui, player):

    choice = ui.show(
"""
Far away in the darkness,
something is standing still.

It does not move.

It does not approach.
""",
[
"Approach it",
"Call out",
"Look away"
]
    )

    if choice == 1:
        ui.show_message("""
The shape does not move.

But the distance between you never closes.

No matter how far you walk.
""")

    elif choice == 2:
        ui.show_message("""
Your voice echoes.

A moment later,

it echoes back.

But slightly wrong.
""")

    elif choice == 3:
        ui.show_message("When you look back, it is still there.")

ALL_ENCOUNTERS = {
    1: [
        (encounter_wandering_soul, 55),
        (encounter_cursed_chest, 90),
        (guideguy, 40),
        (random_combat_encounter, 110),
        (baller, 8),
        (encounter_healing_fountain, 45),
        (encounter_static_broadcast, 20),
        (encounter_missing_team, 30),
        (encounter_memory_wall, 25),
        (encounter_recorder, 25),
        (shopNormal, 20),
    ],

    2: [
        (encounter_wandering_soul, 55),
        (encounter_cursed_chest, 90),
        (guideguy, 40),
        (random_combat_encounter, 110),
        (baller, 8),
        (encounter_healing_fountain, 45),
        (encounter_static_broadcast, 20),
        (encounter_missing_team, 30),
        (encounter_memory_wall, 25),
        (encounter_recorder, 25),
        (shopNormal, 20),
    ],

    3: [
        (encounter_wandering_soul, 55),
        (encounter_cursed_chest, 90),
        (guideguy, 40),
        (random_combat_encounter, 110),
        (baller, 8),
        (encounter_healing_fountain, 45),
        (encounter_static_broadcast, 20),
        (encounter_missing_team, 30),
        (encounter_memory_wall, 25),
        (encounter_recorder, 25),
        (shopNormal, 20),
    ],

    4: [
        (encounter_wandering_soul, 55),
        (encounter_cursed_chest, 90),
        (guideguy, 40),
        (random_combat_encounter, 110),
        (baller, 8),
        (encounter_healing_fountain, 45),
        (encounter_static_broadcast, 20),
        (encounter_missing_team, 30),
        (encounter_memory_wall, 25),
        (encounter_recorder, 25),
        (shopNormal, 20),
    ],

    5: [
        (encounter_wandering_soul, 55),
        (encounter_cursed_chest, 90),
        (guideguy, 40),
        (random_combat_encounter, 110),
        (timid_soul, 40),
        (baller, 8),
        (encounter_healing_fountain, 45),
        (encounter_static_broadcast, 20),
        (encounter_missing_team, 30),
        (encounter_memory_wall, 25),
        (encounter_recorder, 25),
        (shopNormal, 20),
    ],

    6: [
        (encounter_wandering_soul, 55),
        (encounter_cursed_chest, 90),
        (guideguy, 40),
        (random_combat_encounter, 110),
        (baller, 8),
        (encounter_healing_fountain, 45),
        (encounter_static_broadcast, 20),
        (encounter_missing_team, 30),
        (encounter_memory_wall, 25),
        (encounter_recorder, 25),
        (shopNormal, 20),
    ],

    7: [
        (encounter_wandering_soul, 55),
        (encounter_cursed_chest, 90),
        (guideguy, 40),
        (random_combat_encounter, 110),
        (baller, 8),
        (encounter_healing_fountain, 45),
        (encounter_static_broadcast, 20),
        (encounter_missing_team, 30),
        (encounter_memory_wall, 25),
        (encounter_recorder, 25),
        (shopNormal, 20),
    ],

    8: [
        (encounter_wandering_soul, 55),
        (encounter_cursed_chest, 90),
        (guideguy, 40),
        (random_combat_encounter, 110),
        (baller, 8),
        (encounter_healing_fountain, 45),
        (encounter_static_broadcast, 20),
        (encounter_missing_team, 30),
        (encounter_memory_wall, 25),
        (encounter_recorder, 25),
        (shopNormal, 20),
    ],

    9: [
        (encounter_wandering_soul, 55),
        (encounter_cursed_chest, 90),
        (guideguy, 40),
        (random_combat_encounter, 110),
        (baller, 8),
        (encounter_healing_fountain, 45),
        (encounter_static_broadcast, 20),
        (encounter_missing_team, 30),
        (encounter_memory_wall, 25),
        (encounter_recorder, 25),
        (shopNormal, 20),
    ],
}


# ── Main encounter hub ────────────────────────────────────────────────────────

def randomEncounter(ui, player):
    loop = 0
    while loop == 0:
        """
        Present the player with their between-encounter options.
        Returns True normally, or raises SystemExit if the player saves and quits.
        """
        choice = ui.show(
            f"You are in layer {player.layer}. What do you do?",
            ["Explore", "Inventory", "Rest"]
        )
        if choice == 1:
            loop += 1
            if player.encountNumbr == player.shop_number:
                shopNormal(ui, player)
            else:
                encounters = ALL_ENCOUNTERS[player.layer]

                funcs = [e[0] for e in encounters]
                weights = [e[1] for e in encounters]

                chosen = random.choices(funcs, weights=weights, k=1)[0]

                chosen(ui, player)

        # Open inventory to check around
        elif choice == 2:
            show_inventory_menu(ui, player)

        elif choice == 3:
            rest(player, ui)