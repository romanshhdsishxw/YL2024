import sys


def multi_list(tmp: list, avg_all_numbers: int) -> int:
    ans = 1
    for i in [j for j in tmp if j <= avg_all_numbers and j != 0]:
        ans *= i

    return ans


names_file = []
all_numbers = []
for line in sys.stdin:
    with open(f'files_txt/{line.strip()}', mode='r', encoding='utf-8') as input_file:
        tmp = ''.join(input_file.readlines()).lower().split()
        tmp = [int(i) for i in tmp]
        all_numbers += tmp
    names_file.append(line.strip())


avg_all_numbers = sum(all_numbers) // len(all_numbers)

print(avg_all_numbers)

ans = []
for name in names_file:
    with open(f'files_txt/{name}', mode='r', encoding='utf-8') as file:
        data = ''.join(file.readlines()).split('\n')
        for stroka in data:
            stroka = [int(i) for i in stroka.split()]
            ans.append(multi_list(stroka, avg_all_numbers))

with open('ages_ago.txt', mode='w', encoding='utf-8') as output_file:
    for i in ans:
        output_file.write(f"{i}\n")
