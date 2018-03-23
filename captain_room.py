##Reference:
##https://www.hackerrank.com/challenges/py-the-captains-room/problem
##Read the problem on hackerrank page

def find_captain_room(k, rooms):
##    room_nums = set(rooms)
##    for room in room_nums:
##        if rooms.count(room) == 1:
##            return room
    # Multiply all the unique room by group number including captain's room
    # Minus the sum of room so we have (k-1)*captain's room
    # Divide result by (k-1) to get captain's room number
    print ((sum(set(rooms))*5) - (sum(rooms)))/(k-1)

k = 5
rooms = [1, 2, 3, 6, 5, 4, 4, 2, 5, 3, 6, 1, 6, 5, 3, 2, 4, 1, 2, 5, 1, 4,
         3, 6, 8, 4, 3, 1, 5, 6, 2]

find_captain_room(k, rooms)

##Complexity:
##    Space = O(1) are do not need anyother data structure.
##    Time = O(1) , juts one line mathematical formula to find captians room

