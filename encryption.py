import random
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
scrambled = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
random.shuffle(scrambled)
print(alphabet)
print(scrambled)
def cipher(unscrambled):
    text = unscrambled
    encrypted = []
    for i in range(len(text)):
        for j in range(len(alphabet)):
                if alphabet[j] == text[i]:
                    encrypted.append(scrambled[j])
    print(''.join(encrypted))
def undo(unscrambled):
    unencrypted = []
    for i in range(len(unscrambled)):
        for j in range(len(scrambled)):
             if scrambled[j] == unscrambled[i]:
                  unencrypted.append(alphabet[j])
    print(''.join(unencrypted))
def key(unscrambled):
    for i in range(27):
        scrambled[i] = unscrambled[i]
while True:
    unscrambled = list(lower(input("Enter your entire message: ")))
    prompt = input("Do you want to encrypt, decrypt, or enter a key? ")
    if prompt == "encrypt":
        cipher(unscrambled)
    elif prompt == "decrypt":
        undo(unscrambled)
    elif prompt == 'key':
        key(unscrambled)
    else:
        print("Unkown Command")