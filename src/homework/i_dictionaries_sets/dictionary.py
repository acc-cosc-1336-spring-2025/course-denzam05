inventory ={}

def add_inventory (widget_name: str, quantity: int):
    if widget_name in inventory:
        inventory [ widget_name] += quantity
    else:
        inventory [widget_name]= quantity

def remove_inventory_widget ( widget_name: str):
    if widget_name in inventory:
        del inventory [widget_name]
        return True
    return False