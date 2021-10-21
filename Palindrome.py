# to check if palindrome or not

def palindrome(x):
    return x == x[::-1]


text = "HACKTOBER-2021"
check = palindrome(text)

if check:
    print("Yup")
else:
    print("Nope")

