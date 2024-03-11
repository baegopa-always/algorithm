chars = ['A', 'E', 'I', 'O', 'U']
count, answer = 0, 0
def solution(word):
    global answer
    dfs('', word)
    return answer

def dfs(string, word):
    global chars, count, answer
    if len(string) > 4:
        return
    for char in chars:
        string += char
        count += 1
        if word == string:
            answer = count
        dfs(string, word)
        string = string[:-1]
