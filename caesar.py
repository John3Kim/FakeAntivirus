import random

rand_uniform_num = random.randrange(0,27,1)

'''
This particular Caesar cipher scheme will only shift alphanumeric values
If it's not an alphanumeric char, it'll just concatenate the results as is.
'''

def encrypt(text_to_encrypt, shift = rand_uniform_num):
    result = ""

    for char in text_to_encrypt:
        if char.isupper(): # ASCII range from 65-90 (A-Z); convert to range from 0-26
            result = result + chr(((((ord(char) + shift) - 65) % 26) + 65))
        elif char.islower(): # ASCII range from 97-122 (a-z); convert to range from 0-26
            result = result + chr(((((ord(char) + shift) - 97) % 26) + 97))
        else:
            result = result + char
    
    return result


'''
Since we know that the virus is encrypted with a Caesar cipher scheme, we can
try to compare the target text file with the decryption scheme, we can use
a brute-force apporach to find the virus.
-> Iterate through the actual virus file 26 times and compare with the
virus_definition text to determine if virus exists
    -> if exists, inoculate then quarantine
        else, continue on!
'''
def decrypt(text_to_decrypt, shift):
    result = ""

    for char in text_to_decrypt:
        if char.isupper(): # ASCII range from 65-90 (A-Z); convert to range from 0-26
            result = result + chr(((((ord(char) - shift) - 65) % 26) + 65))
        elif char.islower(): # ASCII range from 97-122 (a-z); convert to range from 0-26
            result = result + chr(((((ord(char) - shift) - 97) % 26) + 97))
        else:
            result = result + char
    
    return result

