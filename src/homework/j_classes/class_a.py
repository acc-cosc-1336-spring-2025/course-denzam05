
import random

class die:
    __roll_value = None

    def roll (self):
        self.__roll_value = random.randint (1, 6)

    def get_rolled_value (self):
        return self.__roll_value
    
    def __str__(self):
        return f"the rolled value is {self.__roll_value}"
    
    