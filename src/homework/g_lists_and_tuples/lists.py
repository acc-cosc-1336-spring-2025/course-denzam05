#

def get_lowest_list_value (num):
    if not num:
        return None
    
    lowest= num [0]
    for number in num [1:]:
        if number < lowest:
            lowest= number

    return lowest

def get_highest_list_value (num):
    if not num:
        return None
    
    highest= num[0]
    for number in num [1:]:
        if number> highest:
            highest =number
    return highest