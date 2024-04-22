import hashlib

# Load the dictionary file
def load_dictionary(file_path):
    with open(file_path, 'r') as f:
        words = f.readlines()
    return [word.strip() for word in words]

# Hash a password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Perform dictionary attack
def dictionary_attack(hash_to_crack, dictionary_file):
    words = load_dictionary(dictionary_file)
    
    for word in words:
        hashed_word = hash_password(word)
        
        if hashed_word == hash_to_crack:
            return f"Password cracked: {word}"
    
    return "Password not found in dictionary"

if __name__ == "__main__":
    # Example hash to crack (you would get this from the target system)
    hash_to_crack = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
    
    # Dictionary file containing possible passwords
    dictionary_file = "dictionary.txt"
    
    result = dictionary_attack(hash_to_crack, dictionary_file)
    print(result)
