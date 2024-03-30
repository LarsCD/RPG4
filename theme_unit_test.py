from utilities.GUT_2 import GutColor, GUT

if __name__ == "__main__":
    Gut = GUT()
    GutColor = GutColor()

    print(f"{GutColor.hex_to_ansi('#fc9803')}WOOOOOW{GutColor.rst()}")
    print(f"{GutColor.hex_to_ansi('#03d7fc')}WOOOOOW{GutColor.rst()}")
    print(f"{GutColor.hex_to_ansi('#002a6e')}WOOOOOW{GutColor.rst()}")
    print(f"{GutColor.hex_to_ansi('#94007b')}WOOOOOW{GutColor.rst()}")
    print(f"{GutColor.hex_to_ansi('#5eff5e')}WOOOOOW{GutColor.rst()}")
    print(f"{GutColor.hex_to_ansi('#9c5eff')}WOOOOOW{GutColor.rst()}")
    print("\n")

    rst = GutColor.rst()
    bold = GutColor.bold()
    ital = GutColor.italicize()

    string = f"""
{GutColor.hex_to_ansi('#fc9803')}WARTHOG{rst} | Level {GutColor.hex_to_ansi('#878787')}7{rst}
{GutColor.hex_to_ansi("#ff0000", bold=True)}HP  {rst}: ({GutColor.hex_to_ansi("#ffffff", bold=True)}17{rst}/24) [{GutColor.hex_to_ansi("#ff0000", bold=True)}//////////////{rst}....]
{GutColor.hex_to_ansi("#3d8bff", bold=True)}MANA{rst}: ({GutColor.hex_to_ansi("#ffffff", bold=True)}15{rst}/30) [{GutColor.hex_to_ansi("#3d8bff", bold=True)}/////////{rst}.........]

"""

    options = {'1': 'Option 1', '2': 'Option 2', '3': 'Option 3'}

    Gut.menu_select(f"{GutColor.hex_to_ansi('#ff0000', bold=True)}BATTLE{rst}", options=options, text=string)

    click = input()
