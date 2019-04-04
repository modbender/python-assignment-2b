def write_output():
    s = input("Enter string: ")
    letters = {}
    for i in s:
        if i in letters:
            letters[i]+=1
        else:
            letters[i]=1
    print(letters)

write_output()