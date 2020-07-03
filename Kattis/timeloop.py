def timeLoop(magicNumber): # Function for printing multiple times
    for x in range (0, magicNumber): # For loop
        print((x+1), ' Abracadabra') # Prints Abracadabra x times

def main():
    x  = int(input()) # Converts the input to an integer
    timeLoop(x)    # Calls the timeLoop function passing x as an argument

main()