def add_item(inventory, item):
    inv = inventory()
    if len(inv["items"]) == inv["capacity"]:
        raise ValueError
    if item == "":
        raise ValueError
    inv["items"].append(item)
    return inv

def remove_item(inventory, item):
    pass

def get_item_count(inventory):
    pass