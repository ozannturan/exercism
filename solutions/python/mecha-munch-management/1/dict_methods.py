"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """

    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1
    return current_cart

def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """

    cart = {}
    for item in notes:
        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1
    return cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """

    for update in recipe_updates:
        recipe_name = update[0]
        new_ingredients = update[1]
        ideas[recipe_name] = new_ingredients
    return ideas

def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    line_cart = {}
    for item in sorted(cart.keys()):
        line_cart[item] = cart[item]
    return line_cart

def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """

    fulfillment_cart = {}
    
    for item in cart:
        quantity = cart[item]
        aisle = aisle_mapping[item][0]
        refrigeration = aisle_mapping[item][1]
        fulfillment_cart[item] = [quantity, aisle, refrigeration]
    
    result = {}
    for item in sorted(fulfillment_cart.keys(), reverse=True):
        result[item] = fulfillment_cart[item]
    
    return result

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """

    for item in fulfillment_cart:
        ordered_quantity = fulfillment_cart[item][0]
        current_quantity = store_inventory[item][0]
        new_quantity = current_quantity - ordered_quantity
        
        if new_quantity > 0:
            store_inventory[item][0] = new_quantity
        else:
            store_inventory[item][0] = 'Out of Stock'
    
    return store_inventory