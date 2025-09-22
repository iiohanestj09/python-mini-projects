import random

# Input panjang password
passLen = int(input("Masukkan Panjang Password: "))

#! Versi 1
import math

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%^&*-_+~"

# Panjang password pakai formula 50-30-20
alphaLen = passLen // 2
numLen = math.ceil(passLen * 3/10)
specialLen = passLen - (alphaLen + numLen)

def generatePassword(length, array, isAlpha=False):
    for i in range(length):
        randIndex = random.randint(0, len(array)-1)
        randChar = array[randIndex]
        
        if isAlpha and random.randint(0, 1) == 1:
            randChar = randChar.upper()
        
        password.append(randChar)


# main program
password = []
generatePassword(alphaLen, alpha, True)
generatePassword(numLen, num)
generatePassword(specialLen, special)

random.shuffle(password)      # mengacak urutan elemen list

result = "".join(password)
print(result)



#! Versi 2
import string

total = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.sample(total, passLen))

print(password)