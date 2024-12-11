def reverse():
    with open('files_txt/input.dat', mode='rb') as file:
        data = file.read()

    reversed_data = data[::-1]

    with open('files_txt/output.dat', mode='wb') as ans:
        ans.write(reversed_data)

    return ans


reverse()
