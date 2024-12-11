with open('pipes.txt', mode='r', encoding='utf-8') as file:
    text = file.readlines()

trubProisv = [1 / float(i) if float(i) != 0.0 else 0 for i in text[:-2]]
su = 0
for i in list(map(int, text[-1].split())):
    su += trubProisv[i - 1]
fil = open('time.txt', mode='w', encoding='utf-8')
fil.write(str(1 / su * 60))