def is_isogram(string):
    clear = string.lower()
    alphabet = set()
    
    for char in clear:
        if char.isalpha(): 
            if char in alphabet:
                return False
            else:
                alphabet.add(char)
    
    return True
