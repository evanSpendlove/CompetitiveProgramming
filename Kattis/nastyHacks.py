# Kattis - Nasty Hacks

def nastyHacks():
    n = int(input())

    for i in range(0, n):
        values = input().split(" ") # Get input
        values = [int(i) for i in values] # Convert to integers

        if((values[1] - values[0] > values[2])):
            print('advertise')
        elif((values[1] - values[0] == values[2])):
            print('does not matter')
        else:
            print('do not advertise')

def main():
    nastyHacks()

main()