# Name: The Captain's Room
# Problem: https://www.hackerrank.com/challenges/py-the-captains-room/problem
# Score: 10


from collections import Counter

k = int(input())
room_list = input().split()
count = Counter(room_list)
print(list(count.keys())[list(count.values()).index(1)])


# However, since we were supposed to use Sets in this one, I believe that
# the following solution from itsbruce(https://www.hackerrank.com/itsbruce)
# is the best one:

# nom = int(input())
# members = input().split()
# rooms = set()   # Contains all the rooms.
# room_more_mem = set()   # Contains only the rooms with families.
#
# for m in members:
#     if m not in room_more_mem:
#         target = room_more_mem if m in rooms else rooms
#         target.add(m)
# print(rooms.difference(room_more_mem).pop())
