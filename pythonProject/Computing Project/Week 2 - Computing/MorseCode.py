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
