import sys
input = sys.stdin.readline

people = [int(input()) for _ in range(9)]
height = sum(people)
for i in range(9):
    for j in range(i+1,9):
        if height - people[i] - people[j] == 100:
            people[i], people[j] = 0, 0
            people.sort()
            print(*people[2:],sep="\n")
            exit()