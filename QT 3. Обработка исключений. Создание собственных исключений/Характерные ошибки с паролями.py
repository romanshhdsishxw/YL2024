class PasswordError(Exception):
    pass


class LetterError(PasswordError):
    pass


class LengthError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


class WordError(PasswordError):
    pass


exceptions_combination = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm', 'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю',
                          'qwertyuiop'[::-1], 'asdfghjkl'[::-1], 'zxcvbnm'[::-1], 'йцукенгшщзхъ'[::-1],
                          'фывапролджэё'[::-1], 'ячсмитьбю'[::-1]]

exceptions_words_dict = []
with open('top_1000_words.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        exceptions_words_dict.append(line.strip())

passwords = []
with open('top_10000_passwords.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        passwords.append(line.strip())


def check_SequenceError(s):
    for combo in exceptions_combination:
        for j in range(len(combo) - 2):
            if combo[j: j + 3] in s.lower():
                raise SequenceError


def check_WordError(s):
    for word in exceptions_words_dict:
        if word in s:
            raise WordError


def check_LenghtError(s):
    if len(s) <= 8:
        raise LengthError


def check_LetterError(s):
    cnt_alpha = 0
    cnt_small = 0
    for i in s:
        if i.isupper():
            cnt_alpha += 1
        if i.islower():
            cnt_small += 1
    if cnt_small >= 1 and cnt_alpha >= 1:
        pass
    else:
        raise LetterError


def check_DigitError(s):
    cnt_nums = 0
    for i in s:
        if i in "1234567890":
            cnt_nums += 1
    if cnt_nums >= 1:
        pass
    else:
        raise DigitError


RESL = {"DigitError": 0,
        "LengthError": 0,
        "LetterError": 0,
        "SequenceError": 0,
        "WordError": 0}

"""
Сразу отсортировал исключения в алфавитном порядке

Буду вести статистику так, что если пароль не соответствует 
нескольким условия, то добавляю к каждому исключению
"""

for s in passwords:
    try:
        check_SequenceError(s)
    except SequenceError:
        RESL["SequenceError"] += 1

    try:
        check_LenghtError(s)
    except LengthError:
        RESL["LengthError"] += 1

    try:
        check_WordError(s)
    except WordError:
        RESL["WordError"] += 1

    try:
        check_LetterError(s)
    except LetterError:
        RESL["LetterError"] += 1

    try:
        check_DigitError(s)
    except DigitError:
        RESL["DigitError"] += 1

for i in RESL:
    print(i, "-", RESL[i])
