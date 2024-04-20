from utilities.GUT_2 import Color, GUT
from assets.classes.Item import Tier

if __name__ == "__main__":
    Gut = GUT()
    Color = Color()
    Tier = Tier()

    print(f"{Color.hex('#fc9803', bold=True)}WOOOOOW{Color.rst()}")
    print(f"{Color.hex('#03d7fc')}WOOOOOW{Color.rst()}")
    print(f"{Color.hex('#002a6e')}WOOOOOW{Color.rst()}")
    print(f"{Color.hex('#94007b')}WOOOOOW{Color.rst()}")
    print(f"{Color.hex('#5eff5e', italicize=True)}WOOOOOW{Color.rst()}")
    print(f"{Color.hex('#9c5eff', bold=True, italicize=True)}WOOOOOW{Color.rst()}")
    print("\n")

    rst = Color.rst()
    bold = Color.bold()
    ital = Color.italicize()

    string = f"""
{Color.hex('#fc9803')}WARTHOG{rst} | Level {Color.hex('#ffffff', bold=True)}7{rst}
{Color.hex("#ff0000", bold=True)}HP  {rst}: ({Color.hex("#ffffff", bold=True)}17{rst}/24) [{Color.hex("#ff0000", bold=True)}//////////////{rst}....]
{Color.hex("#3d8bff", bold=True)}MANA{rst}: ({Color.hex("#ffffff", bold=True)}15{rst}/30) [{Color.hex("#3d8bff", bold=True)}/////////{rst}.........]

"""

    options = {'1': 'Option 1', '2': 'Option 2', '3': 'Option 3'}

    item_names = ['Apple', 'Chicken', 'Knight Sword', 'Kalapos\' Axe', 'Metasteel Dwarven Shield',
                  'Golden Wizard\'s Wand']

    for i, name in enumerate(item_names):
        tier_color = Tier.get_tier_hex_color(i + 1)
        print(f'{Color.hex(tier_color, bold=True)}{name}{rst} ({Color.italicize()}{Tier.get_tier_name(i + 1)}{rst})')

    Gut.menu_select(title=f"{Color.hex('#ff0000', bold=True)}BATTLE{rst}", menu_options=options, text=string)

    click = input()
