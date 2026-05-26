import random

def roll(base, variance=0.10): 
    return int(base * random.uniform(1 - variance, 1 + variance))

def layer_multiplier(layer: int) -> float:
    return 1.3 ** (layer - 1)

def layer_scale(layer): 
    return 1.0 * (1.45 ** (layer - 1))


def stat(base: int, layer: int, variance: float = 0.12) -> int:
    """
    Universal stat scaler for ALL enemies.
    """
    scaled = base * layer_multiplier(layer)
    roll = random.uniform(1 - variance, 1 + variance)
    return max(1, int(scaled * roll))


def boss_stat(base: int, layer: int) -> int:
    """
    Bosses scale harder than normal enemies.
    """
    return max(1, int(base * (1.9 ** (layer - 1))))

class Enemy:
    def __init__(self, name, max_health, attack_power, defense):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.attack_power = attack_power
        self.defense = defense

    def is_alive(self):
        return self.current_health > 0

    def attack(self, target):
        damage = max(
            1,
            int(self.attack_power * (100 / (100 + target.get_defense() * 2.2)))
        )
        target.take_damage(damage)

    def get_defense(self):
        return self.defense

    def take_damage(self, damage):
        self.current_health = max(0, self.current_health - damage)

    def __str__(self):
        return f"{self.name} HP: {self.current_health}/{self.max_health}"    

class Boss:
    def __init__(self, name, max_health, attack_power, defense, phases=None):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.attack_power = attack_power
        self.defense = defense

        # optional multi-phase system
        self.phases = phases or {}

    def is_alive(self):
        return self.current_health > 0

    def get_phase(self):
        ratio = self.current_health / self.max_health

        if ratio > 0.66:
            return 1
        elif ratio > 0.33:
            return 2
        else:
            return 3

    def attack(self, target):

        phase = self.get_phase()
        phase_data = self.phases.get(phase, {})

        atk = phase_data.get("atk", self.attack_power)

        damage = max(
            2,
            int(
                atk *
                (100 / (100 + target.get_defense() * 3))
            )
        )

        target.take_damage(damage)

        # Optional DOT damage
        if "dot" in phase_data:
            target.take_damage(phase_data["dot"])

    def get_defense(self):
        return self.defense

    def take_damage(self, damage):
        self.current_health = max(0, self.current_health - damage)

    def __str__(self):
        return f"{self.name} HP: {self.current_health}/{self.max_health}"


class Player:
    def __init__(self, name, max_health):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.inventory = []
        self.equipped_weapon = None
        self.equipped_armor = None
        self.gold = 100
        self.layer = 1
        self.completed_layers = []
        self.rests_remaining = 3
        self.base_defense = 2
        self.base_attack = 8
        self.shop_number = 0
        self.encountNumbr = 0


    def level_up(self, new_health):
        self.max_health = new_health
        self.current_health = self.max_health

    def is_alive(self):
        return self.current_health > 0

    def get_attack_power(self):
        
        if self.equipped_weapon:
            return self.base_attack + self.equipped_weapon.attack_bonus
        return self.base_attack

    def get_defense(self):
        if self.equipped_armor:
            return self.base_defense + self.equipped_armor.defense_bonus
        return self.base_defense

    def attack(self, target):
        damage = max(
            1,
            int(
                self.get_attack_power() *
                (100 / (100 + target.get_defense() * 3))
            )
        )

        target.take_damage(damage)

    def take_damage(self, damage):
        self.current_health -= damage
        self.current_health = max(0, self.current_health)

    def heal(self, healing_item):
        if healing_item in self.inventory:
            self.current_health += healing_item.heal_amount
            self.current_health = min(self.max_health, self.current_health)
            self.inventory.remove(healing_item)

    def equip_weapon(self, weapon):
        self.equipped_weapon = weapon

    def equip_armor(self, armor):
        self.equipped_armor = armor

    def add_to_inventory(self, item):
        """
        Add item to inventory. Auto-equip if it's better than current gear.
        Returns an auto-equip message string, or None if no auto-equip happened.
        """
        self.inventory.append(item)
        auto_msg = None

        if hasattr(item, "attack_bonus"):
            current_bonus = self.equipped_weapon.attack_bonus if self.equipped_weapon else -1
            if item.attack_bonus > current_bonus:
                self.equipped_weapon = item
                auto_msg = f"Auto-equipped {item.name} (+{item.attack_bonus} ATK) — stronger than your old weapon!"

        elif hasattr(item, "defense_bonus"):
            current_bonus = self.equipped_armor.defense_bonus if self.equipped_armor else -1
            if item.defense_bonus > current_bonus:
                self.equipped_armor = item
                auto_msg = f"Auto-equipped {item.name} (+{item.defense_bonus} DEF) — stronger than your old armor!"

        return auto_msg

    def __str__(self):
        return (f"{self.name} HP: {self.current_health}/{self.max_health}\n"
                f"Weapon: {self.equipped_weapon.name if self.equipped_weapon else 'None'}\n"
                f"Armor: {self.equipped_armor.name if self.equipped_armor else 'None'}")

Rat_boy = Enemy(name="The Rat God", max_health=200, attack_power=5, defense=0)

def create_enemy(name, layer, base_hp, base_atk, base_def):
    scale = layer_scale(layer)

    hp = roll(base_hp * scale, 0.10)
    atk = roll(base_atk * scale, 0.08)
    defense = random.randint(base_def, base_def + max(1, layer // 3))

    return Enemy(name, hp, atk, defense)
# Layer 1
def make_l1_1(): return Enemy("Disconnected Dropout", stat(18,1), stat(3,1), stat(1,1))
def make_l1_2(): return Enemy("Isolated Room Dweller", stat(20,1), stat(3,1), stat(1,1))
def make_l1_3(): return Enemy("Forgotten Account Holder", stat(22,1), stat(3,1), stat(1,1))
def make_l1_4(): return Enemy("Passive Observer", stat(19,1), stat(3,1), stat(1,1))
def make_l1_5(): return Enemy("Directionless Browser", stat(21,1), stat(3,1), stat(1,1))

# Layer 2
def make_l2_1(): return Enemy("Dating App Addict", stat(35,2), stat(6,2), stat(2,2))
def make_l2_2(): return Enemy("Club Scene Flirt", stat(38,2), stat(6,2), stat(2,2))
def make_l2_3(): return Enemy("Attention Starved Influencer", stat(40,2), stat(7,2), stat(2,2))
def make_l2_4(): return Enemy("Validation Seeker", stat(36,2), stat(6,2), stat(2,2))
def make_l2_5(): return Enemy("Obsessive Ex Partner", stat(42,2), stat(7,2), stat(2,2))

# Layer 3
def make_l3_1(): return Enemy("Compulsive Eater", stat(55,3), stat(8,3), stat(3,3))
def make_l3_2(): return Enemy("Binge Streamer", stat(58,3), stat(8,3), stat(3,3))
def make_l3_3(): return Enemy("Energy Dependency User", stat(60,3), stat(9,3), stat(3,3))
def make_l3_4(): return Enemy("Loot Hoarder Player", stat(62,3), stat(9,3), stat(3,3))
def make_l3_5(): return Enemy("Overindulgent Consumer", stat(65,3), stat(10,3), stat(4,3))

# Layer 4
def make_l4_1(): return Enemy("Asset Hoarder", stat(85,4), stat(11,4), stat(5,4))
def make_l4_2(): return Enemy("Status Climber", stat(88,4), stat(12,4), stat(5,4))
def make_l4_3(): return Enemy("Financial Control Addict", stat(92,4), stat(12,4), stat(5,4))
def make_l4_4(): return Enemy("Debt Avoidant Worker", stat(90,4), stat(11,4), stat(5,4))
def make_l4_5(): return Enemy("Luxury Obsessive", stat(95,4), stat(13,4), stat(6,4))

# Layer 5
def make_l5_1(): return Enemy("Terminal Arguer", stat(125,5), stat(15,5), stat(7,5))
def make_l5_2(): return Enemy("Volatile Driver", stat(130,5), stat(16,5), stat(7,5))
def make_l5_3(): return Enemy("Flame Instigator", stat(135,5), stat(17,5), stat(8,5))
def make_l5_4(): return Enemy("Explosive Worker", stat(132,5), stat(16,5), stat(8,5))
def make_l5_5(): return Enemy("Resentment Carrier", stat(140,5), stat(18,5), stat(8,5))

# Layer 6
def make_l6_1(): return Enemy("Reality Denier", stat(175,6), stat(20,6), stat(10,6))
def make_l6_2(): return Enemy("Conspiracy Devotee", stat(180,6), stat(21,6), stat(10,6))
def make_l6_3(): return Enemy("Propaganda Distributor", stat(185,6), stat(22,6), stat(11,6))
def make_l6_4(): return Enemy("Dogmatic Contrarian", stat(182,6), stat(21,6), stat(10,6))
def make_l6_5(): return Enemy("Ideological Extremist", stat(190,6), stat(23,6), stat(11,6))

# Layer 7
def make_l7_1(): return Enemy("Private Enforcer", stat(240,7), stat(26,7), stat(13,7))
def make_l7_2(): return Enemy("Contracted Operative", stat(245,7), stat(27,7), stat(13,7))
def make_l7_3(): return Enemy("Exhausted Laborer", stat(250,7), stat(28,7), stat(14,7))
def make_l7_4(): return Enemy("Resource Extractor", stat(255,7), stat(28,7), stat(14,7))
def make_l7_5(): return Enemy("Street Predator", stat(265,7), stat(29,7), stat(15,7))

# Layer 8
def make_l8_1(): return Enemy("Information Fabricator", stat(320,8), stat(32,8), stat(17,8))
def make_l8_2(): return Enemy("Data Exploiter", stat(330,8), stat(33,8), stat(17,8))
def make_l8_3(): return Enemy("Identity Forger", stat(340,8), stat(34,8), stat(18,8))
def make_l8_4(): return Enemy("Influence Manipulator", stat(345,8), stat(35,8), stat(18,8))
def make_l8_5(): return Enemy("System Corruptor", stat(355,8), stat(36,8), stat(19,8))

# Layer 9
def make_l9_1(): return Enemy("Family Betrayer",       420, stat(28,9), stat(14,9))
def make_l9_2(): return Enemy("Trusted Ally Traitor",  440, stat(29,9), stat(14,9))
def make_l9_3(): return Enemy("Institution Insider",   460, stat(30,9), stat(15,9))
def make_l9_4(): return Enemy("False Protector",       480, stat(31,9), stat(15,9))
def make_l9_5(): return Enemy("System Core Betrayer",  510, stat(33,9), stat(16,9))

ENEMY_POOLS = {
    1: [make_l1_1, make_l1_2, make_l1_3, make_l1_4, make_l1_5],
    2: [make_l2_1, make_l2_2, make_l2_3, make_l2_4, make_l2_5],
    3: [make_l3_1, make_l3_2, make_l3_3, make_l3_4, make_l3_5],
    4: [make_l4_1, make_l4_2, make_l4_3, make_l4_4, make_l4_5],
    5: [make_l5_1, make_l5_2, make_l5_3, make_l5_4, make_l5_5],
    6: [make_l6_1, make_l6_2, make_l6_3, make_l6_4, make_l6_5],
    7: [make_l7_1, make_l7_2, make_l7_3, make_l7_4, make_l7_5],
    8: [make_l8_1, make_l8_2, make_l8_3, make_l8_4, make_l8_5],
    9: [make_l9_1, make_l9_2, make_l9_3, make_l9_4, make_l9_5],
}

# Bosses
def make_neil(): return Boss("Neil deGrasse Tyson",
    boss_stat(180,1), boss_stat(4,1), boss_stat(6,1),
    phases={1: {"atk": 5}, 2: {"atk": 7}, 3: {"atk": 9}}
)

def make_jeffrey(): return Boss("Jeffrey Epstein",
    boss_stat(115,2), boss_stat(10,2), boss_stat(4,2),
    phases={1: {"atk": 12}, 2: {"atk": 16}, 3: {"atk": 20}}
)

def make_guy(): return Boss("Guy Fieri",
    boss_stat(88,3), boss_stat(8,3), boss_stat(3,3),
    phases={1: {"atk": 18}, 2: {"atk": 24}, 3: {"atk": 30}}
)

def make_elon(): return Boss("Elon Musk",
    boss_stat(67,4), boss_stat(6,4), boss_stat(3,4),
    phases={1: {"atk": 26}, 2: {"atk": 34}, 3: {"atk": 44}}
)

def make_kanye(): return Boss("Kanye West",
    boss_stat(50,5), boss_stat(4,5), boss_stat(2,5),
    phases={1: {"atk": 38}, 2: {"atk": 50}, 3: {"atk": 64}}
)

def make_alex(): return Boss("Alex Jones",
    boss_stat(37,6), boss_stat(3,6), boss_stat(2,6),
    phases={1: {"atk": 55}, 2: {"atk": 72}, 3: {"atk": 90}}
)

def make_oj(): return Boss("OJ Simpson",
    boss_stat(27,7), boss_stat(2,7), boss_stat(1,7),
    phases={1: {"atk": 75}, 2: {"atk": 95}, 3: {"atk": 118}}
)

def make_sam(): return Boss("Sam Bankman-Fried",
    boss_stat(19,8), boss_stat(2,8), boss_stat(1,8),
    phases={1: {"atk": 95}, 2: {"atk": 125}, 3: {"atk": 155, "dot": 15}}
)

def make_lucifer(): return Boss("Lucifer",
    max_health=2800,
    attack_power=55,
    defense=18,
    phases={
        1: {"atk": 55},
        2: {"atk": 85,  "dot": 10},
        3: {"atk": 120, "dot": 20}
    }
)

BOSSES = {
    1: make_neil,
    2: make_jeffrey,
    3: make_guy,
    4: make_elon,
    5: make_kanye,
    6: make_alex,
    7: make_oj,
    8: make_sam,
    9: make_lucifer,
}

#Secret bosses

Luke = Boss(
    "Luke the Breaking Point",
    boss_stat(100,5),
    boss_stat(7,5),
    boss_stat(4,5),
    phases={
        1: {"atk": 91},
        2: {"atk": 110},
        3: {"atk": 135, "dot": 8}
    }
)

Guyde = Boss(
    "Guyde, The Destroyer of Worlds",

    max_health=12000,
    attack_power=450,
    defense=500,

    phases={

        # Phase 1
        1: {
            "atk": 450,
            "dot": 25
        },

        # Phase 2
        2: {
            "atk": 700,
            "dot": 50
        },

        # Phase 3
        3: {
            "atk": 1200,
            "dot": 100
        }
    }
)