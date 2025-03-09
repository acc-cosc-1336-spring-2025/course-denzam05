#
import strings 
from strings import get_dna_complement, get_hamming_distance

def main ():
    while True:
        print ("\menu:")
        print ("1 - hamming distance")
        print ("2 - dna complement")
        print ("3 - exit")

        choice= input ("enter your choice: ")

        if choice == "1":
            dna1 = input("enter first dna sequence: ")
            dna2 = input ("enter second dna sequence: ")

            try:
                result= get_hamming_distance (dna1, dna2)
                print (f"hamming distance: {result}")
            except ValueError as e: 
                print(f"error {e}")

        elif choice == "2":
            dna = input ("enter dna sequence: ")
            result = get_dna_complement (dna)
            print(f"dna complement: {result}")

        elif choice =="3":
            print ("exiting...")
            break
        else:
            print("invalid choice, try again")

main()


