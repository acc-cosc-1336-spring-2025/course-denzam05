#

def get_options_ratio (options, total):

    ratio = options/ total
    return ratio


def get_faculty_rating (ratio):
    ratio = float (ratio)
    if (ratio <= 1.0 and ratio >= .9):
        return 'Excellent'
    elif (ratio <= .9 and ratio >= .8):
        return 'Very good'
    elif (ratio <= .8 and ratio >= .7):
        return 'Good'
    elif (ratio <= .7 and ratio >= .6):
        return 'Needs Improvement'
    elif (ratio <= .59 and ratio >= 0):
        return 'Unacceptable'

    