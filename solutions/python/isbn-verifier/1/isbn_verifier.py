def is_valid(isbn):
    clear = isbn.replace("-", "")
    if len(clear) != 10:
        return False
    
    sum = 0
    for i, char in enumerate(clear):
        if char.isdigit():
            value = int(char)
        elif char == "X" and i == 9:
            value = 10
        else:
            return False
        
        sum += value * (10 - i)
    
    return sum % 11 == 0
