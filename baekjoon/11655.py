string = input()
for x in string:
    print(chr(((ord(x)-52)%26)+65) if 'A' <= x <= 'Z' else (chr(((ord(x)-84)%26)+97) if 'a' <= x <= 'z' else x), end="")