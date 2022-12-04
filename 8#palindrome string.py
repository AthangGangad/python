#palindrome string
s=input("enter the string")
def isPalindrome(S):
    return s==s[::-1]
p=isPalindrome(s)
if p:
    print("string is palindrome=",s)
else:
    print("string is not palindorome=",s)