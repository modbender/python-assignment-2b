def write_output():
    s = input('Enter string: ')
    last_letter = None
    letters = {}
    for letter in s:
        if letter in letters and last_letter == letter:
            letters[letter]+=1
        else:
            letters[letter]=1
        last_letter = letter
    print(letters)
write_output()