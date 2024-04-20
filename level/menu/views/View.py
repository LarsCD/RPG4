# from assets.classes.Item import Item
from utilities.GUT_2 import GUT, Color


class View:
    def __init__(self, object_class):
        self.Gut = GUT()
        self.Clr = Color()
        self.object_class = object_class
        self.display_manager()

    def display_manager(self):
        if self.object_class.id == 1:
            self.item_display()

    @staticmethod
    def format_description(description):
        formatted_description = "{:<40}".format(description[:40])
        return formatted_description

    def item_display(self):
        item = self.object_class
        self.Gut.clear_screen()
        self.Gut.draw_line(char='█')
        # colors
        r = self.Clr.hex('#ff0000')
        b = self.Clr.hex('#00aaff')
        y = self.Clr.hex('#ffd900')
        g = self.Clr.hex('#03fc13')
        it = self.Clr.italicize()
        rst = self.Clr.rst()
        string = f"""    
        [  {self.Clr.hex(item.tier_hex_color)}{item.name}{rst} [{self.Clr.italicize()}{item.tier_name}{rst}]  ]
        {self.Clr.italicize()}{str(item.type).capitalize()}{rst}
        
        Description: 
        {it}"{item.description}"{rst}
"""
        string2 = f"""
        Amount: x{item.quantity}
        Value: {y}{item.value}{rst} gold"""
        print(string)
        for specific in item.specifics:
            print(f"        {g}{item.specifics[specific]}{rst} {str(specific).replace('_', ' ').title()}")

        print(string2)
        click = input()
