import sys
from collections import deque
from string import ascii_uppercase

alphabet = deque(ascii_uppercase)
alphabet.remove('J')

message = input()
key = input()

key_table = [[0]*5 for _ in range(5)]
used_c = {}
location_c = {}

for i in range(len(key)):
    if key[i] not in used_c:
        key_table[len(used_c)//5][len(used_c)%5] = key[i]
        location_c[(len(used_c)//5,len(used_c)%5)] = key[i]
        used_c[key[i]] = [len(used_c)//5,len(used_c)%5]
    

for i in range(25):
    if alphabet[i] not in used_c:
        key_table[len(used_c)//5][len(used_c)%5] = alphabet[i]
        location_c[(len(used_c)//5,len(used_c)%5)] = alphabet[i]
        used_c[alphabet[i]] = [len(used_c)//5,len(used_c)%5]


split_message = []

idx = 0
while idx < len(message):
    if idx == len(message) - 1:
        split_message.append(message[idx]+'X')
        break
    elif message[idx] != message[idx+1]:
        split_message.append(message[idx:idx+2])
        idx+=2
    elif message[idx] == message[idx+1]:
        if message[idx] == 'X':
            split_message.append(message[idx]+'Q')
        else:
            split_message.append(message[idx]+'X')
        idx+=1

result = ''
for i in split_message:
    x, y = i[0], i[1]
    (x1,y1),(x2,y2) = used_c[x], used_c[y]
   
    if x1 == x2:
        result += location_c[(x1, (y1+1)%5)] + location_c[(x2, (y2+1)%5)]
    elif y1 == y2:
        result += location_c[((x1+1)%5, y1)] + location_c[((x2+1)%5, y2)]
    else:
        result += location_c[(x1, y2)] + location_c[(x2, y1)]
print(result)
