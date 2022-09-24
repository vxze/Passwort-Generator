# Importing modules
from random import choice, randrange
from string import ascii_letters, digits, punctuation
from datetime import datetime
from tqdm import tqdm
from time import sleep
import sys

def genStr():
        print()
        # User input
        lenght = int(input('Strings lenght : '))
        lines = int(input('How many lines to generate : '))

        def randStr (
                chars = ascii_letters + digits + punctuation, N=lenght):
                return ''.join(choice(chars) for _ in range(N))

        print()
        print ("Generating output... press Ctrl+C to stop.")

        # Open file and write output strings
        stdoutOrigin = sys.stdout 
        sys.stdout = open("output.txt", "w")

        # Counting elapsed time
        start = datetime.now()

        # Loop action showing progress bar
        for x in tqdm (range (lines)):
                # Generating strings
                print(randStr())

        # Stop counting
        end = datetime.now()

        sleep(0.5)

        # Close file and revert back to code
        sys.stdout.close()
        sys.stdout = stdoutOrigin

        print("Done! \n")
        print("[ Time elapsed ]")
        print(end-start, "\n")
        print("──────────"*12)


def genRandLenStr():
        # User input
        print()
        minrange = int(input('Strings lenght minimum range : '))
        maxrange = int(input('Strings lenght maximum range : '))
        
        if minrange == maxrange:
                print()
                print("Don't input the same numbers, for that restart the script and use Option n°1. ")
                return genRandLenStr()
        if maxrange < minrange :
                print()
                print("Maximum range can't have a lower value compared to Minimum range.")
                return genRandLenStr()

        lines = int(input('How many lines to generate : '))
        
        print()
        print ("Generating output... press Ctrl+C to stop.")

        # Open file and write output strings
        stdoutOrigin = sys.stdout 
        sys.stdout = open("output.txt", "w")

        # Counting elapsed time
        start = datetime.now()

        # Loop action showing progress bar
        for x in tqdm (range (lines)):
                
                randlen = randrange(minrange, maxrange+1)

                # Generating strings
                def randLenStr (
                chars = ascii_letters + digits + punctuation, N=randlen):
                        return ''.join(choice(chars) for _ in range(N))
                
                print(randLenStr())

        # Stop counting
        end = datetime.now()

        sleep(0.5)

        # Close file and revert back to code
        sys.stdout.close()
        sys.stdout = stdoutOrigin

        print("Done! \n")
        print("[ Time elapsed ]")
        print(end-start, "\n")
        print("──────────"*12)


print()
print("──────────"*12)
print("| gen.py |"*12)
print("──────────"*12)
print()
print("Choose an option.\n")
print("1. Normal lenght")
print("2. Random lenght range")

while True:
        option = input('Option > ')

        if option == '1':
                genStr()
                break
        if option == '2':
                genRandLenStr()
                break
        else:
                print("Invalid option.")
                