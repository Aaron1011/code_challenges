import re

def load_words():
    wordfile = open('/usr/share/dict/american-english', 'r')
    lines = wordfile.read().split('\n')
    wordfile.close()
    return lines

def get_letters(number):
    numbers = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r',
                's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

    return numbers.get(number, [])

def keypad_words(number, words=[""]):
    if type(number) == int:
        number = str(number)
    if number == "":
        return words
    words = [w + letter for w in words for letter in get_letters(number[0])]
    return keypad_words(number[1:], words=words)

def find_real_words(words, WORDLIST=load_words()):
    return [word for word in words if word in WORDLIST]
