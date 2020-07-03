# Kattis - Event Planning
# Written by: Evan Spendlove

def possibleChoice(numPeeps, budget, numWeeks, costPerPeep, weekendsFree) -> bool: # Specifies return type is boolean
    affordableStay = False
    enoughBeds = False

    if((costPerPeep * numPeeps) <= budget):
        affordableStay = True

    for week in range(0, numWeeks): # For each weekend
        if(weekendsFree[week] >= numPeeps):
            enoughBeds = True # If any weekend has enough beds 

    return(affordableStay and enoughBeds)

def eventPlanning():
    # Get initial input
    [numPeeps, budget, numHotels, numWeeks] = input().split(" ")

    # Convert to integers
    numPeeps = int(numPeeps)
    budget = int(budget)
    numHotels = int(numHotels)
    numWeeks = int(numWeeks)

    validChoice = False
    chosenCost = 0

    for hotel in range(0, numHotels): # For each hotel
        currentPrice = int(input()) # Sets currentPrice
        
        bedsPerWeekend = input().split(" ")

        bedsPerWeekend = [int(i, base=10) for i in bedsPerWeekend]
        
        if(possibleChoice(numPeeps, budget, numWeeks, currentPrice, bedsPerWeekend)):
            if(chosenCost == 0): # If first found
                chosenCost = (currentPrice * numPeeps) # Set cost
                
            elif((currentPrice * numPeeps) < chosenCost): # If better option
                chosenCost = currentPrice * numPeeps # Set cost to lower cost
            validChoice = True # Update boolean as valid choice found
                
    
    if(validChoice):
        print(chosenCost)
    else:
        print('stay home')    



def main():
    eventPlanning()

main()