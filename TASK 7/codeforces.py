#1Q
import math
n, m, a = map(int, input().split())
stones = math.ceil(n/a) * math.ceil(m/a)
print(stones)


#2q
for _ in range(int(input())):
    word = input()    
    
    if len(word) > 10:
        
        abbr = word[0] + str(len(word) - 2) + word[-1]
        print(abbr)
    else:
        
        print(word)

#3q
n, k = map(int, input().split())
scores = list(map(int, input().split()))
thr_ore = scores[k - 1]
par_ad= sum(1 for score in scores if score >= thr_ore and score > 0)
print(par_ad)

#4q

n = int(input())
x = 0

for _ in range(n):
    statement = input()
    if "++" in statement:
        x += 1
    else:
        x -= 1

print(x)

#5q

situ = input()

adj = 1
previ = situ[0]
dangerous = False

for player in situ[1:]:
    if player == previ:
        adj += 1
        if adj >= 7:
            dangerous = True
            break
    else:
        adj = 1
        previ = player

if dangerous:
    print("YES")
else:
    print("NO")
