# 백준 - 2007년
# 브론즈 1
import sys
import datetime

input = sys.stdin.readline
m, d = map(int, input().split())
days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

x = datetime.date(2007, m, d)
print(days[x.weekday()])