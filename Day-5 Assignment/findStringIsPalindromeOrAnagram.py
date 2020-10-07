s1 = input("Enter 1st string: ").strip()
s2 = input("Enter 2nd string: ").strip()

if s1 == s1[::-1]:
    print("The given string", s1, "is Palindrome")

elif sorted(s1) == sorted(s2):
    print("The given string is Anagram")

else:
    print("The given string is not belongs to Palindrome or Anagram")