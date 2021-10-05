# An simple program than change upper case to lower case of FULL STRING

def swap_case(s):
    converted_str = ''
    
    for i in s:        
        if i.islower():
            converted_str += i.upper()
        elif i.upper():
            converted_str += i.lower()
    return converted_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
