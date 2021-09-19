def base_conversion(number: str, b1: int, b2: int) -> str:
    gt_nine = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    decimal = 0
    for index, char in enumerate(reversed(number)):
        digit = ord(char) - 48
        decimal += digit * b1 ** index

    s = []
    while decimal:
        digit = decimal % b2
        if digit > 9:
            digit = gt_nine[digit]
            s.append(digit)
        else:
            s.append(chr(ord('0') + digit))
        decimal //= b2
    
    return ''.join(reversed(s))

print(base_conversion('615', 7, 13))
