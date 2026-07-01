def rotate(text, key):
    key = key % 26
    result = ""
    
    for char in text:
        if char.islower():
            old_series = ord(char) - ord('a')
            new_series = (old_series + key) % 26
            new_char = chr(ord('a') + new_series)
            result += new_char
        elif char.isupper():
            old_series = ord(char) - ord('A')
            new_series = (old_series + key) % 26
            new_char = chr(ord('A') + new_series)
            result += new_char
        else:
            result += char
    
    return result

            
