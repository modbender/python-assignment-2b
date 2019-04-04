def write_output():
    print("Type 'exit' as key to stop\n")
    in_list = []
    while True:
        k = input("Enter key: ")
        if k == 'exit':
            break
        v = input("Enter value for key %s: "%k)
        in_list.append((k,v))
    print("Tuple List : "+in_list)
    list_dict = {}
    for key,value in in_list:
        list_dict[key]=value
    print("Converted to dictionary : "+list_dict)
write_output()