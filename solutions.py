def question1(s,t):
    # Check whether arguements are of string data-type
    if type(s) != str or type(t) != str:
        return "Error: Argument(s) not string"

    # Check whether 't' is an empty string
    if len(t) == 0:
        return True

    # Check if s is smaller than 't' or 's' is an empty string
    if len(s) < len(t) or len(s) == 0:
        return False

    # Convert strings to lower case
    s = s.lower()
    t = t.lower()

    l = len(t)
    for i in range(len(s)):
        if sorted(s[i:(i+l)]) == sorted(t):
            return True

    return False

def run_test_q1():
    print "\nQuestion1 Test Cases:"
    # Should return True
    print " question1(\"udacity\", \"ad\"): %s" % (question1("udacity", "ad"))
    # Should return Flase
    print " question1(\"udacity\", \"udy\"): %s" % (question1("udacity", "udy"))
    # Should return True
    print " question1(\"udacity\", \"\"): %s" % (question1("udacity", ""))
    # Should return False
    print " question1(\"\", \"ad\"): %s" % (question1("", "ad"))
    # Should return False
    print " question1(\"ad\", \"udacity\"): %s" % (question1("ad", "udacity"))
    # Should return Error
    print " question1(\"udacity\", 1): %s" % (question1("udacity", 1))

def question2(a):
    # Check whether arguement is of string data-type
    if type(a) != str:
        return "Error: Argument is not a string"

    # If string is empty or single character then return string as it is
    if len(a) < 2:
        return a

    longest = ""
    a = a.lower()
    for i in range(len(a)):
        # Traverse the each substring after the i position
        for j in range(i+1, len(a)+1):
            # Check if substring is palindrom and if it is logner than the current one
            if a[i:j] == a[i:j][::-1] and len(longest) < len(a[i:j]):
                longest = a[i:j]

    return longest

run_test_q1()
