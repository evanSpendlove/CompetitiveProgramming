# Kattis - Quality of Life Problem - Code: qaly
# Written by Evan Spendlove

def qaly():
    numPeriods = int(input())

    sumQaly = 0
    period = numPeriods

    while(period > 0): # For each period in the given number
        [quality, numYears] = input().split(" ") # Gets the quality of life for the given period

        quality = float(quality)
        numYears = float(numYears)

        sumQaly += (quality * numYears) # Add the quality x number of years to the running total
        period = period-1
    
    print(round(sumQaly, 3)) # Output the total Qaly


def main():
    qaly()

main()