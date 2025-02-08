#

from decisions import get_faculty_rating, get_options_ratio

import decisions




options= float (input('enter options value'))
total= float (input('enter total value'))

result= decisions.get_options_ratio (options, total)
print ('get_faculty_rating:', result)

faculty_rating= decisions.get_faculty_rating(result)
print ("faculty rating:", faculty_rating)





