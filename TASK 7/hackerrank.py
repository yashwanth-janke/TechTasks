#1
def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0

    for i in range(3):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1
    
    return [alice_score, bob_score]

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = compareTriplets(a, b)

print(result[0], result[1])

#2
def diagonalDifference(arr):
    n = len(arr)
    left_diag_sum = 0
    right_diag_sum = 0

    for i in range(n):
        left_diag_sum += arr[i][i]
        right_diag_sum += arr[i][n - i - 1]

    return abs(left_diag_sum - right_diag_sum)

n = int(input())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

result = diagonalDifference(matrix)

print(result)

#3
def staircase(n):
    for i in range(1, n + 1):
        spaces = n - i
        print(" " * spaces + "#" * i)


n = int(input())

staircase(n)

#4
def birthdayCakeCandles(candles):
    max_height = max(candles)
    count = candles.count(max_height)
    return count

n = int(input())

candles = list(map(int, input().split()))


result = birthdayCakeCandles(candles)


print(result)

#5
def timeConversion(s):

    hh = int(s[:2])
    mm = int(s[3:5])
    ss = int(s[6:8])
    meridiem = s[8:10]


    if meridiem == "PM" and hh != 12:
        hh += 12
    elif meridiem == "AM" and hh == 12:
        hh = 0

    military_time = f"{hh:02d}:{mm:02d}:{ss:02d}"
    return military_time


time_12_hour = input()


military_time = timeConversion(time_12_hour)
print(military_time)
