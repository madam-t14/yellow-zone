import hashlib
from urllib.request import urlopen

def readlist(url):
    try:
        listfile = urlopen(url).read()
    except Exception as e:
        print("Hey there was some error while reading the wordlist, error:", e)
        exit()
    return listfile
 
 
def hash(password):
    result = hashlib.sha1(password.encode())
    return result.hexdigest()
 
 
def bruteforce(guesspasswordlist, actual_password_hash):
    for guess_password in guesspasswordlist:
        if hash(guess_password) == actual_password_hash:
            print("Ooooops-popsi! your password is:", guess_password,
                  "\n please change ur password, bro")
            exit()

#url
url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
actual_password = 'henry'
actual_password_hash = hash(actual_password)
 
wordlist = readlist(url).decode('UTF-8')
guesspasswordlist = wordlist.split('\n')

#call the function 
bruteforce(guesspasswordlist, actual_password_hash)

#if not found
print("Wel well well... I couldn't crack your password...")
