#
from class_a import die

def main():
    my_die=die()
    print ("welcome to the Die roller.")

    while True:
        input("press enter to roll the die...")
        my_die.roll()
        print (my_die)


        choice = input ("do you want to roll again? (yes /no):").strip().lower()
        if choice != 'yes':
            print ("thanks for playing")
            break

main ()
