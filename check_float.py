##You are given a string N. 
##Your task is to verify that N is a floating point number.
##In this task, a valid float number must satisfy all of the following requirements:
## Number can start with +, - or . symbol.
## Number must contain at least 1 decimal value.
## Number must have exactly one . symbol. 
## Number must not give any exceptions when converted using float(N).

##Input Format
##
##The first line contains an integer , the number of test cases. 
##The next  line(s) contains a string .
##
##Output Format
##
##Output True or False for each test case.

##Explanation:
##    It uses re - regular expression module to compute the result

##Complexity:
##    Space: It just stores the number, so space complexity is O(1)
##    Time: It computes result using re's match() which has complexity O(N), where N is length of the number
    
##Reference:
##    https://docs.python.org/2/library/re.html#re.search

import re
import sys

for num in sys.stdin:
    print bool(re.match(r'^[+-]?\d*?\.{1}\d+$',num))

    
