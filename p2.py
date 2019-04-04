def write_output():
    content = open('log.txt').readlines()
    emails = {}
    for line in content:
        if line.startswith("From:"):
            id = line[5:].strip()
            if id in emails:
                emails[id]+=1
            else:
                emails[id]=1
    for eid,count in emails.items():
        print("%d emails by %s"%(count, eid))

write_output()