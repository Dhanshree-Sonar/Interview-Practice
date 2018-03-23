##You are given an integer,N . Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
##
##Different sizes of alphabet rangoli are shown below:
##
###size 3
##
##----c----
##--c-b-c--
##c-b-a-b-c
##--c-b-c--
##----c----
##
##Input Format
##Only one line of input containing N, the size of the rangoli.
##
##Constraints
##0 < N <27
##
##Output Format
##Print the alphabet rangoli in the format explained above.

import string

def print_rangoli(n):
    if n < 0 or n > 26 or type(n) != int:
        print 'Error!! Enter Integer between 1-26'
        return

    char = string.ascii_lowercase
    rangoli = []
    
    for i in range(n):
        # Concatinate '-' and a letter till specified number
        # n = 5 letters to consider a,b,c,d,e
        # s will be a-b-c-d-e for iteration
        s = "-".join(char[i:n])
        # center() is used for padding fillchar ('-') to maintain width of 4*n -3
        rangoli.append((s[::-1]+s[1:]).center(4*n-3, "-"))

    # Print array items backwards to get upper half of the rangoli
    for i in range(n-1, 0, -1):
        print(rangoli[i])
        
    # Print array items to get lower half of the rangoli
    for i in range(n):
        print(rangoli[i])
    
        
print_rangoli(10)
print_rangoli(27)
print_rangoli('a')

##Complexity:
##    Space = O(n(4n - 3) + (2n-1)), (4n-3) is the width of the rangoli and
##        n is the number of the rows need to store. (2n -1) is the string length
##        of 's'.
##        It can be approximated to O(4N^2)
##
##    Time = O(3N)
##

