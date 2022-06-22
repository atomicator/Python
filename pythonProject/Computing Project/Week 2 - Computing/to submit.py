# NestedFraction.py

# a program to calculate the value of a nested fraction sequence using iterative methods
def nested_fraction(previous_nest):  # calculates the value of the nested fraction given the value of the previous one
    value = 1 + 1/(previous_nest)
    return value


def adjust_digits(number, length):  # adjusts the number of digits of a given float of integer (returning it as text)
    text = str(number)
    if len(text) <= length:
        if not ("." in text):
            text += "."
        text += "0" * (length - len(text))
    else:
        text = text[:length]
    return text


n = 20
initial_value = 1
values = [initial_value]  # used to store the values, and already containing the first
digits = 10

value = initial_value
for i in range(n - 1):  # iterates to find the other values and add them to values
    value = nested_fraction(value)
    values.append(value)

print(values)

for num in values:  # This loop adjusts the length of each digit in values then prints them
    num = adjust_digits(num, digits)
    print(num)

# SimpleAdder.py

# A script that adds two numbers

kwh = float(input("Enter the power in kilowatt hours per day:\n"))  # The number to be converted

watts = (kwh / 24) * 1000  # converts the number

print(f"{kwh} kWh / day is equivalent to {watts} W.\n")  # prints the result

# SquareRootSequence.py

# This uses iterative methods to calculate the value of a square root sequence

import math


def nested_root(previous_root):  # calculates the value of the root using the value of the previous one
    value = math.sqrt(1 + previous_root)
    return value


def adjust_digits(number, length):  # adjusts the number of digits of a given float of integer (returning it as text)
    text = str(number)
    if len(text) <= length:
        if not ("." in text):
            text += "."
        text += "0" * (length - len(text))
    else:
        text = text[:length]
    return text


n = 20  # defining the constants
initial_value = 1
values = [initial_value]
digits = 10

value = initial_value
for i in range(n - 1):  # iterates and calculates the values
    value = nested_root(value)
    values.append(value)

print(values)

for num in values:
    num = adjust_digits(num, digits)
    print(num)

# This tends to a value of 1.61803398, the same as the expected value of (1 + root 5) / 2

# SumOddNumbers.py

# This sums the values of the first N odd numbers (N is given by the user) and checks that it equals the expected value
# of N ** 2

N = input("How many odd numbers should be summed?\n")
valid = True

try:
    N = int(N)
except ValueError:
    print("Please enter a number")
    valid = False

if N < 0:
    print("The number cannot be negative")
    valid = False

if valid:
    total = 0
    i = 1
    while i <= N:
        total += (2 * i - 1)
        i += 1
    print(f"The sum of the first {N} odd integers is {total}")

    if total == N ** 2:
        print(f"The total, {total}, is equal to {N} squared, as expected")
    else:
        print(f"The total, {total}, does not equal {N} squared")

# This is a variation of the text to morse code program. It allows text to be converted to morse, allows morse to be
# converted back to text and allows the playing of morse code files. This file contains references to "beep.mp3" and
# "dash.mp3". This corresponds to the audio files at:
# https://upload.wikimedia.org/wikipedia/commons/transcoded/e/e7/E_morse_code.ogg/E_morse_code.ogg.mp3 and
# https://upload.wikimedia.org/wikipedia/commons/transcoded/b/ba/T_morse_code.ogg/T_morse_code.ogg.mp3 respectively.
import time  # both libraries are used to play audio
import pygame
pygame.init()


def dictionary_flipper(dictionary):  # takes a dictionary as an input, and reverses the keys and values.
    flipped_dict = {}
    items = dictionary.items()
    for pair in items:
        flipped_dict[pair[1]] = pair[0]
    return flipped_dict


text_to_morse_conversion_table = {'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.", 'g': "--.",
                                  'h': "....", 'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..", 'm': "--", 'n': "-.",
                                  'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.", 's': "...", 't': "-", 'u': "..-",
                                  'v': "...-", 'w': ".--", 'x': "-..-", 'y': "-.--", 'z': "--..", '0': "-----",
                                  '1': ".----", '2': "..---", '3': "...--", '4': "....-", '5': ".....", '6': "-....",
                                  '7': "--...", '8': "---..", '9': "----.", " ": "/", ".": ".-.-.-", "": ""}
morse_to_text_conversion_table = dictionary_flipper(text_to_morse_conversion_table)
# This creates two dictionaries, which connect a letter to its equivalent in morse and vice versa


def text_to_morse(text):  # converts a text input to morse code
    morse = ""
    for letter in text:
        morse += text_to_morse_conversion_table[letter] + " "
    return morse


def morse_to_text(morse):  # converts a morse input to text
    text = ""
    letters = morse.split(" ")
    for letter in letters:
        text += morse_to_text_conversion_table[letter]
    return text


def play_morse_code(morse):  # plays a morse code message
    for character in morse:
        if character == ".":
            pygame.mixer.Sound("dot.mp3").play(loops=0)
            time.sleep(1)
        elif character == "-":
            pygame.mixer.Sound("dash.mp3").play(loops=0)
            time.sleep(2)
        elif character == "/":
            time.sleep(5)
        elif character == " ":
            time.sleep(3)


wants_to_exit = False
while not wants_to_exit:  # This while loop creates a menu, allowing the user to select an option or exit.
    choice = input("Do you want to:\n1) Convert text to Morse code\n2) Convert Morse code to text\n3) Play a Morse code"
                   "sample \n4) Exit\nEnter a number to select your choice")
    if choice == "1":
        text = input("Enter the text (punctuation other than '.' will be removed) to be converted to Morse:\n").lower()
        morse = text_to_morse(text)
        print(morse)
    elif choice == "2":
        morse = input("Enter the Morse to be converted to text:\n")
        text = morse_to_text(morse)
        print(text)
    elif choice =="3":
        morse = input("Enter the Morse code sample to be played:\n")
        play_morse_code(morse)
    elif choice == "4":
        exit()
    else:
        print("Invalid, input. Please enter a number to select your choice.")
