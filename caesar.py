def encrypt(text_to_encrypt, shift):
    result = []
    mod_shift = shift % 26

    for c in text_to_encrypt:
        if (c != ' '):
            result = chr(ord(c.upper()) + mod_shift).append()
            print(result)
    
    return result


'''
def decrypt(text_to_decrypt, shift):
    result = []
    mod_shift = shift % 26

    for c in text_to_encrypt:
        if (c != ' '):
            result = ord(c.upper()) - mod_shift
    
   return result
'''
