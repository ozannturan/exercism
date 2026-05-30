def is_pangram(sentence):
    clear_sentence = sentence.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for i in alphabet:
        if i not in clear_sentence:
            return False
    
    return True
