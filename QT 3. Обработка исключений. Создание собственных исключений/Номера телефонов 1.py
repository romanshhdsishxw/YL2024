def to_std(s):
    s = str(s)
    error = 'error'
    s = s.strip()

    s = ''.join(s.split())

    s = s.replace('-', 'c')
    if s.endswith('c'):
        return error
    elif 'cc' in s:
        return error
    else:
        s = s.replace('c', '')

    if s.startswith('+7'):
        s = s[2:]
    elif s.startswith('8'):
        s = s[1:]
    else:
        return error

    if s.count('(') > 0 or s.count(')') > 0:
        s = s.replace('(', 'a').replace(')', 'b')
        if s.count('a') == 1 and s.count('b') == 1 and s.index('a') < s.index('b'):
            s = s.replace('a', '').replace('b', '')
        else:
            return error

    s = '+7' + s

    if s[1:].isdigit() and len(s[1:]) == 11:
        return s
    else:
        return error


print(to_std(input()))