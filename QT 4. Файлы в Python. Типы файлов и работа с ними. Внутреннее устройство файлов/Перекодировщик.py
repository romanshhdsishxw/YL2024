slovar = {
    "й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
    "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
    "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
    "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
    "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
    "б": "b", "ю": "ju", "ё": "jo"
}


def translt(text):
    string = []

    for bukva in text:
        if bukva.lower() in slovar:
            s = slovar[bukva.lower()]
            if bukva.isupper():
                string.append(s.capitalize() if len(s) > 1 else s.upper())
            else:
                string.append(s)
        else:
            string.append(bukva)

    return ''.join(string)


with open('files_txt/cyrillic.txt', mode='r', encoding='utf-8') as cyrillic:
    text = cyrillic.read()

with open('files_txt/transliteration.txt', mode='w', encoding='utf-8') as transliteration:
    transliteration.write(translt(text))