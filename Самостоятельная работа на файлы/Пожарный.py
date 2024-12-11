with open('files_txt/firefighters_1.txt', mode='r', encoding='utf-8') as input_file:
    data = ''.join(input_file.readlines()).lower().split()

tmp = []
for i in data:
    if data.count(i) > 1:
        tmp.append(i)

tmp = sorted(list(set(tmp)))

with open('files_txt/common.txt', mode='w', encoding='utf-8') as output_file:
    for i in tmp:
        output_file.write(f'{i}\n')
