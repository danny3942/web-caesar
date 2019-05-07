from helpers import rot_char, alpha_pos

def encrypt(text , rot):
    new_str = ''
    for char in text:
        new_str += rot_char(rot , char)

    return new_str

def decrypt(txt , r):
    new_str = ''
    for char in txt:
        new_str += rot_char(-r , char)

    return new_str    
    
def main():
    message = input("Type a message:")
    rotation = int(input('Rotate by:'))
    crypt = encrypt(message , rotation)
    print(crypt)
    print(decrypt(crypt , rotation))

if __name__ == '__main__':
    main()
