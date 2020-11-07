"""
Randy Zhu
11-04-2020
Find gcf of numbers from 10 - 20
"""

for index in range(10, 21):
    print(str(index) + ": ", end="")
    for factor in range(1, index + 1):
        if index % factor == 0:
            print(f"{factor}, ", end="")
    print()
