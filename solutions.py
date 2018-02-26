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

# Complexcity  O(n) where n = lengh of s







