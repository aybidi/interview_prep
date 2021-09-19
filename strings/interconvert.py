def  str_to_int(string):
    is_negative, number = 1, 0
    assert len(string) > 0
    
    for index, char in enumerate(string):
        if index == 0 and char == '-':
            is_negative = -1
        else:
            digit = ord(char) - 48
            number = (number * 10) + digit
    return number * is_negative

def int_to_str(integer):
    ans = []
    is_negative = False
    if integer < 0:
        integer, is_negative = -integer, True
    while integer:
        ans.append(chr(ord('0') + (integer % 10)))
        integer //= 10
    return ('-' if is_negative else '') + ''.join(reversed(ans))

# print(str_to_int('-174'))
print(int_to_str(-1234))