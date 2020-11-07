"""
Randy Zhu
11-04-2020
Draw nested pattern of:
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""

for index in range(5):
    for jindex in range(5 - index):
        print(str(jindex + 1) + " ", sep="", end="")
    print()
