# Overview - Write "compilable" code. As if it were on production.


# You have been tasked with parsing menus from a large restaurant group. Each menu is streamed to clients via a provided interface. You must design object(s) that represents a menu and can be hydrated with data from the provided interface. Your design should contain an appropriate class structure to contain the parsed data, as well as a function or set of functions to perform the parsing.

# Consumers will use your object(s) to access a complete representation of the data sent by the menu stream after it has finished loading. Your objects should provide easy access to the full representation of the menu. It should be possible to reconstruct the menu stream from your object.

# The menu stream represents a list of menu items. Each item in the stream is a menu item, and each item will be separated by an empty string. The attributes of each item are as follows:

#   Line 0: The ID of the item
#   Line 1: The item type, either CATEGORY, ENTREE or OPTION
#   Line 2: The name of the item
#   Line 3: The price of the item for ENTREE and OPTION. Not present for CATEGORY items.

#   Any other line: A list of item IDs that are linked to the current item. OPTIONs do not have any linked items.

# Class to model a menu item.
class MenuItem:
    # An item will have an ID, a type, a name, a price, and a possible list of items it is linked to.
    def __init__(self, id: int, item_type: str, item_name: str, item_price: float, linked_items: list):
        # Sanitation of inputs. If we get an item with a "CATEGORY type" it can't have a price.
        # Not all items will have a linked list of other items.
        self.id = id
        self.item_type = item_type
        self.item_name = item_name
        self.item_price = item_price
        self.linked_items = linked_items



# This function parses an incoming menu stream.
def parse_menu(menu_stream):

    print("I get into the parse function!")

    # Make an incoming item raw list that is parsed on the seperating empty strings.
    # item_raw_list = incoming_items.split(" ")

    # Use menu stream construct to construct menu entries.
    # When it returns None, there is no more entries in the list.
    menu_item_list = []


    # Using this menu stream to construct menu entries one at a time. Start off with nothing.
    current_menu_entry = None

    current_string = menu_stream.nextline

    while current_string != None:
        # Find out where you are in the entry. Gather next string.

        # If the current entry is empty, the next thing we're looking at is the ID.
        if current_string is None:
            # Set the ID advance pointer.
            current_menu_entry = MenuItem(current_string, None, None, None, [])
            current_string = menu_stream.nextline

            # Set the type, advance pointer.
            current_menu_entry.item_type = current_string
            current_string = menu_stream.nextline

            # Set the name, advance pointer.
            current_menu_entry.name = current_string
            current_string = menu_stream.nextline

            # Possibility 1. Not a category. Price will be here. Need a way to differentiate price and
            # ID list. Also may not have an ID list.

            # Possibility 2. Is a category.
            # Price will not be here. COULD have a list of ID's. Could be empty.
            # Easy test, only happens if there is no next-string in the MenuStream.

            # Possibility 3. Is a category. Has IDs. No need to differentiate between Price.

            # When parsing we need to pass in "None" for price if we see this, or pop an error.
            # if item_type == "CATEGORY" and item_price is not None:
            #   raise Exception("An item with a category cannot have a price!")

            # Take care of parsing Category flows here.
            if current_menu_entry.item_type == "CATEGORY":
                if current_string != " ":
                    # In this case you've encountered a list of ID's and need to put them in their place.
                    # current_menu_entry.linked_items.append(int(current_string))
                    while current_string != " ":
                        current_menu_entry.linked_items.append(int(current_string))
                        current_string = menu_stream.nextline
                else:
                    menu_item_list.append(current_menu_entry)
                    current_menu_entry = None
                    continue
                menu_item_list.append(current_menu_entry)
                current_menu_entry = None
            # Take care of parsing not-a-category-flows here.
            else:
                # Set the type, advance pointer.
                current_menu_entry.price = current_string
                current_string = menu_stream.nextline

                if current_string != " ":
                    # In this case you've encountered a list of ID's and need to put them in their place.
                    # current_menu_entry.linked_items.append(int(current_string))
                    while current_string != " ":
                        current_menu_entry.linked_items.append(current_string)
                        current_string = menu_stream.nextline
                else:
                    menu_item_list.append(current_menu_entry)
                    current_menu_entry = None
                    continue

        current_string = menu_stream.nextline

    print(menu_item_list)



# Implementation will be supplied when ready for testing.
class MenuStream:
    def __init__(self):
        self.stream = ['4', 'ENTREE', 'Spaghetti', '10.95', '2', '3', '', '1', 'CATEGORY', 'Pasta', '4', '5', '', '2', 'OPTION', 'Meatballs', '1.00', '', '3', 'OPTION', 'Chicken', '2.00', '', '5', 'ENTREE', 'Lasagna', '12.00', '', '6', 'ENTREE', 'Caesar Salad', '9.75', '3', '']

    def nextline(self):

        return self.stream.pop(0) if self.stream else None

parse_menu(MenuStream())


"""
4
ENTREE
Spaghetti
10.95
2
3

1
CATEGORY
Pasta
4
5

2
OPTION
Meatballs
1.00

3
OPTION
Chicken
2.00

5
ENTREE
Lasagna
12.00

6
ENTREE
Caesar Salad
9.75
3
[null]
"""
