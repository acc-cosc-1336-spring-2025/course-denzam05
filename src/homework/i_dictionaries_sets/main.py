from dictionary import get_p_distance_matrix

def display_matrix (matrix):
    for row in matrix:
        print (' '.join (f'{value: .2f}' for value in row))


def main():
    while True:
        print ("menu:")
        print ("1 - get p distance matrix ")
        print (" 2 - exit")

        choice = input ("enter your choice (1 or 2):")
        if choice == "1":
            dna_lists = []
            print ("enter lists, type done when finished ")
            while True:
                user_input = input("enter list:")
                if user_input.lower() == 'done':
                    break
                try:
                    dna_lists.append(user_input.strip(). split())
                except Exception as e:
                    print ("error parsing input:{e}")
                    continue
            try:
                p_distance_matrix = get_p_distance_matrix (dna_lists)
                print ("p- distance matrix:")
                display_matrix (p_distance_matrix)
            except ValueError as e:
                print ("error: {e}")
            except Exception as e:
                print ("an unexpected error occurred: {e}")
        elif choice == "2":
            print("exiting...")
            break
        else:
            print("invalid choice. please enter 1 or 2 ")
if __name__ == "__main__":
    main()
          

            
