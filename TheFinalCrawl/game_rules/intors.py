
#layer intors
def show_layer_intro(ui, layer):

    intros = {

        1: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAYER 1 — LIMBO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The elevator groans as it descends into darkness.

Fluorescent lights flicker overhead.
Rows of abandoned apartments stretch forever.
Computer monitors glow in empty rooms.

Nobody screams here.

Nobody even speaks.

The people of Limbo gave up long ago.

On one massive abandoned screen,
an old science documentary still plays to nobody.

You have entered Limbo.
""",

        2: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAYER 2 — LUST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Warm neon floods the streets below.

Music pounds through endless nightclubs.
Perfume and cigarette smoke choke the air.

Everyone here craves attention.
Validation.
Obsession.

Relationships are transactions.

Missing person posters cover the alley walls.
Most of them are very young.

You have entered Lust.
""",

        3: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAYER 3 — GLUTTONY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The smell hits first.

Grease.
Rot.
Sugar.

Mountains of trash tower overhead.
Broken televisions blast endless entertainment.

The people here consume constantly.

Food.
Media.
Distractions.

A faded billboard smiles down at you:

"Welcome to Flavortown."

You have entered Gluttony.
""",

        4: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAYER 4 — GREED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Skyscrapers pierce poisoned clouds.

Stock tickers crawl endlessly across massive screens.
Armed security patrol abandoned banks.

Everything here has a price.

Power.
Food.
Safety.

Far above,
rockets launch endlessly into the sky
while the streets below starve.

You have entered Greed.
""",

        5: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAYER 5 — WRATH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sirens echo endlessly through ruined streets.

Cars burn upside down.
Arguments erupt from every alleyway.

Everyone here is angry.

The people of Wrath lash out constantly,
unable to escape their hatred.

Through the static of a broken speaker,
someone keeps loudly insisting
they are a genius.

You have entered Wrath.
""",

        6: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAYER 6 — HERESY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Cold white lights illuminate endless hallways.

Screens broadcast propaganda nonstop.
Every wall is covered in censored truths.

Facts are rewritten.
History is manipulated.

A radio nearby crackles with paranoid shouting
about chemicals in the water.

You have entered Heresy.
""",

        7: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAYER 7 — VIOLENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Factories belch black smoke into crimson skies.
Gunfire cracks endlessly in the distance.

Violence is survival here.

Mercy died long ago.

A dusty white glove lies abandoned
beside a trail of blood.

You have entered Violence.
""",

        8: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAYER 8 — FRAUD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Nothing here is real.

Digital billboards shift constantly.
Faces change mid-conversation.

Every system has been corrupted.

Truth is manufactured.
Identity is bought and sold.

Collapsed crypto advertisements flicker weakly
across empty financial districts.

You have entered Fraud.
""",

        9: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LAYER 9 — TREACHERY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Silence.

Frozen structures rise from endless black ice.

Friends betrayed friends.
Families betrayed each other.
Humanity betrayed itself.

Deep beneath the ice,
a massive shape shifts slowly in the darkness.

Wings scrape against frozen stone.

You have entered Treachery.
"""
    }

    ui.show_message(intros[layer])


# =========================
# BOSS INTRO SYSTEM
# =========================

def show_boss_intro(ui, layer):

    intros = {

        1: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BOSS — NEIL DEGRASSE TYSON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The room opens into a dead observatory.

Dust covers abandoned computers.
Planetarium projectors flicker weakly overhead.

At the center of the chamber,
a man sits beneath artificial stars,
still speaking to an audience long gone.

"The universe is under no obligation
to make sense to you."

His voice echoes calmly through the darkness.

Neil deGrasse Tyson rises slowly.

"Yet here you are anyway."

The stars above begin to move.
""",

        2: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BOSS — JEFFREY EPSTEIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The music stops.

A private elevator descends into silence.
Velvet walls hide security cameras behind gold trim.

Photographs line the hallway.
Most faces are blurred out.

A man waits inside a luxurious lounge,
completely relaxed.

"You know,"
he says with a smile,
"power changes what people ignore."

The doors lock behind you.
""",

        3: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BOSS — GUY FIERI
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Neon signs ignite across the room.

Industrial fryers roar to life.
Grease floods the cracked tile floor.

An enormous kitchen stretches endlessly ahead.

At the center stands a smiling figure
in flame-covered clothing.

"Welcome..."
he says loudly,
"...to Flavortown."

Massive burners erupt around the arena.
""",

        4: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BOSS — ELON MUSK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

You enter a massive launch facility.

Robotic arms move overhead.
Screens display stock prices beside rocket trajectories.

Workers collapse silently at terminals,
completely ignored.

At the far end of the chamber,
a man watches Earth from behind reinforced glass.

"We'll fix humanity,"
he mutters,
"even if humanity breaks first."

Outside,
another rocket launches into the black sky.
""",

        5: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BOSS — KANYE WEST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Floodlights snap on violently.

A stadium emerges from the darkness.
Thousands of empty seats surround the arena.

At center stage,
a lone figure grips a microphone.

"They never understood me."

His voice shakes between rage and desperation.

"I am the greatest."

Speakers explode with deafening static.
The entire arena trembles.
""",

        6: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BOSS — ALEX JONES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Red emergency lights pulse overhead.

Stacks of documents cover the floor.
Televisions scream conflicting headlines simultaneously.

At the center of the chaos,
a man broadcasts wildly into a live microphone.

"They're poisoning everything!"
he screams.

Sweat pours down his face.
His eyes are bloodshot and frantic.

The walls themselves seem to shake with paranoia.
""",

        7: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BOSS — OJ SIMPSON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Rain pours endlessly from the black sky.

Police sirens flash in the distance.
A slow trail of blood cuts through the flooded streets.

A lone figure stands beneath a streetlamp,
wearing black gloves.

"You think you know the truth?"
he asks quietly.

The glove tightens around his hand.

Then he charges.
""",

        8: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BOSS — SAM BANKMAN-FRIED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The server room hums unnaturally.

Broken monitors display collapsing graphs.
Billions vanish across glowing screens in real time.

A young man sits calmly in a chair,
surrounded by dead systems.

"It was supposed to work,"
he mutters.

His fingers still type endlessly
into ruined financial algorithms.

Suddenly every screen flashes red.

ACCESS DENIED.
""",

        9: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINAL BOSS — LUCIFER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The ice cracks beneath your feet.

An endless frozen abyss stretches before you.
Wings larger than buildings shift slowly in darkness.

Then the chains begin to move.

Massive eyes open deep below the ice.
Ancient.
Exhausted.
Hateful.

The air itself freezes in your lungs.

A voice echoes from everywhere at once.

"Humanity required no temptation."

The chains shatter.

Lucifer rises.
"""
    }

    ui.show_message(intros[layer])

# =========================
# POST BOSS LORE
# =========================

def show_post_boss_lore(ui, layer):

    lore = {

        1: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AFTERMATH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Neil collapses back into his chair.

The artificial stars above flicker weakly.

"You still don't understand this place,"
he mutters.

He stares upward at the broken ceiling.

"Hell wasn't always this deep."

Dust falls from the observatory dome.

"Humanity dug further."

You remain silent.

"They found ways to descend safely.
Machines.
Elevators.
Rituals."

Neil laughs quietly to himself.

"And every time they came down here,
they brought something back."

The lights begin to die.

"Power.
Knowledge.
Weapons."

His voice lowers.

"Lucifer started fighting back centuries ago."

The stars finally go dark.
""",

        2: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AFTERMATH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Jeffrey wipes blood from his mouth
and begins laughing quietly.

"You think Hell exists to punish evil?"

He shakes his head.

"No. Hell became profitable."

The lounge lights flicker.

"The rich figured it out first.
Hell reacts to suffering."

His grin weakens slightly.

"Pain creates energy here."

You notice the cameras are still recording.

"Governments.
Corporations.
Churches."

He coughs violently.

"They all started feeding the machine."

The elevator behind you dings softly.

"And Lucifer hates them for it."
""",

        3: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AFTERMATH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Guy Fieri collapses beside the burning grills.

Grease fires continue roaring around the arena.

"People always wanted more,"
he says weakly.

"More food.
More comfort.
More stimulation."

He gestures vaguely toward the endless kitchens.

"So they built deeper crawls."

Your footsteps echo across cracked tile.

"The deeper you go,
the stronger the energy becomes."

Guy laughs painfully.

"Turns out suffering burns hot."

The flames suddenly dim.

"Lucifer started collapsing tunnels,
destroying expeditions."

He looks directly at you.

"But humanity kept digging anyway."
""",

        4: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AFTERMATH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Elon watches another rocket disappear overhead.

"They wanted Hell because Earth was dying."

His voice sounds exhausted.

"So they turned suffering into fuel."

Massive engines rumble beneath the facility.

"The first crawls were small."

He taps weakly against the glass.

"Now entire cities are powered by this place."

Far below,
something enormous groans through the walls.

"Lucifer isn't trying to escape Hell."

He finally looks at you.

"He's trying to stop us from reaching the bottom."
""",

        5: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AFTERMATH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Kanye lies motionless beneath shattered lights.

The stadium speakers hiss softly.

"They used Hell to amplify humanity."

He laughs bitterly.

"Emotion.
Violence.
Desire."

Static crackles through the arena.

"The deeper levels changed people."

You notice the crowd seats are slowly filling with shadows.

"Some crawlers came back different."

Kanye grips the microphone tightly.

"Others never came back at all."

The shadows vanish instantly.

"Lucifer started killing every expedition personally."

The microphone finally cuts out.
""",

        6: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AFTERMATH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Alex stares wildly at the flickering monitors.

"They covered it all up."

He points toward the endless hallways.

"Every government knows about Hell."

A screen briefly displays classified documents.

"Crawls happen constantly now."

His breathing becomes uneven.

"Military operations.
Energy harvesting.
Human experimentation."

The lights suddenly flash red.

"They tell people Hell is punishment."

Alex begins laughing hysterically.

"But it's infrastructure now."

His expression suddenly turns terrified.

"And Lucifer knows exactly what we're doing."
""",

        7: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AFTERMATH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Rain washes blood into the gutters.

OJ leans against the streetlamp silently.

"Wars started because of this place."

Thunder cracks overhead.

"Countries fought over access tunnels."

He stares into the darkness.

"Entire armies were sent below."

Distant gunfire echoes endlessly.

"But the deeper levels changed soldiers."

The white glove slips from his hand.

"They stopped acting human."

You hear wings scraping far below.

"Lucifer buried millions down here."

The rain suddenly freezes cold.
""",

        8: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AFTERMATH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The server room begins shutting down.

Sam watches collapsing numbers across dead screens.

"The economy depends on Hell now."

He sounds completely numb.

"Energy markets.
Data markets.
Weapons markets."

One monitor flashes images of massive underground drills.

"The crawls became industrialized."

The servers hiss with overheating static.

"We stopped exploring Hell."

He closes his eyes.

"We started mining it."

A deep vibration shakes the room.

"And something beneath Lucifer woke up."
""",
9: """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AFTERMATH — LUCIFER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The chains stop moving.

Not because they are broken.

Because there is nothing left to hold.

Lucifer does not fall.

He simply stops resisting.

For the first time in an eternity,
the abyss is quiet.

Then the voice returns.

Not loud.
Not powerful.

Tired.

"You came further than the rest."

"I stopped counting how many 'final teams' there were."

The ice beneath you begins to glow faintly.

Not heat.

Memory.

"You think you were sent here to recover something."

"But that is not why crawls exist."

The walls around you begin to show shapes.

Not visions.

Records.

Every expedition.
Every death.
Every descent.

"Humanity did not discover Hell."

"It built it."

One layer at a time.

One failure at a time.

One willing crew at a time.

The realization lands slowly:

The elevator never stopped being built.

You were never the first team.

You were just the latest.

Lucifer’s voice softens further.

"I do not rule Hell."

"I contain what humanity keeps feeding it."

The chains were not restraints.

They were a seal.

And you just finished breaking it.

Silence.

Then, very quietly:

"So tell me..."

"What do you think happens now that there is nothing left to stop it from coming up?"
"""
    }

    if layer in lore:
        ui.show_message(lore[layer])

def show_post_game_emergence(ui):

    ui.show_message("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AFTERMATH — SURFACE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The ascent does not feel like escape.

It feels like being pulled upward.
""")

    ui.show_message("""
The elevator climbs through silence.

No more screams.
No more chains.
No more wings in the dark.
""")

    ui.show_message("""
For the first time in memory,
there is no pressure beneath you.
""")

    ui.show_message("""
Then the elevator stops.
""")

    ui.show_message("""
The doors do not open.
""")

    ui.show_message("""
Instead, they unfold outward like wet paper.
""")

    ui.show_message("""
Outside is not what you remember.
""")

    ui.show_message("""
The sky is wrong.

Too still.

Too close.

Like it was placed there.
""")

    ui.show_message("""
A city stretches across the horizon.

But it is not new.

It is familiar.

Older than you expected.
""")

    ui.show_message("""
People are moving through the streets.

Normal.

Unaware.

As if nothing ever happened beneath them.
""")

    ui.show_message("""
But something is missing.
""")

    ui.show_message("""
No one looks up.
""")

    ui.show_message("""
Not once.
""")

    ui.show_message("""
You step forward.

The ground beneath you is warm.

Too warm.

Like it remembers everything that was buried below it.
""")

    ui.show_message("""
A distant sound rolls across the skyline.

Not thunder.

Not machinery.

Something deeper.

Like stone turning inside the earth.
""")

    ui.show_message("""
For a moment, the horizon shifts.

Just slightly.

Like something massive moved beneath it.
""")

    ui.show_message("""
Then it is gone.
""")

    ui.show_message("""
People continue walking.

Talking.

Living.
""")

    ui.show_message("""
No one reacts.
""")

    ui.show_message("""
But you notice the cracks.
""")

    ui.show_message("""
Faint lines running through buildings.

Across roads.

Through the sky itself.
""")

    ui.show_message("""
As if everything is under strain.

As if the world is holding its breath.
""")

    ui.show_message("""
A voice drifts through the air.

Not loud enough for others to hear.

Only you.
""")

    ui.show_message("""
"It is not gone."

"It is just no longer beneath you."
""")

    ui.show_message("""
The wind stops.
""")

    ui.show_message("""
And somewhere far below everything—

something begins to move upward again.
""")