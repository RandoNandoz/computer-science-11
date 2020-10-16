"""
CCC Junior Problem One
Randy Zhu
"""
score: int = 0
for i in range(3):
    score += int(input()) * (i + 1)
if score >= 10:
    print("happy")
else:
    print("sad")
