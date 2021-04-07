###
### Author: Sornali Rahman
### Description: This program implements a shopping system that allows
###              a user to perform these functions: buy and return items,
###              view user purchases, see what's in the amazon inventory and view
###              items on the amazon website
###

import webbrowser

# This function returns a dictionary called inventory
# Inventory contains information about item name, price and their corresponding
# amazon id
def get_content():

    file = input("Enter info file name: \n")
    read_file = open(file, 'r')

    inventory = {}

    for line in read_file:
        name, price, amazon_id = line.split()
        price = int(price)
        inventory[name] = (price, amazon_id)
    return inventory


# This function takes in a inventory as a parameter
# Prints out the amazon inventory
def print_inventory(inventory):

    print("These are items in inventory:")

    for item in inventory:
        print(item + ' - $' + str(inventory[item][0]))

# This function takes user's current balance and a dictionary of bought_items
# Prints out a summary of the current state of the user's purchases
def print_belongings(curr_money, bought_items):


    print("You have $" + str(curr_money) + " in your wallet.")

    if len(bought_items) == 0:
        print("No items have been purchased.")
    else :
        print("You have purchased these items:")

        for items in bought_items:
            print(items + ' - ' + str(bought_items[items]))

# This functions takesuser's current balance and amount to add as parameter
# Returns the amount of money that can be added
def add_to_wallet(curr_money, money):


    if curr_money + money > 10000:
        print("Wallet can not exceed $10000. Current wallet $" + str(curr_money))
        return 0
    else:
        print("$" + str(money) + " has been added.")
        return money


# This function takes the user's balance, amazon inventory, items that user bought
# and name of the item that user would like to buy
# Returns the price of the item user bought after adding the item to user's bought list
def buy_item(money, inventory, bought_items, buying):


    if buying not in inventory:
        print("Item does not exist.")
        return 0

    if inventory[buying][0] > int(money):
        print("Sorry, you don't have enough money in your wallet.")
        return 0

    if buying not in bought_items:
        bought_items[buying] = 1
    else:
        bought_items[buying] += 1

    print("Item bought.")

    return inventory[buying][0]

# This function takes the inventory, items that user bought and item that
# the user would like to return as parameters
# Returns the price of the item being returned
def return_item(inventory, bought_items, returning):

    if returning not in bought_items:
        print("Item has not been bought")
        return

    if bought_items[returning] == 1:
        del bought_items[returning]
    else:
        bought_items[returning] -= 1

    print("Item has been returned.")
    return inventory[returning][0]

# This function takes in the inventory and item_name as parameters
# Opens an amazon link to specified item
def view_item_on_web(inventory, item_name):

    url = "https://www.amazon.com/dp/" + inventory[item_name][1]
    webbrowser.open(url)

def main():

    # The inventory should be a dictionary mapping product name (string) to tuples.
    # The tuples will be of length two - the first element being the item's price (int)
    # and the second being the item's Amazon ID.
    inventory = get_content()

    # Keeps track of items bought by user.
    # Key is the item name and value is the number of those items that have been bought.
    belongings = {}

    print("\n------ Welcome to Amayzeon! ------")
    balance = 100

    while True:
        user_input = input("What would you like to do?\n")
        if user_input.startswith('buy'):

            # Retrieves the cost of the item the user wants to buy, and then
            # updates the user's wallet balance accordingly
            buying = user_input.split()[1]
            cost = buy_item(balance, inventory, belongings, buying)

            balance -= cost

        elif user_input.startswith('return'):

            # Retrieves the cost of the item the user wants to return, and then
            # updates the user's wallet balance accordingly
            returning = user_input.split()[1]
            returned = return_item(inventory, belongings, returning)

            balance += returned

        elif user_input.startswith('add'):

            # Retrieves the valid amount of money user wants to add
            # to his wallet and reflects it on the wallet balance
            money = int(user_input.split()[1])
            added = add_to_wallet(balance, money)
            balance += added

        elif user_input.startswith('view'):

            # Views select item on amazon.com
            item_to_view = user_input.split()[1]
            view_item_on_web(inventory, item_to_view)

        elif user_input == 'belongings':
            print_belongings(balance, belongings)
        elif user_input == 'inventory':
            print_inventory(inventory)
        elif user_input == 'exit':
            return
        else:
            print("Huh?")

main()