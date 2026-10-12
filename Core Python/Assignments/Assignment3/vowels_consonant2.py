# Write a program to input any alphabet and check whether it is a vowel or consonant.

alp = input("Enter an alphabet: ")
if alp in ("aeiouAEIOU"):
    print(alp, "is a vowel.")
else:
    print(alp, "is a consonant.")
print("The alphabet is:", alp)
