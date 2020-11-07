"""
Randy Zhu
11-04-2020
Print pattern of:
*****
 ****
  ***
   **
    *
"""

for index in range(5):
    print(" " * index, end="")
    for jindex in range(5 - index):
        print("*", end="")
    print()
