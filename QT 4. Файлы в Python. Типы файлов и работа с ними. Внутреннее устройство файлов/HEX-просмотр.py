data = open('files_txt/data.txt', mode='rb').read()
cnt_bukv = len(data)

print(' ' * 10 + ' '.join(f'{hex(i)[2:]:0>2}' for i in range(16)))

for i in range(cnt_bukv // 16 + 1):
    chast_data = data[i * 16: i * 16 + 16]

    if chast_data:
        text_cboku = ''.join((chr(bukva) if chr(bukva).isprintable() else '.' for bukva in chast_data))
        print(('%0.5x0    ' % i) + ''.join(('%0.2x ' % bukva for bukva in chast_data)) +
              ' ' * ((16 - len(chast_data)) * 3 + 4) + text_cboku)