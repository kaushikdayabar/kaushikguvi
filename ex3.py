a=input()
if (a>="a" and a<="z") or (a>="A" and a<="Z"):
    if a in "aeiouAEIOU":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
   
