def write_output():
    contents = open('p3.txt').read().split()
    words = {}
    for w in contents:
        if w in words:
            words[w]+=1
        else:
            words[w]=1
    print(words)

write_output()
