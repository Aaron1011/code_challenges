import itertools
import copy


def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))


def passgen(password, CHOICES={'a': ['@', '4'], 's': ['$', '&']}):

    passwords = set([])
    combinations = []
    matches = {}
    index = 0
    for char in password:
        if char in CHOICES:
            for item in CHOICES[char]:
                if not matches.get(item):
                    matches[item] = []
                matches[item].append(index)
                combinations.append(item)
        index += 1
    combs = powerset(combinations)
    for comb in combs:
        passwd = list(password)
        matches_copy = copy.deepcopy(matches)
        for choice in comb:
            passwd[matches_copy[choice].pop(0)] = choice
        passwords.add("".join(passwd))
    return list(passwords)


def get_letters(letter, choices):
    return [letter] + choices.get(letter, [])


def recurpassgen(password, passwords=[""], CHOICES={'a': ['@', '4'], 's': ['$', '&']}):
    if password == "":
        return passwords
    passwords = [p + letter for p in passwords for letter in get_letters(password[0], CHOICES)]
    return recurpassgen(password[1:], passwords=passwords)
