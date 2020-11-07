"""
Randy Zhu
11-06-2020
"""

number_of_inputs = int(input())

inputs: "list[str]" = []
for _ in range(number_of_inputs):
    inputs += input().split(" ")

# new_inputs = []
# for row in enumerate(inputs):
#     new_inputs += inputs[row[0]].split(" ")
print(inputs)
