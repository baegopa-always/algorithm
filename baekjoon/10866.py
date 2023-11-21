import sys
input = sys.stdin.readline

deque = []
for _ in range(int(input())):
    cmd = input().rstrip()
    if cmd[:10] == "push_front":
        deque.insert(0,int(cmd[11:]))
    elif cmd[:9] == "push_back":
        deque.append(int(cmd[10:]))
    elif cmd == "pop_front":
        print(deque.pop(0) if deque else -1)
    elif cmd == "pop_back":
        print(deque.pop() if deque else -1)
    elif cmd == "size":
        print(len(deque))
    elif cmd == "empty":
        print(0 if deque else 1)
    elif cmd == "front":
        print(deque[0] if deque else -1)
    elif cmd == "back":
        print(deque[-1] if deque else -1)