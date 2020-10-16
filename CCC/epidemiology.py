"""
CCC Problem J2
Randy Zhu
"""

infection_limit = int(input())
patient_zeroes = int(input())
infection_rate = int(input())
infected = 0
# newly_infected = 0
# infected = 0
currently_infected = patient_zeroes
# infected = 0

days = 0
while infected < infection_limit:
    infected += (currently_infected * infection_rate) * \
        infection_rate + patient_zeroes
    currently_infected = infected
    days += 1
print(days)
