
def main():
    print("Welcome to Taco Palace, please view the menu below and \nenter the number that represents your selection")
    print()

    items_selected = {}
    while True:
        menu_items()
        selection = int(input("Enter your selection number or enter '5' to quit: "))

        if selection == 5:
            print("Thank you for using Taco Palace.")
            break

        quantity = int(input("Enter how many would you like to order: "))
        menu_selection(selection, items_selected, quantity)

        add_more = str(input("Do you want to add more items? (Y/N) "))
        add_more_upper = add_more.upper()

        while add_more_upper not in ['Y', 'N']:
            print("Invalid selection, please enter Y or N")
            add_more = str(input("Do you want to add more items? (Y/N) "))
            add_more_upper = add_more.upper()

        if add_more_upper == "N":
            break

    total_due = amount_due(items_selected)
    print("You ordered: ")
    for item, (price, quantity) in items_selected.items():
        print("{} {}".format(quantity, item))
    print("Your amount due is: $", total_due)

    print("Thank you for using Taco Palace.")


def menu_items():
    print("1. Tacos: $3.50 \n2. Burritos: $8.50 \n3. Nachos: $7.50 \n4. Soda: $1.50")
    print()

def menu_selection(choice, items_selected, quantity):
    if choice == 1:
        print("You have selected: \n - Tacos: $3.50")
        items_selected["Tacos"] = (3.50, quantity)
    elif choice == 2:
        print("You have selected: \n - Burritos: $8.50")
        items_selected["Burritos"] = (8.50, quantity)
    elif choice == 3:
        print("You have selected: \n - Nachos: $7.50")
        items_selected["Nachos"] = (7.50, quantity)
    elif choice == 4:
        print("You have selected: \n - Soda: $1.50")
        items_selected["Soda"] = (1.50, quantity)
    else:
        print("Invalid selection, please try again")

    return choice, items_selected, quantity

def amount_due(items_selected):
    total = 0
    for price, quantity in items_selected.values():
        total += price * quantity
    return total


main()
