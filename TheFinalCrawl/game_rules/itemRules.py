# =====================================================
# Weapon Class
# Represents a weapon the player can equip
# =====================================================
class Weapon:
    def __init__(self, name, attack_bonus, price):
        self.name = name
        self.attack_bonus = attack_bonus
        self.price = price

    def __str__(self):
        return f"{self.name} (+{self.attack_bonus} ATK) - {self.price} gold"


# =====================================================
# Armor Class
# =====================================================
class Armor:
    def __init__(self, name, defense_bonus, price):
        self.name = name
        self.defense_bonus = defense_bonus
        self.price = price

    def __str__(self):
        return f"{self.name} (+{self.defense_bonus} DEF) - {self.price} gold"


# =====================================================
# Healing Item
# =====================================================
class HealingItem:
    def __init__(self, name, heal_amount, price):
        self.name = name
        self.heal_amount = heal_amount
        self.price = price

    def __str__(self):
        return f"{self.name} (Heals {self.heal_amount}) - {self.price} gold"


# =====================================================
# Too Important Item
# =====================================================
class TooImportant:
    def __init__(self, name):
        self.name = name
        self.price = 100000000000

    def __str__(self):
        return self.name


key = TooImportant("Horn fragment")


# =====================================================
# ALL ITEMS
# =====================================================
ALL_ITEMS = [
    Weapon("Cracked Screen Knife", 4, 10),
    Weapon("Bent School Ruler Blade", 6, 12),
    Weapon("Plastic Pen Stabber", 8, 15),

    Armor("Worn School Hoodie", 3, 10),
    Armor("Thin Apartment Blanket Coat", 5, 12),
    Armor("Faded Identity Jacket", 7, 15),

    HealingItem("Expired Antidepressants", 5, 8),
    HealingItem("Cold Water Bottle", 6, 10),
    HealingItem("Half Empty Painkillers", 8, 12),

    Weapon("Lipstick Stained Blade", 10, 40),
    Weapon("Heartbreaker Switchblade", 12, 50),
    Weapon("Rose-Tinted Glass Shard", 14, 60),

    Armor("Silk Attention Jacket", 7, 35),
    Armor("Velvet Nightclub Coat", 9, 45),
    Armor("Designer Validation Hoodie", 11, 55),

    HealingItem("Romance Energy Drink", 15, 10),
    HealingItem("Perfume Scent Energy Shot", 20, 15),
    HealingItem("Late Night Text Reply Pack", 30, 20),

    Weapon("Grease Bat of Excess", 16, 70),
    Weapon("Fast Food Tray Club", 18, 80),
    Weapon("Sugar Stained Pipe", 20, 90),

    Armor("Oversized Fast Fashion Coat", 11, 65),
    Armor("Stained Hoodie of Consumption", 13, 75),
    Armor("Loose Lounge Wear Set", 15, 85),

    HealingItem("Fast Food Combo Pack", 35, 20),
    HealingItem("Energy Drink Case", 45, 25),
    HealingItem("Frozen Microwave Meal", 55, 30),

    Weapon("Credit Sever Blade", 24, 110),
    Weapon("Debt Collector Baton", 27, 125),
    Weapon("Tax Form Cutter", 30, 140),

    Armor("Status Symbol Suit", 15, 100),
    Armor("Discount Business Jacket", 18, 115),
    Armor("Luxury Knockoff Coat", 21, 130),

    HealingItem("Illusion Wealth Coins", 60, 35),
    HealingItem("Refund Check Stub", 75, 40),
    HealingItem("Digital Wallet Fragment", 90, 50),

    Weapon("Broken Rage Bottle", 34, 170),
    Weapon("Rust Pipe Handle", 38, 190),
    Weapon("Fractured Traffic Sign Blade", 42, 210),

    Armor("Frayed Aggression Shirt", 21, 150),
    Armor("Sweat-Stained Tank Top", 24, 170),
    Armor("Ripped Work Uniform", 27, 190),

    HealingItem("Burnout Whiskey Flask", 95, 50),
    HealingItem("Cold Coffee Thermos", 115, 60),
    HealingItem("Stress Relief Pills", 135, 70),

    Weapon("Redacted Truth Folder", 48, 240),
    Weapon("Burnt Evidence File", 53, 260),
    Weapon("Corrupted Archive Drive", 58, 280),

    Armor("Sterile Doctrine Coat", 27, 220),
    Armor("Lab-Approved Uniform", 31, 240),
    Armor("Institutional Cover Suit", 35, 260),

    HealingItem("Unverified Cure Pack", 155, 80),
    HealingItem("Experimental Injection Kit", 185, 95),
    HealingItem("Restricted Medication Box", 215, 110),

    Weapon("Rust Execution Blade", 65, 320),
    Weapon("Combat Wire Garrote", 72, 350),
    Weapon("Industrial Cutter Tool", 80, 380),

    Armor("Bloodmarked Riot Armor", 35, 300),
    Armor("Bullet Scored Vest", 40, 330),
    Armor("Tactical Scrap Armor", 45, 360),

    HealingItem("Field Recovery Blood Kit", 245, 120),
    HealingItem("Emergency Trauma Pack", 285, 140),
    HealingItem("Stitched Medical Kit", 325, 160),

    Weapon("Encrypted Execution Device", 90, 420),
    Weapon("Data Spike Injector", 100, 460),
    Weapon("Signal Hijack Tool", 110, 500),

    Armor("Identity Null Mask", 45, 400),
    Armor("Blank Credential Suit", 51, 440),
    Armor("Adaptive Disguise Layer", 57, 480),

    HealingItem("Corrupted Data Core", 385, 170),
    HealingItem("Stolen Access Drive", 435, 190),
    HealingItem("Encrypted Recovery Patch", 485, 210),

    Weapon("Executive Betrayal Blade", 130, 650),
    Weapon("Oathbreaking Dagger", 145, 700),
    Weapon("System Override Spike", 160, 750),

    Armor("Authority Null Suit", 57, 600),
    Armor("Corporate Control Uniform", 64, 650),
    Armor("Final Trust Breakdown Armor", 72, 700),

    HealingItem("Sedation Override Kit", 605, 250),
    HealingItem("Emergency Memory Wipe", 705, 300),
    HealingItem("Pact Severance Injector", 805, 350),
]

ITEM_DICT = {item.name: item for item in ALL_ITEMS}


# =====================================================
# POOLS
# =====================================================
ALL_POOLS = {
    1: [
        "Cracked Screen Knife",
        "Bent School Ruler Blade",
        "Plastic Pen Stabber",
        "Worn School Hoodie",
        "Thin Apartment Blanket Coat",
        "Faded Identity Jacket",
        "Expired Antidepressants",
        "Cold Water Bottle",
        "Half Empty Painkillers"
    ],
    2: [
        "Lipstick Stained Blade",
        "Heartbreaker Switchblade",
        "Rose-Tinted Glass Shard",
        "Silk Attention Jacket",
        "Velvet Nightclub Coat",
        "Designer Validation Hoodie",
        "Romance Energy Drink",
        "Perfume Scent Energy Shot",
        "Late Night Text Reply Pack"
    ],
    3: [
        "Grease Bat of Excess",
        "Fast Food Tray Club",
        "Sugar Stained Pipe",
        "Oversized Fast Fashion Coat",
        "Stained Hoodie of Consumption",
        "Loose Lounge Wear Set",
        "Fast Food Combo Pack",
        "Energy Drink Case",
        "Frozen Microwave Meal"
    ],
    4: [
        "Credit Sever Blade",
        "Debt Collector Baton",
        "Tax Form Cutter",
        "Status Symbol Suit",
        "Discount Business Jacket",
        "Luxury Knockoff Coat",
        "Illusion Wealth Coins",
        "Refund Check Stub",
        "Digital Wallet Fragment"
    ],
    5: [
        "Broken Rage Bottle",
        "Rust Pipe Handle",
        "Fractured Traffic Sign Blade",
        "Frayed Aggression Shirt",
        "Sweat-Stained Tank Top",
        "Ripped Work Uniform",
        "Burnout Whiskey Flask",
        "Cold Coffee Thermos",
        "Stress Relief Pills"
    ],
    6: [
        "Redacted Truth Folder",
        "Burnt Evidence File",
        "Corrupted Archive Drive",
        "Sterile Doctrine Coat",
        "Lab-Approved Uniform",
        "Institutional Cover Suit",
        "Unverified Cure Pack",
        "Experimental Injection Kit",
        "Restricted Medication Box"
    ],
    7: [
        "Rust Execution Blade",
        "Combat Wire Garrote",
        "Industrial Cutter Tool",
        "Bloodmarked Riot Armor",
        "Bullet Scored Vest",
        "Tactical Scrap Armor",
        "Field Recovery Blood Kit",
        "Emergency Trauma Pack",
        "Stitched Medical Kit"
    ],
    8: [
        "Encrypted Execution Device",
        "Data Spike Injector",
        "Signal Hijack Tool",
        "Identity Null Mask",
        "Blank Credential Suit",
        "Adaptive Disguise Layer",
        "Corrupted Data Core",
        "Stolen Access Drive",
        "Encrypted Recovery Patch"
    ],
    9: [
        "Executive Betrayal Blade",
        "Oathbreaking Dagger",
        "System Override Spike",
        "Authority Null Suit",
        "Corporate Control Uniform",
        "Final Trust Breakdown Armor",
        "Sedation Override Kit",
        "Emergency Memory Wipe",
        "Pact Severance Injector"
    ]
}


BOSS_ITEMS = {
    "Neil deGrasse Tyson": [
        Weapon("Cosmic Debate Pointer", 9, 0),
        Armor("Planetarium Lecturer Coat", 8, 0),
    ],
    "Jeffrey Epstein": [
        Weapon("Private Jet Shard", 15, 0),
        Armor("Elite Island Suit", 12, 0),
    ],
    "Guy Fieri": [
        Weapon("Flavortown Grill Hammer", 22, 0),
        Armor("Mayor of Flavortown Jacket", 16, 0),
    ],
    "Elon Musk": [
        Weapon("Prototype Railblade", 32, 0),
        Armor("Billionaire Techwear", 23, 0),
    ],
    "Kanye West": [
        Weapon("Platinum Mic Stand", 44, 0),
        Armor("Runway Riot Armor", 29, 0),
    ],
    "Alex Jones": [
        Weapon("Infowar Broadcast Axe", 62, 0),
        Armor("Tinfoil Panic Vest", 38, 0),
    ],
    "OJ Simpson": [
        Weapon("White Bronco Cleaver", 85, 0),
        Armor("Trial Survivor Pads", 49, 0),
    ],
    "Sam Bankman-Fried": [
        Weapon("Crypto Collapse Blade", 120, 0),
        Armor("Bankruptcy Executive Suit", 60, 0),
    ],
    "Lucifer": [
        Weapon("Thronebreaker", 1000000, 0),
        Armor("Crown of the Fallen King", 1000000, 0),
    ],
    "Luke the Breaking Point": [
        Weapon("Luke's bane", 43, 0),
        Armor("Mindbreak Shell", 28, 0),
    ],
}