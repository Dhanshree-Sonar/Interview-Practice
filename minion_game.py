##Game Rules
##
##Both players are given the same string, S.
##Both players have to make substrings using the letters of the string S.
##Stuart has to make words starting with consonants.
##Kevin has to make words starting with vowels. 
##The game ends when both players have made all possible substrings. 
##
##Scoring
##A player gets +1 point for each occurrence of the substring in the string S.
##
##For Example:
##String S = BANANA
##Kevin's vowel beginning word = ANA
##Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
##
##Your task is to determine the winner of the game and their score.
##
##Input Format
##
##A single line of input containing the string S. 
##Note: The string S  will contain only uppercase letters: [A-Z].
##
##Output Format
##
##Print one line: the name of the winner and their score separated by a space.
##
##If the game is a draw, print Draw.
##
##Sample Input - BANANA
##Sample Output - Stuart 12


# Solution1 -
#   which provides substring with count of occurances of each substring
def minion_game(s):
    stuart = {}
    kevin = {}

    for i in range(len(s)):
        if s[i] in 'AEIOU':
            for j in range(i+1,len(s)+1):               
                if s[i:j] not in kevin:
                    kevin[s[i:j]] = 1
                else:
                    kevin[s[i:j]] += 1
             
        else:
            for j in range(i+1,len(s)+1):
                if s[i:j] not in stuart:
                    stuart[s[i:j]] = 1
                else:
                    stuart[s[i:j]] += 1

    s_count = 0
    k_count = 0
    print '\nStuart Score:'
    for k, v in stuart.items():
        print k + " - " + str(v)
        s_count += v

    print '\nKevin Score:'
    for k, v in kevin.items():
        print k + " - " + str(v)
        k_count += v

    if s_count > k_count:
        print '\nCongratulations Stuart!! Your score is ' + str(s_count)
    elif s_count < k_count:
        print '\nCongratulations Kevin!! Your score is ' + str(k_count)
    else:
        print '\nDraw'

minion_game('BANANA')



# Solution2:
#   Efficient solution which just provides winner name with score
def minion_game_efficient(s):
    s_score = 0
    k_score = 0

    for i in range(len(s)):
        if s[i] in 'AEIOU':
            k_score += (len(s)-i)
        else:
            s_score += (len(s)-i)

    if s_score > k_score:
        print 'Stuart', s_score
    elif s_score < k_score:
        print 'Kevin', k_score
    else:
        print 'Draw'


minion_game_efficient('BANANA')



