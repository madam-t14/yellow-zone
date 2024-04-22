import hashlib
import codecs

def bytes_to_hex(b):
    hex_digits = '0123456789abcdef'
    return ''.join([hex_digits[(b[i] >> 4) & 0x0f] + hex_digits[b[i] & 0x0f] for i in range(len(b))])

def string_to_sha1(input):
    sha1 = hashlib.sha1(input.encode('utf-8')).digest()
    return bytes_to_hex(sha1)

def concatenate_salt_with_string(salt, input):
    return salt + input.encode('utf-8')

def string_to_sha1_salted(salt, input):
    concatenated = concatenate_salt_with_string(salt, input)
    sha1 = hashlib.sha1(concatenated).digest()
    return bytes_to_hex(sha1)

if __name__ == "__main__":
    print("Let's get things started.")

    # Load the provided password file
    with open("password.txt", "r") as f:
        lines = f.readlines()

    non_salted_passwords = {}
    salted_passwords = {}
    salted_passwords_salts = {}

    # Parse password file
    for line in lines:
        splited = line.strip().split()
        
        if len(splited) == 3:
            non_salted_passwords[splited[0]] = splited[2]
        else:
            salted_passwords[splited[0]] = splited[3]
            salted_passwords_salts[splited[0]] = splited[2]

    # Load the provided dictionary file
    with open("english.0", "r") as f:
        dictionary = f.readlines()

    # Dictionary attack
    for word in dictionary:
        word = word.strip()
        
        # Non-salted passwords
        for account_name, account_password_hash in non_salted_passwords.items():
            if account_password_hash == string_to_sha1(word):
                print(f"{account_name}'s password is '{word}'")
            if account_password_hash == string_to_sha1(word[::-1]):
                print(f"{account_name}'s password is '{word[::-1]}'")
            if account_password_hash == string_to_sha1(word.translate({ord(c): None for c in 'AEIOUaeiou'})):
                print(f"{account_name}'s password is '{word.translate({ord(c): None for c in 'AEIOUaeiou'})}'")

        # Salted passwords
        for account_name, account_password_hash in salted_passwords.items():
            salt = codecs.decode(salted_passwords_salts[account_name], 'hex')
            if account_password_hash == string_to_sha1_salted(salt, word):
                print(f"{account_name}'s password is '{word}'")
            if account_password_hash == string_to_sha1_salted(salt, word[::-1]):
                print(f"{account_name}'s password is '{word[::-1]}'")
            if account_password_hash == string_to_sha1_salted(salt, word.translate({ord(c): None for c in 'AEIOUaeiou'})):
                print(f"{account_name}'s password is '{word.translate({ord(c): None for c in 'AEIOUaeiou'})}'")

    print("The program terminated.")
