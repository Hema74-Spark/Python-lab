str = input()
rev = ""
for i in range(len(str)-1,-1,-1):
    rev=rev+str[i]
if str == rev:
    print("The given string is Palindrome")
else:
    print("The given string is not palindrome")