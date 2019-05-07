alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def alpha_pos(let):
    return alpha.index(let.lower())

def rot_char(num , letter):
    if letter.isalpha():
        if letter == letter.lower():
            return alpha[(alpha_pos(letter) + num) % 26]
        elif letter == letter.upper():
            return alpha2[(alpha_pos(letter) + num) % 26]
    return letter
