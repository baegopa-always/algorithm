# 백준 - 너의 평점은
# 실버 5
import sys
input = sys.stdin.readline

points = {"A+": 4.5,"A0": 4.0,
          "B+": 3.5, "B0": 3.0,
          "C+": 2.5, "C0": 2.0,
          "D+": 1.5, "D0": 1.0,
          "F": 0}

s, t = 0, 0
for _ in range(20):
    subject, credit, grade = input().split()
    if grade == "P":
        continue
    s += float(credit) * float(points[grade])
    t += float(credit)

print(format(s/t,".6f"))