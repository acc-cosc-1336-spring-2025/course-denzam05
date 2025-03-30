#
from lists import get_highest_list_value, get_lowest_list_value

def main ():
    while True:


        print("\nMenu:")
        print("1- show the list low / high values")
        print("2- exit")
        choice = input("choose an option:")

        if choice =='1':
            numbers=[]
            while True:
                try:
                  num= int (input("enter a list value:"))
                  numbers.append(num)
                  if len (numbers) >=3:
                   cont=input ("do you want to enter another value? (yes /no):").strip().lower()
                   if cont != "yes":
                        break
                except ValueError:
                   print ( "please enter a valid number.")
        
                 
            if numbers:
                    print(f"lowest value: {get_lowest_list_value (numbers)}")
                    print (f"highest value: {get_highest_list_value (numbers)}")
        elif choice == "2":
            print("existing ...")
            break
        else:
            print ("invalid option")

main () 
            

