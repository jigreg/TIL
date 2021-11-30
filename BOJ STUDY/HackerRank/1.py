#카카오 브레인 1번
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countSubstrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING input_str as parameter.
#

def countSubstrings(input_str):
    letter = {'a': 1 , 'b' : 1, 'c' : 2 ,'d' : 2, 'e' : 2, 'f' : 3, 'g' : 3 ,
    'h' : 3 , 'i' :4 , 'j' : 4 , 'k': 4 , 'l' : 5, 'm' : 5 , 'n' : 5 , 'o' : 6, 'p' : 6 ,
    'q' : 6, ' r': 7 , 's' : 7, 't' : 7 , 'u': 8 ,'w' : 8 , 'x' : 9 , 'y' : 9,'z' : 9}
    input_str.sort()
    total = 0
    for i in input_str(len(input_str)):
        if i in letter :
            total += i.value()
    return total



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    input_str = input()

    result = countSubstrings(input_str)

    fptr.write(str(result) + '\n')

    fptr.close()
