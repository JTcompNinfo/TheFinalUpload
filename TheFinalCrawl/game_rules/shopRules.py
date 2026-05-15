import random
from game_rules.itemRules import ITEM_DICT, ALL_POOLS, Weapon, Armor, HealingItem, TooImportant
from game_rules.gameUI import AdventureUI


# ── Shop name per layer ───────────────────────────────────────────────────────
SHOP_NAMES = {
    1: "Gary's Lost & Found",
    2: "Spencer's",
    3: "City Chinese Pop-Up Shop & Buffet",
    4: "The Gilded Tongue",
    5: "Ashfall Armory",
    6: "The Velvet Vice",
    7: "Bloodprice Bazaar",
    8: "The Fraudster's Market",
    9: "The Frozen Ledger",
}


# ── Format item with stats ────────────────────────────────────────────────────
def item_line(item):
    if isinstance(item, Weapon):
        return f"{item.name} [+{item.attack_bonus} ATK] ({item.price}g)"
    elif isinstance(item, Armor):
        return f"{item.name} [+{item.defense_bonus} DEF] ({item.price}g)"
    elif isinstance(item, HealingItem):
        return f"{item.name} [+{item.heal_amount} HP] ({item.price}g)"
    else:
        return f"{item.name} ({item.price}g)"


# ── Generate shop inventory ──────────────────────────────────────────────────
def generate_shop(layer):
    pool_names = ALL_POOLS.get(layer, ALL_POOLS[1])
    items = [ITEM_DICT[name] for name in pool_names]
    return random.sample(items, len(items))


# ── SELL SUB-MENU ─────────────────────────────────────────────────────────────
def sell_menu(ui: AdventureUI, player):
    """
    Lets the player sell items with page support.
    Prevents inventory overflow from breaking the UI.
    """

    PAGE_SIZE = 6

    while True:

        if not player.inventory:
            ui.show_message("Your inventory is empty. Nothing to sell.")
            return

        page = 0

        while True:

            start = page * PAGE_SIZE
            end = start + PAGE_SIZE

            current_items = player.inventory[start:end]

            lines = [
                "━━ SELL ITEMS ━━",
                f"Gold: {player.gold}",
                "",
                f"Showing items {start + 1}-{min(end, len(player.inventory))}"
                f" of {len(player.inventory)}",
                ""
            ]

            for i, item in enumerate(current_items, 1):

                if isinstance(item, TooImportant):
                    sell_price = "UNSELLABLE"
                else:
                    sell_price = f"{item.price // 2}g"

                lines.append(
                    f"{i}. {item_line(item)} → {sell_price}"
                )

            dialogue = "\n".join(lines)

            choices = []

            for item in current_items:

                if isinstance(item, TooImportant):
                    choices.append(f"{item.name} [CANNOT SELL]")
                else:
                    choices.append(
                        f"Sell {item.name} ({item.price // 2}g)"
                    )

            # Navigation
            if start > 0:
                choices.append("Previous Page")

            if end < len(player.inventory):
                choices.append("Next Page")

            choices.append("Back to shop")

            choice = ui.show(dialogue, choices)

            # =========================
            # BACK
            # =========================
            if choices[choice - 1] == "Back to shop":
                return

            # =========================
            # PAGE CONTROLS
            # =========================
            if choices[choice - 1] == "Next Page":
                page += 1
                continue

            if choices[choice - 1] == "Previous Page":
                page -= 1
                continue

            # =========================
            # SELL ITEM
            # =========================
            item_index = choice - 1

            if item_index < len(current_items):

                item = current_items[item_index]

                if isinstance(item, TooImportant):

                    ui.show_message(
                        f"{item.name} cannot be sold."
                    )

                    continue

                earned = item.price // 2

                player.gold += earned
                player.inventory.remove(item)

                # Unequip automatically if equipped
                if item == player.equipped_weapon:
                    player.equipped_weapon = None

                if item == player.equipped_armor:
                    player.equipped_armor = None

                ui.show_message(
                    f"You sold {item.name} for {earned} gold.\n\n"
                    f"Gold: {player.gold}"
                )

                # If inventory shrinks enough,
                # prevent empty pages
                max_page = max(
                    0,
                    (len(player.inventory) - 1) // PAGE_SIZE
                )

                if page > max_page:
                    page = max_page

                break

# ── MAIN SHOP FUNCTION ────────────────────────────────────────────────────────
def shop(ui: AdventureUI, player):

    shop_name = SHOP_NAMES.get(player.layer, "The Shop")
    shop_items = generate_shop(player.layer)

    while True:

        # =========================
        # BUILD DISPLAY TEXT
        # =========================

        lines = []

        # Header
        lines.append(f"{shop_name}")
        lines.append("")
        lines.append(f"Gold: {player.gold}")
        lines.append("")

        # Shop items — only show 7 with stats
        lines.append("── FOR SALE ──")
        for i, item in enumerate(shop_items[:7], 1):
            lines.append(f"{i}. {item_line(item)}")

        dialogue = "\n".join(lines)

        # =========================
        # BUILD CHOICES
        # =========================

        choices = []

        # Buy options (7, keeping 2 slots for Sell and Leave)
        for item in shop_items[:7]:
            choices.append(f"Buy {item.name} ({item.price}g)")

        # Sell menu entry and exit
        choices.append("Sell items")
        choices.append("Leave shop")

        sell_idx  = len(choices) - 2
        leave_idx = len(choices) - 1

        # =========================
        # SHOW UI
        # =========================

        choice = ui.show(dialogue, choices) - 1

        # =========================
        # LEAVE SHOP
        # =========================

        if choice == leave_idx:
            break

        # =========================
        # OPEN SELL MENU
        # =========================

        if choice == sell_idx:
            sell_menu(ui, player)
            continue

        # =========================
        # BUY LOGIC
        # =========================

        if 0 <= choice < len(shop_items[:7]):
            item = shop_items[choice]

            if player.gold >= item.price:
                player.gold -= item.price
                msg = player.add_to_inventory(item)

                text = (
                    f"You bought {item.name} for {item.price} gold.\n"
                    f"Remaining gold: {player.gold}"
                )

                if msg:
                    text += f"\n\n{msg}"

                ui.show_message(text)

            else:
                ui.show_message(
                    f"Not enough gold.\nNeed {item.price}g but have {player.gold}g."
                )

            continue