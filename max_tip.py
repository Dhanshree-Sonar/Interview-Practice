#https://practice.geeksforgeeks.org/problems/maximum-tip-calculator/0

n, x , y = raw_input().split()
Ai = raw_input().split()
Bi = raw_input().split()
max_tip = 0

for i in range(int(n)):
    max_tip += int(Ai[i]) if int(Ai[i])>int(Bi[i]) else int(Bi[i])

print "Max Tip: " + str(max_tip)

##Complexity:
##    Space: O(1), need just one counter to store max tip
##    Time: O(N) where N is number of orders

##Input:
##5 3 3
##1 2 3 4 5
##5 4 3 2 1
##Output:
##21


