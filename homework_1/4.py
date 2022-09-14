c = str(input("Input a letter of the alphabet:"))
str = "abcdefghijklmnopqrstuvwxyz"

vowel = []
consonant = []
for x in str:
    if x in "aeiouy":
        vowel.append(x)
    else:
        consonant.append(x)
for i in vowel:
        if c == i:
            print(c, "is a vowel")
for j in consonant:            
        if c == j:
            print(c, "is a consonant")
