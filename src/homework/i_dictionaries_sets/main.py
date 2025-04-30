import dictionary

def main ():
    while True:
        print ("\ninventory menu")
        print ("1- add or update item")
        print ("2- Delete item")
        print ("3- exit")

        choice = input ("choose an option:")

        if choice == "1":
           item = input ("enter widget name:")
           try:
               quantity = int(input ("enter quantity:"))
               dictionary.add_inventory(item, quantity)
               print (f"{item} update. Current quantity: {dictionary.inventory [item]}")
           except ValueError:
                 print ("please enter a valid number")

        elif choice =="2":
            item= input ("enter widget name to delete:")
            if dictionary.remove_inventory_widget (item):
              print (f"{item} removed from inventory.")
            else:
              print (f"{item} not found.")

        elif choice =="3":
             print ("exiting program.")
             break

        else:
              print ("invalid choice. try again.")

main () 

    