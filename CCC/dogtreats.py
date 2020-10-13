"""
CCC Junior Problem One
Randy Zhu
"""
treats: "list[int]" = []
score: int = 0
for i in range(3):
    treats.append(int(input()))

for treat in enumerate(treats):
    score += (treat[0] + 1) * treat[1]
if score >= 10:
    print("happy")
else:
    print("sad")
