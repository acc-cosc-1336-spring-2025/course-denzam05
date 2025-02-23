#
def get_factorial(num):
    result =1

    for n in range (1, num+1):
        result = n* result

    return result

def sum_odd_numbers(num):

    sum = 0
    i = 0
    while  i<= num:
        if i%2 == 1:
            sum += i
        i +=1

    return sum

    
def get_valid_number_for_factorial():
    while True:
        
            num= int(input ('enter a number between 8 and 10'))
            if 0< num <10:
                return num
            else:
                print ("number must be greater than 0 and less than 10. please try again")

def get_valid_number_for_sum():
    while True:

        num= int (input ('enter a number between 0 and 100'))
        if 0 <num < 100:
            return num
        else :
            print ("number must be greater than 0 and less that 100. please try again ")


def exiting ():
    exit_option = input ('do you wanna exit? (yes/ no):')
    if exit_option in ('yes'):
        print ( 'Exiting.')
        exit()

    elif exit_option in ('no'):
        print ( 'continuing.')
        return
    else:
        print('invalid input. please answer with "yes" or "no".')



def display_menu():
        print (' 1 - factorial')
        print ('2 - sum odd numbers')
        print ('3 - exit')


def run_menu():
    user_option = '0'

    while ( user_option !='3'):
        display_menu()

        user_option = input ('enter a menu option 1, 2, or 3:')
        handle_menu (user_option)


def handle_menu (user_option):

    if (user_option == '1'):
        number = get_valid_number_for_factorial ()
        result = get_factorial (number)
        print ('factorial =', result)
   
    elif (user_option == '2'):
        number = get_valid_number_for_sum () 
        result = sum_odd_numbers ( number)
        print ('sum of odds =', result)

    elif (user_option== '3'):
         print ('exiting.')
    else:
         print ('invalid menu option') 

    
    


