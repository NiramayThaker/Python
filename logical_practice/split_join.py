# splitted string and joined it with '-' between them 

def split_and_join(line):
    list_str = []
    normal_str = ''
    
    for i in line:
        list_str.append(i)
    for i in list_str:
        normal_str += i       
    split_str = normal_str.split()
    
    return ('-'.join(split_str))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
