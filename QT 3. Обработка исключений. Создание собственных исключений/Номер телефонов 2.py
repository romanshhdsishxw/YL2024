class WrongInput(Exception):
    pass


def checkcherta(s):
    tmp = s.replace('-', 'c')
    if tmp.endswith('c'):
        return False
    elif 'cc' in tmp:
        return False
    else:
        return True


def checkstart(s):
    if s.startswith('+7'):
        return True
    elif s.startswith('8'):
        return True
    else:
        return False


def checkscobka(s):
    if s.count('(') > 0 or s.count(')') > 0:
        s = s.replace('(', 'a').replace(')', 'b')
        if s.count('a') == 1 and s.count('b') == 1 and s.index('a') < s.index('b'):
            return True
        else:
            return False
    return True


s = input()
try:
    s = s.strip()

    s = ''.join(s.split())

    if not checkcherta(s):
        raise WrongInput

    if not checkstart(s):
        raise WrongInput

    if not checkscobka(s):
        raise WrongInput

    if s.startswith('8'):
        s = '+7' + s[1:]

    if '-' in s:
        s = s.replace('-', '')

    if '(' in s:
        s = s.replace('(', '')
    if ')' in s:
        s = s.replace(')', '')

    if not s[1:].isdigit():
        raise WrongInput

    if len(s[1:]) != 11:
        raise WrongInput

    print(s)
except WrongInput:
    print('error')
