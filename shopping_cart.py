import sys  # module exit the program when called


# create a title function
def title():
    print("\n                        $$$$$$$$$$$$$")
    print("                                 $$$$")
    print("          Shopping Cart  V1.0    $$$$")
    print("                                 $$$$")
    print("         $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


title()

name = input("\n           Enter your name: ")
print("\n      ---------------------------------------------")
print(f"      Hello {name}, welcome to your shopping cart ")
print("      ---------------------------------------------")
print("\n       <<< Press Enter to access menu >>>    ")
input("...")

myCart = []


# funtion that returns the user to the menu
def dash_board():
    while True:
        print("    <<<<<<<< OPTION MENU >>>>>>>>   ")
        print("    ****************************")
        print("    Press 1 - 6 to select option")
        print("    ****************************")
        print("     1: Add item")
        print("     2: View cart")
        print("     3: Search item")
        print("     4: Delete item")
        print("     5: Empty cart  ")
        print("     6: Exit app ""\n")
        option = input("Select option: ")
        if option == "1":
            print("    =========================")
            print("    <<  Add item to Cart  >>")
            print("    =========================""\n")
            add_item()
        elif option == "2":
            print("    =========================")
            print("    <<      View cart    >>  ")
            print("    =========================""\n")
            view_cart()
        elif option == "3":
            print("     =========================")
            print("     <<    Search item   >>")
            print("     =========================""\n")
            search_item()
        elif option == "4":
            print("     =========================")
            print("     <<       Delete item   >>")
            print("     =========================""\n")
            delete_item()
        elif option == "5":
            print("     =========================")
            print("     <<      Empty cart     >>")
            print("     =========================""\n")
            empty_cart()
        elif option == "6":
            print("     =========================")
            print("     <<     Exit program    >>")
            print("     =========================""\n")
            print("Press Enter to Exit")
            input()
            sys.exit(" **** Thank you for your time ***")
        else:
            print("Invalid option selected, RETRY!!!")
            print("Press enter to Return to Menu")
            input()


# function to Add items to the shopping cart
def add_item():
    item = input("Add item to cart: ")
    myCart.append(item)
    print(f"\n____{item} added to cart____""\n")


# displays the list of items in the cart
def view_cart():
    line = 0
    for item in myCart:
        line += 1
        if len(myCart) != 0:
            print(f"Item {line}: {item}")
            break
    else:
        print("\n____!!!You have nothing in your cart____""\n")


def search_item():
    item = input("Find item in cart: ")
    if item in myCart:
        print(f"____{item} is in cart____""\n")
    else:
        print(f"____{item} is not in cart____""\n")


dash_board()