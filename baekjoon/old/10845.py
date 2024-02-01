import sys
input = sys.stdin.readline
queue = []

for _ in range(int(input())):
    command = input().split()
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == "pop" and len(queue) > 0:
        print(queue[0])
        queue.pop(0)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front" and len(queue) > 0 :
        print(queue[0])
    elif command[0] == "back" and len(queue) > 0 :
        print(queue[-1])
    else:
        print(-1)