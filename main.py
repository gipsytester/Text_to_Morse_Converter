import winsound
from time import sleep

morse_transformation = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--.',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    '¿': '..-.-', '¡': '--...-', ' ': '/'
}
frequency = 700
duration_short = 240
duration_long = 720


def to_morse(string):
    try:
        new_string = ''
        for char in string:
            new_string += morse_transformation[char] + ' '
        return new_string
    except KeyError as error_msg:
        print(f"Sorry, the character {error_msg} can't be converted")
        return "Not available"


user_text = input('Insert the text to be converted: ')
morse_version = to_morse(user_text.lower())
print(f'Morse version:\n{morse_version}')

for item in morse_version:
    if item == '.':
        winsound.Beep(frequency, duration_short)
        sleep(0.24)
    elif item == '-':
        winsound.Beep(frequency, duration_long)
        sleep(0.24)
    else:
        sleep(0.48)





