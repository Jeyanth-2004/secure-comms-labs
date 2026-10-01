

ciphertext = "66475 19274 92028 78494 24146 68542 17507 39398 32348 59378 70636"
key        = "66153 77185 10800 54937 48159 83271 12892 07132 34987 53954 23074"


c = ciphertext.replace(" ", "")
k = key.replace(" ", "")
plain_digits = ""
for i in range(len(c)):
    plain_digits += str((int(c[i]) + int(k[i])) % 10)

print("Ciphertext :", ciphertext)
print("Key        :", key)
print("Plaintext  :", " ".join(plain_digits[i:i+5] for i in range(0, len(plain_digits), 5)))


top  = {"0": "A", "1": "T", "3": "O", "4": "N", "5": "E", "7": "S", "8": "I", "9": "R"}
row2 = "BCDFGHJKLM"
row6 = "PQUVWXYZ./"

message = ""
i = 0
while i < len(plain_digits):
    d = plain_digits[i]
    if d in top:             
        message += top[d]
        i += 1
    elif d == "2":           
        message += row2[int(plain_digits[i + 1])]
        i += 2
    else:                    
        message += row6[int(plain_digits[i + 1])]
        i += 2

print("Message    :", message)
