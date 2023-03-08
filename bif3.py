s = str(input())
revs = "".join(reversed(s))
if s == revs:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")