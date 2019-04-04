def write_output():
    contents = open('p4.txt').readlines()
    emails = {}
    for line in contents:
        if line.startswith('From:'):
            words = line[5:].strip().split()
            emails[words[0]]= ("%s-%s-%s"%(words[3],words[2],words[5]), words[4])
    print(emails)

write_output()