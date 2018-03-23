n, x , y = raw_input().split()
Ai = raw_input().split()
Bi = raw_input().split()
max_tip = 0

for i in range(int(n)):
    max_tip += int(Ai[i]) if int(Ai[i])>int(Bi[i]) else int(Bi[i])

print "Max Tip: " + str(max_tip)    
