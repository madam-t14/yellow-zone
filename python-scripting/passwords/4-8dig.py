#4 digits crack
from string import digits

for i in digits:
    for k in digits:
        for j in digits:
            for l in digits:
                print(i,k,j,l)

# ascii letters
from string import ascii_letters

for i in ascii_letters:
    for k in ascii_letters:
        for j in ascii_letters:
            for l in ascii_letters:
                print(i, k, j, l)

#ascii + digits + punctuation 

from string import ascii_letters, digits, punctuation

for i in ascii_letters + digits + punctuation:
    for k in ascii_letters + digits + punctuation:
        for j in ascii_letters + digits + punctuation:
            for l in ascii_letters + digits + punctuation:
                print(i, k, j, l)