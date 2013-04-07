def load_words():
    wordfile = open('/usr/share/dict/american-english', 'r')
    lines = wordfile.read().split('\n')
    wordfile.close()
    return lines

def make_trie(words):
    root = dict()
    for word in words:
        curr_dict = root
        for letter in word:
            curr_dict = curr_dict.setdefault(letter, {})
    return root

def get_letters(number):
    numbers = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r',
                's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

    return numbers.get(number, [])

count = 0

def keypad_words(number, trie, words=[""]):
    global count
    if type(number) == int:
        number = str(number)
    if number == "":
        return words
    words_2 = []
    for w in words:
        for letter in get_letters(number[0]):
            curr_dict = trie
            for l in letter + w:
                try:
                    curr_dict = curr_dict.get(l)
                except AttributeError:
                    break
            if curr_dict != None:
                words_2.append(w + letter)
                count += 1


    #words = [w + letter for w in words for letter in get_letters(number[0])]
    return keypad_words(number[1:], trie, words=words_2)

def find_real_words(words, WORDLIST=load_words()):
    return [word for word in words if word in WORDLIST]
