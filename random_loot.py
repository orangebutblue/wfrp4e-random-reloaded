import random as r

cols = ["Brass Pennies", "Silver Shillings", "Gold Crowns", "Domestic", "Gems", "Art", "Cloth", "Scrolls", "Grimoire", "Random"]
random_treasure = {
    "Hovel":
        [1, [50, 1, 10],
         [10, 1, 5],
         [1, 1, 1],
         [10, 1, 5],
         [0, 0, 0],
         [0, 0, 0],
         [10, 1, 1],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
    "House":
        [2, [100, 6, 60],
         [100, 2, 20],
         [25, 1, 10],
         [100, 1, 10],
         [5, 1, 5],
         [10, 1, 2],
         [25, 1, 5],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
    "Estate":
        [3, [100, 2, 200],
         [100, 1, 100],
         [100, 1, 100],
         [100, 2, 20],
         [90, 1, 10],
         [75, 1, 10],
         [100, 1, 10],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
    "Wizard Home":
        [3, [100, 3, 30],
         [75, 5, 50],
         [50, 3, 30],
         [25, 1, 5],
         [75, 1, 5],
         [75, 1, 2],
         [25, 1, 5],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
    "Shrine":
        [1, [100, 1, 10],
         [50, 1, 10],
         [5, 1, 5],
         [0, 0, 0],
         [25, 1, 1],
         [75, 1, 1],
         [5, 1, 1],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
    "Temple":
        [3,[100, 5, 500],
         [75, 1, 100],
         [50, 5, 50],
         [25, 1, 10],
         [75, 1, 5],
         [50, 1, 5],
         [100, 1, 10],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
    "Small Monster":
        [2,[50, 1, 10],
         [15, 2, 20],
         [15, 1, 5],
         [0, 0, 0],
         [15, 1, 1],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
    "Large Monster":
        [3,[75, 2, 200],
         [50, 1, 100],
         [25, 1, 100],
         [5, 1, 10],
         [75, 1, 10],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
    "Chest Open":
        [2,[25, 1, 100],
         [25, 1, 10],
         [5, 1, 10],
         [5, 1, 1],
         [5, 1, 1],
         [0, 0, 0],
         [5, 1, 1],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
    "Chest Secure":
        [3,[100, 5, 50],
         [100, 3, 30],
         [50, 2, 20],
         [10, 1, 1],
         [15, 1, 10],
         [5, 1, 1],
         [15, 1, 1],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
    "Chest Vault":
        [3,[100, 5, 500],
         [100, 4, 400],
         [100, 3, 300],
         [0, 0, 0],
         [100, 1, 100],
         [100, 1, 10],
         [25, 1, 1],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
    "Peasant":
        [1,[15, 1, 10],
         [5, 1, 2],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],
         [1, 1, 1],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
    "Citizen":
        [2,[75, 1, 10],
         [75, 1, 10],
         [5, 1, 5],
         [0, 0, 0],
         [1, 1, 1],
         [0, 0, 0],
         [5, 1, 1],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
    "Noble":
        [3,[100, 1, 100],
         [100, 2, 20],
         [100, 1, 10],
         [0, 0, 0],
         [50, 1, 2],
         [5, 1, 1],
         [100, 1, 5],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
    "Wizard":
        [3,[25, 2, 20],
         [50, 2, 20],
         [50, 1, 10],
         [0, 0, 0],
         [5, 1, 1],
         [0, 0, 0],
         [1, 1, 1],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
    "Test":
        [2,[25, 2, 20],
         [100, 2, 20],
         [100, 1, 10],
         [100, 2, 3],
         [100, 2, 3],
         [100, 2, 3],
         [100, 2, 3],
         [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
}
domestic_items = ["Candelabra & Candles", "Cups & Glasses", "Cutlery", "Goblets", "Lantern & Oil", "Pipe & Tobacco",
                  "Plates & Bowls", "Teaware", "Wine & Spirits", "Other Trapping"]
gems = ["Amber / Amethyst / Beryl", "Agate / Aquamarine / Diamond", "Hematite / Bloodstone / Emerald",
        "Lapis Lazuli / Citrine / Garnet", "Malachite / Jasper / Jade", "Rhodocrosite / Moonstone / Opal",
        "Obsidian / Onyx / Pearl", "Quartz / Peridot / Ruby", "Tiger Eye / Topaz / Sapphire",
        "Turquoise / Zircon / Spinel"]
jewellery = ["Amulet", "Armlet", "Bracelet", "Brooch", "Chain", "Choker", "Circlet", "Cuf Links", "Earrings", "Hairpin",
             "Hatpin", "Locket", "Medallion", "Necklace", "Pendant", "Pocket Watch", "Prayer Beads", "Ring, Decorative",
             "Ring, Promise", "Ring, Wedding", "Signet Ring", "Torc"]
jewellery_p = [5, 4, 5, 4, 4, 3, 4, 4, 9, 4, 4, 5, 5, 5, 4, 4, 4, 5, 4, 4, 5, 5]
art = ["Abacus", "Carved Dragon Egg", "Ceremonial Weapon", "Chalice", "Costume Mask", "Crown (false or real)",
       "Decorative Comb", "Doll", "Engraved Dice", "Figurine", "Flask", "Flute", "Framed Portrait",
       "Game Board & Pieces", "Harp (Toy)", "Idol", "Instrument", "Ivory Drinking Horn", "Jewellery Box",
       "Large Statue", "Letter Opener", "Mini Sarcophagus", "Music Box", "Orrery", "Painting", "Paperweight",
       "Pewter Mug", "Sceptre", "Small Mirror", "Statuette", "Vase", "War Mask", "Wood Carving", "Other Trapping"]
art_p = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1]
clothes = ["Animal Pelt", "Belt", "Blankets", "Boots & Shoes", "Cape", "Cloak", "Clothes, Fine", "Clothes, Practical",
           "Clothes, Travel", "Coat", "Costume", "Courtly Garb ", "Drapes, Fine ", "Embroidery ", "Fur Coat ",
           "Fur Stole", "Gloves, Fine", "Gloves, Practical", "Handkerchief, Silk", "Hat, Fancy", "Hat, Practical",
           "Linens, Fine", "Linens, Practical", "Pouch", "Purse", "Robes", "Rug, Fine", "Rug, Woven", "Shawl",
           "Tapestry", "Uniform", "Walking Cane", "Wall Hanging", "Other Trapping"]
clothes_p = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1]


def roll(num, sides, print_roll=True):
    roll_sum = 0
    for cur in range(0, num):
        diceroll = r.randint(1, sides)
        if print_roll:
            print(str(diceroll))
        roll_sum = roll_sum + diceroll
    return roll_sum


def roll_cat(args):
    # args: p, min, max
    if r.randint(1, 100) < args[0]:
        return r.randint(args[1], args[2])
    else:
        return 0


def get_loc_level(level):
    if level == 1:
        return "brass pennies"
    if level == 2:
        return "silver shillings"
    if level == 3:
        return "gold crowns"


def get_random_treasure_table(status):
    print("Looting: " + status)
    table = random_treasure.get(status)
    cc = 1  # current category (pennies, shillings, ...)
    level = table.pop(0)
    for e in table:
        vals = roll_cat(e)
        if vals != 0:
            print(cols[cc - 1] + ":")
            print(vals)
            match cc:
                case 4:  # domestic
                    for val in range(0, vals):
                        print(domestic_items[r.randint(0, 9)])
                case 5:  # gems
                    for val in range(0, vals):
                        if r.randint(1, 10) < 6:
                            # roll gem
                            spllitted_gems = gems[r.randint(0, 9)].split(" / ")
                            print(spllitted_gems[level - 1])
                        else:
                            # roll jewellery
                            print(r.choices(jewellery, jewellery_p)[0])
                        print("...worth " + str(roll(2, 10, False)) + " " + get_loc_level(level))
                case 6:  # art
                    for val in range(0, vals):
                        print(r.choices(art, art_p)[0])
                case 7:  # cloth
                    for val in range(0, vals):
                        print(r.choices(clothes, clothes_p)[0])
                case 8:  # scrolls
                    ...
                case 9:  # grimoire
                    ...
                case 0:  # random
                    ...

        cc = cc + 1


"""
    Places:
    * Hovel,House,Estate,Wizard Home
    * Workshop,Shrine,Temple
    
    Monsters:
    * Small Monster,Large Monster
    
    Chests:
    * Chest Open, Chest Secure, Chest Vault
    
    NPC:
    * Peasant, Citizen, Noble, Wizard
"""

get_random_treasure_table("House")
